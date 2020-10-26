# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_dialog.ui'
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(367, 240)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.SE_pb = QPushButton(Dialog)
        self.SE_pb.setObjectName(u"SE_pb")

        self.gridLayout.addWidget(self.SE_pb, 4, 1, 1, 1)

        self.QCM_pb = QPushButton(Dialog)
        self.QCM_pb.setObjectName(u"QCM_pb")

        self.gridLayout.addWidget(self.QCM_pb, 3, 1, 1, 1)

        self.XPS_pb = QPushButton(Dialog)
        self.XPS_pb.setObjectName(u"XPS_pb")

        self.gridLayout.addWidget(self.XPS_pb, 5, 1, 1, 1)

        self.FTIR_pb = QPushButton(Dialog)
        self.FTIR_pb.setObjectName(u"FTIR_pb")

        self.gridLayout.addWidget(self.FTIR_pb, 2, 1, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.CF_pb = QPushButton(Dialog)
        self.CF_pb.setObjectName(u"CF_pb")

        self.gridLayout.addWidget(self.CF_pb, 6, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Welcome to the George group gui!", None))
        self.SE_pb.setText(QCoreApplication.translate("Dialog", u"Ellipsometry", None))
        self.QCM_pb.setText(QCoreApplication.translate("Dialog", u"Quartz Crystal Microbalance", None))
        self.XPS_pb.setText(QCoreApplication.translate("Dialog", u"X-ray Photoelectron Spectroscopy", None))
        self.FTIR_pb.setText(QCoreApplication.translate("Dialog", u"Infrared Spectroscopy", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Select what closest matches up with why you are here:", None))
        self.CF_pb.setText(QCoreApplication.translate("Dialog", u"Curve Fitting", None))
    # retranslateUi

