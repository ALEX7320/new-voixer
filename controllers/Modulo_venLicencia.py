from PySide2.QtWidgets import QDialog,QMessageBox
from PySide2.QtCore import Qt

# diseño
from views.ui_venLicencia import Ui_venLicencia

# funciones 
from controllers.Funcion_config import get_guide
from controllers.Licencia import licencia_txt

class Ui_venLicen(QDialog):
    def __init__(self, parent):
        super(Ui_venLicen, self).__init__()

        # clase principal
        self.raizLicen = Ui_venLicencia()
        self.raizLicen.setupUi(self)

        self.raizLicen.hoja.setPlainText(licencia_txt)

        # transparencia y quitar barra superior /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.MSWindowsFixedSizeDialogHint)

        # clase previa  /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        self.parent = parent
        self.raizLicen.fr_move.mouseMoveEvent = self.moveWindow

        # cerrado  /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        self.raizLicen.btn_close.clicked.connect(lambda:self.close())

    # CERRADO DE VENTANA +-+-+-+-+-+-+
    def closeEvent(self, event):
        self.parent.raizOpacidad.close()
        event.accept()

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
       