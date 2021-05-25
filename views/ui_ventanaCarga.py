# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_ventanaCargaJsHBJA.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from . import source

class Ui_VentanaCarga(object):
    def setupUi(self, VentanaCarga):
        if not VentanaCarga.objectName():
            VentanaCarga.setObjectName(u"VentanaCarga")
        VentanaCarga.resize(501, 223)
        icon = QIcon()
        icon.addFile(u":/icones/icons/vx_ticon.png", QSize(), QIcon.Normal, QIcon.Off)
        VentanaCarga.setWindowIcon(icon)
        VentanaCarga.setStyleSheet(u"QToolTip{ \n"
"	background-color: rgb(44, 109, 150);\n"
"color: white; \n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"	gridline-color: rgb(35, 255, 35);\n"
"\n"
"}\n"
"QMenu{ \n"
"	background-color: rgb(44, 109, 150);\n"
"color: white; \n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"}\n"
"QMenu:disabled{\n"
"	color: rgba(255, 255, 255, 0.5);\n"
"}")
        self.frameLoad_2 = QFrame(VentanaCarga)
        self.frameLoad_2.setObjectName(u"frameLoad_2")
        self.frameLoad_2.setGeometry(QRect(20, 20, 111, 181))
        self.frameLoad_2.setStyleSheet(u"#frameLoad_2{\n"
"	background-color: rgb(16, 30, 39);\n"
"border:2px solid rgb(37, 69, 90);\n"
"border-right:0px;\n"
"\n"
"}\n"
"")
        self.frameLoad_2.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frameLoad_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(37, 180, 16, 16))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(6)
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frameLoad_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 50, 91, 81))
        self.label.setStyleSheet(u"background-color: transparent;")
        self.label.setPixmap(QPixmap(u":/icones/icons/vx_sicon.png"))
        self.label.setScaledContents(True)
        self.labTitu_2 = QLabel(self.frameLoad_2)
        self.labTitu_2.setObjectName(u"labTitu_2")
        self.labTitu_2.setGeometry(QRect(10, 156, 81, 21))
        self.labTitu_2.setStyleSheet(u"font-size:12px;\n"
"color: rgb(255, 255, 255);\n"
"font-family: \"Fashion Fetish\";\n"
"font-weight: Bold;")
        self.frameLoad = QFrame(VentanaCarga)
        self.frameLoad.setObjectName(u"frameLoad")
        self.frameLoad.setGeometry(QRect(130, 20, 341, 181))
        self.frameLoad.setStyleSheet(u"#frameLoad{\n"
"\n"
"border:2px solid rgb(37, 69, 90);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0113636 rgba(19, 35, 46, 255), stop:1 rgba(28, 53, 69, 255));\n"
"border-left:0px;\n"
"\n"
"}")
        self.frameLoad.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.frameLoad)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(37, 180, 16, 16))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.labTitu = QLabel(self.frameLoad)
        self.labTitu.setObjectName(u"labTitu")
        self.labTitu.setGeometry(QRect(20, 30, 311, 61))
        self.labTitu.setStyleSheet(u"font-size:40px;\n"
"color: rgb(255, 255, 255);\n"
"font-family: \"Fashion Fetish\";\n"
"font-weight: Bold;")
        self.progreLoad = QProgressBar(self.frameLoad)
        self.progreLoad.setObjectName(u"progreLoad")
        self.progreLoad.setGeometry(QRect(20, 120, 301, 31))
        self.progreLoad.setStyleSheet(u"QProgressBar {\n"
"	color: white;\n"
"	height: 28px;\n"
"	text-align: center;\n"
"border: 2px solid white;\n"
"	background-color: rgb(65, 98, 118);\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0.0113636 rgba(53, 102, 132, 255), stop:1 rgba(40, 77, 112, 255));\n"
"\n"
"}")
        self.progreLoad.setValue(17)
        self.progreLoad.setTextVisible(True)
        self.progreLoad.setOrientation(Qt.Horizontal)
        self.progreLoad.setTextDirection(QProgressBar.TopToBottom)
        self.labTitu_3 = QLabel(self.frameLoad)
        self.labTitu_3.setObjectName(u"labTitu_3")
        self.labTitu_3.setGeometry(QRect(20, 80, 201, 31))
        self.labTitu_3.setStyleSheet(u"color:white;\n"
"font-family: \"MADE Evolve Sans\";\n"
"font-weight:400;\n"
"font-size:20px")

        self.retranslateUi(VentanaCarga)

        QMetaObject.connectSlotsByName(VentanaCarga)
    # setupUi

    def retranslateUi(self, VentanaCarga):
        VentanaCarga.setWindowTitle(QCoreApplication.translate("VentanaCarga", u"Cargando", None))
        self.label.setText("")
        self.labTitu_2.setText(QCoreApplication.translate("VentanaCarga", u"v1.0", None))
        self.labTitu.setText(QCoreApplication.translate("VentanaCarga", u"NEW VOIXER", None))
        self.labTitu_3.setText(QCoreApplication.translate("VentanaCarga", u"Cargando...", None))
    # retranslateUi

