# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_venLicenciaDhujrP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from . import source

class Ui_venLicencia(object):
    def setupUi(self, venLicencia):
        if not venLicencia.objectName():
            venLicencia.setObjectName(u"venLicencia")
        venLicencia.resize(367, 428)
        icon = QIcon()
        icon.addFile(u":/icones/icons/vx_ticon.png", QSize(), QIcon.Normal, QIcon.Off)
        venLicencia.setWindowIcon(icon)
        venLicencia.setStyleSheet(u"QToolTip{ \n"
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
        self.frame_2 = QFrame(venLicencia)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 367, 428))
        self.frame_2.setStyleSheet(u"#frame_2{\n"
"\n"
"	background-color: rgb(28, 53, 69);\n"
"}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(3, 44, 361, 381))
        self.frame.setStyleSheet(u"#frame{\n"
"	background-color: rgb(22, 41, 54);\n"
"}\n"
"\n"
"\n"
"/*SCROLL VERTICAL*/\n"
"\n"
"QScrollBar:vertical{\n"
"	background-color: rgb(19, 36, 47);\n"
"	width: 17px; \n"
"	margin: 4px 0px 4x 9px;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"	background: ;\n"
"	background-color: rgb(53, 111, 162);\n"
"    border-radius:2px;\n"
"	margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0 px;\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.hoja = QPlainTextEdit(self.frame)
        self.hoja.setObjectName(u"hoja")
        self.hoja.setGeometry(QRect(10, 40, 341, 331))
        self.hoja.setStyleSheet(u"/*CAJA TEXTO*/\n"
"QPlainTextEdit{\n"
"	color: white;\n"
"	font-size: 10px;\n"
"	border: 0px;\n"
"	padding: 10px;\n"
"	background-color: rgb(19, 36, 47);\n"
"	font-weight:300\n"
"}\n"
"")
        self.hoja.setTextInteractionFlags(Qt.NoTextInteraction)
        self.labSon1_4 = QLabel(self.frame)
        self.labSon1_4.setObjectName(u"labSon1_4")
        self.labSon1_4.setGeometry(QRect(13, 10, 251, 21))
        self.labSon1_4.setMinimumSize(QSize(60, 0))
        self.labSon1_4.setStyleSheet(u"color:white;\n"
"font-family: \"Fashion Fetish\";\n"
"font-weight: Bold;\n"
"font-size:10px")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(3, 3, 361, 41))
        self.frame_3.setStyleSheet(u"#frame_3{\n"
"\n"
"background-color: rgb(19, 35, 46);\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.btn_close = QPushButton(self.frame_3)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(320, 0, 40, 41))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setFocusPolicy(Qt.NoFocus)
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"\n"
"	outline: 0px;\n"
"border:0px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(53, 111, 162);\n"
"\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/title_bar/icons/titlesq.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon1)
        self.btn_close.setIconSize(QSize(12, 12))
        self.fr_move = QFrame(self.frame_3)
        self.fr_move.setObjectName(u"fr_move")
        self.fr_move.setGeometry(QRect(0, 0, 311, 41))
        self.fr_move.setFrameShape(QFrame.NoFrame)
        self.fr_move.setFrameShadow(QFrame.Raised)
        self.labSon1_3 = QLabel(self.fr_move)
        self.labSon1_3.setObjectName(u"labSon1_3")
        self.labSon1_3.setGeometry(QRect(40, 10, 141, 21))
        self.labSon1_3.setMinimumSize(QSize(60, 0))
        self.labSon1_3.setStyleSheet(u"color:white;\n"
"font-family: \"Fashion Fetish\";\n"
"font-weight: Bold;\n"
"font-size:10px")
        self.label_4 = QLabel(self.fr_move)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 21, 21))
        self.label_4.setStyleSheet(u"background-color: transparent;")
        self.label_4.setPixmap(QPixmap(u":/icones/icons/vx_sicon.png"))
        self.label_4.setScaledContents(True)

        self.retranslateUi(venLicencia)

        QMetaObject.connectSlotsByName(venLicencia)
    # setupUi

    def retranslateUi(self, venLicencia):
        venLicencia.setWindowTitle(QCoreApplication.translate("venLicencia", u"Licencia", None))
        self.hoja.setPlainText("")
        self.labSon1_4.setText(QCoreApplication.translate("venLicencia", u"Acerca de la licencia y t\u00e9rminos de uso.", None))
        self.btn_close.setText("")
        self.labSon1_3.setText(QCoreApplication.translate("venLicencia", u"LICENCIA", None))
        self.label_4.setText("")
    # retranslateUi

