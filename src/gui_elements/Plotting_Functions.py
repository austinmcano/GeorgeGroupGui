from src.Ui_Files.Dialogs.Save_To_CSV import Ui_Dialog as TW_ui
from PySide2 import QtWidgets
import numpy as np
from src.Ui_Files.Dialogs.Save_To_CSV import Ui_Dialog as STC_ui
from src.Ui_Files.Dialogs.app_settings import Ui_Dialog as app_settings
from src.Ui_Files.Dialogs.annotation_dialog import Ui_Dialog as annotation_ui
from src.Ui_Files.Dialogs.simple_text import Ui_Dialog as simple_text_ui
from src.Ui_Files.Dialogs.new_project_dialog import Ui_Dialog as new_project_dialog
from src.Ui_Files.Dialogs.simple_treeWidget_dialog import Ui_Dialog as simple_tw
from src.Ui_Files.Dialogs.bargraph_dialog import Ui_Dialog as bar_dialog
from src.Ui_Files.Dialogs.spine_color_dialog import Ui_Dialog as spine_color_dialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.pyplot import figure
import matplotlib
import pickle
import pandas as pd
from PySide2 import QtCore,QtWidgets,QtGui
import sys
from shutil import copyfile, copytree, rmtree, copy2
import os
import seaborn as sns
from src.gui_elements.settings import ApplicationSettings
from scipy import integrate
from scipy.linalg import norm
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

def keycheck(dict, key):
    if key in dict.keys():
        return True
    else:
        return False

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
        temp_data = pd.read_csv(csv,delimiter=',').to_numpy().T
        data.append(temp_data)
        # data.append(np.genfromtxt(csv, delimiter=',').T)
    sub_list = [data[0][0]]
    print(len(sub_list))
    for l in range(len(data)-1):
        print(len(sub_list))
        print('')
        try:
            sub_list.append(data[l+1][1]-data[l][1])
        except TypeError:
            print('TypeError')
    return sub_list

def subtraction_from_survey(list_of_csv):
    data = []
    for csv in list_of_csv:
        data.append(np.genfromtxt(csv, delimiter=',').T)
    sub_list = [data[0][0]]
    for l in range(len(data) - 1):
        sub_list.append(data[l + 1][1] - data[0][1])
    return sub_list

def diff_select_survey(list_of_csv):
    def finish():
        data = []
        for csv in list_of_csv:
            data.append(np.genfromtxt(csv, delimiter=',').T)
        sub_list = [data[0][0]]
        for l in range(len(data) - 1):
            sub_list.append(data[l + 1][1] - data[l][1])
        return sub_list
    dialog = QtWidgets.QDialog()
    ui = simple_tw()
    ui.setupUi(dialog)
    Key_List = []
    for i in list_of_csv:
        Key_List.append(QtWidgets.QTreeWidgetItem([i]))
    ui.treeWidget.addTopLevelItems(Key_List)
    ui.buttonBox.accepted.connect(lambda: finish())
    dialog.exec_()

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

def smooth(y_data,window_length, poly):
    return savgol_filter(y_data, window_length, poly)

