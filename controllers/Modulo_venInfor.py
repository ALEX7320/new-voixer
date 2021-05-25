from PySide2.QtWidgets import QDialog,QHeaderView,QMessageBox,QSpinBox,QToolButton,QTableView,QSizeGrip
from PySide2.QtCore import QDate,QTime,Qt,QEvent
import webbrowser 

# diseño
from views.ui_venInformacion import Ui_venInformacion

class Ui_venInf(QDialog):
    def __init__(self, parent):
        super(Ui_venInf, self).__init__()

        # clase principal
        self.raizInf = Ui_venInformacion()
        self.raizInf.setupUi(self)

        # clase previa  /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        self.parent = parent

        self.raizInf.fr_move.mouseMoveEvent = self.moveWindow


        # transparencia y quitar barra superior /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.MSWindowsFixedSizeDialogHint)


        # cerrado  /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        self.raizInf.btn_close.clicked.connect(lambda:self.close())

        # contactos url  /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        self.raizInf.btn_ln.clicked.connect(lambda: webbrowser.open('https://www.linkedin.com/in/alex7320/', new=2))
        self.raizInf.btn_git.clicked.connect(lambda: webbrowser.open('https://github.com/alex7320', new=2))
        self.raizInf.btn_yt.clicked.connect(lambda: webbrowser.open('https://www.youtube.com/alex7320', new=2))
         
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
       