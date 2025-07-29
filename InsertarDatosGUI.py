from tkinter import Toplevel,Button,Label,Entry,Scrollbar,Checkbutton,Widget,N,W,VERTICAL,RIGHT,LEFT,BOTH,BOTTOM,Y,X,Frame,Canvas,OptionMenu
from tkinter import ttk
#from MenuGUI import complementos
class adminGUI:
    def __init__(self,Frame):
        self.frameTop=Frame
        self.varX=100
        self.varY=100
        self.vartexto=10
        self.listaEntry=[]
        self.listaCombo=[]
        self.listaLabel0=[]
        self.listaLabel1=[]
        self.listaLabel2=[]
        self.listaBtnX=[]
        self.codigoQR=False
        
        self.valore=["Numeros","Decimal","Moneda","Texto normal","Texto largo","Año/mes/dia","Horas/Minutos/Segundos","Archivos<4GB","Correo electronico","CodigosQR"]
        self.numeroBoton=0
        self.newNumero=0
        self.booleDele=False
        #self.exportComple=complementos()
    def ventCrearTabla(self):
        anchoHere=600
        altoHere=600
        
        self.makeTable=Toplevel(self.frameTop)
        default_color = self.makeTable.cget("bg")
        
        
        
        self.upFrame=Frame(self.makeTable)
        self.upFrame.pack(pady=10)
        self.makeTable.title("Login")
        
        self.makeTable.geometry(f"{anchoHere}x{altoHere}")  # Establece tamaño primero
        self.centrarVentanas(self.makeTable,anchoHere,altoHere)
        self.canvas = Canvas(self.makeTable, bg=default_color)
        
        self.scroll=Scrollbar(self.makeTable,orient=VERTICAL,command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scroll.set)
        
        self.scroll.pack(side=RIGHT, fill=Y)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        
        
        self.frame_interior = Frame(self.canvas)
        
        self.canvas.create_window((0, 0), window=self.frame_interior, anchor="nw")
        
        # Configurar actualización automática del scroll
        self.frame_interior.bind("<Configure>", lambda e: self.actualizar_scrollregion())
        
        self.btnFast(self.upFrame,"Nuevo campo",self.agregar_boton,1,0)
        self.btnFast(self.upFrame,"Guardar cambios",self.mostraDatosentry,1 ,4)
        
        self.entryNameTb=Entry(self.upFrame)
        self.entryNameTb.grid(row=0,column=1,padx=5,pady=10)
        labelNombre=Label(self.upFrame,text="Nombre de la tabla")
        labelNombre.grid(row=0,column=0,padx=5,pady=10)
        
        
        
    def centrarVentanas(self,ventana,ancho,alto):
        screen_width = ventana.winfo_screenwidth()
        screen_height = ventana.winfo_screenheight()
        
        # Calcular posición x, y
        x = (screen_width - ancho) // 2
        y = (screen_height - alto) // 2
        
        # Aplicar geometría
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
    def btnFast(self,upFrame,texto,btnFuncion,rowN,colN):
        
        botonGenerico = Button(upFrame,text=texto,command=btnFuncion)
        botonGenerico.grid(row=rowN,column=colN,padx=60)
        
    def guardaNumero(self,event):
            numero = event.widget.numero
            print(f"{numero} indice del numero")
            self.listaEntry[numero].destroy()
            self.listaCombo[numero].destroy()
            self.listaLabel0[numero].destroy()
            self.listaLabel1[numero].destroy()
            self.listaLabel2[numero].destroy()
            self.listaBtnX[numero].destroy()
            print(f"{len(self.listaEntry)} numero de largo de la lista")
            
            self.listaEntry.pop(numero)
            self.listaCombo.pop(numero)
            self.listaLabel0.pop(numero)
            self.listaLabel1.pop(numero)
            self.listaLabel2.pop(numero)
            self.listaBtnX.pop(numero)
            largoLista=len(self.listaBtnX)
            self.numeroBoton=0
            self.actualizarbtnX(largoLista)
            
    def actualizar_scrollregion(self):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    def actualizarbtnX(self,listLa):
        
        
        

        for i in range(listLa):
            self.listaBtnX[i].numero=i
            print(i)
        
    
    def agregar_boton(self):
        
        self.entryNew = Entry(
            self.frame_interior
            
        )
        self.refCombo=self.combo = ttk.Combobox(
            self.frame_interior,
            state="readonly",
            values=self.valore
        )
        self.labal0=Label(self.frame_interior, text=f"{self.numeroBoton}. -----------------")
        self.labal0.pack(pady=0,padx=50, anchor="nw")
        
        self.labal2=Label(self.frame_interior, text="Nombre del campo")
        self.labal2.pack(pady=0,padx=50, anchor="nw")
        
        
        self.boton0=Button(self.frame_interior,text="X")
        self.boton0.numero = self.numeroBoton  # Valor inicial
        self.boton0.bind("<Button-1>", self.guardaNumero)
        self.entryNew.pack(pady=10,padx=50, anchor="nw",expand=False,ipadx=150)
        
        self.labal1=Label(self.frame_interior, text=" Tipo de dato")
        self.labal1.pack(pady=0,padx=50, anchor="nw")
        
        self.combo.pack(pady=10,padx=50,expand=True, anchor="nw")
        
        self.boton0.pack(pady=5,padx=100)
        
        self.listaEntry.append(self.entryNew)
        self.listaCombo.append(self.refCombo)
        self.listaLabel0.append(self.labal0)
        self.listaLabel1.append(self.labal1)
        self.listaLabel2.append(self.labal2)
        self.listaBtnX.append(self.boton0)
        self.numeroBoton=self.numeroBoton+1
        
        self.actualizar_scrollregion()
    def mostraDatosentry(self):
        
        hola=self.listaEntry[0].get()
        combo1=self.listaCombo[0].get()
        if len(self.listaEntry)>=2:
            hola1=self.listaEntry[1].get()
            combo2=self.listaCombo[1].get()
            
            print(hola1)
            print(combo2)
        print(self.newNumero)
        print(hola)
        print(combo1)
        
    def checkDefaultpass(self,upFrame,texto,varible,roW,colW,commando):
        checkbox = Checkbutton(upFrame, text=texto, variable=varible, command=commando)
        checkbox.grid(row=roW,column=colW,padx=10)