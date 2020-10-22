from src.Ui_Files.main_window import Ui_MainWindow
from src.Ui_Files.Dialogs.Save_To_CSV import Ui_Dialog as STC_ui
from src.gui_elements.DockWidgets.data_browser import DataBrowser
from src.gui_elements.DockWidgets.project_browser import ProjectBrowser
from src.gui_elements.DockWidgets.XPS_view import XPS_view
from src.gui_elements.DockWidgets.QCM_view import QCM_view
from src.gui_elements.DockWidgets.FTIR_view import FTIR_view
from src.gui_elements.DockWidgets.SE_view import SE_view
from src.gui_elements.DockWidgets.Console_view import Console_view
from src.Ui_Files.Dialogs.seaborn_settings import Ui_Dialog as Ui_sns_Dialog
from src.Ui_Files.Dialogs.simple_text import Ui_Dialog as simple_text_ui
from src.Ui_Files.Dialogs.simple_treeWidget_dialog import Ui_Dialog as simple_tw
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.pyplot import figure
import matplotlib
from src.gui_elements.settings import ApplicationSettings
# from gui
from PySide2 import QtCore,QtWidgets,QtGui
import pickle
import seaborn as sns
import numpy as np

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self._init_UI()
        self.init_connections()
    #
    def _init_UI(self):
        # sns.set_style("whitegrid", {"axes.facecolor": "#F0F0F0",
        #                             'figure.facecolor': '#505F69'})
        self.style = 'ticks'
        self.context = 'paper'
        self.fs = 2
        self.c_palette = 'tab10'

        sns.set(context=self.context, style=self.style, palette=self.c_palette,
                font='sans-serif', font_scale=self.fs, color_codes=True)

        self.dw_ProjectView = ProjectBrowser(self)
        self.dw_ProjectView.setObjectName('Project View')
        self.dw_ProjectView.setMinimumSize(QtCore.QSize(400, 50))
        self.dw_ProjectView.setMaximumSize(QtCore.QSize(500, 1000))

        self.dw_Data_Broswer = DataBrowser(self)
        self.dw_Data_Broswer.setObjectName('Data Browser')
        self.dw_Data_Broswer.setMinimumSize(QtCore.QSize(400,50))
        self.dw_Data_Broswer.setMaximumSize(QtCore.QSize(500, 1000))

        self.dw_XPS = XPS_view(self)
        self.dw_XPS.setObjectName('XPS')
        self.dw_XPS.setMinimumSize(QtCore.QSize(400, 50))
        self.dw_XPS.setMaximumSize(QtCore.QSize(500, 1000))

        self.dw_QCM = QCM_view(self)
        self.dw_QCM.setObjectName('QCM')
        self.dw_QCM.setMinimumSize(QtCore.QSize(400, 50))
        self.dw_QCM.setMaximumSize(QtCore.QSize(500, 1000))

        self.dw_FTIR = FTIR_view(self)
        self.dw_FTIR.setObjectName('FTIR')
        self.dw_FTIR.setMinimumSize(QtCore.QSize(400, 50))
        self.dw_FTIR.setMaximumSize(QtCore.QSize(500, 1000))

        self.dw_SE = SE_view(self)
        self.dw_SE.setObjectName('FTIR')
        self.dw_SE.setMinimumSize(QtCore.QSize(400, 50))
        self.dw_SE.setMaximumSize(QtCore.QSize(500, 1000))

        self.dw_Console = Console_view(self)
        self.dw_Console.setObjectName('FTIR')
        self.dw_Console.setMinimumSize(QtCore.QSize(400, 50))
        self.dw_Console.setMaximumSize(QtCore.QSize(500, 1000))

        self.fig = figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
        self.canvas = FigureCanvas(self.fig)
        self.ax = self.fig.add_subplot(111)
        self.canvas.draw()
        self.toolbar = NavigationToolbar(self.canvas, self.canvas, coordinates=True)
        self.ui.verticalLayout.addWidget(self.toolbar)
        self.ui.verticalLayout.addWidget(self.canvas)
        self.canvas.draw()

    def init_connections(self):
        self.context_menu_plot = QtWidgets.QMenu(self)
        self.canvas.installEventFilter(self)

        self.clear_action = self.context_menu_plot.addAction('Clear')
        self.actionSave_To_CSV = self.context_menu_plot.addAction('Save To CSV')
        self.removeplot_action = self.context_menu_plot.addAction('Remove Line')
        self.save_figure_action = self.context_menu_plot.addAction('Save Figure')
        self.sns_settings_action = self.context_menu_plot.addAction('Seaborn Settings')

        self.clear_action.triggered.connect(lambda: self.cleargraph())
        self.removeplot_action.triggered.connect(lambda: plotting_funs.remove_line(self))
        self.actionSave_To_CSV.triggered.connect(lambda: plotting_funs.Save_All_Plotted(self))
        self.save_figure_action.triggered.connect(lambda: plotting_funs.save_fig(self))
        self.sns_settings_action.triggered.connect(lambda: self.sns_settings())
        # self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dw_ProjectView)
        # self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dw_XPS)
        # self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dw_Data_Broswer)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea,self.dw_QCM)
        # self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dw_FTIR)
        # self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dw_SE)
        # self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dw_Console)
        self.ui.actionSeaborn_Settings.triggered.connect(lambda: self.sns_settings())
        self.ui.actionLegend_Toggle.triggered.connect(lambda: plotting_funs.toggle_legend(self))
        self.ui.actionSave_Data.triggered.connect(lambda: plotting_funs.Save_All_Plotted(self))
        self.ui.actionClear_Graph.triggered.connect(lambda: plotting_funs.cleargraph(self))
        self.ui.actionXPS.triggered.connect(lambda: plotting_funs.XPS_view_fun(self))
        self.ui.actionDataBrowser.triggered.connect(lambda: plotting_funs.DataBrowser_view_fun(self))
        self.ui.actionProject_Tree.triggered.connect(lambda: plotting_funs.Project_view_fun(self))
        self.ui.actionQCM.triggered.connect(lambda: plotting_funs.QCM_view_fun(self))
        self.ui.actionFTIR.triggered.connect(lambda: plotting_funs.FTIR_view_fun(self))
        self.ui.actionSE.triggered.connect(lambda: plotting_funs.SE_view_fun(self))
        self.ui.actionConsole.triggered.connect(lambda: plotting_funs.Console_view_fun(self))

        self.ui.actionQCM_Help.triggered.connect(lambda: plotting_funs.random_c_plot(self))
        self.ui.actionOpen_File.triggered.connect(lambda: self.show_pickled_fig())
        self.ax.callbacks.connect('xlim_changed', self.lims_change)

    def lims_change(self, event_ax):
        ApplicationSettings.C_X_LIM = list(event_ax.get_xlim())
        ApplicationSettings.C_Y_LIM = list(event_ax.get_ylim())

    def eventFilter(self, object, event):
        # For right click events
        if event.type() == QtCore.QEvent.ContextMenu:
            self.context_menu_plot.exec_(self.mapToGlobal(QtCore.QPoint(event.pos())))
        return False

    def sns_settings(self):
        def sns_set_fun():
            self.style = ui.style_cb.currentText()
            self.context = ui.context_cb.currentText()
            self.fs = int(ui.fontscale_sb.value())
            self.c_palette = ui.palette_cb.currentText()
            sns.set(style=self.style, context=self.context, font_scale=self.fs,
                                palette=self.c_palette, font='sans-serif', color_codes=True)
            self.fig.delaxes(self.ax)
            self.ax = self.fig.add_subplot(111)
            self.canvas.draw()

        d = QtWidgets.QDialog()
        ui = Ui_sns_Dialog()
        ui.setupUi(d)
        palette_options = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu',
                           'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r',
                           'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired',
                           'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu',
                           'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r',
                           'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn',
                           'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r',
                           'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r',
                           'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r',
                           'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis',
                           'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix',
                           'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r',
                           'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r',
                           'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2','gnuplot2_r',
                           'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'icefire', 'icefire_r',
                           'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'mako', 'mako_r','nipy_spectral',
                           'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism',
                           'prism_r', 'rainbow', 'rainbow_r', 'rocket', 'rocket_r', 'seismic', 'seismic_r', 'spring',
                           'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b',
                           'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'twilight', 'twilight_r',
                           'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'vlag', 'vlag_r',
                           'winter', 'winter_r']
        ui.palette_cb.addItems(palette_options)
        ui.buttonBox.accepted.connect(lambda: sns_set_fun())
        ui.context_cb.setCurrentText(self.context)
        ui.style_cb.setCurrentText(self.style)
        ui.palette_cb.setCurrentText(self.c_palette)
        ui.fontscale_sb.setValue(self.fs)
        d.exec_()

    def cleargraph(self):
        self.ax.clear()
        self.ax.callbacks.connect('xlim_changed', self.lims_change)
        self.ax.callbacks.connect('ylim_changed', self.lims_change)
        ApplicationSettings.ALL_DATA_PLOTTED = {}
        self.canvas.draw()

