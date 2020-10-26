from src.Ui_Files.Dialogs.Save_To_CSV import Ui_Dialog as TW_ui
from PySide2 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from src.gui_elements.settings import *
import numpy as np
from numpy.linalg import norm
from scipy import integrate
import glob
from scipy.signal import savgol_filter

def linear_plot_SE(self):
    dialog = QtWidgets.QDialog()
    ui = TW_ui()
    ui.setupUi(dialog)
    dict = ApplicationSettings.ALL_DATA_PLOTTED
    Key_List = []
    for i in dict.keys():
        Key_List.append(QtWidgets.QTreeWidgetItem([i]))
    ui.treeWidget.addTopLevelItems(Key_List)
    dialog.exec_()
    # save_csv = ui.treeWidget.indexOfTopLevelItem(ui.treeWidget.currentItem())
    for ix in ui.treeWidget.selectedIndexes():
        text = ix.data()  # or ix.data(),
        data = ApplicationSettings.ALL_DATA_PLOTTED[text]

    # trying to deal with nan elements in a list
    new_data = [[], []]
    for b in range(len(data)):
        for c in range(len(data[b])):
            if not np.isnan(data[b][c]):
                new_data[b].append(data[b][c])
            else:
                pass
    fit = np.polyfit(new_data[0], new_data[1], 1)
    self.ax.plot(new_data[0], np.poly1d(fit)(new_data[0]))
    self.canvas.draw()

def addmpl(self,fig):
    self.main_window.canvas = FigureCanvas(fig)
    self.ui.verticalLayout.addWidget(self.main_window.canvas)
    self.main_window.canvas.draw()
    self.toolbar = NavigationToolbar(self.main_window.canvas,
                                     self, coordinates=True)
    self.ui.verticalLayout.addWidget(self.main_window.toolbar)

def rmmpl(self):
    self.ui.verticalLayout.removeWidget(self.main_window.canvas)
    self.main_window.canvas.close()
    self.ui.verticalLayout.removeWidget(self.main_window.toolbar)

def mpl_basic(self):
    try: self.main_window.ax.legend().set_draggable(True)
    except: pass
    self.main_window.ax.set_xlabel("Wavenumber (cm-1)")
    self.main_window.ax.set_ylabel("Absorbance")
    self.main_window.fig.tight_layout()
    self.main_window.canvas.draw()

def qcm_hc_mass(data, start_time=float, end_time=float, purge_time_a=float, purge_time_b=float, num_cycles=int):
    time = data[0]
    mass = data[2]
    exposure = []
    exposure_idx = []
    mass_hc_a = []
    mass_hc_b = []
    exp_length_idx = []
    # time_in_idx = find_nearest(time, end_time) - find_nearest(time, start_time)
    mass_process = mass[find_nearest(time, start_time): find_nearest(time, end_time)]
    time_process = time[find_nearest(time, start_time):find_nearest(time, end_time)]
    print(time_process)
    print(mass_process)
    for i in range(num_cycles):
        if i % 2 == 0:
            exposure.append(start_time + (purge_time_a * i))
            exposure_idx.append(find_nearest(time_process, start_time + (purge_time_a * i)))
        elif i % 2 == 1:
            exposure.append(start_time + (purge_time_b * i))
            exposure_idx.append(find_nearest(time_process, start_time + (purge_time_b * i)))
    for k in range(len(exposure_idx) - 1):
        exp_length_idx.append(exposure_idx[k + 1] - exposure_idx[k])
    for j in range(num_cycles - 1):
        if j % 2 == 0:
            mass_hc_a.append(
                mass_process[int((exposure_idx[j + 1] - exposure_idx[j]) * .9 + exposure_idx[j])] - mass_process[
                    exposure_idx[j]])
        elif j % 2 == 1:
            mass_hc_b.append(
                mass_process[int((exposure_idx[j + 1] - exposure_idx[j]) * .9 + exposure_idx[j])] - mass_process[
                    exposure_idx[j]])
    fc = np.zeros(len(mass_hc_b))
    for i in range(len(mass_hc_b)):
        fc[i] = mass_hc_a[i]+mass_hc_b[i]
    return mass_hc_a,mass_hc_b, fc

