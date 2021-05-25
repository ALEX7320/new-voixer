# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_venGuiaBRJVsm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from . import source

class Ui_venGuia(object):
    def setupUi(self, venGuia):
        if not venGuia.objectName():
            venGuia.setObjectName(u"venGuia")
        venGuia.resize(327, 248)
        icon = QIcon()
        icon.addFile(u":/icones/icons/vx_ticon.png", QSize(), QIcon.Normal, QIcon.Off)
        venGuia.setWindowIcon(icon)
        venGuia.setStyleSheet(u"QToolTip{ \n"
"	background-color: rgb(44, 109, 150);\n"
"color: white; \n"
"border: 1px solid white;\n"
"border-radius: 2px;\n"
"}")
        self.frame_2 = QFrame(venGuia)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 328, 249))
        self.frame_2.setStyleSheet(u"#frame_2{\n"
"\n"
"	background-color: rgb(28, 53, 69);\n"
"}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(3, 44, 321, 201))
        self.frame.setStyleSheet(u"#frame{\n"
"	background-color: rgb(22, 41, 54);\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btn_1 = QToolButton(self.frame)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setGeometry(QRect(10, 10, 91, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setMinimumSize(QSize(60, 0))
        self.btn_1.setFocusPolicy(Qt.NoFocus)
        self.btn_1.setStyleSheet(u"QToolButton{\n"
"	outline: 0px;\n"
"border-radius:2px;\n"
"	background-color: rgb(28, 53, 69);\n"
"font-family: \"Fashion Fetish\";\n"
"font-weight: Bold;\n"
"color:white;\n"
"font-size:11px\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton:disabled{\n"
"border:0px;\n"
"\n"
"	background-color: rgb(38, 81, 116);\n"
"}")
        self.btn_1.setIconSize(QSize(35, 35))
        self.btn_1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.btn_2 = QToolButton(self.frame)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setGeometry(QRect(110, 10, 91, 31))
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setMinimumSize(QSize(60, 0))
        self.btn_2.setFocusPolicy(Qt.NoFocus)
        self.btn_2.setStyleSheet(u"QToolButton{\n"
"	outline: 0px;\n"
"border-radius:2px;\n"
"	background-color: rgb(28, 53, 69);\n"
"font-family: \"Fashion Fetish\";\n"
"font-weight: Bold;\n"
"color:white;\n"
"font-size:11px\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton:disabled{\n"
"border:0px;\n"
"\n"
"	background-color: rgb(38, 81, 116);\n"
"}")
        self.btn_2.setIconSize(QSize(35, 35))
        self.btn_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.btn_3 = QToolButton(self.frame)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setGeometry(QRect(210, 10, 101, 31))
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setMinimumSize(QSize(60, 0))
        self.btn_3.setFocusPolicy(Qt.NoFocus)
        self.btn_3.setStyleSheet(u"QToolButton{\n"
"	outline: 0px;\n"
"border-radius:2px;\n"
"	background-color: rgb(28, 53, 69);\n"
"font-family: \"Fashion Fetish\";\n"
"font-weight: Bold;\n"
"color:white;\n"
"font-size:11px\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton:disabled{\n"
"border:0px;\n"
"\n"
"	background-color: rgb(38, 81, 116);\n"
"}")
        self.btn_3.setIconSize(QSize(35, 35))
        self.btn_3.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.hoja = QPlainTextEdit(self.frame)
        self.hoja.setObjectName(u"hoja")
        self.hoja.setGeometry(QRect(10, 50, 301, 141))
        self.hoja.setStyleSheet(u"/*CAJA TEXTO*/\n"
"QPlainTextEdit{\n"
"	color: white;\n"
"	font-size: 14px;\n"
"	border: 0px;\n"
"	padding: 10px;\n"
"	background-color: rgb(19, 36, 47);\n"
"	font-family: \"MADE Evolve Sans\";\n"
"	font-weight:Regular\n"
"}\n"
"")
        self.hoja.setTextInteractionFlags(Qt.NoTextInteraction)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(3, 3, 321, 41))
        self.frame_3.setStyleSheet(u"#frame_3{\n"
"\n"
"background-color: rgb(19, 35, 46);\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.btn_close = QPushButton(self.frame_3)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(280, 0, 40, 41))
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
        self.fr_move.setGeometry(QRect(0, 0, 241, 41))
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

        self.retranslateUi(venGuia)

        QMetaObject.connectSlotsByName(venGuia)
    # setupUi

    def retranslateUi(self, venGuia):
        venGuia.setWindowTitle(QCoreApplication.translate("venGuia", u"Gu\u00eda", None))
        self.btn_1.setText(QCoreApplication.translate("venGuia", u"Audios", None))
        self.btn_2.setText(QCoreApplication.translate("venGuia", u"Voces", None))
        self.btn_3.setText(QCoreApplication.translate("venGuia", u"Textos", None))
        self.hoja.setPlainText("")
        self.btn_close.setText("")
        self.labSon1_3.setText(QCoreApplication.translate("venGuia", u"GU\u00cdA", None))
        self.label_4.setText("")
    # retranslateUi

