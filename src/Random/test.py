from PySide2 import QtCore
from src.Ui_Files.DockWidgets.dw_XPS import Ui_DockWidget
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
        # self.start_points = np.zeros([5,3])
        self.constraints = np.asarray([[1000,0,9999999,285,0,4000,1,.001,10],[1000,0,9999999,285,0,4000,1,.001,10],
                                       [1000,0,9999999,100,0,4000,1,.001,10],[1000,0,9999999,100,0,4000,1,.001,10],
                                       [1000,0,9999999,100,0,4000,1,.001,10]])

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

        self.peak_num_changed()

        self.ui.plot_pb.clicked.connect(lambda: self.plot())
        self.ui.fit_pb.clicked.connect(lambda: self.fit_fun())
        self.ui.shirley_pb.clicked.connect(lambda: self.shirley_fun())
        self.ui.num_peaks_sb.valueChanged.connect(lambda: self.sb_change())
        self.ui.peak_num_cb.activated.connect(lambda: self.peak_num_changed())
        self.ui.amp_LE.textEdited.connect(lambda: self.save_constraints())
        self.ui.amp_low.textEdited.connect(lambda: self.save_constraints())
        self.ui.amp_high.textEdited.connect(lambda: self.save_constraints())
        self.ui.cen_LE.textEdited.connect(lambda: self.save_constraints())
        self.ui.cen_low.textEdited.connect(lambda: self.save_constraints())
        self.ui.cen_high.textEdited.connect(lambda: self.save_constraints())
        self.ui.sigma_LE.textEdited.connect(lambda: self.save_constraints())
        self.ui.sigma_low.textEdited.connect(lambda: self.save_constraints())
        self.ui.sigma_high.textEdited.connect(lambda: self.save_constraints())
        self.ui.plot_curr_pb.clicked.connect(lambda: self.plot_curr())

    def plot_curr(self):
        con = self.constraints
        if self.ui.num_peaks_sb.value() == 1:
            start_plot = gaussian(self.data_x,con[0][0],con[0][3],con[0][6])
            self.main_window.ax.plot(self.data_x,start_plot+self.shirley,'-y')
        elif self.ui.num_peaks_sb.value() == 2:
            start_plot = gaussian(self.data_x, con[0][0], con[0][3], con[0][6])+gaussian(self.data_x, con[1][0], con[1][3], con[1][6])
            self.main_window.ax.plot(self.data_x, start_plot + self.shirley, '-y')
        elif self.ui.num_peaks_sb.value() == 3:
            start_plot = gaussian(self.data_x, con[0][0], con[0][3], con[0][6])+\
                         gaussian(self.data_x, con[1][0], con[1][3], con[1][6])+\
                         gaussian(self.data_x, con[2][0], con[2][3], con[2][6])

            self.main_window.ax.plot(self.data_x, start_plot + self.shirley, '-y')
        self.main_window.canvas.draw()

    def save_constraints(self):
        try:
            current_index = int(self.ui.peak_num_cb.currentIndex())
            c_list = [float(self.ui.amp_LE.text()),float(self.ui.amp_low.text()),float(self.ui.amp_high.text()),
                    float(self.ui.cen_LE.text()),float(self.ui.cen_low.text()),float(self.ui.cen_high.text()),
                    float(self.ui.sigma_LE.text()),float(self.ui.sigma_low.text()),float(self.ui.sigma_high.text())]
            self.constraints[current_index] = np.asarray(c_list)

        except ValueError:
            print('No constraint save')

    def peak_num_changed(self):
        current_index = int(self.ui.peak_num_cb.currentIndex())
        self.ui.amp_LE.setText(str(self.constraints[current_index][0]))
        self.ui.amp_low.setText(str(self.constraints[current_index][1]))
        self.ui.amp_high.setText(str(self.constraints[current_index][2]))
        self.ui.cen_LE.setText(str(self.constraints[current_index][3]))
        self.ui.cen_low.setText(str(self.constraints[current_index][4]))
        self.ui.cen_high.setText(str(self.constraints[current_index][5]))
        self.ui.sigma_LE.setText(str(self.constraints[current_index][6]))
        self.ui.sigma_low.setText(str(self.constraints[current_index][7]))
        self.ui.sigma_high.setText(str(self.constraints[current_index][8]))

    def sb_change(self):
        self.ui.peak_num_cb.clear()
        num = self.ui.num_peaks_sb.value()
        possible = ['1','2','3','4','5']
        if num < 6:
            self.ui.peak_num_cb.addItems(possible[0:num])

    def shirley_fun(self):
        self.save_constraints()
        self.main_window.cleargraph()
        x_lim = ApplicationSettings.C_X_LIM
        #  Y is data[0]..... whyyyyyyy x is data[1]
        self.data = np.flip(ApplicationSettings.CURRENT_PLOT[0].get_data())
        indexs = [find_nearest(self.data[1], x_lim[0]), find_nearest(self.data[1], x_lim[1])]
        self.data_x = self.data[1][indexs[0]:indexs[1]]
        self.data_y = self.data[0][indexs[0]:indexs[1]]
        self.main_window.ax.plot(self.data_x,self.data_y,'-b')
        self.shirley = shirley_calculate(self.data_x, self.data_y)
        self.main_window.ax.plot(self.data_x, self.shirley, '.k', markersize=4)
        self.xps_basic()
        self.main_window.canvas.draw()

    def eventFilter(self, object, event):
        # For right click events
        if event.type() == QtCore.QEvent.ContextMenu:
            self.context_menu.exec_(self.mapToGlobal(event.pos()))
        return False

    def fit_fun(self):
        self.main_window.cleargraph()
        self.save_constraints()
        con = self.constraints
        #  Y is data[0]..... whyyyyyyy x is data[1]
        if self.ui.fit_shape_cb.currentText()=='Gaussian':
            if self.ui.num_peaks_sb.value()==1:
                gmodel = Model(gaussian)+Model(linear_func)
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('amp',con[0][0]),('cen',con[0][3]),('sigma',con[0][6]),('m',0),('b',0))
                result = gmodel.fit(self.data_y-self.shirley, params, x=self.data_x)
                self.ui.fit_report_TE.setText(result.fit_report())
                self.main_window.ax.plot(self.data_x,self.shirley,'k--',label='Shirley')
                self.main_window.ax.plot(self.data_x, result.best_fit+self.shirley,'r--',label='Result')
                self.main_window.ax.legend(loc='best')

            elif self.ui.num_peaks_sb.value() == 2:
                gmodel = Model(gaussian, prefix='p1_') + Model(gaussian, prefix='p2_')+Model(linear_func)
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amp', con[0][0]),('p1_cen', con[0][3]),('p1_sigma', con[0][6]),
                                ('p2_amp', con[1][0]),('p2_cen', con[1][3]),('p2_sigma', con[1][6]),('m',0),('b',0))

                result = gmodel.fit(self.data_y - self.shirley, params, x=self.data_x)
                comps = result.eval_components()
                self.ui.fit_report_TE.setText(result.fit_report())
                self.main_window.ax.plot(self.data_x,self.shirley,'k--',label='Shirley')
                self.main_window.ax.plot(self.data_x,self.shirley+comps['p1_'],'k--',label='G1')
                self.main_window.ax.plot(self.data_x,self.shirley+comps['p2_'],'k--',label='G2')
                self.main_window.ax.plot(self.data_x, result.best_fit + self.shirley,'r--',label='Result')
                self.main_window.ax.legend(loc='best')

            elif self.ui.num_peaks_sb.value() == 3:
                gmodel = Model(gaussian, prefix='p1_') + Model(gaussian, prefix='p2_')+\
                         Model(gaussian, prefix='p3_') + Model(linear_func)
                params = Parameters()
                # add with tuples: (NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)
                params.add_many(('p1_amp', con[0][0]),('p1_cen', con[0][3]),('p1_sigma', con[0][6]),
                                ('p2_amp', con[1][0]),('p2_cen', con[1][3]),('p2_sigma', con[1][6]),
                                ('p3_amp', con[2][0]),('p3_cen', con[2][3]),('p3_sigma', con[2][6]),('m',0),('b',0))
                result = gmodel.fit(self.data_y - self.shirley, params, x=self.data_x)
                comps = result.eval_components()
                self.main_window.ax.plot(self.data_x,self.shirley,'k--',label='Shirley')
                self.main_window.ax.plot(self.data_x,self.shirley+comps['p1_'],'k--',label='G1')
                self.main_window.ax.plot(self.data_x,self.shirley+comps['p2_'],'k--',label='G2')
                self.main_window.ax.plot(self.data_x,self.shirley+comps['p3_'],'k--',label='G3')
                self.main_window.ax.plot(self.data_x, result.best_fit + self.shirley,'r--',label='Result')
                self.main_window.ax.legend(loc='best')
                self.ui.fit_report_TE.setText(result.fit_report())

        elif self.ui.fit_shape_cb.currentText() == 'Lorentz':
            gmodel = Model(lorenz)
            gmodelparams = gmodel.make_params(amp=float(self.ui.amp_LE.text()), cen=float(self.ui.cen_LE.text())
                                              , sigma=float(self.ui.sigma_LE.text()))
            result = gmodel.fit(self.data_y - self.shirley, gmodelparams, x=self.data_x)
            self.ui.fit_report_TE.setText(result.fit_report())
            self.main_window.ax.plot(self.data_x, result.best_fit + self.shirley)

        self.main_window.ax.plot(self.data_x,self.data_y,'-b')
        self.main_window.canvas.draw()

    def plot(self):
        path = self.model.filePath(self.tree_view.currentIndex())
        self.data = np.genfromtxt(path, delimiter=',').T
        ApplicationSettings.CURRENT_PLOT = self.main_window.ax.plot(self.data[0], self.data[1])
        self.main_window.canvas.draw()

    def xps_basic(self):
        self.main_window.ax.set_xlabel('B. E. (eV)')
        self.main_window.ax.set_ylabel('Counts')
        leg = self.main_window.ax.legend(loc='best')
        leg.set_draggable(True)

        self.main_window.fig.tight_layout()
        self.main_window.canvas.draw()

