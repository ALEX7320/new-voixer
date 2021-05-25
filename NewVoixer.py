# modulos por defecto
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QTranslator,QLibraryInfo,QLocale # copy,paste,cut (en spain)

from controllers.Modulo_venCarga import Ui_VenCarga
from controllers.Funcion_config import suppress_qt_warnings,add_font_app


if __name__ == "__main__":

    import sys
    suppress_qt_warnings() # quitar advertencias

    app = QApplication(sys.argv)
    app.setStyle('Fusion') # opcional

    #---traductor-cajaTexto-(copy,paste,cut)------
    traductor = QTranslator(app)
    lugar = QLocale.system().name()
    path = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    traductor.load("qtbase_%s" % lugar, path)
    app.installTranslator(traductor)

    # definir fonts
    add_font_app(r'font\Fashion Fetish')
    add_font_app(r'font\MADE Evolve Sans')

    mi_aplicacion = Ui_VenCarga()
    mi_aplicacion.show()
    sys.exit(app.exec_())
