from PySide2.QtWidgets import QMainWindow,QMessageBox,QSizeGrip
from PySide2.QtCore import Qt,QTimer
from PySide2.QtGui import QTextCursor
import webbrowser 

# diseño
from views.ui_venPrincipal import Ui_venPincipal

# funciones
from controllers.Funcion_efectos import Clase_Opacidad,abrirVenOpaci
from controllers.Modulo_venInfor import Ui_venInf
from controllers.Modulo_venGuia import Ui_venGuiaUsu
from controllers.Modulo_venLicencia import Ui_venLicen
from controllers.Funcion_venPrinci import (size_hoja,establecer_cambios_text,get_EngiVoces,config_EngiVoces,
                                            config_EngineCtrl,archivo_txt_open,archivo_txt_save,read_engine,
                                            config_EnginePause,sent_generate,cambio_modo_hoja)

class Ui_venPrin(QMainWindow):
    def __init__(self):
        super(Ui_venPrin, self).__init__()

        # clase principal
        self.raizPrin = Ui_venPincipal()
        self.raizPrin.setupUi(self)
        self.sizegrip = QSizeGrip(self.raizPrin.lb_grip)

        # PARA MOVER TEXTO _______
        self.vbar_text = self.raizPrin.hoja.verticalScrollBar()

        # verifica
        self.verificar_lectura = QTimer(self)
        self.verificar_lectura.setInterval(1000)
        self.verificar_lectura.timeout.connect(lambda: self.verificar_lectura_eng())

        self.raizPrin.lb_sms_lectura.hide()

        # 1. instancia clase de opacidad _______
        self.raizOpacidad = Clase_Opacidad(self)
        self.raizOpacidad.close()

        # barra titulo /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.raizPrin.btn_close.clicked.connect(lambda:self.close())
        self.raizPrin.btn_line.clicked.connect(lambda:self.showMinimized())
        self.raizPrin.btn_square.clicked.connect(lambda:self.sizeWindowTitle(None))

        self.raizPrin.frame_10.mouseMoveEvent = self.moveWindow
        self.raizPrin.frame_10.mouseDoubleClickEvent = self.sizeWindowTitle

        # cargar textos  /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        establecer_cambios_text(self.raizPrin.hoja, 'open')
        self.showMaximized()

        # obtener voces del sistema  /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        self.engine = get_EngiVoces(self) 
        if(self.engine is None):
            import sys
            QMessageBox.critical(self, 'Error de ejecución', str('Usted no cuenta con voces en el sistema, deberá\n'
                                                                'descargar alguna para poder usar el programa.'))
            sys.exit()

        # configurar voces del sistema en el cbox  /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        config_EngiVoces(self.engine, self.raizPrin.cb_voz)

        # cambiar de voz  /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        self.raizPrin.cb_voz.currentIndexChanged.connect(lambda index: self.engine.stop())
        self.raizPrin.cb_voz.currentIndexChanged.connect(lambda : cambio_modo_hoja(self, self.raizPrin.hoja, True))

        self.raizPrin.cb_voz.currentIndexChanged.connect(lambda index: self.engine.setVoice(self.raizPrin.cb_voz.itemData(index)[0]))


        # controles de audio  /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        self.raizPrin.btn_iniciar.clicked.connect(lambda : read_engine(self))
        self.raizPrin.btn_detener.clicked.connect(lambda : self.engine.stop())
        self.raizPrin.btn_detener.clicked.connect(lambda : cambio_modo_hoja(self, self.raizPrin.hoja, True))
        self.raizPrin.btn_pausa.clicked.connect(lambda : config_EnginePause(self.engine))

        # aumentar volumen y cambiar label  /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        config_EngineCtrl(self, 10, 'vol')
        config_EngineCtrl(self, 0, 'rate')
        size_hoja(self.raizPrin.hoja,self.raizPrin.sp_font.value())
        self.raizPrin.sp_vol.valueChanged.connect(lambda valor : self.engine.setVolume(valor))
        self.raizPrin.sp_rate.valueChanged.connect(lambda valor : self.engine.setRate(valor))
        self.raizPrin.btn_generar.clicked.connect(lambda : sent_generate(self))
        self.raizPrin.sp_font.valueChanged.connect(lambda valor : 
            size_hoja(self.raizPrin.hoja,valor)
            )

        # manejo de texto  /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        self.raizPrin.btn_guardar_txt.clicked.connect(lambda : archivo_txt_save(self.raizPrin.hoja,self))
        self.raizPrin.btn_abrir_txt.clicked.connect(lambda : archivo_txt_open(self.raizPrin.hoja, self))
        self.raizPrin.btn_borrar.clicked.connect(lambda : self.borrado_texto())
            
        # ventana informacion  /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        self.raizPrin.btn_info.clicked.connect(lambda : abrirVenOpaci(self, self.raizOpacidad, Ui_venInf(self)) )
        self.raizPrin.btn_guide.clicked.connect(lambda : abrirVenOpaci(self, self.raizOpacidad, Ui_venGuiaUsu(self)) )

        # mover en texto  /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        self.raizPrin.btn_down.clicked.connect(lambda: self.mover_texto('down'))
        self.raizPrin.btn_up.clicked.connect(lambda: self.mover_texto('up'))

        # demas botones /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

        self.raizPrin.btn_donate.clicked.connect(lambda: webbrowser.open('https://www.paypal.com/donate?hosted_button_id=8SBG459YE5CE6', new=2))
        self.raizPrin.btn_licence.clicked.connect(lambda: abrirVenOpaci(self, self.raizOpacidad, Ui_venLicen(self)) )

        
    # VERIFICAR LECTURA EN PROCESO +-+-+-+-+-+-+
    def verificar_lectura_eng(self):
        estado = str(self.engine.state())
        if('State.Ready' in estado) or ('State.BackendError' in estado):
            cambio_modo_hoja(self, self.raizPrin.hoja, True)


    # MOVIEMIENTO DE TEXTO +-+-+-+-+-+-+
    def mover_texto(self, tipo):
        cursor = self.raizPrin.hoja.textCursor()
        # UP _______
        if(tipo=='up'):
            self.vbar_text.setValue(self.vbar_text.minimum())  
            cursor.movePosition(QTextCursor.Start)

        # DOWN _______
        else:
            self.vbar_text.setValue(self.vbar_text.maximum())
            cursor.movePosition(QTextCursor.End)

        self.raizPrin.hoja.setTextCursor(cursor)

    # BORRADO DE TEXTO +-+-+-+-+-+-+
    def borrado_texto(self):

        if(self.raizPrin.hoja.toPlainText()==''):
            return
        elif(QMessageBox.question(self, "Advertencia", "¿Desea borrar todo texto?",
                QMessageBox.Yes | QMessageBox.No)== QMessageBox.Yes):
            self.raizPrin.hoja.clear() 

    # CERRADO DE VENTANA +-+-+-+-+-+-+
    def closeEvent(self, event):

        establecer_cambios_text(self.raizPrin.hoja, 'save')
        event.accept()



    # CONFIGURACIONES DE TITLE BAR /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

    def sizeWindowTitle(self,event):
        if(self.isMaximized()):
            self.showNormal()
        else:
            self.showMaximized()
        
    def moveWindow(self,event):
        # MOVE WINDOW
        if(self.isMaximized()):
            event.ignore()
            
        elif event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
       
       
        


