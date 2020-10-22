from PySide2 import QtCore
from src.Ui_Files.DockWidgets.dw_XPS_0 import Ui_DockWidget
from src.gui_elements.RC_Fucntions import *
from src.gui_elements.Plotting_Functions import *
from lmfit import Model, Parameters

class XPS_view(QtWidgets.QDockWidget):
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
        self.shirley = None
        self.model = None
        self.data_x = None
        self.data_y = None
        self.constraints = np.asarray([[100000,0,9999999,285,0,4000,2,.001,4],[100000,0,9999999,285,0,4000,2,.001,4],
                                       [100000,0,9999999,100,0,4000,2,.001,4],[100000,0,9999999,100,0,4000,2,.001,4],
                                       [100000,0,9999999,100,0,4000,2,.001,4]])
        for row in range(9):
            for column in range(5):
                self.ui.tableWidget.setItem(row,column,QtWidgets.QTableWidgetItem(str(self.constraints[column][row])))

    def _init_widgets(self):
        self.tree_view = self.ui.XPS_treeView
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

        # self.peak_num_changed()

        self.ui.plot_pb.clicked.connect(lambda: self.plot())
        self.ui.fit_pb.clicked.connect(lambda: self.fit_fun())
        self.ui.shirley_pb.clicked.connect(lambda: self.shirley_fun())
        # self.ui.num_peaks_sb.valueChanged.connect(lambda: self.sb_change())
        self.ui.tableWidget.cellChanged.connect(lambda: self.save_constraints())
        self.ui.plot_curr_pb.clicked.connect(lambda: self.plot_init())

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

    def eventFilter(self, object, event):
        # For right click events
        if event.type() == QtCore.QEvent.ContextMenu:
            self.context_menu.exec_(self.mapToGlobal(event.pos()))
        return False

    def save_constraints(self):
        try:
            for row in range(9):
                for column in range(5):
                    self.constraints[column][row] = float(self.ui.tableWidget.item(row, column).text())
        except ValueError:
            print('No constraint save')

    def shirley_fun(self):
        self.save_constraints()
        self.main_window.cleargraph()
        x_lim = ApplicationSettings.C_X_LIM
        #  Y is data[0]..... whyyyyyyy x is data[1]
        # self.data = np.flip(ApplicationSettings.CURRENT_PLOT[0].get_data())
        # self.data = np.flip(self.data)
        indexs = [find_nearest(self.data_x, x_lim[1]), find_nearest(self.data_x, x_lim[0])]
        self.data_x = self.data_x[indexs[0]:indexs[1]]
        self.data_y = self.data_y[indexs[0]:indexs[1]]
        ApplicationSettings.ALL_DATA_PLOTTED['Data_y'] = self.main_window.ax.plot(self.data_x,self.data_y,'-b')
        self.shirley = shirley_calculate(self.data_x, self.data_y)
        ApplicationSettings.ALL_DATA_PLOTTED['Shirley'] = self.main_window.ax.plot(self.data_x, self.shirley, '.k', markersize=2)
        self.xps_basic()
        self.main_window.canvas.draw()

    def fit_fun(self):
        self.main_window.cleargraph()
        self.save_constraints()
        con = self.constraints
        #  Y is data[0]..... whyyyyyyy x is data[1]
        if self.ui.fit_shape_cb.currentText() == 'Gaussian':
            if self.ui.num_peaks_sb.value()==1:
                gmodel = Model(gaussian)
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('amp', con[0][0], True, con[0][1], con[0][2]),
                                ('cen', con[0][3], True, con[0][4], con[0][5]),
                                ('sigma', con[0][6], True, con[0][7], con[0][8]),)
                result = gmodel.fit(self.data_y-self.shirley, params, x=self.data_x)
                self.ui.fit_report_TE.setText(result.fit_report())
                ApplicationSettings.ALL_DATA_PLOTTED['Shirley'] = self.main_window.ax.plot(self.data_x,self.shirley,'k--',label='Shirley')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] =self.main_window.ax.plot(self.data_x, result.best_fit+self.shirley,'r--',label='Result')
                leg = self.main_window.ax.legend(loc='best', fontsize='small')
                leg.set_draggable(True)

            elif self.ui.num_peaks_sb.value() == 2:
                gmodel = Model(gaussian, prefix='p1_') + Model(gaussian, prefix='p2_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amp', con[0][0],True,con[0][1],con[0][2]),
                                ('p1_cen', con[0][3],True,con[0][4],con[0][5]),
                                ('p1_sigma', con[0][6],True,con[0][7],con[0][8]),
                                ('p2_amp', con[1][0],True,con[1][1],con[1][2]),
                                ('p2_cen', con[1][3],True,con[1][4],con[1][5]),
                                ('p2_sigma', con[1][6],True,con[1][7],con[1][8]))
                result = gmodel.fit(self.data_y - self.shirley, params, x=self.data_x)
                comps = result.eval_components()
                self.ui.fit_report_TE.setText(result.fit_report())
                ApplicationSettings.ALL_DATA_PLOTTED['Shirley'] = self.main_window.ax.plot(self.data_x,self.shirley,'k--',label='Shirley')
                ApplicationSettings.ALL_DATA_PLOTTED['G1'] = self.main_window.ax.plot(self.data_x,self.shirley+comps['p1_'],'k--',label='G1')
                ApplicationSettings.ALL_DATA_PLOTTED['G2'] = self.main_window.ax.plot(self.data_x,self.shirley+comps['p2_'],'k--',label='G2')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x, result.best_fit + self.shirley,'r--',label='Result')
                leg = self.main_window.ax.legend(loc='best', fontsize='small')
                leg.set_draggable(True)

            elif self.ui.num_peaks_sb.value() == 3:
                gmodel = Model(gaussian, prefix='p1_') + Model(gaussian, prefix='p2_')+Model(gaussian, prefix='p3_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amp', con[0][0],True,con[0][1],con[0][2]),
                                ('p1_cen', con[0][3],True,con[0][4],con[0][5]),
                                ('p1_sigma', con[0][6],True,con[0][7],con[0][8]),
                                ('p2_amp', con[1][0],True,con[1][1],con[1][2]),
                                ('p2_cen', con[1][3],True,con[1][4],con[1][5]),
                                ('p2_sigma', con[1][6],True,con[1][7],con[1][8]),
                                ('p3_amp', con[2][0], True, con[2][1], con[2][2]),
                                ('p3_cen', con[2][3], True, con[2][4], con[2][5]),
                                ('p3_sigma', con[2][6], True, con[2][7], con[2][8]))
                result = gmodel.fit(self.data_y - self.shirley, params, x=self.data_x)
                comps = result.eval_components()
                ApplicationSettings.ALL_DATA_PLOTTED['Shirley'] = self.main_window.ax.plot(self.data_x,self.shirley,'k--',label='Shirley')
                ApplicationSettings.ALL_DATA_PLOTTED['G1'] = self.main_window.ax.plot(self.data_x,self.shirley+comps['p1_'],'k--',label='G1')
                ApplicationSettings.ALL_DATA_PLOTTED['G2'] = self.main_window.ax.plot(self.data_x,self.shirley+comps['p2_'],'k--',label='G2')
                ApplicationSettings.ALL_DATA_PLOTTED['G3'] = self.main_window.ax.plot(self.data_x,self.shirley+comps['p3_'],'k--',label='G3')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x, result.best_fit + self.shirley,'r--',label='Result')
                leg = self.main_window.ax.legend(loc='best', fontsize='small')
                leg.set_draggable(True)
                self.ui.fit_report_TE.setText(result.fit_report())

            elif self.ui.num_peaks_sb.value() == 4:
                gmodel = Model(gaussian, prefix='p1_') + Model(gaussian, prefix='p2_') + \
                         Model(gaussian, prefix='p3_') + Model(gaussian, prefix='p4_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amp', con[0][0], True, con[0][1], con[0][2]),
                                ('p1_cen', con[0][3], True, con[0][4], con[0][5]),
                                ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
                                ('p2_amp', con[1][0], True, con[1][1], con[1][2]),
                                ('p2_cen', con[1][3], True, con[1][4], con[1][5]),
                                ('p2_sigma', con[1][6], True, con[1][7], con[1][8]),
                                ('p3_amp', con[2][0], True, con[2][1], con[2][2]),
                                ('p3_cen', con[2][3], True, con[2][4], con[2][5]),
                                ('p3_sigma', con[2][6], True, con[2][7], con[2][8]),
                                ('p4_amp', con[3][0], True, con[3][1], con[3][2]),
                                ('p4_cen', con[3][3], True, con[3][4], con[3][5]),
                                ('p4_sigma', con[3][6], True, con[3][7], con[3][8]))
                result = gmodel.fit(self.data_y - self.shirley, params, x=self.data_x)
                comps = result.eval_components()
                ApplicationSettings.ALL_DATA_PLOTTED['Shirley'] = self.main_window.ax.plot(self.data_x, self.shirley, 'k--', label='Shirley')
                ApplicationSettings.ALL_DATA_PLOTTED['G1'] = self.main_window.ax.plot(self.data_x, self.shirley + comps['p1_'], 'k--', label='G1')
                ApplicationSettings.ALL_DATA_PLOTTED['G2'] = self.main_window.ax.plot(self.data_x, self.shirley + comps['p2_'], 'k--', label='G2')
                ApplicationSettings.ALL_DATA_PLOTTED['G3'] = self.main_window.ax.plot(self.data_x, self.shirley + comps['p3_'], 'k--', label='G3')
                ApplicationSettings.ALL_DATA_PLOTTED['G4'] = self.main_window.ax.plot(self.data_x, self.shirley + comps['p4_'], 'k--', label='G4')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x, result.best_fit + self.shirley, 'r--', label='Result')
                leg = self.main_window.ax.legend(loc='best',fontsize='small')
                leg.set_draggable(True)
                self.ui.fit_report_TE.setText(result.fit_report())

            elif self.ui.num_peaks_sb.value() == 5:
                gmodel = Model(gaussian, prefix='p1_') + Model(gaussian, prefix='p2_') + \
                         Model(gaussian, prefix='p3_') + Model(gaussian, prefix='p4_') + Model(gaussian, prefix='p5_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amp', con[0][0], True, con[0][1], con[0][2]),
                                ('p1_cen', con[0][3], True, con[0][4], con[0][5]),
                                ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
                                ('p2_amp', con[1][0], True, con[1][1], con[1][2]),
                                ('p2_cen', con[1][3], True, con[1][4], con[1][5]),
                                ('p2_sigma', con[1][6], True, con[1][7], con[1][8]),
                                ('p3_amp', con[2][0], True, con[2][1], con[2][2]),
                                ('p3_cen', con[2][3], True, con[2][4], con[2][5]),
                                ('p3_sigma', con[2][6], True, con[2][7], con[2][8]),
                                ('p4_amp', con[3][0], True, con[3][1], con[3][2]),
                                ('p4_cen', con[3][3], True, con[3][4], con[3][5]),
                                ('p4_sigma', con[3][6], True, con[3][7], con[3][8]),
                                ('p5_amp', con[4][0], True, con[4][1], con[4][2]),
                                ('p5_cen', con[4][3], True, con[4][4], con[4][5]),
                                ('p5_sigma', con[4][6], True, con[4][7], con[4][8]))
                result = gmodel.fit(self.data_y - self.shirley, params, x=self.data_x)
                comps = result.eval_components()
                ApplicationSettings.ALL_DATA_PLOTTED['Shirley'] = self.main_window.ax.plot(self.data_x, self.shirley, 'k--', label='Shirley')
                ApplicationSettings.ALL_DATA_PLOTTED['G1'] =self.main_window.ax.plot(self.data_x, self.shirley + comps['p1_'], 'k--', label='G1')
                ApplicationSettings.ALL_DATA_PLOTTED['G2'] =self.main_window.ax.plot(self.data_x, self.shirley + comps['p2_'], 'k--', label='G2')
                ApplicationSettings.ALL_DATA_PLOTTED['G3'] =self.main_window.ax.plot(self.data_x, self.shirley + comps['p3_'], 'k--', label='G3')
                ApplicationSettings.ALL_DATA_PLOTTED['G4'] =self.main_window.ax.plot(self.data_x, self.shirley + comps['p4_'], 'k--', label='G4')
                ApplicationSettings.ALL_DATA_PLOTTED['G5'] = self.main_window.ax.plot(self.data_x,self.shirley + comps['p5_'],'k--', label='G5')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] =self.main_window.ax.plot(self.data_x, result.best_fit + self.shirley, 'r--', label='Result')
                leg = self.main_window.ax.legend(loc='best',fontsize='small')
                leg.set_draggable(True)
                self.ui.fit_report_TE.setText(result.fit_report())

        elif self.ui.fit_shape_cb.currentText() == 'Lorentz':
            if self.ui.num_peaks_sb.value() == 1:
                lmodel = Model(lorenz)
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('amp', con[0][0], True, con[0][1], con[0][2]),
                                ('cen', con[0][3], True, con[0][4], con[0][5]),
                                ('sigma', con[0][6], True, con[0][7], con[0][8]), )
                result = lmodel.fit(self.data_y - self.shirley, params, x=self.data_x)
                self.ui.fit_report_TE.setText(result.fit_report())
                ApplicationSettings.ALL_DATA_PLOTTED['Shirley'] = self.main_window.ax.plot(self.data_x, self.shirley,
                                                                                           'k--', label='Shirley')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit + self.shirley,
                                                                                       'r--', label='Result')
                leg = self.main_window.ax.legend(loc='best', fontsize='small')
                leg.set_draggable(True)
            elif self.ui.num_peaks_sb.value() == 2:
                lmodel = Model(lorenz, prefix='p1_') + Model(lorenz, prefix='p2_')
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amp', con[0][0], True, con[0][1], con[0][2]),
                                ('p1_cen', con[0][3], True, con[0][4], con[0][5]),
                                ('p1_sigma', con[0][6], True, con[0][7], con[0][8]),
                                ('p2_amp', con[1][0], True, con[1][1], con[1][2]),
                                ('p2_cen', con[1][3], True, con[1][4], con[1][5]),
                                ('p2_sigma', con[1][6], True, con[1][7], con[1][8]))
                result = lmodel.fit(self.data_y - self.shirley, params, x=self.data_x)
                comps = result.eval_components()
                self.ui.fit_report_TE.setText(result.fit_report())
                ApplicationSettings.ALL_DATA_PLOTTED['Shirley'] = self.main_window.ax.plot(self.data_x, self.shirley,
                                                                                           'k--', label='Shirley')
                ApplicationSettings.ALL_DATA_PLOTTED['G1'] = self.main_window.ax.plot(self.data_x,
                                                                                      self.shirley + comps['p1_'],
                                                                                      'k--', label='G1')
                ApplicationSettings.ALL_DATA_PLOTTED['G2'] = self.main_window.ax.plot(self.data_x,
                                                                                      self.shirley + comps['p2_'],
                                                                                      'k--', label='G2')
                ApplicationSettings.ALL_DATA_PLOTTED['Fit'] = self.main_window.ax.plot(self.data_x,
                                                                                       result.best_fit + self.shirley,
                                                                                       'r--', label='Result')
                leg = self.main_window.ax.legend(loc='best', fontsize='small')
                leg.set_draggable(True)

        self.xps_basic()
        ApplicationSettings.ALL_DATA_PLOTTED['Y Data'] = self.main_window.ax.plot(self.data_x,self.data_y,'-b')
        self.main_window.canvas.draw()

    def plot(self):
        path = self.model.filePath(self.tree_view.currentIndex())
        filename, extension = os.path.splitext(path)
        if extension=='.csv' or extension=='.CSV':
            self.data = np.genfromtxt(path, delimiter=',').T
            self.data_x = self.data[0]+float(self.ui.offset_LE.text())
            self.data_y = self.data[1]
            ApplicationSettings.ALL_DATA_PLOTTED['XPS'] = self.main_window.ax.plot(self.data[0], self.data[1])
        elif extension=='.txt':
            self.data = np.genfromtxt(path,skip_header=1).T
            self.data_x = self.data[0]+float(self.ui.offset_LE.text())
            self.data_y = self.data[1]
            ApplicationSettings.ALL_DATA_PLOTTED['XPS'] = self.main_window.ax.plot(self.data_x, self.data_y)
        self.xps_basic()
        self.main_window.canvas.draw()

    def xps_basic(self):
        self.main_window.ax.set_xlabel('B. E. (eV)')
        self.main_window.ax.set_ylabel('Counts')
        leg = self.main_window.ax.legend(loc='best')
        leg.set_draggable(True)
        self.main_window.fig.tight_layout()
        self.main_window.canvas.draw()

