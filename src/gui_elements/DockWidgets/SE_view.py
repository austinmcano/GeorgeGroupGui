from src.Ui_Files.DockWidgets.dw_SE import Ui_DockWidget
from src.gui_elements.RC_Fucntions import *
from PySide2 import QtCore,QtWidgets
import pandas as pd


class SE_view(QtWidgets.QDockWidget):
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

    def _init_widgets(self):
        self.tree_view = self.ui.SE_treeView
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

        self.ui.SEY_tw.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

        self.ui.fill_cols_pb.clicked.connect(lambda: self.fill_cols())
        self.ui.plot_pb.clicked.connect(lambda: self.plot_se())
        self.ui.linear_fit_pb.clicked.connect(lambda: self.linear_SE())

    def eventFilter(self, object, event):
        # For right click events
        if event.type() == QtCore.QEvent.ContextMenu:
            self.context_menu.exec_(self.mapToGlobal(event.pos()))
        return False

    def fill_cols(self):
        self.ui.SEY_tw.clear()
        self.ui.SEX_tw.clear()
        self.data = pd.read_csv(self.model.filePath(self.tree_view.currentIndex()),
                                delimiter=',',skiprows=int(self.ui.skip_header_LE.text()))
        strings = [col for col in self.data.columns]
        column_list_x = []
        column_list_y = []
        for i in strings:
            column_list_x.append(QtWidgets.QTreeWidgetItem([i]))
            column_list_y.append(QtWidgets.QTreeWidgetItem([i]))
            self.ui.SEX_tw.addTopLevelItems(column_list_x)
            self.ui.SEY_tw.addTopLevelItems(column_list_y)

    def plot_se(self):
        path = self.model.filePath(self.tree_view.currentIndex())
        # data = np.genfromtxt(path, delimiter=',', skip_header=int(self.ui.skip_header_LE.text())).T

        x = self.ui.SEX_tw.currentIndex().data()
        y = self.ui.SEY_tw.currentIndex().data()
        ApplicationSettings.ALL_DATA_PLOTTED[str(x)+str(y)] = self.data.plot(x=x,y=y,ax=self.main_window.ax)

        # if self.ui.correction_combo.currentText() == 'Zero From First':
        #     sub_data = np.zeros(len(data[x]))
        #     for i in range(len(sub_data)):
        #         sub_data[i] = data[y][i]-data[y][0]
        #     thick_change = sub_data[0]-sub_data[-1]
        #     quick_fit_p = np.polyfit(data[x],sub_data,1)
        #     self.ui.thick_change_QL.setText(str(thick_change))
        #     self.ui.change_rate_QL.setText(str(quick_fit_p[0]/2))
        #     ApplicationSettings.CURRENT_PLOT = self.main_window.ax.plot(data[x],sub_data)
        #     ApplicationSettings.ALL_DATA_PLOTTED[tail.split('.')[0]+str(x)+str(y)+'SE'+'_corr'] = [data[x],sub_data]
        #     # print(ApplicationSettings.CURRENT_PLOT[0].get_data())
        #
        # elif self.ui.correction_combo.currentText() == 'No Correction':
        #     thick_change = data[y][0] - data[y][-1]
        #     quick_fit_p = np.polyfit(data[x], data[y], 1)
        #     self.ui.thick_change_QL.setText(str(thick_change))
        #     self.ui.change_rate_QL.setText(str(quick_fit_p[0]))
        #     ApplicationSettings.CURRENT_PLOT = self.main_window.ax.plot(data[x],data[y])
        #     ApplicationSettings.ALL_DATA_PLOTTED[tail.split('.')[0] + str(x) + str(y) + 'SE'] = [data[x], data[y]]
        # self.main_window.ax.set_xlabel('Cycles')
        # self.main_window.ax.set_ylabel('Thickness Change ($\AA$)')
        self.main_window.canvas.draw()

    def linear_SE(self):
        # self.data = ApplicationSettings.CURRENT_PLOT[0].get_data()
        self.data = np.asarray(self.data).T
        print(self.data)
        # quick_fit_params = np.polyfit(data[0],data[1],1)
        # quick_fit = np.poly1d(quick_fit_params)
        # self.main_window.ax.plot(data[0],quick_fit(data[0]))
        # self.main_window.ax.set_xlabel('Cycles')
        # self.main_window.ax.set_ylabel('Thickness Change ($\AA$)')
        # self.main_window.canvas.draw()

    def SE_graph_constants(self):
        self.main_window.ax.set_xlabel('Cycles')
        self.main_window.ax.set_ylabel('Thickness Change ($\AA$)')