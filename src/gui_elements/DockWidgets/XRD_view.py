from PySide2 import QtCore
from src.Ui_Files.DockWidgets.dw_XRD import Ui_DockWidget
from src.gui_elements.RC_Fucntions import *
from src.gui_elements.Plotting_Functions import *
from lmfit import Model, Parameters
from lmfit.models import VoigtModel, GaussianModel, LorentzianModel

class XRD_view(QtWidgets.QDockWidget):
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
        self.data = None
        self.baseline = None
        self.model = None
        self.x_data = None
        self.y_data = None


    def _init_widgets(self):
        self.tree_view = self.ui.treeView
        self.context_menu = QtWidgets.QMenu(self)
        # Create context menu
        rc_browser_options(self)

    def _init_UI(self):
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath('')

        self.tree_view.setModel(self.model)
        self.tree_view.setSortingEnabled(True)

        self.tree_view.sortByColumn(True)
        self.tree_view.setRootIndex(self.model.index(self.main_window.settings.value('XRD_PATH')))

        self.tree_view.setModel(self.model)
        self.tree_view.installEventFilter(self)
        self.tree_view.setColumnWidth(0, 200)

        self.ui.fillcols_pb.clicked.connect(lambda: self.fill_cols())
        self.ui.plot_pb.clicked.connect(lambda: self.plot_xrd())
        self.ui.baseline_pb.clicked.connect(lambda: self.baseline_function())

    def eventFilter(self, object, event):
        # For right click events
        if event.type() == QtCore.QEvent.ContextMenu:
            self.context_menu.exec_(self.mapToGlobal(event.pos()))
        return False

    def fill_cols(self):
        self.ui.tw_x.clear()
        self.ui.tw_y.clear()
        self.data = pd.read_csv(self.model.filePath(self.tree_view.currentIndex()),
                                delimiter=',')
        strings = [col for col in self.data.columns]
        column_list_x = []
        column_list_y = []
        for i in strings:
            column_list_x.append(QtWidgets.QTreeWidgetItem([i]))
            column_list_y.append(QtWidgets.QTreeWidgetItem([i]))
            self.ui.tw_x.addTopLevelItems(column_list_x)
            self.ui.tw_y.addTopLevelItems(column_list_y)

    def plot_xrd(self):
        x = self.ui.tw_x.currentIndex().data()
        self.x_data = self.data[x].to_numpy()
        self.x_data = self.x_data[~np.isnan(self.x_data)]
        y = self.ui.tw_y.currentIndex().data()
        self.y_data = self.data[y].to_numpy()
        self.y_data = self.y_data[~np.isnan(self.y_data)]
        ApplicationSettings.ALL_DATA_PLOTTED[str(x)] = \
            self.main_window.ax.plot(self.x_data, self.y_data, label=x)
        self.xrd_basic()

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
        ApplicationSettings.ALL_DATA_PLOTTED['Y_Data'] = self.main_window.ax.plot(self.data_x,self.data_y,'-b')
        ApplicationSettings.ALL_DATA_PLOTTED['Shirley'] = \
            self.main_window.ax.plot(self.data_x,self.shirley,'.k', markersize=4)
        ApplicationSettings.ALL_DATA_PLOTTED['XPS Init Values'] = \
            self.main_window.ax.plot(self.data_x,start_plot + self.shirley, '-y')
        self.main_window.canvas.draw()

    def xrd_basic(self):
        self.main_window.ax.set_xlabel('2$\\theta$ ($^\circ$)')
        self.main_window.ax.set_ylabel('Counts')
        leg = self.main_window.ax.legend(loc='best')
        leg.set_draggable(True)
        self.main_window.fig.tight_layout()
        self.main_window.canvas.draw()

    def baseline_function(self):
        self.main_window.cleargraph()
        print(self.y_data)
        self.baseline = baseline_als(self.y_data,self.ui.lambda_sb.value(),self.ui.p_sb.value())
        ApplicationSettings.ALL_DATA_PLOTTED['corrected'] = \
            self.main_window.ax.plot(self.x_data, self.y_data-self.baseline, label='corrected')
        # ApplicationSettings.ALL_DATA_PLOTTED['baseline'] = \
        #     self.main_window.ax.plot(self.x_data, self.baseline, label='baseline')
        self.xrd_basic()