class plotting_funs:
    def spine_color_fun(self):
        def finish():
            self.ax.spines['bottom'].set_color(ui.bspine_cb.currentText())
            self.ax.spines['top'].set_color(ui.tspine_cb.currentText())
            self.ax.spines['right'].set_color(ui.rspine_cb.currentText())
            self.ax.spines['left'].set_color(ui.lspine_cb.currentText())
            self.ax.xaxis.label.set_color(ui.bspine_cb.currentText())
            self.ax.yaxis.label.set_color(ui.lspine_cb.currentText())
            self.ax.tick_params(axis='x', colors=ui.bspine_cb.currentText())
            self.ax.tick_params(axis='y', colors=ui.lspine_cb.currentText())
            self.settings.setValue('top_spine_color',ui.tspine_cb.currentText())
            self.settings.setValue('bottom_spine_color', ui.bspine_cb.currentText())
            self.settings.setValue('left_spine_color', ui.lspine_cb.currentText())
            self.settings.setValue('right_spine_color', ui.rspine_cb.currentText())
            if self.ax_2 is not None:
                self.ax_2.tick_params(axis='y', colors=ui.rspine_cb.currentText())
            self.canvas.draw()
        dialog = QtWidgets.QDialog()
        ui = spine_color_dialog()
        ui.setupUi(dialog)
        colors = ['black','red','blue','green','purple','orange','yellow','white']
        ui.bspine_cb.addItems(colors)
        ui.bspine_cb.setCurrentText(self.settings.value('bottom_spine_color'))
        ui.tspine_cb.addItems(colors)
        ui.tspine_cb.setCurrentText(self.settings.value('top_spine_color'))
        ui.lspine_cb.addItems(colors)
        ui.lspine_cb.setCurrentText(self.settings.value('left_spine_color'))
        ui.rspine_cb.addItems(colors)
        ui.rspine_cb.setCurrentText(self.settings.value('right_spine_color'))

        ui.buttonBox.accepted.connect(lambda: finish())
        dialog.exec_()

    def graph_test_fun(self):
        path, ext = QtWidgets.QFileDialog.getOpenFileName(self, 'Pickeled Figure', self.settings.value('FIG_PATH'))
        ax = pickle.load(open(path, 'rb'))
        self.ui.verticalLayout.removeWidget(self.toolbar)
        self.ui.verticalLayout.removeWidget(self.canvas)
        self.toolbar.close()
        self.canvas.close()
        self.ax.remove()
        sns.set(context=self.context, style=self.style, palette=self.c_palette,
                font=self.font, font_scale=self.fs, color_codes=True)
        self.fig = figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
        self.canvas = FigureCanvas(self.fig)
        self.ui.verticalLayout.addWidget(NavigationToolbar(self.canvas, self.canvas, coordinates=True))
        self.ui.verticalLayout.addWidget(self.canvas)
        self.ax = ax
        self.canvas.installEventFilter(self)
        self.canvas.draw()

    def tight_figure(self):
        self.fig.tight_layout()
        self.canvas.draw()

    def save_fig(self):
        def finish():
            text = ui.lineEdit.text()
            # pickle.dump(self.ax, self.settings.value('FIG_PATH') + text, 'w')
            with open(self.settings.value('FIG_PATH') + text, 'wb') as f:  # should be 'wb' rather than 'w'
                pickle.dump(self.fig, f)
        dialog = QtWidgets.QDialog()
        ui = simple_text_ui()
        ui.setupUi(dialog)
        ui.buttonBox.accepted.connect(lambda: finish())
        dialog.exec_()

        # pickle.dump(self.fig, open(ApplicationSettings.FIG_PATH+text, 'wb'))

    def show_pickled_fig(self):
        path,ext = QtWidgets.QFileDialog.getOpenFileName(self,'Pickeled Figure',self.settings.value('FIG_PATH'))
        figx = pickle.load(open(path, 'rb'))
        if path == '':
            pass
        else:
            self.ui.verticalLayout.removeWidget(self.toolbar)
            self.ui.verticalLayout.removeWidget(self.canvas)
            self.toolbar.close()
            self.canvas.close()
            sns.set(context=self.context, style=self.style, palette=self.c_palette,
                    font=self.font, font_scale=self.fs, color_codes=True)
            self.fig = figx
            self.ax = self.fig.add_subplot(111)
            self.canvas = FigureCanvas(self.fig)
            self.ui.verticalLayout.addWidget(NavigationToolbar(self.canvas, self.canvas, coordinates=True))
            self.ui.verticalLayout.addWidget(self.canvas)

            self.canvas.installEventFilter(self)
            self.canvas.draw()

    def Project_view_fun(self):
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dw_ProjectView)
        self.restoreDockWidget(self.dw_ProjectView)
        self.dw_ProjectView.show()

    def DataBrowser_view_fun(self):
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dw_Data_Broswer)
        self.restoreDockWidget(self.dw_Data_Broswer)
        self.dw_Data_Broswer.show()

    def XPS_view_fun(self):
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dw_XPS)
        self.restoreDockWidget(self.dw_XPS)
        self.dw_XPS.show()

    def FTIR_view_fun(self):
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dw_FTIR)
        self.restoreDockWidget(self.dw_FTIR)
        self.dw_FTIR.show()

    def QCM_view_fun(self):
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dw_QCM)
        self.restoreDockWidget(self.dw_QCM)
        self.dw_QCM.show()

    def SE_view_fun(self):
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dw_SE)
        self.restoreDockWidget(self.dw_SE)
        self.dw_SE.show()

    def CF_view_fun(self):
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dw_CF)
        self.restoreDockWidget(self.dw_CF)
        self.dw_CF.show()

    def Console_view_fun(self):
        pass
        # import sys
        #
        # from qtpy.QtWidgets import QApplication
        # from pyqtconsole.console import PythonConsole
        #
        # def greet():
        #     print("hello world")
        #
        # if __name__ == '__main__':
        #     appl = QApplication([])
        #
        #     console = PythonConsole()
        #     console.push_local_ns('greet', greet)
        #     console.show()
        #     console.eval_in_thread()
        #     sys.exit(appl.exec_())
        # self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dw_Console)
        # self.restoreDockWidget(self.dw_Console)
        # self.dw_Console.show()

    def Calc_view_fun(self):
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dw_calc)
        self.restoreDockWidget(self.dw_calc)
        self.dw_calc.show()

    def toggle_legend(self):
        if self.ui.actionLegend_Toggle.isChecked()==True:
            self.ax.legend()
            leg_1 = self.ax.legend(loc='best')
            leg_1.set_draggable(True)
            if self.ax_2 is not None:
                self.ax_2.legend()
                leg_2 = self.ax.legend(loc='best')
                leg_2.set_draggable(True)
            self.canvas.draw()
        elif self.ui.actionLegend_Toggle.isChecked()==False:
            if self.ax.get_legend() is None:
                pass
            else:
                self.ax.get_legend().remove()
            if self.ax_2 is not None:
                self.ax_2.get_legend().remove()
            self.canvas.draw()

    def Save_All_Plotted(self):
        # names = self.settings.value('Data_Names')
        # if names is None:
        #     pass
        # else:
        #     for i in names:
        #         self.settings.remove(i)
        def temp():
            temp = []
            for ix in ui.treeWidget.selectedIndexes():
                text = ix.data()
                temp.append(text)
                name = os.path.join(self.settings.value('SAVED_DATA_PATH'),ix.data())
                np.savetxt(str(name)+ui.save_as_LE.text()+ui.comboBox.currentText(),
                           ApplicationSettings.ALL_DATA_PLOTTED[ix.data()][0]._xy,delimiter=',')
                print(ApplicationSettings.ALL_DATA_PLOTTED[ix.data()][0]._xy)
        dialog = QtWidgets.QDialog()
        ui = STC_ui()
        ui.setupUi(dialog)
        dict = ApplicationSettings.ALL_DATA_PLOTTED
        Key_List = []
        for i in dict.keys():
            Key_List.append(QtWidgets.QTreeWidgetItem([i]))
        ui.treeWidget.addTopLevelItems(Key_List)
        ui.buttonBox.accepted.connect(lambda: temp())
        ui.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        dialog.exec_()

    def remove_line(self):
        def finish():
            for j in ui.treeWidget.selectedIndexes():
                line = ApplicationSettings.ALL_DATA_PLOTTED[j.data()]
                try:
                    if isinstance(line, list):
                        self.ax.lines.remove(line[0])
                        ApplicationSettings.ALL_DATA_PLOTTED.pop(j.data())
                        del line
                        self.canvas.draw()
                    elif isinstance(line,matplotlib.lines.Line2D):
                        self.ax.lines.remove(line)
                        ApplicationSettings.ALL_DATA_PLOTTED.pop(j.data())
                        del line
                        self.canvas.draw()
                    else:
                        line_0 = line.lines[0]
                        self.ax.lines.remove(line_0)
                        ApplicationSettings.ALL_DATA_PLOTTED.pop(j.data())
                        del line_0
                except IndexError:
                    print("Index Error")
        all_lines = ApplicationSettings.ALL_DATA_PLOTTED
        dialog = QtWidgets.QDialog()
        ui = simple_tw()
        ui.setupUi(dialog)
        ui.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        Key_List = []
        for i in all_lines.keys():
            Key_List.append(QtWidgets.QTreeWidgetItem([i]))
        ui.treeWidget.addTopLevelItems(Key_List)
        ui.buttonBox.accepted.connect(lambda:finish())
        dialog.exec_()
        self.canvas.draw()

    def send_to_cf(self):
        # def finish():
        #     for j in ui.treeWidget.selectedIndexes():
        #         line = ApplicationSettings.ALL_DATA_PLOTTED[j.data()]
        # all_lines = ApplicationSettings.ALL_DATA_PLOTTED
        # dialog = QtWidgets.QDialog()
        # ui = simple_tw()
        # ui.setupUi(dialog)
        # ui.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        # Key_List = []
        # for i in all_lines.keys():
        #     Key_List.append(QtWidgets.QTreeWidgetItem([i]))
        # ui.treeWidget.addTopLevelItems(Key_List)
        # ui.buttonBox.accepted.connect(lambda:finish())
        # dialog.exec_()
        # self.canvas.draw()
        fit_list = self.dw_SE.fitted_slopes
        self.dw_CF.ui.tableWidget.setRowCount(len(fit_list))
        for row in range(len(fit_list)):
            self.dw_CF.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(fit_list[row])))

    def random_c_plot(self):
        Z = np.random.rand(6, 10)
        c = self.ax.pcolor(Z)
        self.canvas.draw()
        self.fig.colorbar(c, ax=self.ax)

    def app_settings_fun(self):
        def function():
            self.settings.setValue('app_style',ui.comboBox.currentText())
            os.execl(sys.executable, sys.executable, *sys.argv)
        def change_path(settings_type):
            path = QtWidgets.QFileDialog.getExistingDirectory()
            self.settings.setValue(settings_type, path)
            if settings_type == 'FTIR_PATH':
                self.dw_FTIR.tree_view.setRootIndex(self.dw_FTIR.model.index(path))
            elif settings_type == 'QCM_PATH':
                self.dw_QCM.tree_view.setRootIndex(self.dw_QCM.model.index(path))
            elif settings_type == 'SE_PATH':
                self.dw_SE.tree_view.setRootIndex(self.dw_SE.model.index(path))
            elif settings_type == 'XPS_PATH':
                self.dw_XPS.tree_view.setRootIndex(self.dw_XPS.model.index(path))
            update()
        def update():
            ui.datapath_le.setText(str(self.settings.value('DATA_PATH')))
            ui.projectpath_le.setText(str(self.settings.value('PROJECT_PATH')))
            ui.savepath_le.setText(str(self.settings.value('SAVED_DATA_PATH')))
            ui.fig_path_label.setText(str(self.settings.value('FIG_PATH')))
            ui.ftir_path_label.setText(str(self.settings.value('FTIR_PATH')))
            ui.se_path_label.setText(str(self.settings.value('SE_PATH')))
            ui.qcm_path_label.setText(str(self.settings.value('QCM_PATH')))
            ui.cf_path_label.setText(str(self.settings.value('CF_PATH')))
            ui.xps_path_label.setText(str(self.settings.value('XPS_PATH')))
            ui.comboBox.setCurrentText(self.settings.value('app_style'))

        d = QtWidgets.QDialog()
        ui = app_settings()
        ui.setupUi(d)
        ui.comboBox.addItems(QtWidgets.QStyleFactory.keys())
        ui.comboBox.addItems(['DarkStyle'])
        ui.comboBox.addItems(['DarkFusion'])
        ui.comboBox.addItems(['GrayFusion'])
        update()
        # ui.buttonBox.accepted.connect(lambda: function())
        ui.comboBox.currentTextChanged.connect(lambda: function())
        ui.changedatapath_pb.clicked.connect(lambda: change_path('DATA_PATH'))
        ui.changesavepath_pb.clicked.connect(lambda: change_path('SAVED_DATA_PATH'))
        ui.changeprojectpath_pb.clicked.connect(lambda: change_path('PROJECT_PATH'))
        ui.change_figpath_pb.clicked.connect(lambda: change_path('FIG_PATH'))
        ui.change_ir_pb.clicked.connect(lambda: change_path('FTIR_PATH'))
        ui.change_qcm_pb.clicked.connect(lambda: change_path('QCM_PATH'))
        ui.change_se_pb.clicked.connect(lambda: change_path('SE_PATH'))
        ui.change_cf_pb.clicked.connect(lambda: change_path('CF_PATH'))
        ui.change_xps_pb.clicked.connect(lambda: change_path('XPS_PATH'))
        d.exec_()

    def send_to_custom_data(self):
        pass
        def temp():
            for ix in ui.treeWidget.selectedIndexes():
                text = ix.data()  # or ix.data()
                np.savetxt(ui.save_as_LE.text() + '.csv',
                           ApplicationSettings.ALL_DATA_PLOTTED[text][0]._xy, delimiter=',')
        dialog = QtWidgets.QDialog()
        ui = STC_ui()
        ui.setupUi(dialog)
        dict = ApplicationSettings.ALL_DATA_PLOTTED
        Key_List = []
        for i in dict.keys():
            Key_List.append(QtWidgets.QTreeWidgetItem([i]))
        ui.treeWidget.addTopLevelItems(Key_List)
        ui.buttonBox.accepted.connect(lambda: temp())
        dialog.exec_()

    def new_project(self):
        def new_pro(project_name):
            os.makedirs(os.path.join(project_name,ui.project_le.text()))
            os.makedirs(os.path.join(project_name,ui.project_le.text(),'Data'))
            os.makedirs(os.path.join(project_name, ui.project_le.text(), 'Saved'))
            project_path = os.path.join(project_name, ui.project_le.text())

            self.settings.setValue('PROJECT_PATH',project_path)
            self.settings.setValue('SAVED_DATA_PATH', os.path.join(project_path,'Saved'))
            self.settings.setValue('DATA_PATH', os.path.join(project_path, 'Data'))
        dialog_path = QtWidgets.QFileDialog.getExistingDirectory()
        d = QtWidgets.QDialog()
        ui = new_project_dialog()
        ui.setupUi(d)
        ui.buttonBox.accepted.connect(lambda: new_pro(dialog_path))
        d.exec_()

    def open_project(self):
        dialog = QtWidgets.QFileDialog.getExistingDirectory()
        self.settings.setValue('PROJECT_PATH', dialog)

    def load_data(self):
        temp = self.settings.value()
        key_list = [i for i in temp.keys()]
        for i in key_list:
            data = temp[i][0]._xy.T
            self.ax.plot(data[0],data[1])
        self.canvas.draw()

    def import_file(self):
        filepath = QtWidgets.QFileDialog.getOpenFileName()[0]
        try:
            filename = os.path.basename(filepath)
            datapath = self.settings.value('DATA_PATH')
            copy2(filepath, os.path.join(datapath,filename))
        except FileNotFoundError:
            pass

    def import_directiory_function(self):
        src_directory = QtWidgets.QFileDialog.getExistingDirectory()
        dirname = src_directory.split('/')[-1]
        print(os.path.join(self.settings.value('DATA_PATH'),dirname))
        copytree(src_directory,os.path.join(self.settings.value('DATA_PATH'),dirname))

    def plot_annotation(self):
        def finish():
            spot = [np.average(ApplicationSettings.C_X_LIM),np.average(ApplicationSettings.C_Y_LIM)]
            self.ax.annotate(ui.text_le.text(),xy=(spot[0],spot[1])).draggable()
            self.canvas.draw()
        d = QtWidgets.QDialog()
        ui = annotation_ui()
        ui.setupUi(d)
        ui.buttonBox.accepted.connect(lambda: finish())
        d.exec_()

    def bar_graph(self):
        def plot_bar():
            N = ui.num_sb.value()
            xlist = ui.x_list.text().split(' ')
            ind = np.arange(N)
            width = float(ui.width_le.text())
            try:
                y1list_ = ui.y1_list.text().split(' ')
                y1list = [float(i) for i in y1list_]
                self.ax.bar(ind, y1list, width, label=ui.label1_le.text())
            except ValueError:
                print('ValueError')
            try:
                y2list_ = ui.y2_list.text().split(' ')
                y2list = [float(i) for i in y2list_]
                self.ax.bar(ind+width, y2list, width, label=ui.label2_le.text())
            except ValueError:
                print('ValueError')
            try:
                y3list_ = ui.y3_list.text().split(' ')
                y3list = [float(i) for i in y3list_]
                self.ax.bar(ind+width+width, y3list, width, label=ui.label3_le.text())
            except ValueError:
                print('ValueError')
            self.bar['xlist'] = ui.x_list.text()
            self.bar['y1list'] = ui.y1_list.text()
            self.bar['y2list'] = ui.y2_list.text()
            self.bar['y3list'] = ui.y3_list.text()
            self.bar['label1'] = ui.label1_le.text()
            self.bar['label2'] = ui.label2_le.text()
            self.bar['label3'] = ui.label3_le.text()
            self.bar['width'] = ui.width_le.text()
            self.bar['num'] = ui.num_sb.value()
            self.ax.set_xticks(ind + width / N, xlist)
            self.ax.legend(loc='best')
            self.canvas.draw()
        d = QtWidgets.QDialog()
        ui = bar_dialog()
        ui.setupUi(d)
        ui.x_list.setText(self.bar['xlist'])
        ui.y1_list.setText(self.bar['y1list'])
        ui.y2_list.setText(self.bar['y2list'])
        ui.y3_list.setText(self.bar['y3list'])
        ui.label1_le.setText(self.bar['label1'])
        ui.label2_le.setText(self.bar['label2'])
        ui.label3_le.setText(self.bar['label3'])
        ui.width_le.setText(self.bar['width'])
        ui.num_sb.setValue(self.bar['num'])
        ui.buttonBox.accepted.connect(lambda: plot_bar())
        d.exec_()
