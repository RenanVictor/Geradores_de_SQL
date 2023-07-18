import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"



setup(name= 'Finalizador',
    version='0.1',
    description='',
    executables = [Executable('Janela_Finalizar.py')])


    #python setup.py build - Usar esse comando no terminal para executar.
