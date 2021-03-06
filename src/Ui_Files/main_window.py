# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(747, 536)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.actionOpen_File = QAction(MainWindow)
        self.actionOpen_File.setObjectName(u"actionOpen_File")
        self.actionOpen_Directory = QAction(MainWindow)
        self.actionOpen_Directory.setObjectName(u"actionOpen_Directory")
        self.actionSave_Data = QAction(MainWindow)
        self.actionSave_Data.setObjectName(u"actionSave_Data")
        self.actionNew_Project = QAction(MainWindow)
        self.actionNew_Project.setObjectName(u"actionNew_Project")
        self.actionCurrent_Path = QAction(MainWindow)
        self.actionCurrent_Path.setObjectName(u"actionCurrent_Path")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionFTIR = QAction(MainWindow)
        self.actionFTIR.setObjectName(u"actionFTIR")
        self.actionQCM = QAction(MainWindow)
        self.actionQCM.setObjectName(u"actionQCM")
        self.actionPlot_Left = QAction(MainWindow)
        self.actionPlot_Left.setObjectName(u"actionPlot_Left")
        self.actionPlot_Right = QAction(MainWindow)
        self.actionPlot_Right.setObjectName(u"actionPlot_Right")
        self.actionClear = QAction(MainWindow)
        self.actionClear.setObjectName(u"actionClear")
        self.actionGraph_Options = QAction(MainWindow)
        self.actionGraph_Options.setObjectName(u"actionGraph_Options")
        self.actionSmooth = QAction(MainWindow)
        self.actionSmooth.setObjectName(u"actionSmooth")
        self.actionPlot_Mass = QAction(MainWindow)
        self.actionPlot_Mass.setObjectName(u"actionPlot_Mass")
        self.actionPlot_Pressure = QAction(MainWindow)
        self.actionPlot_Pressure.setObjectName(u"actionPlot_Pressure")
        self.actionGet_Info = QAction(MainWindow)
        self.actionGet_Info.setObjectName(u"actionGet_Info")
        self.actionInitalize = QAction(MainWindow)
        self.actionInitalize.setObjectName(u"actionInitalize")
        self.actionLinear_Fit = QAction(MainWindow)
        self.actionLinear_Fit.setObjectName(u"actionLinear_Fit")
        self.actionClear_2 = QAction(MainWindow)
        self.actionClear_2.setObjectName(u"actionClear_2")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionRandom_Plot = QAction(MainWindow)
        self.actionRandom_Plot.setObjectName(u"actionRandom_Plot")
        self.actionClear_Graph = QAction(MainWindow)
        self.actionClear_Graph.setObjectName(u"actionClear_Graph")
        self.actionAdd_Figure = QAction(MainWindow)
        self.actionAdd_Figure.setObjectName(u"actionAdd_Figure")
        self.actionRemove_Figure = QAction(MainWindow)
        self.actionRemove_Figure.setObjectName(u"actionRemove_Figure")
        self.actionImport_File = QAction(MainWindow)
        self.actionImport_File.setObjectName(u"actionImport_File")
        self.actionProject_View = QAction(MainWindow)
        self.actionProject_View.setObjectName(u"actionProject_View")
        self.actionSystem_View = QAction(MainWindow)
        self.actionSystem_View.setObjectName(u"actionSystem_View")
        self.actionLinear_Fit_2 = QAction(MainWindow)
        self.actionLinear_Fit_2.setObjectName(u"actionLinear_Fit_2")
        self.actionCorrect_From_First = QAction(MainWindow)
        self.actionCorrect_From_First.setObjectName(u"actionCorrect_From_First")
        self.actionClear_Current_Data = QAction(MainWindow)
        self.actionClear_Current_Data.setObjectName(u"actionClear_Current_Data")
        self.actionXPS = QAction(MainWindow)
        self.actionXPS.setObjectName(u"actionXPS")
        self.actionProject_Tree = QAction(MainWindow)
        self.actionProject_Tree.setObjectName(u"actionProject_Tree")
        self.actionDataBrowser = QAction(MainWindow)
        self.actionDataBrowser.setObjectName(u"actionDataBrowser")
        self.actionSE = QAction(MainWindow)
        self.actionSE.setObjectName(u"actionSE")
        self.actionConsole = QAction(MainWindow)
        self.actionConsole.setObjectName(u"actionConsole")
        self.actionQCM_Help = QAction(MainWindow)
        self.actionQCM_Help.setObjectName(u"actionQCM_Help")
        self.actionFTIR_Help = QAction(MainWindow)
        self.actionFTIR_Help.setObjectName(u"actionFTIR_Help")
        self.actionXPS_Help = QAction(MainWindow)
        self.actionXPS_Help.setObjectName(u"actionXPS_Help")
        self.actionSE_Help = QAction(MainWindow)
        self.actionSE_Help.setObjectName(u"actionSE_Help")
        self.actionOther_Help = QAction(MainWindow)
        self.actionOther_Help.setObjectName(u"actionOther_Help")
        self.actionLegend_Toggle = QAction(MainWindow)
        self.actionLegend_Toggle.setObjectName(u"actionLegend_Toggle")
        self.actionLegend_Toggle.setCheckable(True)
        self.actionSave_To_CSV = QAction(MainWindow)
        self.actionSave_To_CSV.setObjectName(u"actionSave_To_CSV")
        self.actionDark = QAction(MainWindow)
        self.actionDark.setObjectName(u"actionDark")
        self.actionLight = QAction(MainWindow)
        self.actionLight.setObjectName(u"actionLight")
        self.actionDarkGrid = QAction(MainWindow)
        self.actionDarkGrid.setObjectName(u"actionDarkGrid")
        self.actionLightGrid = QAction(MainWindow)
        self.actionLightGrid.setObjectName(u"actionLightGrid")
        self.actionTicks = QAction(MainWindow)
        self.actionTicks.setObjectName(u"actionTicks")
        self.actionPaper = QAction(MainWindow)
        self.actionPaper.setObjectName(u"actionPaper")
        self.actionTalk = QAction(MainWindow)
        self.actionTalk.setObjectName(u"actionTalk")
        self.actionNotebook = QAction(MainWindow)
        self.actionNotebook.setObjectName(u"actionNotebook")
        self.actionPoster = QAction(MainWindow)
        self.actionPoster.setObjectName(u"actionPoster")
        self.action1 = QAction(MainWindow)
        self.action1.setObjectName(u"action1")
        self.action2 = QAction(MainWindow)
        self.action2.setObjectName(u"action2")
        self.action3 = QAction(MainWindow)
        self.action3.setObjectName(u"action3")
        self.actionDirectory = QAction(MainWindow)
        self.actionDirectory.setObjectName(u"actionDirectory")
        self.actionFile = QAction(MainWindow)
        self.actionFile.setObjectName(u"actionFile")
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        self.action4 = QAction(MainWindow)
        self.action4.setObjectName(u"action4")
        self.action5 = QAction(MainWindow)
        self.action5.setObjectName(u"action5")
        self.actiondeep = QAction(MainWindow)
        self.actiondeep.setObjectName(u"actiondeep")
        self.actionblue = QAction(MainWindow)
        self.actionblue.setObjectName(u"actionblue")
        self.actionflare = QAction(MainWindow)
        self.actionflare.setObjectName(u"actionflare")
        self.actionhls = QAction(MainWindow)
        self.actionhls.setObjectName(u"actionhls")
        self.actionmako = QAction(MainWindow)
        self.actionmako.setObjectName(u"actionmako")
        self.actioncrest = QAction(MainWindow)
        self.actioncrest.setObjectName(u"actioncrest")
        self.actionmagma = QAction(MainWindow)
        self.actionmagma.setObjectName(u"actionmagma")
        self.actioncubehelix = QAction(MainWindow)
        self.actioncubehelix.setObjectName(u"actioncubehelix")
        self.actionlight_b = QAction(MainWindow)
        self.actionlight_b.setObjectName(u"actionlight_b")
        self.actionseagreen = QAction(MainWindow)
        self.actionseagreen.setObjectName(u"actionseagreen")
        self.actionspectral = QAction(MainWindow)
        self.actionspectral.setObjectName(u"actionspectral")
        self.actioncoolwarm = QAction(MainWindow)
        self.actioncoolwarm.setObjectName(u"actioncoolwarm")
        self.actionSeaborn_Settings = QAction(MainWindow)
        self.actionSeaborn_Settings.setObjectName(u"actionSeaborn_Settings")
        self.actionNew_Project_2 = QAction(MainWindow)
        self.actionNew_Project_2.setObjectName(u"actionNew_Project_2")
        self.actionOpen_Project = QAction(MainWindow)
        self.actionOpen_Project.setObjectName(u"actionOpen_Project")
        self.actionRecent_Projects = QAction(MainWindow)
        self.actionRecent_Projects.setObjectName(u"actionRecent_Projects")
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionPrint = QAction(MainWindow)
        self.actionPrint.setObjectName(u"actionPrint")
        self.actionSettings_2 = QAction(MainWindow)
        self.actionSettings_2.setObjectName(u"actionSettings_2")
        self.actionSettings_3 = QAction(MainWindow)
        self.actionSettings_3.setObjectName(u"actionSettings_3")
        self.actionSettings_4 = QAction(MainWindow)
        self.actionSettings_4.setObjectName(u"actionSettings_4")
        self.actionSettings_5 = QAction(MainWindow)
        self.actionSettings_5.setObjectName(u"actionSettings_5")
        self.actionSettings_6 = QAction(MainWindow)
        self.actionSettings_6.setObjectName(u"actionSettings_6")
        self.actionChange_Settings = QAction(MainWindow)
        self.actionChange_Settings.setObjectName(u"actionChange_Settings")
        self.actionCurve_Fitting = QAction(MainWindow)
        self.actionCurve_Fitting.setObjectName(u"actionCurve_Fitting")
        self.actionLoad_Data = QAction(MainWindow)
        self.actionLoad_Data.setObjectName(u"actionLoad_Data")
        self.actionCalculator = QAction(MainWindow)
        self.actionCalculator.setObjectName(u"actionCalculator")
        self.actionBar_Graph = QAction(MainWindow)
        self.actionBar_Graph.setObjectName(u"actionBar_Graph")
        self.actionGraph_Test = QAction(MainWindow)
        self.actionGraph_Test.setObjectName(u"actionGraph_Test")
        self.actionTight_Layout = QAction(MainWindow)
        self.actionTight_Layout.setObjectName(u"actionTight_Layout")
        self.actionXRD = QAction(MainWindow)
        self.actionXRD.setObjectName(u"actionXRD")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.graphWidget = QWidget(self.centralwidget)
        self.graphWidget.setObjectName(u"graphWidget")
        self.graphWidget.setMinimumSize(QSize(600, 0))
        self.verticalLayout = QVBoxLayout(self.graphWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.gridLayout.addWidget(self.graphWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 747, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuImport = QMenu(self.menuFile)
        self.menuImport.setObjectName(u"menuImport")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuViews = QMenu(self.menubar)
        self.menuViews.setObjectName(u"menuViews")
        self.menuFigure = QMenu(self.menubar)
        self.menuFigure.setObjectName(u"menuFigure")
        self.menuHELP = QMenu(self.menubar)
        self.menuHELP.setObjectName(u"menuHELP")
        self.menuTesting = QMenu(self.menubar)
        self.menuTesting.setObjectName(u"menuTesting")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuViews.menuAction())
        self.menubar.addAction(self.menuFigure.menuAction())
        self.menubar.addAction(self.menuHELP.menuAction())
        self.menubar.addAction(self.menuTesting.menuAction())
        self.menuFile.addAction(self.actionNew_Project_2)
        self.menuFile.addAction(self.actionOpen_Project)
        self.menuFile.addAction(self.actionRecent_Projects)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionChange_Settings)
        self.menuFile.addAction(self.actionSave_Data)
        self.menuFile.addAction(self.actionLoad_Data)
        self.menuFile.addAction(self.menuImport.menuAction())
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuImport.addAction(self.actionDirectory)
        self.menuImport.addAction(self.actionFile)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuViews.addAction(self.actionFTIR)
        self.menuViews.addAction(self.actionQCM)
        self.menuViews.addAction(self.actionSE)
        self.menuViews.addAction(self.actionXPS)
        self.menuViews.addAction(self.actionXRD)
        self.menuViews.addAction(self.actionCurve_Fitting)
        self.menuViews.addAction(self.actionCalculator)
        self.menuViews.addSeparator()
        self.menuViews.addSeparator()
        self.menuViews.addAction(self.actionProject_Tree)
        self.menuViews.addAction(self.actionDataBrowser)
        self.menuViews.addAction(self.actionConsole)
        self.menuFigure.addSeparator()
        self.menuFigure.addAction(self.actionClear_Graph)
        self.menuFigure.addAction(self.actionSave_To_CSV)
        self.menuFigure.addAction(self.actionLegend_Toggle)
        self.menuFigure.addAction(self.actionSeaborn_Settings)
        self.menuFigure.addAction(self.actionBar_Graph)
        self.menuFigure.addAction(self.actionTight_Layout)
        self.menuHELP.addSeparator()
        self.menuHELP.addAction(self.actionQCM_Help)
        self.menuHELP.addAction(self.actionXPS_Help)
        self.menuHELP.addAction(self.actionFTIR_Help)
        self.menuHELP.addAction(self.actionSE_Help)
        self.menuHELP.addSeparator()
        self.menuHELP.addAction(self.actionOther_Help)
        self.menuTesting.addAction(self.actionGraph_Test)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"George Group", None))
        self.actionOpen_File.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.actionOpen_Directory.setText(QCoreApplication.translate("MainWindow", u"Open Directory", None))
        self.actionSave_Data.setText(QCoreApplication.translate("MainWindow", u"Save Data", None))
        self.actionNew_Project.setText(QCoreApplication.translate("MainWindow", u"New Project", None))
        self.actionCurrent_Path.setText(QCoreApplication.translate("MainWindow", u"Current Path", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionFTIR.setText(QCoreApplication.translate("MainWindow", u"FTIR", None))
#if QT_CONFIG(shortcut)
        self.actionFTIR.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
        self.actionQCM.setText(QCoreApplication.translate("MainWindow", u"QCM", None))
#if QT_CONFIG(shortcut)
        self.actionQCM.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+M", None))
#endif // QT_CONFIG(shortcut)
        self.actionPlot_Left.setText(QCoreApplication.translate("MainWindow", u"Plot Left", None))
        self.actionPlot_Right.setText(QCoreApplication.translate("MainWindow", u"Plot Right", None))
        self.actionClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.actionGraph_Options.setText(QCoreApplication.translate("MainWindow", u"Graph Options", None))
        self.actionSmooth.setText(QCoreApplication.translate("MainWindow", u"Smooth", None))
        self.actionPlot_Mass.setText(QCoreApplication.translate("MainWindow", u"Plot Mass", None))
        self.actionPlot_Pressure.setText(QCoreApplication.translate("MainWindow", u"Plot Pressure", None))
        self.actionGet_Info.setText(QCoreApplication.translate("MainWindow", u"Get Info", None))
        self.actionInitalize.setText(QCoreApplication.translate("MainWindow", u"Initalize", None))
        self.actionLinear_Fit.setText(QCoreApplication.translate("MainWindow", u"Linear Fit", None))
        self.actionClear_2.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionRandom_Plot.setText(QCoreApplication.translate("MainWindow", u"Random Plot", None))
        self.actionClear_Graph.setText(QCoreApplication.translate("MainWindow", u"Clear Graph", None))
#if QT_CONFIG(shortcut)
        self.actionClear_Graph.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.actionAdd_Figure.setText(QCoreApplication.translate("MainWindow", u"Add Figure", None))
        self.actionRemove_Figure.setText(QCoreApplication.translate("MainWindow", u"Remove Plot", None))
        self.actionImport_File.setText(QCoreApplication.translate("MainWindow", u"Import File", None))
        self.actionProject_View.setText(QCoreApplication.translate("MainWindow", u"Project View", None))
        self.actionSystem_View.setText(QCoreApplication.translate("MainWindow", u"System View", None))
        self.actionLinear_Fit_2.setText(QCoreApplication.translate("MainWindow", u"Linear Fit", None))
        self.actionCorrect_From_First.setText(QCoreApplication.translate("MainWindow", u"Correct From First", None))
        self.actionClear_Current_Data.setText(QCoreApplication.translate("MainWindow", u"Clear Current Data", None))
        self.actionXPS.setText(QCoreApplication.translate("MainWindow", u"XPS", None))
#if QT_CONFIG(shortcut)
        self.actionXPS.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.actionProject_Tree.setText(QCoreApplication.translate("MainWindow", u"Project Tree", None))
        self.actionDataBrowser.setText(QCoreApplication.translate("MainWindow", u"Data Browser", None))
        self.actionSE.setText(QCoreApplication.translate("MainWindow", u"SE", None))
#if QT_CONFIG(shortcut)
        self.actionSE.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionConsole.setText(QCoreApplication.translate("MainWindow", u"Console", None))
        self.actionQCM_Help.setText(QCoreApplication.translate("MainWindow", u"QCM Help", None))
        self.actionFTIR_Help.setText(QCoreApplication.translate("MainWindow", u"FTIR Help", None))
        self.actionXPS_Help.setText(QCoreApplication.translate("MainWindow", u"XPS Help", None))
        self.actionSE_Help.setText(QCoreApplication.translate("MainWindow", u"SE Help", None))
        self.actionOther_Help.setText(QCoreApplication.translate("MainWindow", u"Other Help", None))
        self.actionLegend_Toggle.setText(QCoreApplication.translate("MainWindow", u"Legend Toggle", None))
        self.actionSave_To_CSV.setText(QCoreApplication.translate("MainWindow", u"Save To CSV", None))
        self.actionDark.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.actionLight.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.actionDarkGrid.setText(QCoreApplication.translate("MainWindow", u"DarkGrid", None))
        self.actionLightGrid.setText(QCoreApplication.translate("MainWindow", u"LightGrid", None))
        self.actionTicks.setText(QCoreApplication.translate("MainWindow", u"Ticks", None))
        self.actionPaper.setText(QCoreApplication.translate("MainWindow", u"Paper", None))
        self.actionTalk.setText(QCoreApplication.translate("MainWindow", u"Talk", None))
        self.actionNotebook.setText(QCoreApplication.translate("MainWindow", u"Notebook", None))
        self.actionPoster.setText(QCoreApplication.translate("MainWindow", u"Poster", None))
        self.action1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.action2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.action3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.actionDirectory.setText(QCoreApplication.translate("MainWindow", u"Directory", None))
        self.actionFile.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.actionPaste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.action4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.action5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.actiondeep.setText(QCoreApplication.translate("MainWindow", u"deep", None))
        self.actionblue.setText(QCoreApplication.translate("MainWindow", u"blue", None))
        self.actionflare.setText(QCoreApplication.translate("MainWindow", u"flare", None))
        self.actionhls.setText(QCoreApplication.translate("MainWindow", u"hls", None))
        self.actionmako.setText(QCoreApplication.translate("MainWindow", u"mako", None))
        self.actioncrest.setText(QCoreApplication.translate("MainWindow", u"crest", None))
        self.actionmagma.setText(QCoreApplication.translate("MainWindow", u"magma", None))
        self.actioncubehelix.setText(QCoreApplication.translate("MainWindow", u"cubehelix", None))
        self.actionlight_b.setText(QCoreApplication.translate("MainWindow", u"light:b", None))
        self.actionseagreen.setText(QCoreApplication.translate("MainWindow", u"seagreen", None))
        self.actionspectral.setText(QCoreApplication.translate("MainWindow", u"spectral", None))
        self.actioncoolwarm.setText(QCoreApplication.translate("MainWindow", u"coolwarm", None))
        self.actionSeaborn_Settings.setText(QCoreApplication.translate("MainWindow", u"Seaborn Settings", None))
        self.actionNew_Project_2.setText(QCoreApplication.translate("MainWindow", u"New Project", None))
        self.actionOpen_Project.setText(QCoreApplication.translate("MainWindow", u"Open Project", None))
        self.actionRecent_Projects.setText(QCoreApplication.translate("MainWindow", u"Recent Projects", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionPrint.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.actionSettings_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionSettings_3.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionSettings_4.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionSettings_5.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionSettings_6.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionChange_Settings.setText(QCoreApplication.translate("MainWindow", u"Change Settings", None))
        self.actionCurve_Fitting.setText(QCoreApplication.translate("MainWindow", u"Curve Fitting", None))
#if QT_CONFIG(shortcut)
        self.actionCurve_Fitting.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionLoad_Data.setText(QCoreApplication.translate("MainWindow", u"Load Data", None))
        self.actionCalculator.setText(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.actionBar_Graph.setText(QCoreApplication.translate("MainWindow", u"Bar Graph", None))
        self.actionGraph_Test.setText(QCoreApplication.translate("MainWindow", u"Graph_Test", None))
        self.actionTight_Layout.setText(QCoreApplication.translate("MainWindow", u"Tight Layout", None))
#if QT_CONFIG(shortcut)
        self.actionTight_Layout.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionXRD.setText(QCoreApplication.translate("MainWindow", u"XRD", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuImport.setTitle(QCoreApplication.translate("MainWindow", u"Import", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuViews.setTitle(QCoreApplication.translate("MainWindow", u"Views", None))
        self.menuFigure.setTitle(QCoreApplication.translate("MainWindow", u"Graph", None))
        self.menuHELP.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuTesting.setTitle(QCoreApplication.translate("MainWindow", u"Testing", None))
    # retranslateUi

