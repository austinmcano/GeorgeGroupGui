from PySide2 import QtCore
from src.Ui_Files.DockWidgets.dw_FTIR import Ui_DockWidget
from src.gui_elements.RC_Fucntions import *
from src.gui_elements.Plotting_Functions import subtraction_from_survey
import glob
from scipy.signal import savgol_filter
from lmfit.models import VoigtModel, GaussianModel, LorentzianModel, LinearModel
from lmfit import Model, Parameters
from src.Ui_Files.Dialogs.simple_treeWidget_dialog import Ui_Dialog as twDialog_ui

class FTIR_view(QtWidgets.QDockWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.ui = Ui_DockWidget()
        self.ui.setupUi(self)

        self._init_vars()
        self._init_widgets()
        self._init_UI()

    def _init_vars(self):
        self.current_data_container = None
        self.sub = None
        self.diff = None
        self.model = None
        self.data = None
        self.data_x = None
        self.data_y = None
        self.constraints = np.asarray(
            [[10, -1000, 1000, 3700, 400, 4000, 50, 1, 400], [10, -1000, 2900, 285, 400, 4000, 50, 1, 400],
             [1, -1000, 1000, 2890, 400, 4000, 50, 1, 400], [10, -1000, 1000, 1215, 400, 4000, 50, 1, 400],
             [10, -1000, 1000, 900, 400, 4000, 50, 1, 400]])
        for row in range(9):
            for column in range(5):
                self.ui.tableWidget_2.setItem(row, column, QtWidgets.QTableWidgetItem(str(self.constraints[column][row])))

    def _init_widgets(self):
        self.tree_view = self.ui.FTIR_treeView
        self.context_menu = QtWidgets.QMenu(self)
        # Create context menu
        rc_browser_options(self)

    def _init_UI(self):
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath('')

        self.tree_view.setModel(self.model)
        self.tree_view.setSortingEnabled(True)

        # self.tree_view.sortByColumn(True)
        self.tree_view.setRootIndex(self.model.index(self.main_window.settings.value('FTIR_PATH')))
        self.tree_view.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

        self.tree_view.setModel(self.model)
        self.tree_view.installEventFilter(self)
        self.tree_view.setColumnWidth(0, 200)

        self.ui.pushButton.clicked.connect(lambda: self.ir_plot())
        self.ui.smooth_pb.clicked.connect(lambda: self.smooth())
        self.ui.integrate_pb.clicked.connect(lambda: self.integrate())
        # self.ui.

        self.ui.fit_pb.clicked.connect(lambda: self.fitting_function())
        self.ui.plot_current_pb.clicked.connect(lambda: self.plot_init())
        self.ui.tableWidget_2.cellChanged.connect(lambda: self.save_constraints())
        self.ui.selectdata_pb.clicked.connect(lambda: self.select_data())


    def eventFilter(self, object, event):
        # For right click events
        if event.type() == QtCore.QEvent.ContextMenu:
            self.context_menu.exec_(self.mapToGlobal(event.pos()))
        return False

    # def pick_data(self):
    #     dialog = QtWidgets.QDialog()
    #     ui = STC_ui()
    #     ui.setupUi(dialog)
    #     dict = ApplicationSettings.ALL_DATA_PLOTTED
    #     Key_List = []
    #     for i in dict.keys():
    #         Key_List.append(QtWidgets.QTreeWidgetItem([i]))
    #     ui.treeWidget.addTopLevelItems(Key_List)
    #     # ui.buttonBox.accepted.connect(lambda: temp())
    #     ui.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
    #     dialog.exec_()

    def save_constraints(self):
        try:
            for row in range(9):
                for column in range(5):
                    self.constraints[column][row] = float(self.ui.tableWidget_2.item(row, column).text())
        except ValueError:
            print('No constraint save')

    def fitting_function(self):
        self.main_window.cleargraph()
        self.save_constraints()
        con = self.constraints
        #  Y is data[0]..... whyyyyyyy x is data[1]
        linearmod = LinearModel()

        if self.ui.fit_shape_cb.currentText() == 'Gaussian':
            if self.ui.num_peaks_sb.value() == 1:
                gmodel = GaussianModel()
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('amplitude', con[0][0], True, con[0][1], con[0][2]),
                                ('center', con[0][3], True, con[0][4], con[0][5]),
                                ('sigma', con[0][6], True, con[0][7], con[0][8]))
                result = gmodel.fit(self.data_y, params, x=self.data_x)
                self.ui.fit_report_TE.setText(result.fit_report())
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')

            elif self.ui.num_peaks_sb.value() == 2:
                gmodel = GaussianModel(prefix='p1_') + GaussianModel(prefix='p2_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amplitude', con[0][0], True, con[0][1], con[0][2]),
                                ('p1_center', con[0][3], True, con[0][4], con[0][5]),
                                ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
                                ('p2_amplitude', con[1][0], True, con[1][1], con[1][2]),
                                ('p2_center', con[1][3], True, con[1][4], con[1][5]),
                                ('p2_sigma', con[1][6], True, con[1][7], con[1][8]))
                result = gmodel.fit(self.data_y, params, x=self.data_x)
                comps = result.eval_components()
                self.ui.fit_report_TE.setText(result.fit_report())
                ApplicationSettings.ALL_DATA_PLOTTED['G1'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p1_'],
                                                                                      'k--', label='G1')
                ApplicationSettings.ALL_DATA_PLOTTED['G2'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p2_'],
                                                                                      'k--', label='G2')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
                leg = self.main_window.ax.legend(loc='best', fontsize='small')
                leg.set_draggable(True)

            elif self.ui.num_peaks_sb.value() == 3:
                gmodel = GaussianModel(prefix='p1_') + GaussianModel(prefix='p2_') + Model(prefix='p3_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amplitude', con[0][0], True, con[0][1], con[0][2]),
                                ('p1_center', con[0][3], True, con[0][4], con[0][5]),
                                ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
                                ('p2_amplitude', con[1][0], True, con[1][1], con[1][2]),
                                ('p2_center', con[1][3], True, con[1][4], con[1][5]),
                                ('p2_sigma', con[1][6], True, con[1][7], con[1][8]),
                                ('p3_amplitude', con[2][0], True, con[2][1], con[2][2]),
                                ('p3_center', con[2][3], True, con[2][4], con[2][5]),
                                ('p3_sigma', con[2][6], True, con[2][7], con[2][8]))
                result = gmodel.fit(self.data_y, params, x=self.data_x)
                comps = result.eval_components()
                ApplicationSettings.ALL_DATA_PLOTTED['G1'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p1_'],
                                                                                      'k--', label='G1')
                ApplicationSettings.ALL_DATA_PLOTTED['G2'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p2_'],
                                                                                      'k--', label='G2')
                ApplicationSettings.ALL_DATA_PLOTTED['G3'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p3_'],
                                                                                      'k--', label='G3')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
                self.ui.fit_report_TE.setText(result.fit_report())

            elif self.ui.num_peaks_sb.value() == 4:
                gmodel = GaussianModel(prefix='p1_') + GaussianModel(prefix='p2_') + \
                         GaussianModel(prefix='p3_') + GaussianModel(prefix='p4_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amplitude', con[0][0], True, con[0][1], con[0][2]),
                                ('p1_center', con[0][3], True, con[0][4], con[0][5]),
                                ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
                                ('p2_amplitude', con[1][0], True, con[1][1], con[1][2]),
                                ('p2_center', con[1][3], True, con[1][4], con[1][5]),
                                ('p2_sigma', con[1][6], True, con[1][7], con[1][8]),
                                ('p3_amplitude', con[2][0], True, con[2][1], con[2][2]),
                                ('p3_center', con[2][3], True, con[2][4], con[2][5]),
                                ('p3_sigma', con[2][6], True, con[2][7], con[2][8]),
                                ('p4_amplitude', con[3][0], True, con[3][1], con[3][2]),
                                ('p4_center', con[3][3], True, con[3][4], con[3][5]),
                                ('p4_sigma', con[3][6], True, con[3][7], con[3][8]))
                result = gmodel.fit(self.data_y, params, x=self.data_x)
                comps = result.eval_components()
                ApplicationSettings.ALL_DATA_PLOTTED['G1'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p1_'],
                                                                                      'k--', label='G1')
                ApplicationSettings.ALL_DATA_PLOTTED['G2'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p2_'],
                                                                                      'k--', label='G2')
                ApplicationSettings.ALL_DATA_PLOTTED['G3'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p3_'],
                                                                                      'k--', label='G3')
                ApplicationSettings.ALL_DATA_PLOTTED['G4'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p4_'],
                                                                                      'k--', label='G4')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
                leg = self.main_window.ax.legend(loc='best', fontsize='small')
                leg.set_draggable(True)
                self.ui.fit_report_TE.setText(result.fit_report())

            elif self.ui.num_peaks_sb.value() == 5:

                gmodel = GaussianModel(prefix='p1_') + GaussianModel(prefix='p2_') + \
                         GaussianModel(prefix='p3_') + GaussianModel(prefix='p4_') + GaussianModel(prefix='p5_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amplitude', con[0][0], True, con[0][1], con[0][2]),
                                ('p1_center', con[0][3], True, con[0][4], con[0][5]),
                                ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
                                ('p2_amplitude', con[1][0], True, con[1][1], con[1][2]),
                                ('p2_center', con[1][3], True, con[1][4], con[1][5]),
                                ('p2_sigma', con[1][6], True, con[1][7], con[1][8]),
                                ('p3_amplitude', con[2][0], True, con[2][1], con[2][2]),
                                ('p3_center', con[2][3], True, con[2][4], con[2][5]),
                                ('p3_sigma', con[2][6], True, con[2][7], con[2][8]),
                                ('p4_amplitude', con[3][0], True, con[3][1], con[3][2]),
                                ('p4_center', con[3][3], True, con[3][4], con[3][5]),
                                ('p4_sigma', con[3][6], True, con[3][7], con[3][8]),
                                ('p5_amplitude', con[4][0], True, con[4][1], con[4][2]),
                                ('p5_center', con[4][3], True, con[4][4], con[4][5]),
                                ('p5_sigma', con[4][6], True, con[4][7], con[4][8]))
                result = gmodel.fit(self.data_y, params, x=self.data_x)
                comps = result.eval_components()
                ApplicationSettings.ALL_DATA_PLOTTED['G1'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p1_'],
                                                                                      'k--', label='G1')
                ApplicationSettings.ALL_DATA_PLOTTED['G2'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p2_'],
                                                                                      'k--', label='G2')
                ApplicationSettings.ALL_DATA_PLOTTED['G3'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p3_'],
                                                                                      'k--', label='G3')
                ApplicationSettings.ALL_DATA_PLOTTED['G4'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p4_'],
                                                                                      'k--', label='G4')
                ApplicationSettings.ALL_DATA_PLOTTED['G5'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p5_'],
                                                                                      'k--', label='G5')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
                self.ui.fit_report_TE.setText(result.fit_report())

        elif self.ui.fit_shape_cb.currentText() == 'Lorentz':
            if self.ui.num_peaks_sb.value() == 1:
                lmodel = LorentzianModel()
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('amplitude', con[0][0], True, con[0][1], con[0][2]),
                                ('center', con[0][3], True, con[0][4], con[0][5]),
                                ('sigma', con[0][6], True, con[0][7], con[0][8]), )
                result = lmodel.fit(self.data_y, params, x=self.data_x)
                self.ui.fit_report_TE.setText(result.fit_report())
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
                leg = self.main_window.ax.legend(loc='best', fontsize='small')
                leg.set_draggable(True)
            elif self.ui.num_peaks_sb.value() == 2:
                lmodel = LorentzianModel(prefix='p1_') + LorentzianModel(prefix='p2_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amplitude', con[0][0], True, con[0][1], con[0][2]),
                                ('p1_center', con[0][3], True, con[0][4], con[0][5]),
                                ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
                                ('p2_amplitude', con[1][0], True, con[1][1], con[1][2]),
                                ('p2_center', con[1][3], True, con[1][4], con[1][5]),
                                ('p2_sigma', con[1][6], True, con[1][7], con[1][8]))
                result = lmodel.fit(self.data_y, params, x=self.data_x)
                comps = result.eval_components()
                self.ui.fit_report_TE.setText(result.fit_report())
                ApplicationSettings.ALL_DATA_PLOTTED['L1'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p1_'],
                                                                                      'k--', label='L1')
                ApplicationSettings.ALL_DATA_PLOTTED['L2'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p2_'],
                                                                                      'k--', label='L2')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
                leg = self.main_window.ax.legend(loc='best', fontsize='small')
                leg.set_draggable(True)

        elif self.ui.fit_shape_cb.currentText() == 'Voigt':
            if self.ui.num_peaks_sb.value() == 1:
                vmodel = VoigtModel()
                params = Parameters()
                params.add_many(('amplitude', con[0][0], True, con[0][1], con[0][2]),
                                ('center', con[0][3], True, con[0][4], con[0][5]),
                                ('sigma', con[0][6], True, con[0][7], con[0][8]))
                result = vmodel.fit(self.data_y, params, x=self.data_x)
                # self.ui.fit_report_TE.setText(result.fit_report())
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
            elif self.ui.num_peaks_sb.value() == 2:
                vmodel = VoigtModel(prefix='p1_') + VoigtModel(prefix='p2_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amplitude', con[0][0], True, con[0][1], con[0][2]),
                                ('p1_center', con[0][3], True, con[0][4], con[0][5]),
                                ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
                                ('p2_amplitude', con[1][0], True, con[1][1], con[1][2]),
                                ('p2_center', con[1][3], True, con[1][4], con[1][5]),
                                ('p2_sigma', con[1][6], True, con[1][7], con[1][8]))
                result = vmodel.fit(self.data_y, params, x=self.data_x)
                comps = result.eval_components()
                self.ui.fit_report_TE.setText(result.fit_report())
                ApplicationSettings.ALL_DATA_PLOTTED['V1'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p1_'],
                                                                                      'k--', label='V1')
                ApplicationSettings.ALL_DATA_PLOTTED['V2'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p2_'],
                                                                                      'k--', label='V2')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
            elif self.ui.num_peaks_sb.value() == 3:
                vmodel = VoigtModel(prefix='p1_') + VoigtModel(prefix='p2_') + VoigtModel(prefix='p3_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amplitude', con[0][0], True, con[0][1], con[0][2]),
                                ('p1_center', con[0][3], True, con[0][4], con[0][5]),
                                ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
                                ('p2_amplitude', con[1][0], True, con[1][1], con[1][2]),
                                ('p2_center', con[1][3], True, con[1][4], con[1][5]),
                                ('p2_sigma', con[1][6], True, con[1][7], con[1][8]),
                                ('p3_amplitude', con[2][0], True, con[2][1], con[2][2]),
                                ('p3_center', con[2][3], True, con[2][4], con[2][5]),
                                ('p3_sigma', con[2][6], True, con[2][7], con[2][8]))
                result = vmodel.fit(self.data_y, params, x=self.data_x)
                comps = result.eval_components()
                ApplicationSettings.ALL_DATA_PLOTTED['V1'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p1_'],
                                                                                      'k--', label='V1')
                ApplicationSettings.ALL_DATA_PLOTTED['V2'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p2_'],
                                                                                      'k--', label='V2')
                ApplicationSettings.ALL_DATA_PLOTTED['V3'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p3_'],
                                                                                      'k--', label='V3')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
                self.ui.fit_report_TE.setText(result.fit_report())
            elif self.ui.num_peaks_sb.value() == 4:
                vmodel = VoigtModel(prefix='p1_') + VoigtModel(prefix='p2_') + \
                         VoigtModel(prefix='p3_') + VoigtModel(prefix='p4_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amplitude', con[0][0], True, con[0][1], con[0][2]),
                                ('p1_center', con[0][3], True, con[0][4], con[0][5]),
                                ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
                                ('p2_amplitude', con[1][0], True, con[1][1], con[1][2]),
                                ('p2_center', con[1][3], True, con[1][4], con[1][5]),
                                ('p2_sigma', con[1][6], True, con[1][7], con[1][8]),
                                ('p3_amplitude', con[2][0], True, con[2][1], con[2][2]),
                                ('p3_center', con[2][3], True, con[2][4], con[2][5]),
                                ('p3_sigma', con[2][6], True, con[2][7], con[2][8]),
                                ('p4_amplitude', con[3][0], True, con[3][1], con[3][2]),
                                ('p4_center', con[3][3], True, con[3][4], con[3][5]),
                                ('p4_sigma', con[3][6], True, con[3][7], con[3][8]))
                result = vmodel.fit(self.data_y, params, x=self.data_x)
                comps = result.eval_components()
                ApplicationSettings.ALL_DATA_PLOTTED['V1'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p1_'],
                                                                                      'k--', label='V1')
                ApplicationSettings.ALL_DATA_PLOTTED['V2'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p2_'],
                                                                                      'k--', label='V2')
                ApplicationSettings.ALL_DATA_PLOTTED['V3'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p3_'],
                                                                                      'k--', label='V3')
                ApplicationSettings.ALL_DATA_PLOTTED['V4'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p4_'],
                                                                                      'k--', label='V4')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
                leg = self.main_window.ax.legend(loc='best', fontsize='small')
                leg.set_draggable(True)
                self.ui.fit_report_TE.setText(result.fit_report())
            elif self.ui.num_peaks_sb.value() == 5:
                vmodel = VoigtModel(prefix='p1_') + VoigtModel(prefix='p2_') + \
                         VoigtModel(prefix='p3_') + VoigtModel(prefix='p4_') + VoigtModel(prefix='p5_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amplitude', con[0][0], True, con[0][1], con[0][2]),
                                ('p1_center', con[0][3], True, con[0][4], con[0][5]),
                                ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
                                ('p2_amplitude', con[1][0], True, con[1][1], con[1][2]),
                                ('p2_center', con[1][3], True, con[1][4], con[1][5]),
                                ('p2_sigma', con[1][6], True, con[1][7], con[1][8]),
                                ('p3_amplitude', con[2][0], True, con[2][1], con[2][2]),
                                ('p3_center', con[2][3], True, con[2][4], con[2][5]),
                                ('p3_sigma', con[2][6], True, con[2][7], con[2][8]),
                                ('p4_amplitude', con[3][0], True, con[3][1], con[3][2]),
                                ('p4_center', con[3][3], True, con[3][4], con[3][5]),
                                ('p4_sigma', con[3][6], True, con[3][7], con[3][8]),
                                ('p5_amplitude', con[4][0], True, con[4][1], con[4][2]),
                                ('p5_center', con[4][3], True, con[4][4], con[4][5]),
                                ('p5_sigma', con[4][6], True, con[4][7], con[4][8]))
                result = vmodel.fit(self.data_y, params, x=self.data_x)
                comps = result.eval_components()
                ApplicationSettings.ALL_DATA_PLOTTED['V1'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p1_'],
                                                                                      'k--', label='V1')
                ApplicationSettings.ALL_DATA_PLOTTED['V2'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p2_'],
                                                                                      'k--', label='V2')
                ApplicationSettings.ALL_DATA_PLOTTED['V3'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p3_'],
                                                                                      'k--', label='V3')
                ApplicationSettings.ALL_DATA_PLOTTED['V4'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p4_'],
                                                                                      'k--', label='V4')
                ApplicationSettings.ALL_DATA_PLOTTED['V5'] = self.main_window.ax.plot(self.data_x,
                                                                                      comps['p5_'],
                                                                                      'k--', label='V5')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit,
                                                                                       'r--', label='Result')
                self.ui.fit_report_TE.setText(result.fit_report())

        ApplicationSettings.ALL_DATA_PLOTTED['Y Data'] = self.main_window.ax.plot(self.data_x, self.data_y)
        self.ir_basic()

    def select_data(self):
        def finish():
            key = ui.treeWidget.currentItem().text(0)
            self.data_x = dict[key]._xy.T[0]
            self.data_y = dict[key]._xy.T[1]
            x_lim = ApplicationSettings.C_X_LIM
            indexs = [find_nearest(self.data_x, x_lim[1]), find_nearest(self.data_x, x_lim[0])]
            self.data_x = self.data_x[indexs[0]:indexs[1]]
            self.data_y = self.data_y[indexs[0]:indexs[1]]
        dialog = QtWidgets.QDialog()
        ui = twDialog_ui()
        ui.setupUi(dialog)
        dict = ApplicationSettings.ALL_DATA_PLOTTED
        Key_List = []
        for i in dict.keys():
            Key_List.append(QtWidgets.QTreeWidgetItem([i]))
        ui.treeWidget.addTopLevelItems(Key_List)
        ui.buttonBox.accepted.connect(lambda: finish())
        dialog.exec_()

    def save_constraints(self):
        try:
            for row in range(9):
                for column in range(5):
                    self.constraints[column][row] = float(self.ui.tableWidget_2.item(row, column).text())
        except ValueError:
            print('No constraint save')

    def plot_init(self):
        self.main_window.cleargraph()
        con = self.constraints
        if self.ui.num_peaks_sb.value() == 1:
            start_plot = gaussian(self.data_x,con[0][0],con[0][3],con[0][6])
        elif self.ui.num_peaks_sb.value() == 2:
            start_plot = gaussian(self.data_x, con[0][0], con[0][3], con[0][6])+gaussian(self.data_x, con[1][0], con[1][3], con[1][6])
        elif self.ui.num_peaks_sb.value() == 3:
            start_plot = gaussian(self.data_x, con[0][0], con[0][3], con[0][6])+\
                         gaussian(self.data_x, con[1][0], con[1][3], con[1][6])+\
                         gaussian(self.data_x, con[2][0], con[2][3], con[2][6])
        elif self.ui.num_peaks_sb.value() == 4:
            start_plot = gaussian(self.data_x, con[0][0], con[0][3], con[0][6]) + \
                         gaussian(self.data_x, con[1][0], con[1][3], con[1][6]) + \
                         gaussian(self.data_x, con[2][0], con[2][3], con[2][6]) + \
                         gaussian(self.data_x, con[3][0], con[3][3], con[3][6])
        elif self.ui.num_peaks_sb.value() == 5:
            start_plot = gaussian(self.data_x, con[0][0], con[0][3], con[0][6]) + \
                         gaussian(self.data_x, con[1][0], con[1][3], con[1][6]) + \
                         gaussian(self.data_x, con[2][0], con[2][3], con[2][6]) + \
                         gaussian(self.data_x, con[3][0], con[3][3], con[3][6]) + \
                         gaussian(self.data_x, con[4][0], con[4][3], con[4][6])


        ApplicationSettings.ALL_DATA_PLOTTED['Y_Data'] = self.main_window.ax.plot(self.data_x,self.data_y)
        ApplicationSettings.ALL_DATA_PLOTTED['FTIR Init Values'] = \
            self.main_window.ax.plot(self.data_x,start_plot, '--k')
        self.ir_basic()

    def ir_plot(self):
        path = self.model.filePath(self.tree_view.currentIndex())
        # head, tail = os.path.split(path)
        combo = self.ui.ir_plot_cb.currentText()
        if combo == 'Plot':
            self.data = np.genfromtxt(path,delimiter=',').T
            self.x_data = self.data[0]
            self.y_data = self.data[1]
            ApplicationSettings.ALL_DATA_PLOTTED['FTIR'] = self.main_window.ax.plot(self.data[0],self.data[1],'-b',label='IR Plot')
        elif combo == 'Sub Plot (dir)':
            if os.path.isdir(path):
                csv_list = sorted(glob.glob(path + '/*CSV'))
                self.sub = subtraction_from_survey(csv_list)
                for i in range(0,len(self.sub)-1,self.ui.skip_sb.value()+1):
                    ApplicationSettings.ALL_DATA_PLOTTED['Sub_'+str(i)] = \
                        self.main_window.ax.plot(self.sub[0],self.sub[i+1],label='Sub_'+str(i))
        elif combo == 'Diff Plot (dir)':
            if os.path.isdir(path):
                csv_list = sorted(glob.glob(path + '/*CSV'))
                self.diff = difference_from_survey(csv_list)
                for i in range(0,len(self.diff)-1,self.ui.skip_sb.value()+1):
                    ApplicationSettings.ALL_DATA_PLOTTED['Diff_'+str(i)] = \
                        self.main_window.ax.plot(self.diff[0],self.diff[i+1],label='Diff_'+str(i))
        elif combo == 'Plot (dir)':
            if os.path.isdir(path):
                csv_list = sorted(glob.glob(path + '/*CSV'))
                data = []
                for csv in csv_list:
                    data.append(np.genfromtxt(csv, delimiter=',').T)
                self.data = [data[0][0]]
                for i in range(0,len(data),self.ui.skip_sb.value()+1):
                    self.data.append(data[i][1])
                for j in range(0,len(self.data)-1,self.ui.skip_sb.value()+1):
                    ApplicationSettings.ALL_DATA_PLOTTED['IR_'+str(j)] = \
                        self.main_window.ax.plot(self.data[0],self.data[j+1])

        elif combo == 'Diff (2)':
            pass
        self.ir_basic()

    def ir_basic(self):
        self.main_window.ax.set_xlim(4000, 400)
        self.main_window.ax.set_xlabel('Wavenumber ($cm^{-1}$)')
        self.main_window.ax.set_ylabel('Absorbance')
        self.main_window.fig.tight_layout()
        self.main_window.canvas.draw()

    def integrate(self):
        path = self.model.filePath(self.tree_view.currentIndex())
        csv_list = sorted(glob.glob(path + '/*CSV'))
        self.sub = subtraction_from_survey(csv_list)
        min_max = [[400,4000],[400,4000],[400,4000],[400,4000]]
        labels = ['','','','']
        for row in range(4):
            labels[row] = self.ui.tableWidget.item(row, 2).text()
            for column in range(2):
                min_max[row][column] = float(self.ui.tableWidget.item(row,column).text())
        print(labels)
        minimum = float(self.ui.tableWidget.item(0,0).text())
        maximum = float(self.ui.tableWidget.item(0, 1).text())
        num_of_int = self.ui.spinBox.value()

        if self.ui.comboBox.currentText()=='Left Axis':
            ax = self.main_window.ax
        elif self.ui.comboBox.currentText()=='Right Axis':
            if self.main_window.ax_2 is None:
                self.main_window.ax_2 = self.main_window.ax.twinx()
            ax = self.main_window.ax_2
        if self.ui.int_type_cb.currentText() == 'Integrate Plot (dir)':
            pass
        if self.ui.int_type_cb.currentText() == 'Integrate Sub (dir) Corrected':
            for i in range(num_of_int):
                self.sub = subtraction_from_survey(csv_list)
                inte = integrate_ir(self.sub, min_max[i][0], min_max[i][1])
                inte_c = [i-inte[0] for i in inte]
                ApplicationSettings.ALL_DATA_PLOTTED['Int. ' + str(minimum) + '-' + str(maximum)] = \
                    ax.plot(inte_c, '.-', label=labels[i] + str(minimum) + '-' + str(maximum))
        elif self.ui.int_type_cb.currentText() == 'Integrate Sub (dir)':
            for i in range(num_of_int):
                self.sub = subtraction_from_survey(csv_list)
                inte = integrate_ir(self.sub, min_max[i][0], min_max[i][1])
                ApplicationSettings.ALL_DATA_PLOTTED['Int. '+str(minimum)+'-'+str(maximum)] = \
                    ax.plot(inte,'.-',label='Int. '+str(minimum)+'-'+str(maximum))
        elif self.ui.int_type_cb.currentText() == 'Integrate Diff (dir)':
            for i in range(num_of_int):
                self.diff = difference_from_survey(csv_list)
                inte = integrate_ir(self.diff, min_max[i][0], min_max[i][1])
                ApplicationSettings.ALL_DATA_PLOTTED['Int. ' + str(minimum) + '-' + str(maximum)] = \
                    ax.plot(inte,'.-', label='Int. ' + str(minimum) + '-' + str(maximum))
        self.main_window.canvas.draw()

    def smooth(self):
        # keys = ApplicationSettings.ALL_DATA_PLOTTED.keys()
        self.main_window.cleargraph()
        if self.ui.ir_plot_cb.currentText() == 'Sub Plot (dir)':
            for i in range(len(self.sub)-1):
                ApplicationSettings.ALL_DATA_PLOTTED[str(i)+'sm_sub'] = self.main_window.ax.plot(self.sub[0],savgol_filter(self.sub[i+1], 51, 3))
        elif self.ui.ir_plot_cb.currentText() == 'Diff Plot (dir)':
            for i in range(len(self.diff)-1):
                ApplicationSettings.ALL_DATA_PLOTTED[str(i)+'sm_diff'] = self.main_window.ax.plot(self.diff[0],savgol_filter(self.diff[i+1], 51, 3))
        elif self.ui.ir_plot_cb.currentText() == 'Plot (dir)':
            for i in range(len(self.data) - 1):
                ApplicationSettings.ALL_DATA_PLOTTED[str(i) + 'sm_diff'] = self.main_window.ax.plot(self.data[0],
                                                                                                    savgol_filter(
                                                                                                        self.data[
                                                                                                            i + 1], 51,
                                                                                                        3))
        self.ir_basic()