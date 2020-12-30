from src.Ui_Files.DockWidgets.dw_SE import Ui_DockWidget
from src.gui_elements.RC_Fucntions import *
from PySide2 import QtCore,QtWidgets
import pandas as pd
from lmfit.models import LinearModel


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
        self.fitted_slopes = None

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

        self.tree_view.sortByColumn(0, QtCore.Qt.AscendingOrder)
        self.tree_view.setRootIndex(self.model.index(self.main_window.settings.value('SE_PATH')))

        self.tree_view.setModel(self.model)
        self.tree_view.installEventFilter(self)
        self.tree_view.setColumnWidth(0, 200)

        self.ui.SEY_tw.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

        self.ui.fill_cols_pb.clicked.connect(lambda: self.fill_cols())
        self.ui.plot_pb.clicked.connect(lambda: self.plot_type_organizer())

    def eventFilter(self, object, event):
        # For right click events
        if event.type() == QtCore.QEvent.ContextMenu:
            self.context_menu.exec_(self.mapToGlobal(event.pos()))
        return False

    def plot_type_organizer(self):
        if self.ui.plot_type_cb.currentText() == 'X vs Y':
            self.plot_se()
        elif self.ui.plot_type_cb.currentText() == 'Ext. Plot':
            self.extended_plot_fun()
        elif self.ui.plot_type_cb.currentText() == 'Linear Fit':
            self.linear_SE()

    def fill_cols(self):
        self.ui.SEY_tw.clear()
        self.ui.SEX_tw.clear()
        self.data = pd.read_csv(self.model.filePath(self.tree_view.currentIndex()),
                                delimiter=',',skiprows=self.ui.skip_rows_sb.value())
        strings = [col for col in self.data.columns]
        column_list_x = []
        column_list_y = []
        for i in strings:
            column_list_x.append(QtWidgets.QTreeWidgetItem([i]))
            column_list_y.append(QtWidgets.QTreeWidgetItem([i]))
            self.ui.SEX_tw.addTopLevelItems(column_list_x)
            self.ui.SEY_tw.addTopLevelItems(column_list_y)

    def plot_se(self):
        if self.ui.ax_cb.currentText() == 'Left Ax':
            ax = self.main_window.ax
        elif self.ui.ax_cb.currentText() == 'Right Ax':
            if self.main_window.ax_2 is None:
                self.main_window.ax_2 = self.main_window.ax.twinx()
            ax = self.main_window.ax_2
        x = self.ui.SEX_tw.currentIndex().data()
        # y = self.ui.SEY_tw.currentIndex().data()
        x_data = self.data[x].to_numpy()

        if self.ui.zero_correct_checkb.isChecked():
            for i in self.ui.SEY_tw.selectedItems():
                y_data = self.data[i.text(0)].to_numpy()
                ApplicationSettings.ALL_DATA_PLOTTED[str(x) + str(i.text(0))] = \
                    ax.plot(x_data, y_data-y_data[0],self.ui.linetype_cb.currentText())
        elif not self.ui.zero_correct_checkb.isChecked():
            for i in self.ui.SEY_tw.selectedItems():
                y_data = self.data[i.text(0)].to_numpy()
                ApplicationSettings.ALL_DATA_PLOTTED[str(x) + str(i.text(0))] = \
                    ax.plot(x_data, y_data, self.ui.linetype_cb.currentText())
        if self.ui.checkBox.isChecked():
            pass
        if not self.ui.checkBox.isChecked():
            self.main_window.ax.set_xlabel(self.ui.xlabel_le.text())
            self.main_window.ax.set_ylabel(self.ui.ylabel_le.text())
        self.main_window.fig.tight_layout()
        self.main_window.canvas.draw()

    def linear_SE(self):
        model = LinearModel()
        self.fitted_slopes = []
        all_data_list = [i for i in ApplicationSettings.ALL_DATA_PLOTTED.keys()]
        for i in all_data_list:
            data = ApplicationSettings.ALL_DATA_PLOTTED[i][0]._xy.T
            print(data)
            print(len(data[0]))
            print(len(data[1]))
            pars = model.guess(data[1],x=data[0])
            fit = model.fit(data[1],pars,x=data[0])
            ApplicationSettings.ALL_DATA_PLOTTED[str(i) + 'fit'] = self.main_window.ax.plot(data[0],fit.best_fit)
            self.fitted_slopes.append(fit.params['slope'].value)
        self.main_window.canvas.draw()

    def extended_plot_fun(self):
        if self.ui.ax_cb.currentText() == 'Left Ax':
            ax = self.main_window.ax
        elif self.ui.ax_cb.currentText() == 'Right Ax':
            if self.main_window.ax_2 is None:
                self.main_window.ax_2 = self.main_window.ax.twinx()
            ax = self.main_window.ax_2
        y_data = []
        if self.ui.zero_correct_checkb.isChecked():
            for i in self.ui.SEY_tw.selectedItems():
                temp = self.data[i.text(0)].to_numpy()
                for j in temp:
                    if not np.isnan(j):
                        y_data.append(j)
            y_data = y_data-y_data[0]
            if self.ui.x_list_cb.currentText() == 'X From List':
                pass
            elif self.ui.x_list_cb.currentText() == 'X (ints)':
                ApplicationSettings.ALL_DATA_PLOTTED['test'] = \
                    ax.plot(np.linspace(0, len(y_data) - 1, len(y_data)), y_data, self.ui.linetype_cb.currentText())
            elif self.ui.x_list_cb.currentText() == 'X (half-ints)':
                ApplicationSettings.ALL_DATA_PLOTTED['test'] = \
                    ax.plot(np.linspace(0, (len(y_data) - 1) / 2, len(y_data)), y_data,
                            self.ui.linetype_cb.currentText())
        elif not self.ui.zero_correct_checkb.isChecked():
            for i in self.ui.SEY_tw.selectedItems():
                temp = self.data[i.text(0)].to_numpy()
                for j in temp:
                    if not np.isnan(j):
                        y_data.append(j)

            # if self.ui.x_list_cb.currentText() == 'X From List':
            #     pass
            if self.ui.x_list_cb.currentText() == 'X (ints)':
                ApplicationSettings.ALL_DATA_PLOTTED['test'] = \
                    ax.plot(np.linspace(0,len(y_data)-1,len(y_data)), y_data, self.ui.linetype_cb.currentText())
            elif self.ui.x_list_cb.currentText() == 'X (half-ints)':
                ApplicationSettings.ALL_DATA_PLOTTED['test'] = \
                    ax.plot(np.linspace(0, (len(y_data) - 1)/2, len(y_data)), y_data, self.ui.linetype_cb.currentText())
        if self.ui.checkBox.isChecked():
            pass
        if not self.ui.checkBox.isChecked():
            self.main_window.ax.set_xlabel(self.ui.xlabel_le.text())
            self.main_window.ax.set_ylabel(self.ui.ylabel_le.text())
        self.main_window.fig.tight_layout()
        self.main_window.canvas.draw()