class plotting_funs:

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

    def cleargraph(self):
        self.ax.clear()
        self.ax.callbacks.connect('xlim_changed', self.lims_change)
        self.ax.callbacks.connect('ylim_changed', self.lims_change)
        ApplicationSettings.ALL_DATA_PLOTTED = {}
        self.canvas.draw()

    def toggle_legend(self):
        if self.ui.actionLegend_Toggle.isChecked()==True:
            self.ax.legend()
            leg = self.ax.legend(loc='best')
            leg.set_draggable(True)
            self.canvas.draw()
        elif self.ui.actionLegend_Toggle.isChecked()==False:
            self.ax.get_legend().remove()
            self.canvas.draw()

    def Save_All_Plotted(self):
        def temp():
            for ix in ui.treeWidget.selectedIndexes():
                text = ix.data()  # or ix.data()
                np.savetxt(ApplicationSettings.SAVED_DATA_PATH+text+'.csv',
                           ApplicationSettings.ALL_DATA_PLOTTED[text][0]._xy,delimiter=',')
        dialog = QtWidgets.QDialog()
        ui = STC_ui()
        ui.setupUi(dialog)
        dict = ApplicationSettings.ALL_DATA_PLOTTED
        Key_List = []
        for i in dict.keys():
            Key_List.append(QtWidgets.QTreeWidgetItem([i]))
        ui.treeWidget.addTopLevelItems(Key_List)
        ui.buttonBox.accepted.connect(lambda: temp())
        ui.buttonBox.rejected.connect(dialog.reject())
        dialog.exec_()

    def save_fig(self):
        dialog = QtWidgets.QDialog()
        ui = simple_text_ui()
        ui.setupUi(dialog)
        dialog.exec_()
        text = ui.lineEdit.text()
        with open(ApplicationSettings.FIG_PATH+text, 'wb') as f:  # should be 'wb' rather than 'w'
            pickle.dump(self.fig, f)
        print(self.fig.__dict__)
        # pickle.dump(self.fig, open(ApplicationSettings.FIG_PATH+text, 'wb'))

    def show_pickled_fig(self):
        path,ext = QtWidgets.QFileDialog.getOpenFileName(self,'Pickeled Figure',ApplicationSettings.FIG_PATH)
        # print(path)
        figx = pickle.load(open(path, 'rb'))
        print(figx.__dict__)
        # self.fig = figx
        # self.canvas.draw()
        self.ui.verticalLayout.removeWidget(self.canvas)
        self.ui.verticalLayout.removeWidget(self.toolbar)
        self.canvas.close()
        self.toolbar.close()
        self.fig = figx
        self.canvas = FigureCanvas(self.fig)
        # self.fig.draw(self.fig.canvas.draw())

        self.ui.gridLayout.addWidget(NavigationToolbar(self.canvas, self.canvas, coordinates=True))
        self.ui.gridLayout.addWidget(self.canvas)

        self.ax = self.fig.add_subplot(111)
        print(self.fig.__dict__)
        # sns.set_style("darkgrid")

        self.canvas.installEventFilter(self)
        self.canvas.draw()

    def remove_line(self):
        def finish():
            for j in ui.treeWidget.selectedIndexes():
                line = ApplicationSettings.ALL_DATA_PLOTTED[j.data()]
                try:
                    if isinstance(line, list):
                        print(type(line[0]))
                        self.ax.lines.remove(line[0])
                        ApplicationSettings.ALL_DATA_PLOTTED.pop(j.data())
                        del line
                        self.canvas.draw()
                    elif isinstance(line,matplotlib.lines.Line2D):
                        # print(type(line))
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
        # ui.buttonBox.rejected.connect(dialog.reject)
        dialog.exec_()
        self.canvas.draw()

    def random_c_plot(self):
        Z = np.random.rand(6, 10)
        c = self.ax.pcolor(Z)
        self.canvas.draw()
        self.fig.colorbar(c, ax=self.ax)