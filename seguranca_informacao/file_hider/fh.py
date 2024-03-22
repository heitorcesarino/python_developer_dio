import ctypes

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('/FORMACAO-PYTHON-DIO/seguranca_informacao/file_hider/ocultar.txt', atributo_ocultar)

if retorno:
    print('arquivo foi ocultado')
else:
    print('arquivo nãofoi ocultado')