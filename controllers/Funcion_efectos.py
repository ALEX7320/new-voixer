from PySide2.QtWidgets import QWidget,QGraphicsDropShadowEffect
from PySide2.QtGui import QPainter,QColor

# OPACIDAD VENTANA (POPUP) |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|

class Clase_Opacidad(QWidget):
    def __init__(self, parent=None):
        super(Clase_Opacidad, self).__init__(parent)

    # evento de QPainter
    def paintEvent(self, event):
        
        qp = QPainter()
        qp.begin(self)
        # color (r,g,b,a) tomar en cuenta que en a→255 es el valor maximo de opacidad
        qp.setBrush(QColor(0, 0, 0, 210)) #180 rgb(66, 74, 90)
        # poner el efecto al tamaño que se le aplico a esta clase
        # nota: -1 y +1 es para quitar los bordes negros (normalemente iria 0)
        qp.drawRect(-1, -1, self.size().width()+1, self.size().height()+1)
        qp.end()


def abrirVenOpaci(parent,opacidad,ventana):
    # abrimos la clase tomando el tamaño de nuestra ventana principal
    opacidad.resize(parent.width(), parent.height())
    opacidad.show()

    # abirmos la ventana secundaria
    ventana.exec_()



# SOMBRA |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|

def createSombra(cantidad=1, radio=28, ejex=0, ejey=0, colores=[0,0,0,80]):
    
    lista_sombras = []
    for i in range(cantidad):
        efecto_sombra = QGraphicsDropShadowEffect()
        efecto_sombra.setBlurRadius(radio)
        efecto_sombra.setXOffset(ejex)
        efecto_sombra.setYOffset(ejey)
        # color (r,g,b,a) tomar en cuenta que en a→255 es el valor maximo de opacidad
        cr, cg, cb, ca = colores
        efecto_sombra.setColor(QColor(cr, cg, cb, ca));

        lista_sombras.append(efecto_sombra)

    if(cantidad==1):
        return lista_sombras[0]

    else:
        return lista_sombras

def setSombra(objeto, efecto_sombra):
    objeto.setGraphicsEffect(efecto_sombra)