def plot_QCM(self, time,pressure,mass,a_exp=int,b_exp=int,ttp=float,threshold=float,from_time=int,to_time=int,
             wait_time=float, density = float):
    #  Few more assignments Exposures is the time of each Exposure, the Index is just what index it
    #  shows up as. M_Diff and P_Diff are the mass and pressure difference at different exposures
    #  Purge Time Index is the number of data points between one exposure and the next, does not
    #  differentiate for the exposure time.
    Exposures = []
    A_Exposures = a_exp
    Exposure_index = []
    QCM_M_Diff = []
    QCM_P_Diff = []
    MC_A = []
    MC_B = []
    MC_P = []
    MC_N = []
    MC_Cycle = []

    t = 0
    #  Time through purge is the time to "wait" after there is an exposure to not overcount exposures
    #  Time is just a temp variable that gives the time of the last exposure

    # This for loop is just for appending the exposures to Exposures and Exposure_index nee
    for num in range(len(pressure) - 10):
        QCM_M_Diff.append(mass[num + 3] - mass[num])
        QCM_P_Diff.append(pressure[num + 3] - pressure[num])
        if QCM_P_Diff[num] >= threshold and time[num] - t > wait_time and time[num] > from_time and time[num] < to_time:
            Exposures.append(time[num])
            Exposure_index.append(num)
            t = time[num]

            # self.main_window.ax.axvline(time[num], color='gray', lw=1, alpha=0.5)
            # above line will add a line for each exposure if someone is uncertain about if its right

    # This for loop is knowing how long each purge time is (or time from one exposure to next)
    Purge_Time_Index = np.zeros(len(Exposure_index))

    for num in range(len(Exposure_index) - 1):
        if (Exposure_index[num + 1] - Exposure_index[num]) < 2000:
            Purge_Time_Index[num] = Exposure_index[num + 1] - Exposure_index[num]

    # for num in Purge_Time_Index:
    #     if

    Purge_Time_Index[-1] = Purge_Time_Index[0]

    # print(Purge_Time_Index)

    #  for loop finds the mass at the: Exposure time + Purge_time*(time_through_purge) which takes the time
    #  of the last exposure and then adds something like 0.8*Time of purge... Insert is to do the last one
    #  if else says if Mass_Middle was bigger or smaller than the last one and sorts it into one of two lists
    #  Last if else sorts based on if num is odd or even... For A-B experiemtns.. Nothing for A BBB or some
    #  Thing like that
    mass_middle = np.zeros(len(Exposure_index)+2)
    mass_middle[0] = mass[Exposure_index[0] - int(Purge_Time_Index[0] * ttp)]
    # mass_middle.insert(0, mass[Exposure_index[0] - int(Purge_Time_Index[0] * ttp)])

    for num in range(len(Exposure_index)):
        # mass_middle.append(mass[int(Exposure_index[num] + int(Purge_Time_Index[num] * ttp))])
        mass_middle[num+1] = mass[int(Exposure_index[num] + int(Purge_Time_Index[num] * ttp))]
        # self.main_window.ax.axvline(time[num], color='gray', lw=1, alpha=0.5)
        # above line will add a line for each time if someone is uncertain about if its right

    # mass_middle.append(mass[Exposure_index[-1] + int(Purge_Time_Index[0] * ttp)])
    mass_middle[-1] = mass[Exposure_index[-1] + int(Purge_Time_Index[0] * ttp)]

    # print('There was ' + str(len(Exposures)) + '  Precursor Exposures')
    self.main_window.dw_QCM.ui.num_doses.setText(str(len(Exposures)))

    for num in range(len(Exposure_index)):
        if mass_middle[num + 1] - mass_middle[num] > 0:
            MC_P.append(mass_middle[num + 1] - mass_middle[num])
        elif mass_middle[num + 1] - mass_middle[num] < 0:
            MC_N.append(mass_middle[num + 1] - mass_middle[num])
        if num % (b_exp + A_Exposures) == 0:
            MC_Cycle.append(mass_middle[num + b_exp + A_Exposures] - mass_middle[num])
        if num == a_exp - 1:
            MC_A.append(mass_middle[num + 1] - mass_middle[num + 1 - A_Exposures])
        elif num == b_exp + a_exp - 1:
            MC_B.append(mass_middle[num + 1] - mass_middle[num + 1 - b_exp])
        elif num == a_exp + b_exp:
            a_exp = a_exp + A_Exposures + b_exp
            if num == a_exp - 1:
                MC_A.append(mass_middle[num + 1] - mass_middle[
                    num + 1 - A_Exposures])


            # elif num == B_Doses + A_Doses:
            #     self.QCM_Dict['MC_B'].QCM_B.append(Mass_Middle[num] - Mass_Middle[num + 1 - int(B_Exposures.text())])
    half_cycle_density_A = np.zeros(len(MC_A))
    half_cycle_density_B = np.zeros(len(MC_B))
    full_cycle_density = np.zeros(len(MC_Cycle))
    for i in range(len(MC_A)):
        half_cycle_density_A[i] = MC_A[i] / (10.0 * density)
    for i in range(len(MC_B)):
        half_cycle_density_B[i] = MC_B[i] / (10.0 * density)
    for i in range(len(MC_Cycle)):
        full_cycle_density[i] = MC_Cycle[i] / (10 * density)

    return MC_A, MC_B, MC_Cycle, half_cycle_density_A, half_cycle_density_B, full_cycle_density

    # if QCM_fun == 0:
    #     x_values_A = np.linspace(0,int(len(MC_A)),len(MC_A))
    #     x_values_B = np.linspace(0, int(len(MC_B)), len(MC_B))
    #     self.main_window.ax.plot(x_values_A,MC_A)
    #     self.main_window.ax.plot(x_values_B,MC_B)
    #     self.main_window.ax.set_xlabel('Cycles')
    #     self.main_window.ax.set_ylabel('Mass Change (ng/cm$^3$)')
    #     self.main_window.fig.tight_layout()
    #     ApplicationSettings.LAST_DATA_PLOTTED.clear()
    #     ApplicationSettings.LAST_DATA_PLOTTED.append([MC_A, MC_B])
    #     ApplicationSettings.ALL_DATA_PLOTTED[path.split('/')[-1].split('.')[0]+'MC_AB.csv'] = [x_values_A, MC_A, x_values_B, MC_B]
    #
    # elif QCM_fun == 1:
    #     x_values = np.linspace(1, len(MC_Cycle),len(MC_Cycle))
    #     self.main_window.ax.plot(x_values,MC_Cycle)
    #     self.main_window.ax.set_xlabel('Cycles')
    #     self.main_window.ax.set_ylabel('Mass Change (ng/cm$^3$)')
    #     self.main_window.fig.tight_layout()
    #     ApplicationSettings.LAST_DATA_PLOTTED.clear()
    #     ApplicationSettings.LAST_DATA_PLOTTED.append([MC_Cycle])
    #     ApplicationSettings.ALL_DATA_PLOTTED[path.split('/')[-1].split('.')[0] + 'MC_AB.csv'] = [x_values, MC_Cycle]
    #
    # elif QCM_fun == 2:
    #     x_values = np.linspace(1, 30, 30)
    #     self.main_window.ax.plot(x_values, MC_P)
    #     self.main_window.ax.plot(x_values, MC_N)
    #     self.main_window.ax.set_xlabel('Cycles')
    #     self.main_window.ax.set_ylabel('Mass Change (ng/cm$^3$)')
    #     self.main_window.fig.tight_layout()
    #     ApplicationSettings.LAST_DATA_PLOTTED.clear()
    #     ApplicationSettings.LAST_DATA_PLOTTED.append([MC_N, MC_P])
    #     ApplicationSettings.ALL_DATA_PLOTTED[path.split('/')[-1].split('.')[0] + 'MC_AB.csv'] = [x_values, MC_P, MC_N]
    #
    # elif QCM_fun == 3:
    #     # self.main_window.ax.plot(time, pressure)
    #     self.main_window.ax.plot(time, mass)
    #     self.main_window.ax.set_xlabel('Time (s)')
    #     self.main_window.ax.set_ylabel('Mass (ng/cm$^3$)')
    #     # self.main_window.ax.axvline(time_at_num, color='gray', lw=1, alpha=0.5)
    #
    # elif QCM_fun == 4:
    #     self.main_window.ax.plot(time, pressure)
    #     # self.main_window.ax.plot(time, mass)
    #     self.main_window.ax.set_xlabel('Time (s)')
    #     self.main_window.ax.set_ylabel('Pressure (Torr)')
    #
    # elif QCM_fun == 5:
    #     for i in range(len(MC_A)):
    #         half_cycle_density_A[i] = MC_A[i] / (10.0 * density)
    #     for i in range(len(MC_B)):
    #         half_cycle_density_B[i] = MC_B[i] / (10.0 * density)
    #     x_values_A = np.linspace(0, int(len(MC_A)), len(MC_A))
    #     x_values_B = np.linspace(0, int(len(MC_B)), len(MC_B))
    #     self.main_window.ax.plot(x_values_A, half_cycle_density_A)
    #     self.main_window.ax.plot(x_values_B, half_cycle_density_B)
    #     self.main_window.ax.set_xlabel('Cycles')
    #     self.main_window.ax.set_ylabel('Thickness ($\AA$)')
    #     self.main_window.fig.tight_layout()
    #     ApplicationSettings.LAST_DATA_PLOTTED.clear()
    #     ApplicationSettings.LAST_DATA_PLOTTED.append([half_cycle_density_A, half_cycle_density_B])
    #     ApplicationSettings.ALL_DATA_PLOTTED[path.split('/')[-1].split('.')[0] + 'MC_AB_den.csv'] = \
    #         [x_values_A, half_cycle_density_A,x_values_B, half_cycle_density_B]
    #
    # elif QCM_fun == 6:
    #     for i in range(len(MC_Cycle)):
    #         full_cycle_density[i] = MC_Cycle[i] / (10 * density)
    #     x_values = np.linspace(0, int(len(MC_Cycle)), len(MC_Cycle))
    #     self.main_window.ax.plot(x_values, full_cycle_density)
    #     self.main_window.ax.set_xlabel('Cycles')
    #     self.main_window.ax.set_ylabel('Thickness ($\AA$)')
    #     self.main_window.fig.tight_layout()
    #     ApplicationSettings.LAST_DATA_PLOTTED.clear()
    #     ApplicationSettings.LAST_DATA_PLOTTED.append([full_cycle_density])
    #     ApplicationSettings.ALL_DATA_PLOTTED[path.split('/')[-1].split('.')[0] + 'MC_Cycle_den.csv'] = \
    #         [x_values, full_cycle_density]


