from PySide2.QtWidgets import QDialog,QHeaderView,QMessageBox,QSpinBox,QToolButton,QTableView,QSizeGrip
from PySide2.QtCore import QDate,QTime,Qt,QEvent
import webbrowser 

# diseño
from views.ui_venGuia import Ui_venGuia

# funciones 
from controllers.Funcion_config import get_guide

class Ui_venGuiaUsu(QDialog):
    def __init__(self, parent):
        super(Ui_venGuiaUsu, self).__init__()

        # clase principal
        self.raizGuia = Ui_venGuia()
        self.raizGuia.setupUi(self)

        # transparencia y quitar barra superior /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.MSWindowsFixedSizeDialogHint)

        # clase previa  /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        self.parent = parent
        self.raizGuia.fr_move.mouseMoveEvent = self.moveWindow

        # mostrar guia  /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        self.change_guide(1,'btn_1')
        self.raizGuia.btn_1.clicked.connect(lambda : self.change_guide(1,'btn_1'))
        self.raizGuia.btn_2.clicked.connect(lambda : self.change_guide(2,'btn_2'))
        self.raizGuia.btn_3.clicked.connect(lambda : self.change_guide(3,'btn_3'))

        # cerrado  /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        self.raizGuia.btn_close.clicked.connect(lambda:self.close())

    def change_guide(self,num,btn):
        btns_obj = ['btn_1','btn_2','btn_3']
        for obj in btns_obj:
            getattr(self.raizGuia, obj).setEnabled(True)

        getattr(self.raizGuia, btn).setEnabled(False)
        self.raizGuia.hoja.setPlainText(get_guide(num))

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
       