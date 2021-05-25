from PySide2.QtWidgets import QDialog,QMessageBox
from PySide2.QtCore import QTimer,Qt,QThreadPool
import os, webbrowser 

# diseño
from views.ui_venGenerar import Ui_venGenerar

# funciones
from controllers.Funcion_generar import generar_audio_wav,generar_audio_mp3,get_icon_notifi
from controllers.Funcion_hilos import Worker

class Ui_venGen(QDialog):
    def __init__(self, parent, modo, ruta, voz, rate, texto):
        super(Ui_venGen, self).__init__()

        # clase principal
        self.raizGen = Ui_venGenerar()
        self.raizGen.setupUi(self)

        # variables  /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        self.sw_close = False # cerrado ventana
        self.parent = parent # clase previa
        self.raizGen.stackedWidget.setCurrentIndex(0) # stk por defecto

        self.sw_error = False

        # transparencia y quitar barra superior  /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.MSWindowsFixedSizeDialogHint)

        # barra titulo  /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        self.raizGen.btn_close.clicked.connect(lambda:self.close())
        self.raizGen.fr_move.mouseMoveEvent = self.moveWindow

        # hilo de ejecucion  /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        self.threadpool = QThreadPool()

        # contador de segundos /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        self.time_count = 0
        self.cronometro = QTimer(self)
        self.cronometro.setInterval(1000)
        self.cronometro.timeout.connect(lambda: self.aumentar_cronometro())
        self.cronometro.start()

        # datos para generar audio  /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        self.ruta = ruta
        self.voz = voz
        self.rate = rate 
        self.texto = texto

        # btn cerrado /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        self.raizGen.btn_final.clicked.connect(lambda : self.close())

        # genera audio dependiendo de opc /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        if(modo == 'wav'):
            self.hilo_genera_wav()
        else:
            self.hilo_genera_mp3()


    # AUMENTA VISTA DE CONTADOR +-+-+-+-+-+-+
    def aumentar_cronometro(self):
        self.time_count += 1
        self.raizGen.lb_tiempo.setText(f'{self.time_count}s')

    # MENSAJE FINAL DE CONVERSION +-+-+-+-+-+-+
    def mesaje_usuario(self, ruta):

        try:
            from win10toast_click import ToastNotifier 
            toaster = ToastNotifier()
            toaster.show_toast(
                "Proceso finalizado", # title
                "Audio generado correctamente.\nClic para abrir ubicación del archivo.",  #url()
                icon_path=get_icon_notifi(),
                duration=5, 
                threaded=True, 
                callback_on_click=lambda : webbrowser.open(ruta, new=2)
                )

        except:
            # en caso de que el sistema no tenga win10
            QMessageBox.information(self,"Proceso finalizado","Audio generado correctamente.")

    # PROCESOS FINAL DE CONVERSION +-+-+-+-+-+-+
    def finalizar_conversion(self):
        # cerrado ventana activado ---
        self.sw_close = True

        if(self.sw_error):

            self.raizGen.btn_openfolder.hide()
            self.raizGen.stackedWidget.setCurrentIndex(1)

            QMessageBox.critical(self,"Proceso fallido","Ocurrió un error inesperado al generar el audio.")

        else:
            # clic para abrir carpeta ---
            root_s, file_s = os.path.split(self.ruta)
            self.raizGen.btn_openfolder.clicked.connect(lambda : webbrowser.open(root_s, new=2))
            
            # sms usuario y cambio de stak ---
            self.raizGen.stackedWidget.setCurrentIndex(1)
            self.mesaje_usuario(root_s)

    # HILO GENERADOR DE WAV +-+-+-+-+-+-+
    def hilo_genera_wav(self):
        worker = Worker(generar_audio_wav, self.ruta, self.texto, self.voz, self.rate, self)
        worker.signals.finished.connect(lambda : self.cronometro.stop())
        worker.signals.finished.connect(self.finalizar_conversion)
        self.threadpool.start(worker)   

    # HILO GENERADOR DE MP3 +-+-+-+-+-+-+
    def hilo_genera_mp3(self):
        worker = Worker(generar_audio_mp3, self.ruta, self.texto, self.voz, self.rate, self)
        worker.signals.finished.connect(lambda : self.cronometro.stop())
        worker.signals.finished.connect(self.finalizar_conversion)
        self.threadpool.start(worker)   

    # CERRADO DE VENTANA +-+-+-+-+-+-+
    def closeEvent(self, event):
        if(self.sw_close):
            self.parent.raizOpacidad.close()
            event.accept()
        else:
            event.ignore()


    # CONFIGURACIONES DE TITLE BAR /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        
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
       