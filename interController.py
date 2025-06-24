import tkinter as tk
from time import strftime
from generadorBarras import numero as codigoBarras
from MenuGUI import MiApp as frameGUI



class conecDatos:



    def imprimirdato(dato):
        return print(dato)
    
    ventansUsuario = frameGUI()
    dato=ventansUsuario.devolver()
    imprimirdato(dato)

    barrasCode39='code39'
    numeroInvitado=input("Coloque el numero ultimo invitado")
    numeroLargo=input("Coloque el largo del codigo de barras")
    nombreInvitado=input("Coloque el nombre del invitado")




    geneCall = codigoBarras()
    geneCall.runGenerador(numeroInvitado,numeroLargo,nombreInvitado,barrasCode39)



