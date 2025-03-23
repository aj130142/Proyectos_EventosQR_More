import barcode
import os
from numpy import random
from barcode.writer import ImageWriter
from pathlib import Path
#argumentos default

barrasCode39='code39'
numeroInvitado=input("Coloque el numero ultimo invitado")
numeroLargo=input("Coloque el largo del codigo de barras")
nombreInvitado=input("Coloque el nombre del invitado")
class numero():
    def letrasRandom(self,numeroLetras):#metodo funcional sirve para poder extraer una cantidad determinadad de letras
        lista=[]                         
        abcd=["A","B","C","D","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        i=0
        codigoLetras=""
        while(i<=numeroLetras):
            x = random.randint(0,25)
            i=i+1
            lista.append(abcd[x])
        codigoLetras="".join(lista)
        return codigoLetras
    def numeroContar(self,numero): #extrae la ultima cantidad de participantes le suma uno al agregar otro y numeros de digitos que tiene
        numero =numero+1
        contadorNumero=len(str(numero))
        
        return numero,contadorNumero
    
    def codigoBarras(self,numCode,nameCode,tipoCodigo):#crea codigos de barras tipo formato, numero y nombre 
        
        code3 = barcode.get_barcode_class(tipoCodigo)
        codigo = code3(numCode, writer=ImageWriter(),add_checksum=False)
        rutaBase=Path.cwd().as_posix()
        ruta=rutaBase+"/media/"+numCode
        codigo.save(ruta)
        
    def unionCodigo(self,justoSTR,justInt):
        codigoFinal=''+justoSTR+justInt
        
        return codigoFinal
    def iniciarCodigo(self):
        hola=clases.numeroContar(int(numeroInvitado))#metodo para obtener datos y sumar + 1

        number=int(numeroLargo)-hola[1]-1 #ajusta la cantidad de letras requeridas

        abecario= clases.letrasRandom(number) #crea letras random

        codigoBar= clases.unionCodigo(abecario,str(hola[0])) # devuelve un numero de barras

        clases.codigoBarras(codigoBar,nombreInvitado,barrasCode39) #crea la imagen para codigo de barras
clases=numero()
clases.iniciarCodigo()