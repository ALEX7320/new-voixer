# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_venGenerarcbVYIb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from . import source

class Ui_venGenerar(object):
    def setupUi(self, venGenerar):
        if not venGenerar.objectName():
            venGenerar.setObjectName(u"venGenerar")
        venGenerar.resize(277, 278)
        icon = QIcon()
        icon.addFile(u":/icones/icons/vx_ticon.png", QSize(), QIcon.Normal, QIcon.Off)
        venGenerar.setWindowIcon(icon)
        venGenerar.setStyleSheet(u"QToolTip{ \n"
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
        self.frame_2 = QFrame(venGenerar)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 278, 278))
        self.frame_2.setStyleSheet(u"#frame_2{\n"
"\n"
"	background-color: rgb(28, 53, 69);\n"
"}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(3, 44, 271, 231))
        self.frame.setStyleSheet(u"#frame{\n"
"	background-color: rgb(22, 41, 54);\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lb_tiempo = QLineEdit(self.frame)
        self.lb_tiempo.setObjectName(u"lb_tiempo")
        self.lb_tiempo.setGeometry(QRect(20, 50, 231, 41))
        self.lb_tiempo.setFocusPolicy(Qt.NoFocus)
        self.lb_tiempo.setStyleSheet(u"\n"
"QLineEdit{\n"
"	border: 0px;\n"
"	background-color: white;\n"
"	color:rgb(19, 35, 46);\n"
"	font-size: 18px;\n"
"border-radius:5px;\n"
"\n"
"\n"
"font-family: \"MADE Evolve Sans\";\n"
"font-weight:400\n"
"}\n"
"")
        self.lb_tiempo.setAlignment(Qt.AlignCenter)
        self.lb_tiempo.setReadOnly(True)
        self.labSon1_4 = QLabel(self.frame)
        self.labSon1_4.setObjectName(u"labSon1_4")
        self.labSon1_4.setGeometry(QRect(20, 20, 231, 31))
        self.labSon1_4.setMinimumSize(QSize(60, 0))
        self.labSon1_4.setStyleSheet(u"color:white;\n"
"font-family: \"MADE Evolve Sans\";\n"
"font-weight:500;\n"
"font-size:15px")
        self.labSon1_4.setAlignment(Qt.AlignCenter)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(20, 100, 231, 111))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"#frame_4{\n"
"\n"
"	background-color: rgb(22, 41, 54);\n"
"}")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.labSon1_5 = QLabel(self.frame_4)
        self.labSon1_5.setObjectName(u"labSon1_5")
        self.labSon1_5.setGeometry(QRect(0, 0, 221, 111))
        self.labSon1_5.setMinimumSize(QSize(60, 0))
        self.labSon1_5.setStyleSheet(u"color:white;\n"
"font-family: \"MADE Evolve Sans\";\n"
"font-weight:100;\n"
"font-size:13px")
        self.labSon1_5.setWordWrap(True)

        self.gridLayout.addWidget(self.frame_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_2 = QGridLayout(self.page_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.page_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"#frame_5{\n"
"\n"
"	background-color: rgb(22, 41, 54);\n"
"}")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.btn_openfolder = QPushButton(self.frame_5)
        self.btn_openfolder.setObjectName(u"btn_openfolder")
        self.btn_openfolder.setGeometry(QRect(0, 10, 231, 41))
        self.btn_openfolder.setFocusPolicy(Qt.NoFocus)
        self.btn_openfolder.setStyleSheet(u"QPushButton{\n"
"\n"
"	outline: 0px;\n"
"	background-color: rgb(28, 53, 69);\n"
"border:0px;\n"
"font-family: \"MADE Evolve Sans\";\n"
"font-weight:400;\n"
"color:white;\n"
"}\n"
"QPushButton:pressed{\n"
"\n"
"background-color: rgb(38, 81, 116);\n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/general/icons/sv_fol.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_openfolder.setIcon(icon1)
        self.btn_final = QPushButton(self.frame_5)
        self.btn_final.setObjectName(u"btn_final")
        self.btn_final.setGeometry(QRect(0, 60, 231, 41))
        self.btn_final.setFocusPolicy(Qt.NoFocus)
        self.btn_final.setStyleSheet(u"QPushButton{\n"
"\n"
"	outline: 0px;\n"
"	background-color: rgb(28, 53, 69);\n"
"border:0px;\n"
"font-family: \"MADE Evolve Sans\";\n"
"font-weight:400;\n"
"color:white;\n"
"}\n"
"QPushButton:pressed{\n"
"\n"
"background-color: rgb(38, 81, 116);\n"
"\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/general/icons/sv_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_final.setIcon(icon2)

        self.gridLayout_2.addWidget(self.frame_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(3, 3, 271, 41))
        self.frame_3.setStyleSheet(u"#frame_3{\n"
"\n"
"background-color: rgb(19, 35, 46);\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.btn_close = QPushButton(self.frame_3)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(230, 0, 40, 41))
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
        icon3 = QIcon()
        icon3.addFile(u":/title_bar/icons/titlesq.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon3)
        self.btn_close.setIconSize(QSize(12, 12))
        self.fr_move = QFrame(self.frame_3)
        self.fr_move.setObjectName(u"fr_move")
        self.fr_move.setGeometry(QRect(0, 0, 221, 41))
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
        self.label = QLabel(self.fr_move)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 21, 21))
        self.label.setStyleSheet(u"background-color: transparent;")
        self.label.setPixmap(QPixmap(u":/icones/icons/vx_sicon.png"))
        self.label.setScaledContents(True)

        self.retranslateUi(venGenerar)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(venGenerar)
    # setupUi

    def retranslateUi(self, venGenerar):
        venGenerar.setWindowTitle(QCoreApplication.translate("venGenerar", u"Generando audio", None))
        self.lb_tiempo.setText(QCoreApplication.translate("venGenerar", u"0s", None))
        self.labSon1_4.setText(QCoreApplication.translate("venGenerar", u"Tiempo Transcurrido", None))
        self.labSon1_5.setText(QCoreApplication.translate("venGenerar", u"ESTO PUEDE DEMORAR UNOS SEGUNDOS.\n"
"\n"
"EL ARCHIVO MP3 DEMORA EN GENERAR EL DOBLE DEL ARCHIVO WAV.", None))
        self.btn_openfolder.setText(QCoreApplication.translate("venGenerar", u" ABRIR CARPETA DESTINO", None))
        self.btn_final.setText(QCoreApplication.translate("venGenerar", u" CERRA VENTANA", None))
        self.btn_close.setText("")
        self.labSon1_3.setText(QCoreApplication.translate("venGenerar", u"GENERANDO AUDIO", None))
        self.label.setText("")
    # retranslateUi

