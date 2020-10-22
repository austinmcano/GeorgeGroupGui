from PySide2 import QtCore
from src.Ui_Files.DockWidgets.dw_FTIR import Ui_DockWidget
from src.gui_elements.RC_Fucntions import *
from src.gui_elements.Plotting_Functions import subtraction_from_survey
import glob
from scipy.signal import savgol_filter

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

    def _init_widgets(self):
        self.tree_view = self.ui.FTIR_treeView
        self.context_menu = QtWidgets.QMenu(self)
        # Create context menu
        rc_browser_options(self)

    def _init_UI(self):
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath(QtCore.QDir.currentPath())

        self.tree_view.setModel(self.model)
        self.tree_view.setSortingEnabled(True)

        self.tree_view.sortByColumn(True)
        self.tree_view.setRootIndex(self.model.index(ApplicationSettings.PROJECT_PATH))

        self.tree_view.setModel(self.model)
        self.tree_view.installEventFilter(self)
        self.tree_view.setColumnWidth(0, 200)

        self.ui.pushButton.clicked.connect(lambda: self.ir_plot())
        self.ui.smooth_pb.clicked.connect(lambda: self.smooth())
        self.ui.integrate_pb.clicked.connect(lambda: self.integrate())

        # self.ui.tryfit_pb.clicked.connect(lambda: self.try_fit())

    def eventFilter(self, object, event):
        # For right click events
        if event.type() == QtCore.QEvent.ContextMenu:
            self.context_menu.exec_(self.mapToGlobal(event.pos()))
        return False

    def try_fit(self):
        pass

    def ir_plot(self):
        path = self.model.filePath(self.tree_view.currentIndex())
        # head, tail = os.path.split(path)
        combo = self.ui.ir_plot_cb.currentText()
        if combo == 'Plot':
            self.data = np.genfromtxt(path,delimiter=',').T
            ApplicationSettings.ALL_DATA_PLOTTED['FTIR'] = self.main_window.ax.plot(self.data[0],self.data[1],'-b',label='IR Plot')
        elif combo == 'Sub Plot (dir)':
            if os.path.isdir(path):
                csv_list = sorted(glob.glob(path + '/*CSV'))
                self.sub = subtraction_from_survey(csv_list)

                for i in range(len(self.sub)-1):
                    ApplicationSettings.ALL_DATA_PLOTTED['Sub_'+str(i)] = \
                        self.main_window.ax.plot(self.sub[0],self.sub[i+1],label='Sub_'+str(i))
        elif combo == 'Diff Plot (dir)':
            if os.path.isdir(path):
                csv_list = sorted(glob.glob(path + '/*CSV'))
                self.diff = difference_from_survey(csv_list)
                for i in range(len(self.diff)-1):
                    ApplicationSettings.ALL_DATA_PLOTTED['Diff_'+str(i)] = \
                        self.main_window.ax.plot(self.diff[0],self.diff[i+1],label='Diff_'+str(i))
        elif combo == 'Plot (dir)':
            if os.path.isdir(path):
                csv_list = sorted(glob.glob(path + '/*CSV'))
                data = []
                for csv in csv_list:
                    data.append(np.genfromtxt(csv, delimiter=',').T)
                self.data = [data[0][0]]
                for i in range(len(data)):
                    self.data.append(data[i][1])
                for j in range(len(self.data)-1):
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
        minimum = float(self.ui.tableWidget.item(0,0).text())
        maximum = float(self.ui.tableWidget.item(0, 1).text())
        if self.ui.int_type_cb.currentText() == 'Integrate Plot (dir)':
            pass
        elif self.ui.int_type_cb.currentText() == 'Integrate Sub (dir)':
            self.sub = subtraction_from_survey(csv_list)
            inte = integrate_ir(self.sub,minimum,maximum)
            ApplicationSettings.ALL_DATA_PLOTTED['Int. '+str(minimum)+'-'+str(maximum)] = \
                self.main_window.ax.plot(inte,'.-b',label='Int. '+str(minimum)+'-'+str(maximum))
        elif self.ui.int_type_cb.currentText() == 'Integrate Diff (dir)':
            self.diff = difference_from_survey(csv_list)
            inte = integrate_ir(self.diff, minimum, maximum)
            ApplicationSettings.ALL_DATA_PLOTTED['Int. ' + str(minimum) + '-' + str(maximum)] = \
                self.main_window.ax.plot(inte,'.-b', label='Int. ' + str(minimum) + '-' + str(maximum))
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