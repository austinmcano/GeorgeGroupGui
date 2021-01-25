# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dw_FTIR.ui'
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


class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        if not DockWidget.objectName():
            DockWidget.setObjectName(u"DockWidget")
        DockWidget.resize(468, 510)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout = QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.FTIR_treeView = QTreeView(self.dockWidgetContents)
        self.FTIR_treeView.setObjectName(u"FTIR_treeView")

        self.gridLayout.addWidget(self.FTIR_treeView, 0, 0, 1, 3)

        self.lineEdit_4 = QLineEdit(self.dockWidgetContents)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 5, 1, 1, 2)

        self.label_4 = QLabel(self.dockWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.tabWidget = QTabWidget(self.dockWidgetContents)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line = QFrame(self.tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 4)

        self.ir_plot_cb = QComboBox(self.tab)
        self.ir_plot_cb.addItem("")
        self.ir_plot_cb.addItem("")
        self.ir_plot_cb.addItem("")
        self.ir_plot_cb.addItem("")
        self.ir_plot_cb.addItem("")
        self.ir_plot_cb.setObjectName(u"ir_plot_cb")

        self.gridLayout_2.addWidget(self.ir_plot_cb, 0, 0, 1, 2)

        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 2, 1, 1, 1)

        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 0, 2, 1, 2)

        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 1)

        self.label_13 = QLabel(self.tab)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 2, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.tab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_2.addWidget(self.lineEdit_2, 2, 2, 1, 1)

        self.smooth_pb = QPushButton(self.tab)
        self.smooth_pb.setObjectName(u"smooth_pb")

        self.gridLayout_2.addWidget(self.smooth_pb, 4, 2, 1, 1)

        self.skip_sb = QSpinBox(self.tab)
        self.skip_sb.setObjectName(u"skip_sb")
        self.skip_sb.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.skip_sb.setKeyboardTracking(False)
        self.skip_sb.setValue(0)

        self.gridLayout_2.addWidget(self.skip_sb, 4, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.int_type_cb = QComboBox(self.tab_3)
        self.int_type_cb.addItem("")
        self.int_type_cb.addItem("")
        self.int_type_cb.addItem("")
        self.int_type_cb.addItem("")
        self.int_type_cb.addItem("")
        self.int_type_cb.setObjectName(u"int_type_cb")
        self.int_type_cb.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_4.addWidget(self.int_type_cb, 0, 4, 1, 1)

        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.label_2, 0, 2, 1, 1)

        self.spinBox = QSpinBox(self.tab_3)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximumSize(QSize(100, 16777215))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(4)

        self.gridLayout_4.addWidget(self.spinBox, 0, 3, 1, 1)

        self.tableWidget = QTableWidget(self.tab_3)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 4):
            self.tableWidget.setRowCount(4)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(3, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(3, 2, __qtablewidgetitem18)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(320, 0))
        self.tableWidget.setMaximumSize(QSize(1000, 1000))
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(3)

        self.gridLayout_4.addWidget(self.tableWidget, 2, 2, 4, 3)

        self.integrate_pb = QPushButton(self.tab_3)
        self.integrate_pb.setObjectName(u"integrate_pb")
        self.integrate_pb.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_4.addWidget(self.integrate_pb, 6, 4, 1, 1)

        self.comboBox = QComboBox(self.tab_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_4.addWidget(self.comboBox, 6, 3, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.num_peaks_sb = QSpinBox(self.tab_2)
        self.num_peaks_sb.setObjectName(u"num_peaks_sb")
        self.num_peaks_sb.setMinimum(1)
        self.num_peaks_sb.setMaximum(5)

        self.gridLayout_3.addWidget(self.num_peaks_sb, 0, 1, 1, 1)

        self.tableWidget_2 = QTableWidget(self.tab_2)
        if (self.tableWidget_2.columnCount() < 5):
            self.tableWidget_2.setColumnCount(5)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem23)
        if (self.tableWidget_2.rowCount() < 9):
            self.tableWidget_2.setRowCount(9)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, __qtablewidgetitem32)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.gridLayout_3.addWidget(self.tableWidget_2, 1, 0, 1, 3)

        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.fit_shape_cb = QComboBox(self.tab_2)
        self.fit_shape_cb.addItem("")
        self.fit_shape_cb.addItem("")
        self.fit_shape_cb.addItem("")
        self.fit_shape_cb.setObjectName(u"fit_shape_cb")

        self.gridLayout_3.addWidget(self.fit_shape_cb, 0, 2, 1, 1)

        self.fit_pb = QPushButton(self.tab_2)
        self.fit_pb.setObjectName(u"fit_pb")

        self.gridLayout_3.addWidget(self.fit_pb, 2, 0, 1, 1)

        self.plot_current_pb = QPushButton(self.tab_2)
        self.plot_current_pb.setObjectName(u"plot_current_pb")

        self.gridLayout_3.addWidget(self.plot_current_pb, 2, 1, 1, 1)

        self.selectdata_pb = QPushButton(self.tab_2)
        self.selectdata_pb.setObjectName(u"selectdata_pb")

        self.gridLayout_3.addWidget(self.selectdata_pb, 2, 2, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_5 = QGridLayout(self.tab_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.fit_report_TE = QTextEdit(self.tab_4)
        self.fit_report_TE.setObjectName(u"fit_report_TE")

        self.gridLayout_5.addWidget(self.fit_report_TE, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout.addWidget(self.tabWidget, 3, 0, 1, 3)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"FTIR", None))
        self.label_4.setText(QCoreApplication.translate("DockWidget", u"Error Log", None))
        self.ir_plot_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"Sub Plot (dir)", None))
        self.ir_plot_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"Plot (dir)", None))
        self.ir_plot_cb.setItemText(2, QCoreApplication.translate("DockWidget", u"Diff Plot (dir)", None))
        self.ir_plot_cb.setItemText(3, QCoreApplication.translate("DockWidget", u"Diff (2)", None))
        self.ir_plot_cb.setItemText(4, QCoreApplication.translate("DockWidget", u"Plot", None))

        self.pushButton.setText(QCoreApplication.translate("DockWidget", u"Plot or Fit FTIR", None))
        self.label.setText(QCoreApplication.translate("DockWidget", u"Skip Every", None))
        self.label_13.setText(QCoreApplication.translate("DockWidget", u"From:To", None))
        self.smooth_pb.setText(QCoreApplication.translate("DockWidget", u"Smooth", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("DockWidget", u"IR Plot", None))
        self.int_type_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"Integrate Sub (dir)", None))
        self.int_type_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"Integrate Sub (dir) Corrected", None))
        self.int_type_cb.setItemText(2, QCoreApplication.translate("DockWidget", u"Integrate Diff (dir)", None))
        self.int_type_cb.setItemText(3, QCoreApplication.translate("DockWidget", u"Integrate Plot (dir)", None))
        self.int_type_cb.setItemText(4, QCoreApplication.translate("DockWidget", u"Integrate", None))

        self.label_2.setText(QCoreApplication.translate("DockWidget", u"Num of Ints", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DockWidget", u"From", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DockWidget", u"To", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DockWidget", u"Label", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DockWidget", u"Int. 1", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("DockWidget", u"Int. 2", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("DockWidget", u"Int. 3", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("DockWidget", u"Int. 4", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("DockWidget", u"400", None));
        ___qtablewidgetitem8 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("DockWidget", u"4000", None));
        ___qtablewidgetitem9 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("DockWidget", u"400", None));
        ___qtablewidgetitem10 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("DockWidget", u"4000", None));
        ___qtablewidgetitem11 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("DockWidget", u"400", None));
        ___qtablewidgetitem12 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("DockWidget", u"4000", None));
        ___qtablewidgetitem13 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("DockWidget", u"400", None));
        ___qtablewidgetitem14 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("DockWidget", u"4000", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.integrate_pb.setText(QCoreApplication.translate("DockWidget", u"Integrate", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("DockWidget", u"Left Axis", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("DockWidget", u"Right Axis", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("DockWidget", u"Integrate", None))
        ___qtablewidgetitem15 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("DockWidget", u"Peak 1", None));
        ___qtablewidgetitem16 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("DockWidget", u"Peak 2", None));
        ___qtablewidgetitem17 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("DockWidget", u"Peak 3", None));
        ___qtablewidgetitem18 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("DockWidget", u"Peak 4", None));
        ___qtablewidgetitem19 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("DockWidget", u"Peak 5", None));
        ___qtablewidgetitem20 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("DockWidget", u"Amp", None));
        ___qtablewidgetitem21 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("DockWidget", u"Amp Low", None));
        ___qtablewidgetitem22 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("DockWidget", u"New Row", None));
        ___qtablewidgetitem23 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("DockWidget", u"Cen", None));
        ___qtablewidgetitem24 = self.tableWidget_2.verticalHeaderItem(4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("DockWidget", u"Cen Low", None));
        ___qtablewidgetitem25 = self.tableWidget_2.verticalHeaderItem(5)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("DockWidget", u"New Row", None));
        ___qtablewidgetitem26 = self.tableWidget_2.verticalHeaderItem(6)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("DockWidget", u"Sigma", None));
        ___qtablewidgetitem27 = self.tableWidget_2.verticalHeaderItem(7)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("DockWidget", u"Sigma Low", None));
        ___qtablewidgetitem28 = self.tableWidget_2.verticalHeaderItem(8)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("DockWidget", u"Sigma High", None));
        self.label_5.setText(QCoreApplication.translate("DockWidget", u"Num of Peak", None))
        self.fit_shape_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"Voigt", None))
        self.fit_shape_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"Gaussian", None))
        self.fit_shape_cb.setItemText(2, QCoreApplication.translate("DockWidget", u"Lorentz", None))

        self.fit_pb.setText(QCoreApplication.translate("DockWidget", u"Fit", None))
        self.plot_current_pb.setText(QCoreApplication.translate("DockWidget", u"Plot Current", None))
        self.selectdata_pb.setText(QCoreApplication.translate("DockWidget", u"Select Data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("DockWidget", u"Fitting", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("DockWidget", u"Fit Report", None))
    # retranslateUi