def ir_plot_basic(self):
    try: self.main_window.ax.legend().set_draggable(True)
    except: pass
    self.main_window.ax.set_xlabel("Wavenumber (cm-1)")
    self.main_window.ax.set_ylabel("Absorbance")
    self.main_window.ax.set_xlim([4000, 400])
    self.main_window.fig.tight_layout()
    self.main_window.canvas.draw()

def difference_from_survey(list_of_csv):
    data = []
    for csv in list_of_csv:
        data.append(np.genfromtxt(csv, delimiter=',').T)
    sub_list = [data[0][0]]
    for l in range(len(data)-1):
        sub_list.append(data[l+1][1]-data[l][1])
    return sub_list


def subtraction_from_survey(list_of_csv):
    data = []
    for csv in list_of_csv:
        data.append(np.genfromtxt(csv, delimiter=',').T)
    sub_list = [data[0][0]]
    for l in range(len(data) - 1):
        sub_list.append(data[l + 1][1] - data[0][1])
    return sub_list

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

def integrate_ir(data,minimum,maximum):
    integral_list = []
    lim = [min(range(len(data[0])),key=lambda i: abs(data[0][i] - minimum)),
           min(range(len(data[0])),key=lambda i: abs(data[0][i] - maximum))]
    for numb in range(len(data) - 1):
        integral_list.append(integrate.trapz(data[numb + 1][lim[0]:lim[1]],data[0][lim[0]:lim[1]]))
    return integral_list

    # if cycle_exposure_combo.currentText() == 'Cycles':
    #     print(integral_list)
    #     if len(integral_list) % 2 == 0:
    #         self.ax.plot(np.linspace(.5, len(integral_list) / 2, len(integral_list)), integral_list, '-o')
    #     elif len(integral_list) % 2 == 1:
    #         self.ax.plot(np.linspace(0, (len(integral_list) - 1) / 2, len(integral_list)), integral_list,
    #                      '-o')
    #     self.figure.tight_layout()
    #     self.canvas.draw()
    # elif cycle_exposure_combo.currentText() == 'Exposures':
    #     if len(integral_list) % 2 == 0:
    #         self.ax.plot(np.linspace(0, len(integral_list) - 1, len(integral_list)), integral_list, '-o')
    #     elif len(integral_list) % 2 == 1:
    #         self.ax.plot(np.linspace(0, len(integral_list) - 1, len(integral_list)), integral_list, '-o')
    #     self.figure.tight_layout()
    #     self.ax.set_xlabel('Exposures')
    #     self.canvas.draw()
    # self.FTIR_Dict[str(X_Range_Min) + '-' + str(X_Range_Max)] = integral_list

