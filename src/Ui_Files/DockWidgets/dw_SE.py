# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dw_SE.ui'
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
        DockWidget.resize(437, 489)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout = QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.fill_cols_pb = QPushButton(self.dockWidgetContents)
        self.fill_cols_pb.setObjectName(u"fill_cols_pb")

        self.gridLayout.addWidget(self.fill_cols_pb, 3, 4, 1, 1)

        self.SE_treeView = QTreeView(self.dockWidgetContents)
        self.SE_treeView.setObjectName(u"SE_treeView")

        self.gridLayout.addWidget(self.SE_treeView, 0, 2, 1, 5)

        self.plot_pb = QPushButton(self.dockWidgetContents)
        self.plot_pb.setObjectName(u"plot_pb")

        self.gridLayout.addWidget(self.plot_pb, 3, 5, 1, 2)

        self.tabWidget = QTabWidget(self.dockWidgetContents)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_3 = QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_7 = QLabel(self.tab_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_9 = QLabel(self.tab_3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 1)

        self.skip_rows_sb = QSpinBox(self.tab_3)
        self.skip_rows_sb.setObjectName(u"skip_rows_sb")

        self.gridLayout_3.addWidget(self.skip_rows_sb, 0, 1, 1, 1)

        self.ax_cb = QComboBox(self.tab_3)
        self.ax_cb.addItem("")
        self.ax_cb.addItem("")
        self.ax_cb.setObjectName(u"ax_cb")

        self.gridLayout_3.addWidget(self.ax_cb, 0, 2, 1, 1)

        self.zero_correct_checkb = QCheckBox(self.tab_3)
        self.zero_correct_checkb.setObjectName(u"zero_correct_checkb")

        self.gridLayout_3.addWidget(self.zero_correct_checkb, 3, 0, 1, 1)

        self.linetype_cb = QComboBox(self.tab_3)
        self.linetype_cb.addItem("")
        self.linetype_cb.addItem("")
        self.linetype_cb.addItem("")
        self.linetype_cb.addItem("")
        self.linetype_cb.addItem("")
        self.linetype_cb.addItem("")
        self.linetype_cb.setObjectName(u"linetype_cb")

        self.gridLayout_3.addWidget(self.linetype_cb, 3, 1, 1, 1)

        self.comboBox = QComboBox(self.tab_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_3.addWidget(self.comboBox, 3, 2, 1, 1)

        self.xlabel_le = QLineEdit(self.tab_3)
        self.xlabel_le.setObjectName(u"xlabel_le")

        self.gridLayout_3.addWidget(self.xlabel_le, 1, 1, 1, 2)

        self.ylabel_le = QLineEdit(self.tab_3)
        self.ylabel_le.setObjectName(u"ylabel_le")

        self.gridLayout_3.addWidget(self.ylabel_le, 2, 1, 1, 2)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_4 = QGridLayout(self.tab_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lineEdit = QLineEdit(self.tab_4)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_4.addWidget(self.lineEdit, 2, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.tab_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_4.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_4 = QLabel(self.tab_4)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)

        self.checkBox = QCheckBox(self.tab_4)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_4.addWidget(self.checkBox, 0, 1, 1, 1)

        self.label_2 = QLabel(self.tab_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.change_rate_QL = QLabel(self.tab)
        self.change_rate_QL.setObjectName(u"change_rate_QL")

        self.gridLayout_2.addWidget(self.change_rate_QL, 1, 1, 1, 1)

        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.thick_change_QL = QLabel(self.tab)
        self.thick_change_QL.setObjectName(u"thick_change_QL")

        self.gridLayout_2.addWidget(self.thick_change_QL, 0, 1, 1, 1)

        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 2, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")

        self.gridLayout.addWidget(self.tabWidget, 2, 2, 1, 5)

        self.plot_type_cb = QComboBox(self.dockWidgetContents)
        self.plot_type_cb.addItem("")
        self.plot_type_cb.addItem("")
        self.plot_type_cb.addItem("")
        self.plot_type_cb.setObjectName(u"plot_type_cb")

        self.gridLayout.addWidget(self.plot_type_cb, 3, 2, 1, 1)

        self.x_list_cb = QComboBox(self.dockWidgetContents)
        self.x_list_cb.addItem("")
        self.x_list_cb.addItem("")
        self.x_list_cb.setObjectName(u"x_list_cb")

        self.gridLayout.addWidget(self.x_list_cb, 3, 3, 1, 1)

        self.SEY_tw = QTreeWidget(self.dockWidgetContents)
        self.SEY_tw.setObjectName(u"SEY_tw")
        self.SEY_tw.setSelectionMode(QAbstractItemView.SingleSelection)

        self.gridLayout.addWidget(self.SEY_tw, 1, 4, 1, 3)

        self.SEX_tw = QTreeWidget(self.dockWidgetContents)
        self.SEX_tw.setObjectName(u"SEX_tw")

        self.gridLayout.addWidget(self.SEX_tw, 1, 2, 1, 2)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"SE", None))
        self.fill_cols_pb.setText(QCoreApplication.translate("DockWidget", u"Grab Columns", None))
        self.plot_pb.setText(QCoreApplication.translate("DockWidget", u"Plot", None))
        self.label_8.setText(QCoreApplication.translate("DockWidget", u"X Label", None))
        self.label_7.setText(QCoreApplication.translate("DockWidget", u"Skip Rows: ", None))
        self.label_9.setText(QCoreApplication.translate("DockWidget", u"Y Label", None))
        self.ax_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"Left Ax", None))
        self.ax_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"Right Ax", None))

        self.zero_correct_checkb.setText(QCoreApplication.translate("DockWidget", u"Zero Correct", None))
        self.linetype_cb.setItemText(0, QCoreApplication.translate("DockWidget", u".-", None))
        self.linetype_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"-.", None))
        self.linetype_cb.setItemText(2, QCoreApplication.translate("DockWidget", u".", None))
        self.linetype_cb.setItemText(3, QCoreApplication.translate("DockWidget", u"-", None))
        self.linetype_cb.setItemText(4, QCoreApplication.translate("DockWidget", u"--", None))
        self.linetype_cb.setItemText(5, QCoreApplication.translate("DockWidget", u",", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("DockWidget", u"r", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("DockWidget", u"b", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("DockWidget", u"g", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("DockWidget", u"k", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("DockWidget", u"Axis Properties", None))
        self.lineEdit.setText(QCoreApplication.translate("DockWidget", u"0", None))
        self.lineEdit_2.setText(QCoreApplication.translate("DockWidget", u"0", None))
        self.label_4.setText(QCoreApplication.translate("DockWidget", u"Use Cols:", None))
        self.checkBox.setText(QCoreApplication.translate("DockWidget", u"Use Column Name", None))
        self.label_2.setText(QCoreApplication.translate("DockWidget", u"Skip Columns:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("DockWidget", u"Params", None))
        self.label_5.setText(QCoreApplication.translate("DockWidget", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("DockWidget", u"Growth/Etch Rate (A)/Cyc", None))
        self.change_rate_QL.setText(QCoreApplication.translate("DockWidget", u"0", None))
        self.label.setText(QCoreApplication.translate("DockWidget", u"Thickness Change (A)", None))
        self.thick_change_QL.setText(QCoreApplication.translate("DockWidget", u"0", None))
        self.label_6.setText(QCoreApplication.translate("DockWidget", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("DockWidget", u"Calculated", None))
        self.plot_type_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"Ext. Plot", None))
        self.plot_type_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"Linear Fit", None))
        self.plot_type_cb.setItemText(2, QCoreApplication.translate("DockWidget", u"X vs Y", None))

        self.x_list_cb.setItemText(0, QCoreApplication.translate("DockWidget", u"X (ints)", None))
        self.x_list_cb.setItemText(1, QCoreApplication.translate("DockWidget", u"X (half-ints)", None))

        ___qtreewidgetitem = self.SEY_tw.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("DockWidget", u"SE-Y", None));
        ___qtreewidgetitem1 = self.SEX_tw.headerItem()
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("DockWidget", u"SE-X", None));
    # retranslateUi

