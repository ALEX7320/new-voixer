# QUITAR ADVERTENCIAS DE QT
def suppress_qt_warnings():
    '''omitir advertencias de qt'''
    from os import environ

    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

# AGREGAR FUENTES
def add_font_app(ruta, extension):
    '''extension: ttf, otf '''
    
    try:
        from PySide2.QtGui import QFontDatabase
        import os

        for font in os.listdir(ruta):
            if(font.endswith('ttf')):
                font_set = os.path.join(ruta, font)
                QFontDatabase.addApplicationFont(font_set)
    except:
        pass

def get_guide(num):
    guia_txt = {
            1 : str(
                    'El archivo mp3 demora en generar el doble del archivo wav.\n'
                    '\n'
                    'Bitrate:\n'
                    'wav: 352kbps (pesado)\n'
                    'mp3: 60kbps (ligero)'
                ),

            2 : str(
                'New Voixer utiliza los sintetizadores de Windows, para obtener más tipos de voces, deberá descargarlo directamente del sistema.'
                ),
                
            3 : str(
                'Si usted selecciona el texto y posteriormente activa la lectura o genera un '
                'archivo de audio, este se basará en dicho texto, pero si no se seleccionó nada '
                'tomará todo el texto por defecto.'    
            )
        }

    return guia_txt[num]