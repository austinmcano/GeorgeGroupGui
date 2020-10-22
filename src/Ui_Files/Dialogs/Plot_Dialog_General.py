# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Plot_Dialog_General.ui'
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(527, 410)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 7, 1, 1, 1)

        self.treeWidget = QTreeWidget(Dialog)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setMaximumSize(QSize(16777215, 175))

        self.gridLayout_2.addWidget(self.treeWidget, 1, 0, 1, 1)

        self.treeWidget_2 = QTreeWidget(Dialog)
        self.treeWidget_2.setObjectName(u"treeWidget_2")
        self.treeWidget_2.setMaximumSize(QSize(16777215, 175))

        self.gridLayout_2.addWidget(self.treeWidget_2, 1, 1, 1, 1)

        self.skip_rows_num = QTextEdit(Dialog)
        self.skip_rows_num.setObjectName(u"skip_rows_num")
        self.skip_rows_num.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.skip_rows_num, 5, 1, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 5, 0, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)

        self.x_label = QLineEdit(Dialog)
        self.x_label.setObjectName(u"x_label")

        self.gridLayout_2.addWidget(self.x_label, 2, 1, 1, 1)

        self.y_label = QLineEdit(Dialog)
        self.y_label.setObjectName(u"y_label")

        self.gridLayout_2.addWidget(self.y_label, 3, 1, 1, 1)

        self.QP_pushbutton = QPushButton(Dialog)
        self.QP_pushbutton.setObjectName(u"QP_pushbutton")

        self.gridLayout_2.addWidget(self.QP_pushbutton, 7, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Dialog", u"X Axes", None));
        ___qtreewidgetitem1 = self.treeWidget_2.headerItem()
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Dialog", u"Y Axes", None));
        self.skip_rows_num.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.SF NS Text'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"X Axis Label", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Skip Rows Number", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Y Axis Label", None))
        self.x_label.setText("")
        self.y_label.setText("")
        self.QP_pushbutton.setText(QCoreApplication.translate("Dialog", u"Quick Plot", None))
    # retranslateUi

