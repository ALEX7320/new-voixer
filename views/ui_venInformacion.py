# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_venInformacionqqVtQH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from . import source

class Ui_venInformacion(object):
    def setupUi(self, venInformacion):
        if not venInformacion.objectName():
            venInformacion.setObjectName(u"venInformacion")
        venInformacion.resize(248, 299)
        icon = QIcon()
        icon.addFile(u":/icones/icons/vx_ticon.png", QSize(), QIcon.Normal, QIcon.Off)
        venInformacion.setWindowIcon(icon)
        venInformacion.setStyleSheet(u"QToolTip{ \n"
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
        self.frame_2 = QFrame(venInformacion)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 248, 299))
        self.frame_2.setStyleSheet(u"#frame_2{\n"
"\n"
"	background-color: rgb(28, 53, 69);\n"
"}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(3, 44, 241, 251))
        self.frame.setStyleSheet(u"#frame{\n"
"	background-color: rgb(22, 41, 54);\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btn_ln = QPushButton(self.frame)
        self.btn_ln.setObjectName(u"btn_ln")
        self.btn_ln.setGeometry(QRect(70, 200, 30, 30))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ln.sizePolicy().hasHeightForWidth())
        self.btn_ln.setSizePolicy(sizePolicy)
        self.btn_ln.setFocusPolicy(Qt.NoFocus)
        self.btn_ln.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(28, 53, 69);\n"
"border:0px;\n"
"	outline: 0px;\n"
"}\n"
"QPushButton:pressed{\n"
"\n"
"background-color: rgb(38, 81, 116);\n"
"\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/contacto/icons/cn_lk.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ln.setIcon(icon1)
        self.btn_ln.setIconSize(QSize(15, 15))
        self.btn_git = QPushButton(self.frame)
        self.btn_git.setObjectName(u"btn_git")
        self.btn_git.setGeometry(QRect(110, 200, 30, 30))
        sizePolicy.setHeightForWidth(self.btn_git.sizePolicy().hasHeightForWidth())
        self.btn_git.setSizePolicy(sizePolicy)
        self.btn_git.setFocusPolicy(Qt.NoFocus)
        self.btn_git.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(28, 53, 69);\n"
"border:0px;\n"
"	outline: 0px;\n"
"}\n"
"QPushButton:pressed{\n"
"\n"
"background-color: rgb(38, 81, 116);\n"
"\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/contacto/icons/cn_git.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_git.setIcon(icon2)
        self.btn_git.setIconSize(QSize(15, 15))
        self.btn_yt = QPushButton(self.frame)
        self.btn_yt.setObjectName(u"btn_yt")
        self.btn_yt.setGeometry(QRect(150, 200, 30, 30))
        sizePolicy.setHeightForWidth(self.btn_yt.sizePolicy().hasHeightForWidth())
        self.btn_yt.setSizePolicy(sizePolicy)
        self.btn_yt.setFocusPolicy(Qt.NoFocus)
        self.btn_yt.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(28, 53, 69);\n"
"border:0px;\n"
"	outline: 0px;\n"
"}\n"
"QPushButton:pressed{\n"
"\n"
"background-color: rgb(38, 81, 116);\n"
"\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/contacto/icons/cn_yt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_yt.setIcon(icon3)
        self.btn_yt.setIconSize(QSize(15, 15))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 140, 20, 20))
        self.label_2.setPixmap(QPixmap(u":/contacto/icons/cn_per.png"))
        self.label_2.setScaledContents(True)
        self.labSon1_4 = QLabel(self.frame)
        self.labSon1_4.setObjectName(u"labSon1_4")
        self.labSon1_4.setGeometry(QRect(30, 110, 141, 21))
        self.labSon1_4.setMinimumSize(QSize(60, 0))
        self.labSon1_4.setStyleSheet(u"color:white;\n"
"font-family: \"Fashion Fetish\";\n"
"font-weight: Bold;\n"
"font-size:10px")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 170, 21, 21))
        self.label.setPixmap(QPixmap(u":/contacto/icons/cn_cor.png"))
        self.label.setScaledContents(True)
        self.labSon1_6 = QLabel(self.frame)
        self.labSon1_6.setObjectName(u"labSon1_6")
        self.labSon1_6.setGeometry(QRect(60, 140, 141, 21))
        self.labSon1_6.setMinimumSize(QSize(60, 0))
        self.labSon1_6.setStyleSheet(u"color:white;\n"
"	font-family: \"MADE Evolve Sans\";\n"
"font-weight: 300;\n"
"font-size:15px")
        self.labSon1_7 = QLabel(self.frame)
        self.labSon1_7.setObjectName(u"labSon1_7")
        self.labSon1_7.setGeometry(QRect(60, 170, 161, 21))
        self.labSon1_7.setMinimumSize(QSize(60, 0))
        self.labSon1_7.setStyleSheet(u"color:white;\n"
"	font-family: \"MADE Evolve Sans\";\n"
"font-weight: 300;\n"
"font-size:15px")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 20, 41, 41))
        self.label_3.setPixmap(QPixmap(u":/icones/icons/vx_sicon.png"))
        self.label_3.setScaledContents(True)
        self.labSon1_5 = QLabel(self.frame)
        self.labSon1_5.setObjectName(u"labSon1_5")
        self.labSon1_5.setGeometry(QRect(80, 30, 131, 31))
        self.labSon1_5.setMinimumSize(QSize(60, 0))
        self.labSon1_5.setStyleSheet(u"color:white;\n"
"font-family: \"Fashion Fetish\";\n"
"font-weight: Bold;\n"
"font-size:25px")
        self.labSon1_8 = QLabel(self.frame)
        self.labSon1_8.setObjectName(u"labSon1_8")
        self.labSon1_8.setGeometry(QRect(80, 10, 131, 31))
        self.labSon1_8.setMinimumSize(QSize(60, 0))
        self.labSon1_8.setStyleSheet(u"color:white;\n"
"font-family: \"Fashion Fetish\";\n"
"font-weight: Bold;\n"
"font-size:11px")
        self.labSon1_9 = QLabel(self.frame)
        self.labSon1_9.setObjectName(u"labSon1_9")
        self.labSon1_9.setGeometry(QRect(30, 70, 60, 21))
        self.labSon1_9.setMinimumSize(QSize(60, 0))
        self.labSon1_9.setStyleSheet(u"color:white;\n"
"font-family: \"Fashion Fetish\";\n"
"font-weight: Bold;\n"
"font-size:10px")
        self.labSon1_10 = QLabel(self.frame)
        self.labSon1_10.setObjectName(u"labSon1_10")
        self.labSon1_10.setGeometry(QRect(80, 70, 141, 21))
        self.labSon1_10.setMinimumSize(QSize(60, 0))
        self.labSon1_10.setStyleSheet(u"color:white;\n"
"	font-family: \"MADE Evolve Sans\";\n"
"font-weight: 300;\n"
"font-size:15px")
        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 90, 221, 16))
        self.line_2.setStyleSheet(u"color: rgba(255, 255, 255,0.2);")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setFrameShape(QFrame.HLine)
        self.labSon1_8.raise_()
        self.btn_ln.raise_()
        self.btn_git.raise_()
        self.btn_yt.raise_()
        self.label_2.raise_()
        self.labSon1_4.raise_()
        self.label.raise_()
        self.labSon1_6.raise_()
        self.labSon1_7.raise_()
        self.label_3.raise_()
        self.labSon1_5.raise_()
        self.labSon1_9.raise_()
        self.labSon1_10.raise_()
        self.line_2.raise_()
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(3, 3, 241, 41))
        self.frame_3.setStyleSheet(u"#frame_3{\n"
"\n"
"background-color: rgb(19, 35, 46);\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.btn_close = QPushButton(self.frame_3)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(200, 0, 40, 41))
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
        icon4 = QIcon()
        icon4.addFile(u":/title_bar/icons/titlesq.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon4)
        self.btn_close.setIconSize(QSize(12, 12))
        self.fr_move = QFrame(self.frame_3)
        self.fr_move.setObjectName(u"fr_move")
        self.fr_move.setGeometry(QRect(0, 0, 191, 41))
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

        self.retranslateUi(venInformacion)

        QMetaObject.connectSlotsByName(venInformacion)
    # setupUi

    def retranslateUi(self, venInformacion):
        venInformacion.setWindowTitle(QCoreApplication.translate("venInformacion", u"Informaci\u00f3n", None))
#if QT_CONFIG(tooltip)
        self.btn_ln.setToolTip(QCoreApplication.translate("venInformacion", u"Linkedin", None))
#endif // QT_CONFIG(tooltip)
        self.btn_ln.setText("")
#if QT_CONFIG(tooltip)
        self.btn_git.setToolTip(QCoreApplication.translate("venInformacion", u"GitHub", None))
#endif // QT_CONFIG(tooltip)
        self.btn_git.setText("")
#if QT_CONFIG(tooltip)
        self.btn_yt.setToolTip(QCoreApplication.translate("venInformacion", u"YouTube", None))
#endif // QT_CONFIG(tooltip)
        self.btn_yt.setText("")
        self.labSon1_4.setText(QCoreApplication.translate("venInformacion", u"Desarrollador:", None))
        self.labSon1_6.setText(QCoreApplication.translate("venInformacion", u"Alex Chuquillanqui", None))
        self.labSon1_7.setText(QCoreApplication.translate("venInformacion", u"alex7320k@gmail.com", None))
        self.labSon1_5.setText(QCoreApplication.translate("venInformacion", u"VOIXER", None))
        self.labSon1_8.setText(QCoreApplication.translate("venInformacion", u"NEW", None))
        self.labSon1_9.setText(QCoreApplication.translate("venInformacion", u"Versi\u00f3n:", None))
        self.labSon1_10.setText(QCoreApplication.translate("venInformacion", u"1.0", None))
        self.btn_close.setText("")
        self.labSon1_3.setText(QCoreApplication.translate("venInformacion", u"INFORMACI\u00d3N", None))
        self.label_4.setText("")
    # retranslateUi

