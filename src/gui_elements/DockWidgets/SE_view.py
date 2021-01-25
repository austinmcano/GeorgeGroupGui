from src.Ui_Files.DockWidgets.dw_SE import Ui_DockWidget
from src.gui_elements.RC_Fucntions import *
from PySide2 import QtCore,QtWidgets
import pandas as pd
from lmfit.models import LinearModel
from src.Ui_Files.Dialogs.simple_treeWidget_dialog import Ui_Dialog as twDialog_ui


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
        self.data_x = None
        self.data_y = None

    def _init_widgets(self):
        self.tree_view = self.ui.SE_treeView
        self.context_menu = QtWidgets.QMenu(self)
        # Create context menu
        rc_browser_options(self)

    def _init_UI(self):
        self.model = QtWidgets.QFileSystemModel()
        # self.model.setRootPath(QtCore.QDir.currentPath())
        self.model.setRootPath('')

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
        self.ui.lin_fit_pb.clicked.connect(lambda: self.linear_SE())

    def eventFilter(self, object, event):
        # For right click events
        if event.type() == QtCore.QEvent.ContextMenu:
            self.context_menu.exec_(self.mapToGlobal(event.pos()))
        return False

    def plot_type_organizer(self):
        if self.ui.plot_type_cb.currentText() == 'X vs Y':
            self.plot_se()
        elif self.ui.plot_type_cb.currentText() == 'Ext. Plot (half-ints)' or \
                self.ui.plot_type_cb.currentText() == 'Ext. Plot (ints)':
            self.extended_plot_fun()

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
                    ax.plot(x_data, y_data-y_data[0],self.ui.linetype_cb.currentText(),label=x)
        elif not self.ui.zero_correct_checkb.isChecked():
            for i in self.ui.SEY_tw.selectedItems():
                y_data = self.data[i.text(0)].to_numpy()
                ApplicationSettings.ALL_DATA_PLOTTED[str(x) + str(i.text(0))] = \
                    ax.plot(x_data, y_data, self.ui.linetype_cb.currentText(),label=x)
        self.main_window.ax.set_xlabel(self.ui.xlabel_le.text())
        self.main_window.ax.set_ylabel(self.ui.ylabel_le.text())
        self.main_window.fig.tight_layout()
        self.main_window.canvas.draw()



    def linear_SE(self):
        def finish():
            if self.ui.line_name_checkbox.isChecked():
                name = self.ui.line_name_le.text()
            else:
                name = self.ui.SEY_tw.currentIndex().data()
            if keycheck(dict, name) is True:
                name = name + '_'
            key = ui.treeWidget.currentItem().text(0)
            self.data_x = dict[key][0]._xy.T[0]
            self.data_y = dict[key][0]._xy.T[1]
            x_lim = ApplicationSettings.C_X_LIM
            indexs = [find_nearest(self.data_x, x_lim[0]), find_nearest(self.data_x, x_lim[1])]
            self.data_x = self.data_x[indexs[0]:indexs[1]]
            self.data_y = self.data_y[indexs[0]:indexs[1]]
            model = LinearModel()
            pars = model.guess(self.data_y,x=self.data_x)
            fit = model.fit(self.data_y,pars,x=self.data_x)
            ApplicationSettings.ALL_DATA_PLOTTED[name+' Fit'] = \
                self.main_window.ax.plot(self.data_x,fit.best_fit,label=name+' Fit')
            self.ui.fit_results_TE.setText(fit.fit_report())
            self.main_window.canvas.draw()
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

    def extended_plot_fun(self):
        if self.ui.line_name_checkbox.isChecked():
            name = self.ui.line_name_le.text()
        else:
            name = self.ui.SEY_tw.currentIndex().data()
        if keycheck(ApplicationSettings.ALL_DATA_PLOTTED,name) is True:
                name = name + '_'
        if self.ui.ax_cb.currentText() == 'Left Ax':
            ax = self.main_window.ax
        elif self.ui.ax_cb.currentText() == 'Right Ax':
            if self.main_window.ax_2 is None:
                self.main_window.ax_2 = self.main_window.ax.twinx()
            ax = self.main_window.ax_2
        y_data = []
        for i in self.ui.SEY_tw.selectedItems():
            temp = self.data[i.text(0)].to_numpy()
            for j in temp:
                if not np.isnan(j):
                    y_data.append(j)
        if self.ui.zero_correct_checkb.isChecked():
            y_data = y_data-y_data[0]
        if self.ui.plot_type_cb.currentText() == 'Ext. Plot (ints)':
            ApplicationSettings.ALL_DATA_PLOTTED[name] = \
                ax.plot(np.linspace(0, len(y_data) - 1, len(y_data)), y_data, self.ui.linetype_cb.currentText()
                        ,label=self.ui.line_name_le.text()+name)
        elif self.ui.plot_type_cb.currentText() == 'Ext. Plot (half-ints)':
            ApplicationSettings.ALL_DATA_PLOTTED[name] = \
                ax.plot(np.linspace(0, (len(y_data) - 1) / 2, len(y_data)), y_data,
                        self.ui.linetype_cb.currentText(),label=name)
        self.main_window.ax.set_xlabel(self.ui.xlabel_le.text())
        self.main_window.ax.set_ylabel(self.ui.ylabel_le.text())
        self.main_window.fig.tight_layout()
        self.main_window.canvas.draw()