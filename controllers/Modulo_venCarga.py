# funciones PySide2
from PySide2.QtWidgets import QDialog
from PySide2.QtCore import Qt,QTimer

# diseño principal
from views.ui_ventanaCarga import Ui_VentanaCarga 

# efecto opacidad ----
from controllers.Funcion_efectos import createSombra,setSombra

# ventana que se abrira
from controllers.Modulo_venPrinci import Ui_venPrin

class Ui_VenCarga(QDialog):

    def __init__(self):
        super(Ui_VenCarga, self).__init__()
        
        self.raizCarga = Ui_VentanaCarga()
        self.raizCarga.setupUi(self)

        # MODIFICAR PRIORIDAD DE VENTANA
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.contador=0

        # QUITAR FONDO, TRANSAPARENCIA
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.configuraciones_widgets()

        # EJECUTANDO LA BARRA DE PROGRESO
        self.timeLoad = QTimer()
        self.timeLoad.timeout.connect(self.progresoView)
        self.timeLoad.start(18)#30

    def configuraciones_widgets(self):

        self.l1, self.l2 = createSombra(2)
        setSombra(self.raizCarga.frameLoad,self.l1)     
        setSombra(self.raizCarga.frameLoad_2,self.l2)     

    # CARGANDO BARRA
    def progresoView(self):

        self.raizCarga.progreLoad.setValue(self.contador)

        if(self.contador > 100):
            self.timeLoad.stop()

            self.close()
            
            self.main = Ui_venPrin()
            self.main.show()

        self.contador += 1
