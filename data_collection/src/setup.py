from cx_Freeze import setup, Executable

setup(name = "Teleport Data Tool" ,
      version = "0.1" ,
      description = "" ,
      executables = [Executable("main.py")])