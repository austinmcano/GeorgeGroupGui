# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dw_FTIR.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
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
        DockWidget.resize(456, 536)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout = QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.dockWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.dockWidgetContents)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 5, 1, 1, 2)

        self.FTIR_treeView = QTreeView(self.dockWidgetContents)
        self.FTIR_treeView.setObjectName(u"FTIR_treeView")

        self.gridLayout.addWidget(self.FTIR_treeView, 0, 0, 1, 3)

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

        self.skip_every_LE = QLineEdit(self.tab)
        self.skip_every_LE.setObjectName(u"skip_every_LE")

        self.gridLayout_2.addWidget(self.skip_every_LE, 4, 1, 1, 1)

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

        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)

        self.spinBox = QSpinBox(self.tab_3)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(4)

        self.gridLayout_4.addWidget(self.spinBox, 4, 0, 1, 1)

        self.int_type_cb = QComboBox(self.tab_3)
        self.int_type_cb.addItem("")
        self.int_type_cb.addItem("")
        self.int_type_cb.addItem("")
        self.int_type_cb.addItem("")
        self.int_type_cb.setObjectName(u"int_type_cb")

        self.gridLayout_4.addWidget(self.int_type_cb, 3, 0, 1, 1)

        self.integrate_pb = QPushButton(self.tab_3)
        self.integrate_pb.setObjectName(u"integrate_pb")

        self.gridLayout_4.addWidget(self.integrate_pb, 5, 0, 1, 1)

        self.tableWidget = QTableWidget(self.tab_3)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 4):
            self.tableWidget.setRowCount(4)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(3, 1, __qtablewidgetitem13)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMaximumSize(QSize(240, 1000))
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)

        self.gridLayout_4.addWidget(self.tableWidget, 2, 2, 4, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_5 = QGridLayout(self.tab_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalSlider = QSlider(self.tab_4)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_5.addWidget(self.horizontalSlider, 0, 1, 1, 1)

        self.label_3 = QLabel(self.tab_4)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSlider_3 = QSlider(self.tab_2)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.horizontalSlider_3, 1, 1, 1, 2)

        self.horizontalSlider_4 = QSlider(self.tab_2)
        self.horizontalSlider_4.setObjectName(u"horizontalSlider_4")
        self.horizontalSlider_4.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.horizontalSlider_4, 4, 1, 1, 2)

        self.horizontalSlider_2 = QSlider(self.tab_2)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.horizontalSlider_2, 3, 1, 1, 2)

        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 4, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.tab_2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_3.addWidget(self.radioButton_2, 0, 1, 1, 1)

        self.radioButton_3 = QRadioButton(self.tab_2)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout_3.addWidget(self.radioButton_3, 0, 2, 1, 1)

        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)

        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 3, 0, 1, 1)

        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 1, 3, 1, 1)

        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 3, 3, 1, 1)

        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 4, 3, 1, 1)

        self.radioButton = QRadioButton(self.tab_2)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_3.addWidget(self.radioButton, 0, 3, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 3, 0, 1, 3)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"FTIR", None))
        self.label_4.setText(QCoreApplication.translate("DockWidget", u"Error Log", None))
        self.skip_every_LE.setText(QCoreApplication.translate("DockWidget", u"0", None))
        self.ir_plot_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"Plot", None))
        self.ir_plot_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"Plot (dir)", None))
        self.ir_plot_cb.setItemText(2, QCoreApplication.translate("DockWidget", u"Sub Plot (dir)", None))
        self.ir_plot_cb.setItemText(3, QCoreApplication.translate("DockWidget", u"Diff Plot (dir)", None))
        self.ir_plot_cb.setItemText(4, QCoreApplication.translate("DockWidget", u"Diff (2)", None))

        self.pushButton.setText(QCoreApplication.translate("DockWidget", u"Plot or Fit FTIR", None))
        self.label.setText(QCoreApplication.translate("DockWidget", u"Skip Every", None))
        self.label_13.setText(QCoreApplication.translate("DockWidget", u"From:To", None))
        self.smooth_pb.setText(QCoreApplication.translate("DockWidget", u"Smooth", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("DockWidget", u"IR Plot", None))
        self.label_2.setText(QCoreApplication.translate("DockWidget", u"Num of Ints", None))
        self.int_type_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"Integrate Sub (dir)", None))
        self.int_type_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"Integrate Diff (dir)", None))
        self.int_type_cb.setItemText(2, QCoreApplication.translate("DockWidget", u"Integrate Plot (dir)", None))
        self.int_type_cb.setItemText(3, QCoreApplication.translate("DockWidget", u"Integrate", None))

        self.integrate_pb.setText(QCoreApplication.translate("DockWidget", u"Integrate", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DockWidget", u"From", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DockWidget", u"To", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DockWidget", u"Int. 1", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DockWidget", u"Int. 2", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("DockWidget", u"Int. 3", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("DockWidget", u"Int. 4", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("DockWidget", u"400", None));
        ___qtablewidgetitem7 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("DockWidget", u"4000", None));
        ___qtablewidgetitem8 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("DockWidget", u"400", None));
        ___qtablewidgetitem9 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("DockWidget", u"4000", None));
        ___qtablewidgetitem10 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("DockWidget", u"400", None));
        ___qtablewidgetitem11 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("DockWidget", u"4000", None));
        ___qtablewidgetitem12 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("DockWidget", u"400", None));
        ___qtablewidgetitem13 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("DockWidget", u"4000", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("DockWidget", u"Integrate", None))
        self.label_3.setText(QCoreApplication.translate("DockWidget", u"Threshold", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("DockWidget", u"Find Peaks", None))
        self.label_9.setText(QCoreApplication.translate("DockWidget", u"Position", None))
        self.radioButton_2.setText(QCoreApplication.translate("DockWidget", u"Peak 1", None))
        self.radioButton_3.setText(QCoreApplication.translate("DockWidget", u"Peak 2", None))
        self.label_7.setText(QCoreApplication.translate("DockWidget", u"Amp", None))
        self.label_8.setText(QCoreApplication.translate("DockWidget", u"FWHM", None))
        self.label_10.setText(QCoreApplication.translate("DockWidget", u"0", None))
        self.label_11.setText(QCoreApplication.translate("DockWidget", u"0", None))
        self.label_12.setText(QCoreApplication.translate("DockWidget", u"0", None))
        self.radioButton.setText(QCoreApplication.translate("DockWidget", u"Peak 3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("DockWidget", u"Fitting", None))
    # retranslateUi

