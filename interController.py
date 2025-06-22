import tkinter as tk
from time import strftime
from generadorBarras import numero as hola
from MenuGUI import MiApp



class conecDatos:



    def __init__(self):
        pass
    

barrasCode39='code39'
numeroInvitado=input("Coloque el numero ultimo invitado")
numeroLargo=input("Coloque el largo del codigo de barras")
nombreInvitado=input("Coloque el nombre del invitado")


geneCall = hola()
geneCall.runGenerador(numeroInvitado,numeroLargo,nombreInvitado,barrasCode39)


