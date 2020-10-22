# from matplotlib.figure import Figure
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# import numpy as np
# from PySide2 import QtWidgets
# from PySide2 import QtCore
# from Ui_Files.Dialogs.FigureName import Ui_Dialog as Figure_Dialog
# # from gui_elements.views.plotting_view import PlottingView
# # from Austin_Tests.UI_Files.Canvas_Dialog import Ui_Dialog
# import glob
#
#
# def save_fig(self,fig):
#     # fig_dict['practice']=fig
#     pass
#
# def restoreDock(self,view):
#     self.restoreDockWidget(view)
#     print(view)
#
# @QtCore.Slot()
# def plot_rand(graph, fig, ax, canvas):
#     # for the plotting in central window add
#     # fig = fig_dict[item.text()]
#     # graph.canvas = FigureCanvas(fig)
#     graph.ui.verticalLayout.addWidget(canvas)
#     x = np.linspace(0, 10, 101)
#     ax.plot(x, np.random.rand(101))
#     canvas.draw()
#
#
# def addfig(graph, fig_dict, ax_dict):
#     dialog_figname = QtWidgets.QDialog()
#     dialog_figname.setObjectName('fig_list')
#     dialog_figname_ui = Figure_Dialog()
#     dialog_figname_ui.setupUi(dialog_figname)
#     dialog_figname.exec_()
#
#     fig = Figure()
#     ax = fig.add_subplot(111)
#
#     fig_dict[dialog_figname_ui.lineEdit.text()] = fig
#     ax_dict[dialog_figname_ui.lineEdit.text()] = ax
#     graph.main_window.ui_LW.listWidget.addItem(dialog_figname_ui.lineEdit.text())
#
#     graph.main_window.ui_FTIR.treeWidget.addItem(dialog_figname_ui.lineEdit.text())
#
#
#
# def addmpl(graph, fig):
#     graph.canvas = FigureCanvas(fig)
#     graph.ui.verticalLayout.addWidget(graph.canvas)
#     graph.canvas.draw()
#     # graph.toolbar = NavigationToolbar(graph.canvas,
#     #                                  graph, coordinates=True)
#     # graph.addToolBar(graph.toolbar)
#
#
# def rmmpl(graph):
#     graph.ui.verticalLayout.removeWidget(graph.canvas)
#     graph.canvas.close()
#     # graph.ui_Plot_Widget.plot_layout.removeWidget(graph.toolbar)
#     # graph.ui.ui_Plot_Widget.verticalLayout.removeWidget(graph.toolbar)
#
#     # PlottingView.toolbar.close()
#
#
#
# def find_nearest(self, array, value):
#     array = np.asarray(array)
#     idx = (np.abs(array - value)).argmin()
#     return idx, array[idx]
#
# def opendirectoryorfile(self, combotext, filename, from_spectra, to_spectra):
#     try:
#         if combotext.currentText() == 'OpenDir' or combotext.currentText() == 'Open Dir':
#             txt = QtWidgets.QFileDialog.getExistingDirectory(self, "QFileDialog.getOpenFileName()")
#             filename.setText(txt)
#             loadcsv = sorted(glob.glob(filename.text() + '/*CSV'))
#             current_spectra = []
#             for csv in loadcsv:
#                 current_spectra.append(np.loadtxt(csv, delimiter=',', dtype='float'))
#                 to_spectra.setText(str(len(loadcsv)) + 1)
#                 from_spectra.setText('1')
#             return current_spectra
#         elif combotext.currentText() == 'OpenFile' or combotext.currentText() == 'Open File':
#             txt = QtWidgets.QFileDialog.getOpenFileName(self, 'Choose One File')
#             current_spectra = np.loadtxt(txt[0], dtype='float', delimiter=',')
#             filename.setText(txt[0])
#             to_spectra.setText('1')
#             from_spectra.setText('0')
#             return current_spectra
#
#     except:
#         print('Something Went Wrong')
#
# def grab_filename(self, filename):
#     current = np.loadtxt(filename.text(), delimiter=',').T
#     return current
#
# def openfile(self, filename):
#     try:
#         txt = QtWidgets.QFileDialog.getOpenFileName()
#         # current_spectra = np.loadtxt(txt[0], dtype='float', delimiter=',').T
#         # ax.plot(current_spectra[0],current_spectra[1])
#         filename.setText(txt[0])
#     except:
#         print('Something wrong with filename')
#     # return current_spectra
#
#
#
# def Clear_Graph(self, ax, canvas):
#     ax.clear()
#     try:
#         self.ax2.clear()
#     except:
#         print('No secondary axis')
#     canvas.draw()
#
# def make_photo(self, viewer):
#     viewer.setPhoto(QtGui.QPixmap('Images/Full_Reactor.jpg'))
#
# def Save_Current_Values(self, option_combo, make_sub_spectra, make_diff_spectra, make_abs_spectra):
#     # loadcsv = sorted(glob.glob(self.filename.text() + '/*CSV'))
#     if option_combo.currentText() == 'Sub':
#         spectra = make_sub_spectra()
#     elif option_combo.currentText() == 'Diff':
#         spectra = make_diff_spectra()
#     elif option_combo.currentText() == 'Abs':
#         spectra = make_abs_spectra()
#     # from_to = [int(self.from_spectra.text()),int(self.to_spectra.text())]
#     np.savetxt('spectra.csv', list(map(list, zip(*spectra))), delimiter=',')
#
# def clipboardchanged(self):
#     QtWidgets.QApplication.clipboard().text()
#
# def shirley_calculate(self, x, y, tol=1e-5, maxit=15):
#     """ S = specs.shirley_calculate(x,y, tol=1e-5, maxit=10)
#     Calculate the best auto-Shirley background S for a dataset (x,y). Finds the biggest peak
#     and then uses the minimum value either side of this peak as the terminal points of the
#     Shirley background.
#     The tolerance sets the convergence criterion, maxit sets the maximum number
#     of iterations.
#     """
#
#     # Make sure we've been passed arrays and not lists.
#     x = np.array(x)
#     y = np.array(y)
#
#     # Sanity check: Do we actually have data to process here?
#     if not (x.any() and y.any()):
#         print("specs.shirley_calculate: One of the arrays x or y is empty. Returning zero background.")
#         return np.zeros(x.shape)
#
#     # Next ensure the energy values are *decreasing* in the array,
#     # if not, reverse them.
#     if x[0] < x[-1]:
#         is_reversed = True
#         x = x[::-1]
#         y = y[::-1]
#     else:
#         is_reversed = False
#
#     # Locate the biggest peak.
#     maxidx = abs(y - np.amax(y)).argmin()
#
#     # It's possible that maxidx will be 0 or -1. If that is the case,
#     # we can't use this algorithm, we return a zero background.
#     if maxidx == 0 or maxidx >= len(y) - 1:
#         print("specs.shirley_calculate: Boundaries too high for algorithm: returning a zero background.")
#         return np.zeros(x.shape)
#
#     # Locate the minima either side of maxidx.
#     lmidx = abs(y[0:maxidx] - np.amin(y[0:maxidx])).argmin()
#     rmidx = abs(y[maxidx:] - np.amin(y[maxidx:])).argmin() + maxidx
#     xl = x[lmidx]
#     yl = y[lmidx]
#     xr = x[rmidx]
#     yr = y[rmidx]
#
#     # Max integration index
#     imax = rmidx - 1
#
#     # Initial value of the background shape B. The total background S = yr + B,
#     # and B is equal to (yl - yr) below lmidx and initially zero above.
#     B = np.zeros(x.shape)
#     B[:lmidx] = yl - yr
#     Bnew = B.copy()
#
#     it = 0
#     while it < maxit:
#         # if DEBUG:
#         #     print("Shirley iteration: ", it)
#         # Calculate new k = (yl - yr) / (int_(xl)^(xr) J(x') - yr - B(x') dx')
#         ksum = 0.0
#         for i in range(lmidx, imax):
#             ksum += (x[i] - x[i + 1]) * 0.5 * (y[i] + y[i + 1]
#                                                - 2 * yr - B[i] - B[i + 1])
#         k = (yl - yr) / ksum
#         # Calculate new B
#         for i in range(lmidx, rmidx):
#             ysum = 0.0
#             for j in range(i, imax):
#                 ysum += (x[j] - x[j + 1]) * 0.5 * (y[j] +
#                                                    y[j + 1] - 2 * yr - B[j] - B[j + 1])
#             Bnew[i] = k * ysum
#         # If Bnew is close to B, exit.
#         if norm(Bnew - B) < tol:
#             B = Bnew.copy()
#             break
#         else:
#             B = Bnew.copy()
#         it += 1
#
#     if it >= maxit:
#         print("specs.shirley_calculate: Max iterations exceeded before convergence.")
#     if is_reversed:
#         return (yr + B)[::-1]
#     else:
#         return yr + B
#
# def plot_initial(self):
#     starting_guess_3 = [float(self.amplitude_1.text()), float(self.fwhm_1.text()) / 2.3584,
#                         float(self.position_wn_1.text()), float(self.amplitude_2.text()),
#                         float(self.fwhm_2.text()) / 2.3584,
#                         float(self.position_wn_2.text()), float(self.amplitude_3.text()),
#                         float(self.fwhm_3.text()) / 2.3584,
#                         float(self.position_wn_3.text()), 0]
#
#     def g_1(x, a, s, m, i):
#         return i + a / (s * (3.1415926 * 2) ** (1 / 2)) * np.exp(-((x - m) ** 2 / (2 * (s ** 2))))
#
#     def g_2(x, a1, s1, m1, a2, s2, m2, i):
#         return a1 / (s1 * (3.1415926 * 2) ** (1 / 2)) * np.exp(-((x - m1) ** 2 / (2 * (s1 ** 2)))) + \
#                a2 / (s2 * (3.1415926 * 2) ** (1 / 2)) * np.exp(-((x - m2) ** 2 / (2 * (s2 ** 2)))) + i
#
#     def g_3(x, a1, s1, m1, a2, s2, m2, a3, s3, m3, i):
#         return a1 / (s1 * (3.1415926 * 2) ** (1 / 2)) * np.exp(-((x - m1) ** 2 / (2 * (s1 ** 2)))) + \
#                a2 / (s2 * (3.1415926 * 2) ** (1 / 2)) * np.exp(-((x - m2) ** 2 / (2 * (s2 ** 2)))) + \
#                a3 / (s3 * (3.1415926 * 2) ** (1 / 2)) * np.exp(-((x - m3) ** 2 / (2 * (s3 ** 2)))) + i
#
#     x_data = np.arange(400, 4000, 1)
#
#     self.ax.plot(x_data,
#                  g_3(x_data, starting_guess_3[0], starting_guess_3[1], starting_guess_3[2], starting_guess_3[3],
#                      starting_guess_3[4], starting_guess_3[5], starting_guess_3[6], starting_guess_3[7],
#                      starting_guess_3[8], starting_guess_3[9]))
#     self.canvas.draw()
#
# def smooth(self, smooth_combo, current_spectra, ax, canvas, figure):
#     if smooth_combo.currentText() == 'Smooth On':
#         ax.clear()
#         for s in range(len(current_spectra) - 1):
#             ax.plot(current_spectra[0], signal.savgol_filter(current_spectra[s + 1], 53, 5))
#         # self.ax.set_xlim(int(self.X_Range_Max.text()), int(self.X_Range_Min.text()))
#         # self.ax.set_ylim(int(self.Y_Range_Min.text()), int(self.Y_Range_Max.text()))
#         ax.set_ylabel('Absorbance')
#         ax.set_xlabel('Wavenumber $cm^{-1}$')
#         ax.set_xlim(auto=True)
#         ax.invert_xaxis()
#         ax.set_ylim(auto=True)
#         figure.tight_layout()
#         canvas.draw()
#     else:
#         print('Smooth Off')
#
# def axis_tight(self, ax, canvas, spectra, xmin, xmax, ymin, ymax):
#     ax.set_xlim(xmin=np.amin(spectra[0]), xmax=np.amax(spectra[0]))
#     xmin.setText(str(int(np.amin(spectra[0]))))
#     xmax.setText(str(int(np.amax(spectra[0]))))
#     ax.set_ylim(ymin=np.amin(spectra[1::]), ymax=np.amax(spectra[1::]))
#     ymin.setText(str(int(np.amin(spectra[1::]))))
#     ymax.setText(str(int(np.amax(spectra[1::]))))
#     canvas.draw()
#
# def fit_report_message(self, fit_report):
#     fit_report_box = QtWidgets.QMessageBox()
#     fit_report_box.setText(fit_report)
#     fit_report_box.exec()