def plot_all_in_directory(self,list_of_csv, f, t, skip_every):
    data = []
    for csv in list_of_csv:
        data.append(np.genfromtxt(csv, delimiter=',').T)
    sub_list = []
    sub_list.append(data[0][0])
    for l in range(len(data)):
        sub_list.append(data[l][1])

    for s in range(len(sub_list) - 1):
        if f <= s <= t:
            if skip_every == 0:
                self.main_window.ax.plot(sub_list[0], sub_list[s + 1])
            elif s % skip_every == 0:
                self.main_window.ax.plot(sub_list[0], sub_list[s + 1])
            else:
                pass
        else:
            pass
    ir_plot_basic(self)
    self.main_window.canvas.draw()

def shirley_calculate(x, y, tol=1e-5, maxit=15):
    """ S = specs.shirley_calculate(x,y, tol=1e-5, maxit=10)
    Calculate the best auto-Shirley background S for a dataset (x,y). Finds the biggest peak
    and then uses the minimum value either side of this peak as the terminal points of the
    Shirley background.
    The tolerance sets the convergence criterion, maxit sets the maximum number
    of iterations.
    """

    # Make sure we've been passed arrays and not lists.
    x = np.array(x)
    y = np.array(y)

    # Sanity check: Do we actually have data to process here?
    if not (x.any() and y.any()):
        print("specs.shirley_calculate: One of the arrays x or y is empty. Returning zero background.")
        return np.zeros(x.shape)

    # Next ensure the energy values are *decreasing* in the array,
    # if not, reverse them.
    if x[0] < x[-1]:
        is_reversed = True
        x = x[::-1]
        y = y[::-1]
    else:
        is_reversed = False

    # Locate the biggest peak.
    maxidx = abs(y - np.amax(y)).argmin()

    # It's possible that maxidx will be 0 or -1. If that is the case,
    # we can't use this algorithm, we return a zero background.
    if maxidx == 0 or maxidx >= len(y) - 1:
        print("specs.shirley_calculate: Boundaries too high for algorithm: returning a zero background.")
        return np.zeros(x.shape)

    # Locate the minima either side of maxidx.
    lmidx = abs(y[0:maxidx] - np.amin(y[0:maxidx])).argmin()
    rmidx = abs(y[maxidx:] - np.amin(y[maxidx:])).argmin() + maxidx
    xl = x[lmidx]
    yl = y[lmidx]
    xr = x[rmidx]
    yr = y[rmidx]

    # Max integration index
    imax = rmidx - 1

    # Initial value of the background shape B. The total background S = yr + B,
    # and B is equal to (yl - yr) below lmidx and initially zero above.
    B = np.zeros(x.shape)
    B[:lmidx] = yl - yr
    Bnew = B.copy()

    it = 0
    while it < maxit:
        # if DEBUG:
        #     print("Shirley iteration: ", it)
        # Calculate new k = (yl - yr) / (int_(xl)^(xr) J(x') - yr - B(x') dx')
        ksum = 0.0
        for i in range(lmidx, imax):
            ksum += (x[i] - x[i + 1]) * 0.5 * (y[i] + y[i + 1]
                                               - 2 * yr - B[i] - B[i + 1])
        k = (yl - yr) / ksum
        # Calculate new B
        for i in range(lmidx, rmidx):
            ysum = 0.0
            for j in range(i, imax):
                ysum += (x[j] - x[j + 1]) * 0.5 * (y[j] +
                                                   y[j + 1] - 2 * yr - B[j] - B[j + 1])
            Bnew[i] = k * ysum
        # If Bnew is close to B, exit.
        if norm(Bnew - B) < tol:
            B = Bnew.copy()
            break
        else:
            B = Bnew.copy()
        it += 1

    if it >= maxit:
        print("specs.shirley_calculate: Max iterations exceeded before convergence.")
    if is_reversed:
        return (yr + B)[::-1]
    else:
        return yr + B

def linear(x,a,b):
    return (a*x)+b

def gaussian(x, amp, cen, sigma):
    return amp/(sigma*np.sqrt(2*np.pi))*np.exp(-(x-cen)**2/(2*sigma**2))

def lorentz(x, amp, cen, sigma):
    return (amp/np.pi)*(1/2*sigma)/((x-cen)**2+(1/2*sigma)**2)

def plateau(x,a,b):
    return (x*a)/(b+x)

def self_limiting(x,a,b,c):
    return a-b*np.exp(-c*x)

# def smooth(y_data,window_length, poly):
#     return savgol_filter(y_data, window_length, poly)
