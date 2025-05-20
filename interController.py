import tkinter as tk
from time import strftime
import generadorBarras as generador
import MenuGUI as MenuG


barrasCode39='code39'
numeroInvitado=input("Coloque el numero ultimo invitado")
numeroLargo=input("Coloque el largo del codigo de barras")
nombreInvitado=input("Coloque el nombre del invitado")

generador.clases.runGenerador(numeroInvitado,numeroLargo,nombreInvitado,barrasCode39)


 # Ejecutar el bucle principal

