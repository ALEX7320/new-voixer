# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_venPrincipaljbNTxA.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from . import source

class Ui_venPincipal(object):
    def setupUi(self, venPincipal):
        if not venPincipal.objectName():
            venPincipal.setObjectName(u"venPincipal")
        venPincipal.resize(919, 574)
        icon = QIcon()
        icon.addFile(u":/icones/icons/vx_ticon.png", QSize(), QIcon.Normal, QIcon.Off)
        venPincipal.setWindowIcon(icon)
        venPincipal.setStyleSheet(u"QToolTip{ \n"
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
        self.centralwidget = QWidget(venPincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"#frame{\n"
"border:2px solid rgb(16, 30, 39);\n"
"}")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 37))
        self.frame_4.setStyleSheet(u"#frame_4{\n"
"	background-color: rgb(19, 35, 46);\n"
"}")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.frame_15 = QFrame(self.frame_4)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_15)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.btn_info = QPushButton(self.frame_15)
        self.btn_info.setObjectName(u"btn_info")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_info.sizePolicy().hasHeightForWidth())
        self.btn_info.setSizePolicy(sizePolicy)
        self.btn_info.setMinimumSize(QSize(36, 0))
        self.btn_info.setFocusPolicy(Qt.NoFocus)
        self.btn_info.setStyleSheet(u"QPushButton{\n"
"	outline: 0px;\n"
"border:0px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(53, 111, 162);\n"
"\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/general/icons/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_info.setIcon(icon1)
        self.btn_info.setIconSize(QSize(18, 18))

        self.gridLayout_12.addWidget(self.btn_info, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_15)

        self.btn_guide = QPushButton(self.frame_4)
        self.btn_guide.setObjectName(u"btn_guide")
        sizePolicy.setHeightForWidth(self.btn_guide.sizePolicy().hasHeightForWidth())
        self.btn_guide.setSizePolicy(sizePolicy)
        self.btn_guide.setMinimumSize(QSize(36, 0))
        self.btn_guide.setFocusPolicy(Qt.NoFocus)
        self.btn_guide.setStyleSheet(u"QPushButton{\n"
"	outline: 0px;\n"
"border:0px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(53, 111, 162);\n"
"\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/general/icons/guide.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_guide.setIcon(icon2)
        self.btn_guide.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.btn_guide)

        self.btn_licence = QPushButton(self.frame_4)
        self.btn_licence.setObjectName(u"btn_licence")
        sizePolicy.setHeightForWidth(self.btn_licence.sizePolicy().hasHeightForWidth())
        self.btn_licence.setSizePolicy(sizePolicy)
        self.btn_licence.setMinimumSize(QSize(36, 0))
        self.btn_licence.setFocusPolicy(Qt.NoFocus)
        self.btn_licence.setStyleSheet(u"QPushButton{\n"
"	outline: 0px;\n"
"border:0px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(53, 111, 162);\n"
"\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/general/icons/licen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_licence.setIcon(icon3)
        self.btn_licence.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.btn_licence)

        self.btn_descarga = QPushButton(self.frame_4)
        self.btn_descarga.setObjectName(u"btn_descarga")
        sizePolicy.setHeightForWidth(self.btn_descarga.sizePolicy().hasHeightForWidth())
        self.btn_descarga.setSizePolicy(sizePolicy)
        self.btn_descarga.setMinimumSize(QSize(36, 0))
        self.btn_descarga.setFocusPolicy(Qt.NoFocus)
        self.btn_descarga.setStyleSheet(u"QPushButton{\n"
"	outline: 0px;\n"
"border:0px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(53, 111, 162);\n"
"\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/general/icons/descargar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_descarga.setIcon(icon4)
        self.btn_descarga.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.btn_descarga)

        self.btn_donate = QPushButton(self.frame_4)
        self.btn_donate.setObjectName(u"btn_donate")
        sizePolicy.setHeightForWidth(self.btn_donate.sizePolicy().hasHeightForWidth())
        self.btn_donate.setSizePolicy(sizePolicy)
        self.btn_donate.setMinimumSize(QSize(36, 0))
        self.btn_donate.setFocusPolicy(Qt.NoFocus)
        self.btn_donate.setStyleSheet(u"QPushButton{\n"
"	outline: 0px;\n"
"border:0px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(53, 111, 162);\n"
"\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/general/icons/donate.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_donate.setIcon(icon5)
        self.btn_donate.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.btn_donate)

        self.frame_10 = QFrame(self.frame_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_10)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalSpacer_3 = QSpacerItem(637, 12, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)


        self.horizontalLayout.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_line = QPushButton(self.frame_11)
        self.btn_line.setObjectName(u"btn_line")
        sizePolicy.setHeightForWidth(self.btn_line.sizePolicy().hasHeightForWidth())
        self.btn_line.setSizePolicy(sizePolicy)
        self.btn_line.setMinimumSize(QSize(40, 0))
        self.btn_line.setFocusPolicy(Qt.NoFocus)
        self.btn_line.setStyleSheet(u"QPushButton{\n"
"	outline: 0px;\n"
"\n"
"border:0px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(53, 111, 162);\n"
"\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/title_bar/icons/titlemin.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_line.setIcon(icon6)
        self.btn_line.setIconSize(QSize(12, 12))

        self.horizontalLayout_2.addWidget(self.btn_line)

        self.btn_square = QPushButton(self.frame_11)
        self.btn_square.setObjectName(u"btn_square")
        sizePolicy.setHeightForWidth(self.btn_square.sizePolicy().hasHeightForWidth())
        self.btn_square.setSizePolicy(sizePolicy)
        self.btn_square.setMinimumSize(QSize(40, 0))
        self.btn_square.setFocusPolicy(Qt.NoFocus)
        self.btn_square.setStyleSheet(u"QPushButton{\n"
"	outline: 0px;\n"
"border:0px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(53, 111, 162);\n"
"\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/title_bar/icons/titlecua.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_square.setIcon(icon7)
        self.btn_square.setIconSize(QSize(12, 12))

        self.horizontalLayout_2.addWidget(self.btn_square)

        self.btn_close = QPushButton(self.frame_11)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setFocusPolicy(Qt.NoFocus)
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"	outline: 0px;\n"
"border:0px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(53, 111, 162);\n"
"\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/title_bar/icons/titlesq.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon8)
        self.btn_close.setIconSize(QSize(12, 12))

        self.horizontalLayout_2.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_11)


        self.gridLayout_2.addWidget(self.frame_4, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(230, 123))
        self.frame_3.setMaximumSize(QSize(230, 16777215))
        self.frame_3.setStyleSheet(u"#frame_3{\n"
"\n"
"	background-color: rgb(16, 30, 39);\n"
"\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.verticalSpacer = QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_10.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_10.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.frame_12 = QFrame(self.frame_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_12)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_12)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 18))
        self.label_2.setStyleSheet(u"font-size:20px;\n"
"color: rgb(255, 255, 255);\n"
"font-family: \"Fashion Fetish\";\n"
"font-weight: Bold;")

        self.verticalLayout.addWidget(self.label_2)

        self.label = QLabel(self.frame_12)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 60))
        self.label.setStyleSheet(u"font-size:45px;\n"
"color: rgb(255, 255, 255);\n"
"font-family: \"Fashion Fetish\";\n"
"font-weight: Bold;")
        self.label.setFrameShape(QFrame.NoFrame)

        self.verticalLayout.addWidget(self.label)


        self.gridLayout_10.addWidget(self.frame_12, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(12, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 2, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"#frame_2{\n"
"	background-color: rgb(28, 53, 69);\n"
"}\n"
"\n"
"\n"
"/*SCROLL VERTICAL*/\n"
"\n"
"QScrollBar:vertical{\n"
"	background-color: rgb(19, 36, 47);\n"
"	width: 22px; \n"
"	margin: 4px 5px 4x 5px;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"	background: ;\n"
"	background-color: rgb(53, 111, 162);\n"
"    border-radius:5px;\n"
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
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.hoja = QPlainTextEdit(self.frame_2)
        self.hoja.setObjectName(u"hoja")
        self.hoja.setStyleSheet(u"/*CAJA TEXTO*/\n"
"QPlainTextEdit{\n"
"	color: white;\n"
"	font-size: 17px;\n"
"	border: 0px;\n"
"	padding: 10px;\n"
"	background-color: rgb(19, 36, 47);\n"
"	font-family: \"MADE Evolve Sans\";\n"
"	font-weight:Regular\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.hoja, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 2, 0, 1, 2)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 63))
        self.frame_6.setStyleSheet(u"#frame_6{\n"
"	background-color: rgb(22, 41, 54);\n"
"}")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.gridLayout_5 = QGridLayout(self.frame_6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.btn_pausa = QPushButton(self.frame_6)
        self.btn_pausa.setObjectName(u"btn_pausa")
        sizePolicy.setHeightForWidth(self.btn_pausa.sizePolicy().hasHeightForWidth())
        self.btn_pausa.setSizePolicy(sizePolicy)
        self.btn_pausa.setMinimumSize(QSize(50, 0))
        self.btn_pausa.setFocusPolicy(Qt.NoFocus)
        self.btn_pausa.setStyleSheet(u"QPushButton{\n"
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
        icon9 = QIcon()
        icon9.addFile(u":/ctrl_sound/icons/sd_pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pausa.setIcon(icon9)
        self.btn_pausa.setIconSize(QSize(22, 22))

        self.gridLayout_5.addWidget(self.btn_pausa, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)

        self.btn_detener = QPushButton(self.frame_6)
        self.btn_detener.setObjectName(u"btn_detener")
        sizePolicy.setHeightForWidth(self.btn_detener.sizePolicy().hasHeightForWidth())
        self.btn_detener.setSizePolicy(sizePolicy)
        self.btn_detener.setMinimumSize(QSize(50, 0))
        self.btn_detener.setFocusPolicy(Qt.NoFocus)
        self.btn_detener.setStyleSheet(u"QPushButton{\n"
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
        icon10 = QIcon()
        icon10.addFile(u":/ctrl_sound/icons/sd_stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_detener.setIcon(icon10)
        self.btn_detener.setIconSize(QSize(22, 22))

        self.gridLayout_5.addWidget(self.btn_detener, 0, 1, 1, 1)

        self.btn_iniciar = QPushButton(self.frame_6)
        self.btn_iniciar.setObjectName(u"btn_iniciar")
        sizePolicy.setHeightForWidth(self.btn_iniciar.sizePolicy().hasHeightForWidth())
        self.btn_iniciar.setSizePolicy(sizePolicy)
        self.btn_iniciar.setMinimumSize(QSize(50, 0))
        self.btn_iniciar.setFocusPolicy(Qt.NoFocus)
        self.btn_iniciar.setStyleSheet(u"QPushButton{\n"
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
        icon11 = QIcon()
        icon11.addFile(u":/ctrl_sound/icons/sd_play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_iniciar.setIcon(icon11)
        self.btn_iniciar.setIconSize(QSize(22, 22))

        self.gridLayout_5.addWidget(self.btn_iniciar, 0, 3, 1, 1)

        self.btn_guardar_txt = QPushButton(self.frame_6)
        self.btn_guardar_txt.setObjectName(u"btn_guardar_txt")
        sizePolicy.setHeightForWidth(self.btn_guardar_txt.sizePolicy().hasHeightForWidth())
        self.btn_guardar_txt.setSizePolicy(sizePolicy)
        self.btn_guardar_txt.setMinimumSize(QSize(50, 0))
        self.btn_guardar_txt.setFocusPolicy(Qt.NoFocus)
        self.btn_guardar_txt.setStyleSheet(u"QPushButton{\n"
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
        icon12 = QIcon()
        icon12.addFile(u":/strl_file/icons/fe_save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_guardar_txt.setIcon(icon12)
        self.btn_guardar_txt.setIconSize(QSize(30, 30))

        self.gridLayout_5.addWidget(self.btn_guardar_txt, 0, 10, 1, 1)

        self.btn_up = QPushButton(self.frame_6)
        self.btn_up.setObjectName(u"btn_up")
        sizePolicy.setHeightForWidth(self.btn_up.sizePolicy().hasHeightForWidth())
        self.btn_up.setSizePolicy(sizePolicy)
        self.btn_up.setMinimumSize(QSize(50, 0))
        self.btn_up.setFocusPolicy(Qt.NoFocus)
        self.btn_up.setStyleSheet(u"QPushButton{\n"
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
        icon13 = QIcon()
        icon13.addFile(u":/general/icons/fle_up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_up.setIcon(icon13)
        self.btn_up.setIconSize(QSize(22, 22))

        self.gridLayout_5.addWidget(self.btn_up, 0, 5, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_5, 0, 7, 1, 1)

        self.btn_down = QPushButton(self.frame_6)
        self.btn_down.setObjectName(u"btn_down")
        sizePolicy.setHeightForWidth(self.btn_down.sizePolicy().hasHeightForWidth())
        self.btn_down.setSizePolicy(sizePolicy)
        self.btn_down.setMinimumSize(QSize(50, 0))
        self.btn_down.setFocusPolicy(Qt.NoFocus)
        self.btn_down.setStyleSheet(u"QPushButton{\n"
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
        icon14 = QIcon()
        icon14.addFile(u":/general/icons/fle_down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_down.setIcon(icon14)
        self.btn_down.setIconSize(QSize(22, 22))

        self.gridLayout_5.addWidget(self.btn_down, 0, 6, 1, 1)

        self.btn_borrar = QToolButton(self.frame_6)
        self.btn_borrar.setObjectName(u"btn_borrar")
        sizePolicy.setHeightForWidth(self.btn_borrar.sizePolicy().hasHeightForWidth())
        self.btn_borrar.setSizePolicy(sizePolicy)
        self.btn_borrar.setMinimumSize(QSize(50, 0))
        self.btn_borrar.setFocusPolicy(Qt.NoFocus)
        self.btn_borrar.setStyleSheet(u"QToolButton{\n"
"	background-color: rgb(28, 53, 69);\n"
"border:0px;\n"
"	outline: 0px;\n"
"}\n"
"QToolButton:pressed{\n"
"\n"
"background-color: rgb(38, 81, 116);\n"
"\n"
"}\n"
"\n"
"QToolButton:disabled{\n"
"	background-color: rgb(22, 41, 54);\n"
"}\n"
"")
        icon15 = QIcon()
        icon15.addFile(u":/strl_file/icons/fe_clear.png", QSize(), QIcon.Normal, QIcon.Off)
        icon15.addFile(u":/lock/icons/fe_clear_block.png", QSize(), QIcon.Disabled, QIcon.Off)
        self.btn_borrar.setIcon(icon15)
        self.btn_borrar.setIconSize(QSize(30, 30))

        self.gridLayout_5.addWidget(self.btn_borrar, 0, 8, 1, 1)

        self.btn_abrir_txt = QToolButton(self.frame_6)
        self.btn_abrir_txt.setObjectName(u"btn_abrir_txt")
        sizePolicy.setHeightForWidth(self.btn_abrir_txt.sizePolicy().hasHeightForWidth())
        self.btn_abrir_txt.setSizePolicy(sizePolicy)
        self.btn_abrir_txt.setMinimumSize(QSize(50, 0))
        self.btn_abrir_txt.setFocusPolicy(Qt.NoFocus)
        self.btn_abrir_txt.setStyleSheet(u"QToolButton{\n"
"	background-color: rgb(28, 53, 69);\n"
"border:0px;\n"
"	outline: 0px;\n"
"}\n"
"QToolButton:pressed{\n"
"\n"
"background-color: rgb(38, 81, 116);\n"
"\n"
"}\n"
"\n"
"QToolButton:disabled{\n"
"	background-color: rgb(22, 41, 54);\n"
"}\n"
"")
        icon16 = QIcon()
        icon16.addFile(u":/strl_file/icons/fe_open.png", QSize(), QIcon.Normal, QIcon.Off)
        icon16.addFile(u":/lock/icons/fe_open_block.png", QSize(), QIcon.Disabled, QIcon.Off)
        self.btn_abrir_txt.setIcon(icon16)
        self.btn_abrir_txt.setIconSize(QSize(30, 30))

        self.gridLayout_5.addWidget(self.btn_abrir_txt, 0, 9, 1, 1)


        self.gridLayout_2.addWidget(self.frame_6, 3, 0, 1, 2)

        self.frame_13 = QFrame(self.frame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 24))
        self.frame_13.setStyleSheet(u"#frame_13{\n"
"	background-color: rgb(16, 30, 39);\n"
"}")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_13)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font-family: \"Fashion Fetish\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalSpacer_6 = QSpacerItem(948, 6, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.lb_sms_lectura = QLabel(self.frame_13)
        self.lb_sms_lectura.setObjectName(u"lb_sms_lectura")
        self.lb_sms_lectura.setMinimumSize(QSize(253, 0))
        self.lb_sms_lectura.setMaximumSize(QSize(16777215, 12))
        self.lb_sms_lectura.setStyleSheet(u"color:white;\n"
"font-family: \"MADE Evolve Sans\";\n"
"font-weight:Medium;\n"
"font-size:13px")

        self.horizontalLayout_3.addWidget(self.lb_sms_lectura)

        self.lb_grip = QLabel(self.frame_13)
        self.lb_grip.setObjectName(u"lb_grip")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lb_grip.sizePolicy().hasHeightForWidth())
        self.lb_grip.setSizePolicy(sizePolicy1)
        self.lb_grip.setMinimumSize(QSize(25, 0))
        self.lb_grip.setMaximumSize(QSize(25, 16777215))
        self.lb_grip.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_3.addWidget(self.lb_grip)


        self.gridLayout_2.addWidget(self.frame_13, 4, 0, 1, 2)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"#frame_5{\n"
"\n"
"\n"
"background-color: rgb(22, 41, 54);\n"
"}")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(12)
        self.line_3 = QFrame(self.frame_5)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"color: rgba(255, 255, 255,0.2);")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setFrameShape(QFrame.VLine)

        self.gridLayout_4.addWidget(self.line_3, 0, 1, 2, 1)

        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_9)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.sp_rate = QDoubleSpinBox(self.frame_9)
        self.sp_rate.setObjectName(u"sp_rate")
        sizePolicy.setHeightForWidth(self.sp_rate.sizePolicy().hasHeightForWidth())
        self.sp_rate.setSizePolicy(sizePolicy)
        self.sp_rate.setMinimumSize(QSize(90, 0))
        self.sp_rate.setFocusPolicy(Qt.ClickFocus)
        self.sp_rate.setStyleSheet(u"QDoubleSpinBox {\n"
"	color: white;\n"
"	background-color: rgb(28, 53, 69);\n"
"	font-size: 20px;\n"
"	padding-left: 20px;\n"
"\n"
"font-family: \"MADE Evolve Sans\";\n"
"font-weight:Regular\n"
" }\n"
"\n"
"\n"
"QDoubleSpinBox::up-button {\n"
"min-width: 25px; min-height: 25px; \n"
"	background-color: rgb(28, 53, 69);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"min-width: 25px; min-height: 25px; \n"
"	background-color: rgb(28, 53, 69);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-arrow{\n"
"	image: url(:/general/icons/comDown.png);\n"
"     width:15px;\n"
"     height: 15px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-arrow{\n"
"	image: url(:/general/icons/comUp.png);\n"
"     width:15px;\n"
"     height: 15px;\n"
"}")
        self.sp_rate.setDecimals(1)
        self.sp_rate.setMinimum(-1.000000000000000)
        self.sp_rate.setMaximum(1.000000000000000)
        self.sp_rate.setSingleStep(0.100000000000000)

        self.gridLayout_8.addWidget(self.sp_rate, 1, 0, 1, 1)

        self.labSon3 = QLabel(self.frame_9)
        self.labSon3.setObjectName(u"labSon3")
        self.labSon3.setMinimumSize(QSize(60, 0))
        self.labSon3.setMaximumSize(QSize(16777215, 12))
        self.labSon3.setStyleSheet(u"color:white;\n"
"font-family: \"MADE Evolve Sans\";\n"
"font-weight:Medium;\n"
"font-size:13px")

        self.gridLayout_8.addWidget(self.labSon3, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_9, 0, 4, 2, 1)

        self.line_2 = QFrame(self.frame_5)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"color: rgba(255, 255, 255,0.2);")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setFrameShape(QFrame.VLine)

        self.gridLayout_4.addWidget(self.line_2, 0, 3, 2, 1)

        self.line_4 = QFrame(self.frame_5)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"color: rgba(255, 255, 255,0.2);")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setFrameShape(QFrame.VLine)

        self.gridLayout_4.addWidget(self.line_4, 0, 5, 2, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 8, 1, 1)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_8)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.sp_vol = QDoubleSpinBox(self.frame_8)
        self.sp_vol.setObjectName(u"sp_vol")
        sizePolicy.setHeightForWidth(self.sp_vol.sizePolicy().hasHeightForWidth())
        self.sp_vol.setSizePolicy(sizePolicy)
        self.sp_vol.setMinimumSize(QSize(90, 0))
        self.sp_vol.setFocusPolicy(Qt.ClickFocus)
        self.sp_vol.setStyleSheet(u"QDoubleSpinBox {\n"
"	color: white;\n"
"	background-color: rgb(28, 53, 69);\n"
"	font-size: 20px;\n"
"	padding-left: 20px;\n"
"\n"
"font-family: \"MADE Evolve Sans\";\n"
"font-weight:Regular\n"
" }\n"
"\n"
"\n"
"QDoubleSpinBox::up-button {\n"
"min-width: 25px; min-height: 25px; \n"
"	background-color: rgb(28, 53, 69);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"min-width: 25px; min-height: 25px; \n"
"	background-color: rgb(28, 53, 69);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-arrow{\n"
"	image: url(:/general/icons/comDown.png);\n"
"     width:15px;\n"
"     height: 15px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-arrow{\n"
"	image: url(:/general/icons/comUp.png);\n"
"     width:15px;\n"
"     height: 15px;\n"
"}")
        self.sp_vol.setDecimals(1)
        self.sp_vol.setMinimum(0.000000000000000)
        self.sp_vol.setMaximum(1.000000000000000)
        self.sp_vol.setSingleStep(0.100000000000000)
        self.sp_vol.setValue(1.000000000000000)

        self.gridLayout_7.addWidget(self.sp_vol, 1, 0, 1, 1)

        self.labSon1 = QLabel(self.frame_8)
        self.labSon1.setObjectName(u"labSon1")
        self.labSon1.setMinimumSize(QSize(60, 0))
        self.labSon1.setMaximumSize(QSize(16777215, 12))
        self.labSon1.setStyleSheet(u"color:white;\n"
"font-family: \"MADE Evolve Sans\";\n"
"font-weight:Medium;\n"
"font-size:13px")

        self.gridLayout_7.addWidget(self.labSon1, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_8, 0, 2, 2, 1)

        self.frame_14 = QFrame(self.frame_5)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_14)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.sp_font = QSpinBox(self.frame_14)
        self.sp_font.setObjectName(u"sp_font")
        sizePolicy.setHeightForWidth(self.sp_font.sizePolicy().hasHeightForWidth())
        self.sp_font.setSizePolicy(sizePolicy)
        self.sp_font.setMinimumSize(QSize(110, 0))
        self.sp_font.setFocusPolicy(Qt.ClickFocus)
        self.sp_font.setStyleSheet(u"QSpinBox {\n"
"	color: white;\n"
"	background-color: rgb(28, 53, 69);\n"
"	font-size: 20px;\n"
"	padding-left: 20px;\n"
"\n"
"font-family: \"MADE Evolve Sans\";\n"
"font-weight:Regular\n"
" }\n"
"\n"
"\n"
"QSpinBox::up-button {\n"
"min-width: 25px; min-height: 25px; \n"
"	background-color: rgb(28, 53, 69);\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"min-width: 25px; min-height: 25px; \n"
"	background-color: rgb(28, 53, 69);\n"
"}\n"
"\n"
"QSpinBox::up-arrow{\n"
"	image: url(:/general/icons/comDown.png);\n"
"     width:15px;\n"
"     height: 15px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow{\n"
"	image: url(:/general/icons/comUp.png);\n"
"     width:15px;\n"
"     height: 15px;\n"
"}")
        self.sp_font.setMinimum(7)
        self.sp_font.setMaximum(80)
        self.sp_font.setValue(17)

        self.gridLayout_11.addWidget(self.sp_font, 1, 0, 1, 1)

        self.labSon1_3 = QLabel(self.frame_14)
        self.labSon1_3.setObjectName(u"labSon1_3")
        self.labSon1_3.setMinimumSize(QSize(60, 0))
        self.labSon1_3.setMaximumSize(QSize(16777215, 12))
        self.labSon1_3.setStyleSheet(u"color:white;\n"
"font-family: \"MADE Evolve Sans\";\n"
"font-weight:Medium;\n"
"font-size:13px")

        self.gridLayout_11.addWidget(self.labSon1_3, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_14, 0, 6, 2, 1)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.labSon1_2 = QLabel(self.frame_7)
        self.labSon1_2.setObjectName(u"labSon1_2")
        self.labSon1_2.setMaximumSize(QSize(16777215, 12))
        self.labSon1_2.setStyleSheet(u"color:white;\n"
"font-family: \"MADE Evolve Sans\";\n"
"font-weight:Medium;\n"
"font-size:13px")

        self.gridLayout_6.addWidget(self.labSon1_2, 0, 0, 1, 1)

        self.cb_voz = QComboBox(self.frame_7)
        self.cb_voz.addItem("")
        self.cb_voz.addItem("")
        self.cb_voz.addItem("")
        self.cb_voz.addItem("")
        self.cb_voz.addItem("")
        self.cb_voz.addItem("")
        self.cb_voz.addItem("")
        self.cb_voz.addItem("")
        self.cb_voz.addItem("")
        self.cb_voz.addItem("")
        self.cb_voz.addItem("")
        self.cb_voz.addItem("")
        self.cb_voz.addItem("")
        self.cb_voz.addItem("")
        self.cb_voz.addItem("")
        self.cb_voz.addItem("")
        self.cb_voz.addItem("")
        self.cb_voz.addItem("")
        self.cb_voz.addItem("")
        self.cb_voz.setObjectName(u"cb_voz")
        sizePolicy1.setHeightForWidth(self.cb_voz.sizePolicy().hasHeightForWidth())
        self.cb_voz.setSizePolicy(sizePolicy1)
        self.cb_voz.setMinimumSize(QSize(180, 0))
        self.cb_voz.setFocusPolicy(Qt.ClickFocus)
        self.cb_voz.setStyleSheet(u"\n"
"QComboBox{\n"
"	border: 0px;\n"
"	background-color: rgb(28, 53, 69);\n"
"	color:white;\n"
"	font-size: 18px;\n"
"	padding-left: 10px;\n"
"\n"
"combobox-popup: 0;\n"
"\n"
"\n"
"font-family: \"MADE Evolve Sans\";\n"
"font-weight:Regular\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"	image: url(:/general/icons/comUp.png);\n"
"     width: 22px;\n"
"     height: 22px;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    width: 40px;\n"
"    border-left-width: 1px;\n"
" }\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: white;	\n"
"	padding: 14px;\n"
"	padding:10px;\n"
"	background-color: rgb(19, 35, 46);\n"
"\n"
"	selection-background-color: rgb(38, 81, 116);\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/*SCROLL VERTICAL*/\n"
"\n"
"QScrollBar:vertical{\n"
"	background-color: rgb(19, 35, 46);\n"
"	width: 19px; \n"
"	margin: 4px 5px 4x 5px;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"	background: ;\n"
"	background-color: rgb(53, 111, 162);\n"
"    border-radius:3px;\n"
"	margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScro"
                        "llBar::add-line:vertical {\n"
"	height: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0 px;\n"
"}\n"
"\n"
"")

        self.gridLayout_6.addWidget(self.cb_voz, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_7, 0, 0, 2, 1)

        self.btn_generar = QToolButton(self.frame_5)
        self.btn_generar.setObjectName(u"btn_generar")
        sizePolicy.setHeightForWidth(self.btn_generar.sizePolicy().hasHeightForWidth())
        self.btn_generar.setSizePolicy(sizePolicy)
        self.btn_generar.setMinimumSize(QSize(60, 0))
        self.btn_generar.setFocusPolicy(Qt.NoFocus)
        self.btn_generar.setStyleSheet(u"QToolButton{\n"
"	outline: 0px;\n"
"border-radius:2px;\n"
"	background-color: rgb(28, 53, 69);\n"
"padding-top:7px;\n"
"font-family: \"MADE Evolve Sans\";\n"
"font-weight:Medium;\n"
"color:white;\n"
"\n"
"}\n"
"QToolButton:pressed{\n"
"border:0px;\n"
"\n"
"	background-color: rgb(38, 81, 116);\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/general/icons/sd_generate.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_generar.setIcon(icon17)
        self.btn_generar.setIconSize(QSize(35, 35))
        self.btn_generar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_4.addWidget(self.btn_generar, 0, 9, 2, 1)

        self.line_5 = QFrame(self.frame_5)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"color: rgba(255, 255, 255,0.2);")
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setFrameShape(QFrame.VLine)

        self.gridLayout_4.addWidget(self.line_5, 0, 7, 2, 1)


        self.gridLayout_2.addWidget(self.frame_5, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        venPincipal.setCentralWidget(self.centralwidget)

        self.retranslateUi(venPincipal)

        QMetaObject.connectSlotsByName(venPincipal)
    # setupUi

    def retranslateUi(self, venPincipal):
        venPincipal.setWindowTitle(QCoreApplication.translate("venPincipal", u"New Voixer", None))
#if QT_CONFIG(tooltip)
        self.btn_info.setToolTip(QCoreApplication.translate("venPincipal", u"Informaci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
        self.btn_info.setText("")
#if QT_CONFIG(tooltip)
        self.btn_guide.setToolTip(QCoreApplication.translate("venPincipal", u"Gu\u00eda", None))
#endif // QT_CONFIG(tooltip)
        self.btn_guide.setText("")
#if QT_CONFIG(tooltip)
        self.btn_licence.setToolTip(QCoreApplication.translate("venPincipal", u"Licencia", None))
#endif // QT_CONFIG(tooltip)
        self.btn_licence.setText("")
#if QT_CONFIG(tooltip)
        self.btn_descarga.setToolTip(QCoreApplication.translate("venPincipal", u"Versiones", None))
#endif // QT_CONFIG(tooltip)
        self.btn_descarga.setText("")
#if QT_CONFIG(tooltip)
        self.btn_donate.setToolTip(QCoreApplication.translate("venPincipal", u"Donaci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
        self.btn_donate.setText("")
        self.btn_line.setText("")
        self.btn_square.setText("")
        self.btn_close.setText("")
        self.label_2.setText(QCoreApplication.translate("venPincipal", u"NEW", None))
        self.label.setText(QCoreApplication.translate("venPincipal", u"VOIXER", None))
        self.hoja.setPlainText("")
#if QT_CONFIG(tooltip)
        self.btn_pausa.setToolTip(QCoreApplication.translate("venPincipal", u"Pausar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_pausa.setText("")
#if QT_CONFIG(tooltip)
        self.btn_detener.setToolTip(QCoreApplication.translate("venPincipal", u"Detener", None))
#endif // QT_CONFIG(tooltip)
        self.btn_detener.setText("")
#if QT_CONFIG(tooltip)
        self.btn_iniciar.setToolTip(QCoreApplication.translate("venPincipal", u"Reproducir", None))
#endif // QT_CONFIG(tooltip)
        self.btn_iniciar.setText("")
#if QT_CONFIG(tooltip)
        self.btn_guardar_txt.setToolTip(QCoreApplication.translate("venPincipal", u"Guardar texto", None))
#endif // QT_CONFIG(tooltip)
        self.btn_guardar_txt.setText("")
#if QT_CONFIG(tooltip)
        self.btn_up.setToolTip(QCoreApplication.translate("venPincipal", u"Inicio del texto", None))
#endif // QT_CONFIG(tooltip)
        self.btn_up.setText("")
#if QT_CONFIG(tooltip)
        self.btn_down.setToolTip(QCoreApplication.translate("venPincipal", u"Final del texto", None))
#endif // QT_CONFIG(tooltip)
        self.btn_down.setText("")
#if QT_CONFIG(tooltip)
        self.btn_borrar.setToolTip(QCoreApplication.translate("venPincipal", u"Eliminar texto", None))
#endif // QT_CONFIG(tooltip)
        self.btn_borrar.setText("")
#if QT_CONFIG(tooltip)
        self.btn_abrir_txt.setToolTip(QCoreApplication.translate("venPincipal", u"Cargar texto", None))
#endif // QT_CONFIG(tooltip)
        self.btn_abrir_txt.setText("")
        self.label_4.setText(QCoreApplication.translate("venPincipal", u"  NEW VOIXER - \u00a9ALEX7320", None))
        self.lb_sms_lectura.setText(QCoreApplication.translate("venPincipal", u"Para habilitar el texto debe detener la lectura.", None))
        self.lb_grip.setText("")
        self.labSon3.setText(QCoreApplication.translate("venPincipal", u"RATE", None))
        self.labSon1.setText(QCoreApplication.translate("venPincipal", u"V\u00d3LUMEN", None))
        self.sp_font.setSuffix(QCoreApplication.translate("venPincipal", u" px", None))
        self.labSon1_3.setText(QCoreApplication.translate("venPincipal", u"FUENTE", None))
        self.labSon1_2.setText(QCoreApplication.translate("venPincipal", u"TIPO DE VOZ", None))
        self.cb_voz.setItemText(0, QCoreApplication.translate("venPincipal", u"Nuevo elemento", None))
        self.cb_voz.setItemText(1, QCoreApplication.translate("venPincipal", u"Nuevo elemento", None))
        self.cb_voz.setItemText(2, QCoreApplication.translate("venPincipal", u"Nuevo elemento", None))
        self.cb_voz.setItemText(3, QCoreApplication.translate("venPincipal", u"Nuevo elemento", None))
        self.cb_voz.setItemText(4, QCoreApplication.translate("venPincipal", u"Nuevo elemento", None))
        self.cb_voz.setItemText(5, QCoreApplication.translate("venPincipal", u"Nuevo elemento", None))
        self.cb_voz.setItemText(6, QCoreApplication.translate("venPincipal", u"Nuevo elemento", None))
        self.cb_voz.setItemText(7, QCoreApplication.translate("venPincipal", u"Nuevo elemento", None))
        self.cb_voz.setItemText(8, QCoreApplication.translate("venPincipal", u"Nuevo elemento", None))
        self.cb_voz.setItemText(9, QCoreApplication.translate("venPincipal", u"Nuevo elemento", None))
        self.cb_voz.setItemText(10, QCoreApplication.translate("venPincipal", u"Nuevo elemento", None))
        self.cb_voz.setItemText(11, QCoreApplication.translate("venPincipal", u"Nuevo elemento", None))
        self.cb_voz.setItemText(12, QCoreApplication.translate("venPincipal", u"Nuevo elemento", None))
        self.cb_voz.setItemText(13, QCoreApplication.translate("venPincipal", u"Nuevo elemento", None))
        self.cb_voz.setItemText(14, QCoreApplication.translate("venPincipal", u"Nuevo elemento", None))
        self.cb_voz.setItemText(15, QCoreApplication.translate("venPincipal", u"Nuevo elemento", None))
        self.cb_voz.setItemText(16, QCoreApplication.translate("venPincipal", u"Nuevo elemento", None))
        self.cb_voz.setItemText(17, QCoreApplication.translate("venPincipal", u"Nuevo elemento", None))
        self.cb_voz.setItemText(18, QCoreApplication.translate("venPincipal", u"Nuevo elemento", None))

#if QT_CONFIG(tooltip)
        self.btn_generar.setToolTip(QCoreApplication.translate("venPincipal", u"Guardar audio", None))
#endif // QT_CONFIG(tooltip)
        self.btn_generar.setText(QCoreApplication.translate("venPincipal", u"GENERAR", None))
    # retranslateUi

