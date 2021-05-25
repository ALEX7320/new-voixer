from PySide2.QtTextToSpeech import QTextToSpeech # texto a voz
from PySide2.QtWidgets import QFileDialog,QMessageBox
from PySide2.QtCore import Qt

# FUNCIONES GENERALES /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

# ESTILOS HOJA +-+-+-+-+-+-+
def size_hoja(hoja, size):

    hoja.setStyleSheet(u"/*CAJA TEXTO*/\n"
        "QPlainTextEdit{\n"
        "	color: white;\n"
        f"	font-size: {size}px;\n"
        "	border: 0px;\n"
        "	padding: 10px;\n"
        "	background-color: rgb(19, 36, 47);\n"
        "	font-family: \"MADE Evolve Sans\";\n"
        "	font-weight:Regular\n"
        "}\n"
        "")

# VALIDAR TEXTO VACIO +-+-+-+-+-+-+
def verificar_texto(texto):
    texto = texto.replace('\n','')
    texto = texto.replace('\t','')
    texto = texto.replace(' ','')

    if(texto == ''):
        return False
    else:
        return True

# CONFIGURACIONES DE VOCES /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

# CARGAR ENGINES DEL SISTEMA +-+-+-+-+-+-+
def get_EngiVoces(parent):
    # lista de voces del sistema
    engineNombres = QTextToSpeech.availableEngines()  
    if(engineNombres):
        return QTextToSpeech(engineNombres[0])
    else:
        return None

# OBTENER VOCES DEL SISTEMA +-+-+-+-+-+-+
def config_EngiVoces(eng, cbox):
    cbox.clear()
    for regi in eng.availableLocales():#availableVoices
        eng.setLocale(regi)

        for voice in eng.availableVoices():#availableVoices
            cbox.addItem(
                        voice.name(), # texto 
                        [voice,voice.name()] # valores
                        )


# CONTROLES DE AUDIO /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

# CTRL PAUSE Y RESUME +-+-+-+-+-+-+
def config_EnginePause(eng):

    estado = str(eng.state())
    
    if('State.Paused' in estado):
        eng.resume()

    elif('State.Speaking' in estado):
        eng.pause()

# CAMBIAR RATE O VOLUMEN +-+-+-+-+-+-+
def config_EngineCtrl(parent, valor, opc):
    
    # Volumen ___________________
    if(opc=='vol'):
        parent.engine.setVolume(valor)

    # Rate ___________________
    else:
        parent.engine.setRate(valor)

# TEXTO DE CURSOR SELECCIONADO +-+-+-+-+-+-+
def config_EngineRead(parent, praiz):

    # texto del cursor
    cursor = praiz.hoja.textCursor()
    texto = cursor.selectedText()
    texto = texto.replace('\u2029','\n')

    if(not verificar_texto(texto)):
        # todo el texto de la caja
        texto = praiz.hoja.toPlainText()

        if(not verificar_texto(texto)):
            return ''

    return texto

# LEER TEXTO +-+-+-+-+-+-+
def read_engine(parent):
    texto_select = config_EngineRead(parent,parent.raizPrin)
    if(texto_select==''):
        QMessageBox.warning(parent, 'Denegado', f'Documento vacio, por favor agregar texto.')
        return 

    cambio_modo_hoja(parent, parent.raizPrin.hoja, False)
    parent.engine.say(texto_select)




# PREVIO A GENERAR /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
def cambio_modo_hoja(parent, hoja, modo):
    # ACTIVADO __________________
    if(modo):
        hoja.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard |
                                    Qt.TextEditable | Qt.TextEditorInteraction)
        parent.raizPrin.lb_sms_lectura.hide()
        parent.verificar_lectura.stop()

    # DESACTIVADO __________________
    else:
        hoja.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard )
        parent.raizPrin.lb_sms_lectura.show()
        parent.verificar_lectura.start()
    
    parent.raizPrin.btn_borrar.setEnabled(modo)
    parent.raizPrin.btn_abrir_txt.setEnabled(modo)

# PREVIO A GENERAR /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
def sent_generate(parent):
    from controllers.Funcion_efectos import abrirVenOpaci
    from controllers.Modulo_generar import Ui_venGen

    parent.engine.stop()
    cambio_modo_hoja(parent, parent.raizPrin.hoja, True)

    texto_select = config_EngineRead(parent,parent.raizPrin)
    if(texto_select==''):
        QMessageBox.warning(parent, 'Denegado', f'Documento vacio, por favor agregar texto.')
        return  

    ruta= QFileDialog.getSaveFileName(None, 'Guardar archivo', '','Audio (*.mp3);;Audio (*.wav)')

    if(ruta[0]==''):
        return

    indice_voz = parent.raizPrin.cb_voz.currentIndex()
    voz_select = parent.raizPrin.cb_voz.itemData(indice_voz)[1]
    rate_select = round(parent.raizPrin.sp_rate.value()*10)

    opc = 'wav' if('(*.wav)' in ruta[1]) else 'mp3'

    abrirVenOpaci(
        parent,
        parent.raizOpacidad,
        Ui_venGen(parent, opc, ruta[0], voz_select, rate_select, texto_select)
        )
        

# MANIPULACION DE TXT /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

# ABRIR TEXTO +-+-+-+-+-+-+
def archivo_txt_open(hoja, parent):
    ruta= QFileDialog.getOpenFileName(None, 'Seleccionar archivo','','Texto (*.txt)')
    if(ruta[0]!=''):
        with open(ruta[0], 'r', encoding="utf8") as archivo:
            hoja.appendPlainText(''.join(archivo.readlines()))

        parent.mover_texto('down')

# GUARDAR TEXTO +-+-+-+-+-+-+
def archivo_txt_save(hoja,parent):

    texto_sel = hoja.toPlainText()
    if(not verificar_texto(texto_sel)):
        QMessageBox.warning(parent, 'Denegado', f'Documento vacio, por favor agregar texto.')
        return

    ruta= QFileDialog.getSaveFileName(None, 'Guardar archivo','','Texto (*.txt)')
    if(ruta[0]!=''):
        with open(ruta[0], 'w', encoding="utf8") as archivo:
            archivo.write(texto_sel)


# CARGAR UTIMA MODIFINCACION /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

# VERIFICAR CARPETA DE TEXTO TEMPORAL +-+-+-+-+-+-+
def verificar_carpeta_text():
    import os
    if not(os.path.isdir("temp")):
        os.makedirs("temp")

# RESTABLECER Y GUARDAR CAMBIOS EN TXT TEMPORTAL +-+-+-+-+-+-+
def establecer_cambios_text(hoja, opc):
    '''opc : open save '''

    ruta_domcumento = r'temp/temp_text.txt'
    verificar_carpeta_text()

    # open _________________________
    if(opc == 'open'):
        try:
            with open(ruta_domcumento, 'r', encoding="utf8") as archivo:
                hoja.setPlainText(''.join(archivo.readlines()))
        except:
            pass

    # save _________________________
    else:
        with open(ruta_domcumento, 'w', encoding="utf8") as archivo:
                archivo.write(hoja.toPlainText())



