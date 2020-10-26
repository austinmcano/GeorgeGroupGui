from src.Ui_Files.DockWidgets.dw_CF import Ui_DockWidget
from src.gui_elements.RC_Fucntions import *
from PySide2 import QtCore,QtWidgets
from src.Ui_Files.Dialogs.fit_dialog_cf import Ui_Dialog as fit_dialog
from lmfit import Model
from lmfit.models import GaussianModel,LorentzianModel,VoigtModel,LinearModel,ThermalDistributionModel,\
    PowerLawModel
import matplotlib.pyplot as plt
import src.gui_elements.Plotting_Functions

class CurveFit_view(QtWidgets.QDockWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.ui = Ui_DockWidget()
        self.ui.setupUi(self)
        self._init_vars()
        self._init_widgets()
        self._init_UI()
        self.cf_model = None
        self.cf_data = [[],[]]
        self.params = None
        self.function = None

    def _init_vars(self):
        self.current_data_container = None

    def _init_widgets(self):
        self.function_options = ['Gaussian', 'Lorentz', 'Voigt', 'Linear', 'ThermalDist', 'PowerLaw', 'Plateau']
        self.ui.function_cb.addItems(self.function_options)
        self.tree_view = self.ui.treeView
        self.context_menu = QtWidgets.QMenu(self)
        rc_browser_options(self)

    def _init_UI(self):
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath(QtCore.QDir.currentPath())
        self.ui.treeView.setModel(self.model)
        self.ui.treeView.setSortingEnabled(True)

        self.ui.treeView.sortByColumn(True)
        self.ui.treeView.setRootIndex(self.model.index(ApplicationSettings.PROJECT_PATH))
        self.ui.treeView.setModel(self.model)
        self.ui.treeView.installEventFilter(self)
        self.ui.treeView.setColumnWidth(0, 200)

        self.ui.import_pb.clicked.connect(lambda: self.import_to_table())
        self.ui.function_cb.currentTextChanged.connect(lambda: self.function_combo_changed())
        self.ui.tableWidget.itemActivated.connect(lambda: self.custom_data_event())
        self.ui.y_sb.valueChanged.connect(lambda: self.sb_change_event())
        self.ui.addx_pb.clicked.connect(lambda: self.add_x_values())
        self.ui.plot_pb.clicked.connect(lambda: self.plot_CF())
        self.ui.fit_data_pb.clicked.connect(lambda: self.fit_pb_clicked())

    def eventFilter(self, object, event):
        # For right click events
        if event.type() == QtCore.QEvent.ContextMenu:
            self.context_menu.exec_(self.mapToGlobal(event.pos()))
        return False

    def plot_CF(self):
        self.custom_data_event()
        ApplicationSettings.ALL_DATA_PLOTTED['data'] = self.main_window.ax.plot(self.cf_data[0],self.cf_data[1],
                                                                                '.',label='data')
        self.main_window.canvas.draw()

    def add_x_values(self):
        x_array = np.arange(0,self.ui.tableWidget.rowCount())
        for row in range(self.ui.tableWidget.rowCount()):
            self.ui.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(str(x_array[row])))
            self.cf_data[0] = x_array

    def sb_change_event(self):
        self.ui.tableWidget.setRowCount(self.ui.y_sb.value())

    def custom_data_event(self):
        self.cf_data = np.zeros((self.ui.tableWidget.columnCount(),self.ui.tableWidget.rowCount()))
        for row in range(self.ui.tableWidget.rowCount()):
            for column in range(self.ui.tableWidget.columnCount()):
                if self.ui.tableWidget.item(row, column) is None:
                    pass
                else:
                    self.cf_data[column][row] = float(self.ui.tableWidget.item(row, column).text())

    def function_combo_changed(self):
        pass

    def fit_pb_clicked(self):
        self.custom_data_event()
        self.function = self.ui.function_cb.currentText()
        def fun(function):
            if function == 'Linear':
                self.cf_model = LinearModel()
                self.params = self.cf_model.guess(np.asarray(self.cf_data[1]), x=np.asarray(self.cf_data[1]))
            elif function == 'Plateau':
                self.cf_model = Model(plateau)
                a = float(ui.a_le.text())
                b = float(ui.b_le.text())
                self.params = self.cf_model.make_params(a=a, b=b)
            elif function == 'self_limiting':
                self.cf_model = Model(self_limiting)
                a = float(ui.a_le.text())
                b = float(ui.b_le.text())
                c = float(ui.c_le.text())
                self.params = self.cf_model.make_params(a=a, b=b, c=c)
            elif function == 'Gaussian':
                self.cf_model = GaussianModel()
                self.params = self.cf_model.guess(np.asarray(self.cf_data[1]), x=np.asarray(self.cf_data[1]))
            elif function == 'Voigt':
                self.cf_model = VoigtModel()
                self.params = self.cf_model.guess(np.asarray(self.cf_data[1]), x=np.asarray(self.cf_data[1]))
            elif function == 'PowerLaw':
                self.cf_model = PowerLawModel()
                self.params = self.cf_model.guess(np.asarray(self.cf_data[1]), x=np.asarray(self.cf_data[1]))
            elif function == 'Lorentz':
                self.cf_model = LorentzianModel()
                self.params = self.cf_model.guess(np.asarray(self.cf_data[1]), x=np.asarray(self.cf_data[1]))
            x_data = np.linspace(ApplicationSettings.C_X_LIM[0],ApplicationSettings.C_X_LIM[1],101)
            result = self.cf_model.fit(self.cf_data[1], self.params, x=self.cf_data[0])
            self.ui.results_te.setText(result.fit_report())
            ApplicationSettings.ALL_DATA_PLOTTED['fit'] = self.main_window.ax.plot(x_data,result.eval(x=x_data))
            self.main_window.canvas.draw()
        d = QtWidgets.QDialog()
        ui = fit_dialog()
        ui.setupUi(d)
        ui.buttonBox.accepted.connect(lambda: fun(self.function))
        d.exec_()

    def import_to_table(self):
        self.ui.tableWidget.clear()
        path = self.model.filePath(self.tree_view.currentIndex())
        self.cf_data = np.genfromtxt(path, delimiter=',').T
        self.ui.tableWidget.setColumnCount(len(self.cf_data))
        self.ui.tableWidget.setRowCount(len(self.cf_data[0]))
        for column in range(len(self.cf_data)):
            for row in range(len(self.cf_data[0])):
                self.ui.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(self.cf_data[column][row])))
