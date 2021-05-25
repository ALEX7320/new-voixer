# VERIFICAR IMAGEN CARGA

def get_icon_notifi():
    from pathlib import Path
    ruta = r"image/vx_ticon_full.ico"
    fileObj = Path(ruta)

    if(fileObj.is_file()):
        return ruta
    else:
        return None

# GENERAR MP3 /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

# VERIFICAR CARPETA DE GUARDADO AUXILIAR +-+-+-+-+-+-+
def verificar_carpeta_sound():
    import os
    if not(os.path.isdir("sounds")):
        os.makedirs("sounds")

# PROCESO DE MP3 +-+-+-+-+-+-+
def generar_audio_mp3(ruta_mp3, texto, voz, rate, parent):
    import os
    try:
        # ruta auxiliar para generar el .wav
        ruta_wav = os.path.join(os.getcwd(), 'sounds\\sample.wav')

        # verificar la carpeta
        verificar_carpeta_sound()
    
        # genera archivo wav
        generar_audio_wav(ruta_wav, texto, voz, rate, parent)

        # convierte wav a mp3
        convertir_audio_mp3(ruta_wav, ruta_mp3)

        # borrar el archivos wav temporal
        os.unlink(ruta_wav)

        # verificar errores en el hilo
        parent.sw_error = False

    except:
        parent.sw_error = True

# CONVERTIR WAV A MP3 +-+-+-+-+-+-+
def convertir_audio_mp3(ruta_wav, ruta_mp3):
    import subprocess
    import os

    # Formatos soportados
    # ("flac", "aac", "aiff", "m4a", "ogg", "opus", "raw", "wav", "wma", "webm")

    # rutas de guardado
    full_path = ruta_wav
    new_path = ruta_mp3

    # ocultar ventana
    DETACHED_PROCESS = 0x00000008

    # proceso
    subprocess.run(["ffmpeg",
                    "-loglevel",
                    "quiet",
                    "-hide_banner",
                    "-y",
                    "-i",
                    full_path,
                    "-write_id3v1",
                    "1",
                    "-id3v2_version",
                    "3",
                    "-codec:a",
                    "libmp3lame",
                    "-q:a",
                    "3",
                    new_path],
                    stderr=subprocess.DEVNULL,
                    stdout=subprocess.DEVNULL,
                    stdin=subprocess.PIPE,
                    
                    creationflags=DETACHED_PROCESS)

# GENERAR WAV /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
def generar_audio_wav(ruta_wav, texto, voz, rate, parent):
    try:

        import comtypes.client##este es para generar el archivo
        
        speaker=comtypes.client.CreateObject("SAPI.SpVoice")
        speaker.Rate = rate # rango -10(lento) - 10(rapido)
        speaker.Volume = 100# rango 0(vajo) - 100(alto)

        speaker.Voice = speaker.GetVoices('Name='+voz).Item(0)

        ##--------GENERAR
        fileCreate = comtypes.client.CreateObject("SAPI.spFileStream")##creamos archivo
        fileCreate.open(ruta_wav,3, False)##abrimos archivo
        speaker.AudioOutputStream = fileCreate
        
        ##acá puedes cambiar la VOZ y poner el VOLUMEN y RATE
        speaker.Speak(texto)##este texto no se leera, solo se guarda
        fileCreate.close()##cerramos archivo##--------GENERAR_FIN

        # verificar errores en el hilo
        parent.sw_error = False

    except:
        parent.sw_error = True

