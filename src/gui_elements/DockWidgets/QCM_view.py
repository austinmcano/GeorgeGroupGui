from PySide2 import QtCore
from src.Ui_Files.DockWidgets.dw_QCM import Ui_DockWidget
from src.gui_elements.RC_Fucntions import *
import pandas as pd

class QCM_view(QtWidgets.QDockWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.ui = Ui_DockWidget()
        self.ui.setupUi(self)

        self._init_vars()
        self._init_widgets()
        self._init_UI()

    def _init_vars(self):
        # self.ax = self.main_window.ax
        self.current_data_container = None
        self.time = None
        self.pressure = None
        self.mass = None
        self.data = None

    def _init_widgets(self):
        self.tree_view = self.ui.QCMtreeView
        self.context_menu = QtWidgets.QMenu(self)
        # Create context menu
        rc_browser_options(self)

    def _init_UI(self):
        self.model = QtWidgets.QFileSystemModel()
        # self.model.setRootPath(QtCore.QDir.currentPath())
        self.model.setRootPath('')

        self.tree_view.setModel(self.model)
        self.tree_view.setSortingEnabled(True)

        self.tree_view.sortByColumn(True)
        self.tree_view.setRootIndex(self.model.index(self.main_window.settings.value('QCM_PATH')))

        self.tree_view.setModel(self.model)
        self.tree_view.installEventFilter(self)
        self.tree_view.setColumnWidth(0, 200)
        self.model.sort(0, order=QtCore.Qt.SortOrder.AscendingOrder)

        # self.ui.plot_pb.clicked.connect(lambda: self.qcm())
        # self.ui.hc_mass_pb.clicked.connect(lambda: self.qcm_mass_hc())
        # self.ui.time_option.currentTextChanged.connect(lambda: self.time_change())
        self.ui.fill_cols_pb.clicked.connect(lambda: self.fill_colls())
        self.ui.cols_plot_pb.clicked.connect(lambda: self.qcm_tw())
        self.ui.treeWidget_time.currentItemChanged.connect(lambda: self.load_data(self.ui.treeWidget_time))
        self.ui.treeWidget_pressure.currentItemChanged.connect(lambda: self.load_data(self.ui.treeWidget_pressure))
        self.ui.treeWidget_mass.currentItemChanged.connect(lambda: self.load_data(self.ui.treeWidget_mass))

    def time_change(self):
        if self.ui.time_option.currentText()=='From:To Time':
            self.ui.From_Time.setText('0')
            self.ui.To_Time.setText('9999999')

    def eventFilter(self, object, event):
        # For right click events
        if event.type() == QtCore.QEvent.ContextMenu:
            self.context_menu.exec_(self.mapToGlobal(event.pos()))
        return False

    def qcm_mass_hc(self):
        if self.ui.ax_cb.currentText() == 'Left Ax':
            self.ax = self.main_window.ax
        elif self.ui.ax_cb.currentText() == 'Right Ax':
            if self.main_window.ax_2 is None:
                self.main_window.ax_2 = self.main_window.ax.twinx()
            self.ax = self.main_window.ax_2
        # self.main_window.cleargraph()
        path = self.model.filePath(self.tree_view.currentIndex())
        filename, file_extension = os.path.splitext(path)
        if file_extension == '.CSV' or file_extension == '.csv':
            data = np.genfromtxt(path, delimiter=',', skip_header=1, usecols=[0, 1, 2]).T
        else:
            data = np.genfromtxt(path, skip_header=1,usecols=[0,1,2]).T
        mc_a, mc_b, mc_f = qcm_hc_mass(data,float(self.ui.start_time_LE.text()), float(self.ui.end_time_LE.text()),
                    float(self.ui.adp_time_LE.text()),float(self.ui.bdp_time_LE.text()),int(self.ui.num_exp_LE.text()))
        if self.ui.comboBox_2.currentText() == 'Half+Full Cycle':
            # hc_a, hc_b, fc = qcm_hc_mass(data, float(self.ui.start_time_LE.text()), float(self.ui.end_time_LE.text()),
            #                          float(self.ui.adp_time_LE.text()), float(self.ui.bdp_time_LE.text()),
            #                          int(self.ui.num_exp_LE.text()))
            ApplicationSettings.ALL_DATA_PLOTTED['Full Cycle'] =self.ax.plot(mc_f, label='Full Cycle')
            ApplicationSettings.ALL_DATA_PLOTTED['Half Cycle A'] =self.ax.plot(mc_a,label='Mass Change A')
            ApplicationSettings.ALL_DATA_PLOTTED['Half Cycle B'] =self.ax.plot(mc_b,label='Mass Change B')
        elif self.ui.comboBox_2.currentText() == 'Density Half+Full Cycle':
            pass
        elif self.ui.comboBox_2.currentText() == 'Plot Mass':
            ApplicationSettings.ALL_DATA_PLOTTED['Mass'] = self.ax.plot(data[0],data[2],label='Mass')
        self.ui.ave_mcpahc_label.setText(str(np.average(mc_a)))
        self.ui.ave_mcpbhc_label.setText(str(np.average(mc_b)))
        self.ui.ave_mcpc_label.setText(str(np.average(mc_f)))
        self.ui.total_ml_label.setText(str(np.sum(mc_f)))
        self.qcm_basic()
        self.main_window.canvas.draw()

    def fill_colls(self):
        self.time = None
        self.mass = None
        self.pressure = None
        self.ui.treeWidget_time.clear()
        self.ui.treeWidget_pressure.clear()
        self.ui.treeWidget_mass.clear()

        path = self.model.filePath(self.tree_view.currentIndex())
        filename, file_extension = os.path.splitext(path)
        if file_extension == '.CSV' or file_extension == '.csv':
            self.data = pd.read_csv(self.model.filePath(self.tree_view.currentIndex()),
                                    delimiter=',', skiprows=0)
        else:
            self.data = pd.read_csv(self.model.filePath(self.tree_view.currentIndex()),
                                    sep='\t')
        strings = [col for col in self.data.columns]
        column_list_time = []
        column_list_pressure = []
        column_list_mass = []
        for i in strings:
            column_list_time.append(QtWidgets.QTreeWidgetItem([i]))
            column_list_pressure.append(QtWidgets.QTreeWidgetItem([i]))
            column_list_mass.append(QtWidgets.QTreeWidgetItem([i]))
            self.ui.treeWidget_time.addTopLevelItems(column_list_time)
            self.ui.treeWidget_pressure.addTopLevelItems(column_list_pressure)
            self.ui.treeWidget_mass.addTopLevelItems(column_list_mass)

    def load_data(self, widget):
        try:
            name = widget.currentIndex().data()
            if widget is self.ui.treeWidget_time:
                self.time = self.data[name].to_numpy()
            elif widget is self.ui.treeWidget_pressure:
                self.pressure = self.data[name].to_numpy()
                if type(self.pressure[0]) is str:
                    for i in range(len(self.pressure)):
                        self.pressure[i] = float(self.pressure[i].split(' ')[0])
            elif widget is self.ui.treeWidget_mass:
                self.mass = self.data[name].to_numpy()
            print(self.time)
            print(self.pressure)
            print(self.mass)
        except KeyError:
            print('Change Came From Fill Columns')

    def qcm_tw(self):
        if self.ui.ax_cb.currentText() == 'Left Ax':
            self.ax = self.main_window.ax
        elif self.ui.ax_cb.currentText() == 'Right Ax':
            if self.main_window.ax_2 is None:
                self.main_window.ax_2 = self.main_window.ax.twinx()
            self.ax = self.main_window.ax_2
        if self.ui.time_option.currentText()=='From:To Time':
            lims = [int(self.ui.From_Time.text()),int(self.ui.To_Time.text())]
        elif self.ui.time_option.currentText()=='Plot Limits':
            lims = ApplicationSettings.C_X_LIM
            self.ui.From_Time.setText(str(int(lims[0])))
            self.ui.To_Time.setText(str(int(lims[1])))
        if self.ui.plot_type_cb.currentText() == "Pressure":
            ApplicationSettings.ALL_DATA_PLOTTED['Pressure'] = self.ax.plot(self.time,self.pressure, label='Pressure')
        elif self.ui.plot_type_cb.currentText() == "Mass":
            ApplicationSettings.ALL_DATA_PLOTTED['Mass'] = self.ax.plot(self.time,self.mass, label='Mass (ng/cm$^2$)')
        elif self.ui.plot_type_cb.currentText() == "Mass Sub":
            ApplicationSettings.ALL_DATA_PLOTTED['Mass'] = self.ax.plot(self.time,self.mass-self.mass[0], label='Mass (ng/cm$^2$)')
        elif self.ui.plot_type_cb.currentText()=="Half+Full Cycle":
            mc_a, mc_b, mc_f, hcd_a, hcd_b, fc_d = plot_QCM(self, self.time, self.pressure, self.mass,
                                                            a_exp=int(self.ui.Num_A.text()),
                                                            b_exp=int(self.ui.Num_B.text()),
                                                            ttp=float(self.ui.time_through_purge.text()),
                                                            threshold=float(self.ui.P_Threshold.text()),
                                                            from_time=lims[0],
                                                            to_time=lims[1],
                                                            wait_time=float(self.ui.wait_LE.text()),
                                                            density=float(self.ui.Density.text()))
            ApplicationSettings.ALL_DATA_PLOTTED['MC_A'] = self.ax.plot(mc_a, label='Mass Change A')
            ApplicationSettings.ALL_DATA_PLOTTED['MC_B'] = self.ax.plot(mc_b, label='Mass Change B')
            ApplicationSettings.ALL_DATA_PLOTTED['MC_F'] = self.ax.plot(mc_f, label='Cycle Mass Change')
        elif self.ui.plot_type_cb.currentText() == "Half Cycle":
            mc_a, mc_b, mc_f, hcd_a, hcd_b, fc_d = plot_QCM(self, self.time, self.pressure, self.mass,
                                                            a_exp=int(self.ui.Num_A.text()),
                                                            b_exp=int(self.ui.Num_B.text()),
                                                            ttp=float(self.ui.time_through_purge.text()),
                                                            threshold=float(self.ui.P_Threshold.text()),
                                                            from_time=lims[0],
                                                            to_time=lims[1],
                                                            wait_time=float(self.ui.wait_LE.text()),
                                                            density=float(self.ui.Density.text()))
            ApplicationSettings.ALL_DATA_PLOTTED['MC_A'] = self.ax.plot(mc_a, label='Mass Change A')
            ApplicationSettings.ALL_DATA_PLOTTED['MC_B'] = self.ax.plot(mc_b, label='Mass Change B')
        elif self.ui.plot_type_cb.currentText() == "Half Cycle Density":
            pass
        self.main_window.canvas.draw()


    def qcm(self):
        if self.ui.ax_cb.currentText() == 'Left Ax':
            self.ax = self.main_window.ax
        elif self.ui.ax_cb.currentText() == 'Right Ax':
            if self.main_window.ax_2 is None:
                self.main_window.ax_2 = self.main_window.ax.twinx()
            self.ax = self.main_window.ax_2
        # self.main_window.cleargraph()
        path = self.model.filePath(self.tree_view.currentIndex())
        filename, file_extension = os.path.splitext(path)
        # self.main_window.cleargraph()
        if file_extension == '.csv' or file_extension =='.CSV':
            data = np.genfromtxt(self.model.filePath(self.tree_view.currentIndex()), delimiter=',', skip_header=1,
                                 usecols=[0, 1, 2]).T
        elif file_extension == '':
            data = np.genfromtxt(self.model.filePath(self.tree_view.currentIndex()), skip_header=1,
                                 usecols=[0, 1, 2]).T
        if self.ui.time_option.currentText()=='From:To Time':
            lims = [int(self.ui.From_Time.text()),int(self.ui.To_Time.text())]
        elif self.ui.time_option.currentText()=='Plot Limits':
            lims = ApplicationSettings.C_X_LIM
            self.ui.From_Time.setText(str(int(lims[0])))
            self.ui.To_Time.setText(str(int(lims[1])))
        mc_a, mc_b, mc_f, hcd_a, hcd_b, fc_d = \
            plot_QCM(self, data[0], data[1], data[2],
                 a_exp=int(self.ui.Num_A.text()), b_exp=int(self.ui.Num_B.text()),
                 ttp=float(self.ui.time_through_purge.text()),threshold=float(self.ui.P_Threshold.text()),
                 from_time=lims[0], to_time=lims[1],wait_time=float(self.ui.wait_LE.text()),
                 density=float(self.ui.Density.text()))
        if self.ui.comboBox.currentText() == 'Half+Full Cycle':
            ApplicationSettings.ALL_DATA_PLOTTED['MC_A'] = self.ax.plot(mc_a,label='Mass Change A')
            ApplicationSettings.ALL_DATA_PLOTTED['MC_B'] = self.ax.plot(mc_b,label='Mass Change B')
            ApplicationSettings.ALL_DATA_PLOTTED['MC_F'] = self.ax.plot(mc_f,label='Cycle Mass Change')
            # print(ApplicationSettings.ALL_DATA_PLOTTED['MC_F'])
        elif self.ui.comboBox.currentText() == 'QCM Mass_Sub':
            pass
        elif self.ui.comboBox.currentText() == 'Plot Mass':
            ApplicationSettings.ALL_DATA_PLOTTED['Mass'] = self.ax.plot(data[0],data[2],label='Mass')

        elif self.ui.comboBox.currentText() == 'Plot Pressure':
            ApplicationSettings.ALL_DATA_PLOTTED['Mass'] = self.ax.plot(data[0], data[1],label='Pressure')

        elif self.ui.comboBox.currentText() == 'Density Half+Full Cycle':
            ApplicationSettings.ALL_DATA_PLOTTED['MCD_A'] = self.ax.plot(hcd_a,label='Thickness Change A')
            ApplicationSettings.ALL_DATA_PLOTTED['MCD_B'] = self.ax.plot(hcd_a,label='Thickness Change B')
            ApplicationSettings.ALL_DATA_PLOTTED['MCD_F'] = self.ax.plot(fc_d,label='Thickness Cycle Change')
        self.ui.total_ml_label.setText(str(np.sum(mc_f)))
        self.ui.ave_mcpahc_label.setText(str(np.average(mc_a)))
        self.ui.ave_mcpbhc_label.setText(str(np.average(mc_b)))
        self.ui.ave_mcpc_label.setText(str(np.average(mc_f)))
        self.qcm_basic()
        self.main_window.canvas.draw()

    def qcm_basic(self):
        self.main_window.ax.set_xlabel('Cycles')
        self.main_window.ax.set_ylabel('Thickness Change (ng/cm$^2$ cycle)')
        leg = self.main_window.ax.legend(loc='best')
        leg.set_draggable(True)
        self.main_window.fig.tight_layout()
        self.main_window.canvas.draw()
