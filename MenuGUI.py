from controllerVentana import conectarControles as conectSimple
from abc import ABC,abstractmethod
from Core_BDD.Sql import mySQLOperacion
from tkinter import messagebox as MessageBox
from InsertarDatosGUI import adminGUI
import tkinter as tk



class MiApp(tk.Tk):
    def __init__(self):
        super().__init__()  # Inicializar la clase padre (tk.Tk)
        contador=[0]
        # Configuración inicial de la ventana
        self.sqlOpera= mySQLOperacion()
        self.strAlto="600"
        variable=self.strAlto
        self.strAncho="600"
        self.title("Botones Dinámicos con Scroll")          # Título
        self.centrarventanaPrincipal()      # Tamaño (ancho x alto)
        self.resizable(True, False)     # Permitir redimensionar (ancho, alto)
        self.contador= contador
        #otra parte del codigo
        self.crear_PrincipalFrame()
        #self.agregar_boton()
        #self.cargar_botones()
        self.primerBoton()
        self.auto_btn()
        self.ventanaLogin()
        
        
        
        
        # Llamar a métodos de inicialización
        #self.contador[0]()
        
    def centrarventanaPrincipal(self):
    # Obtener dimensiones de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        ancho=int(self.strAncho)
        alto=int(self.strAncho)
        # Calcular posición x, y
        x = (screen_width - ancho) // 2
        y = (screen_height - alto) // 2
        
        # Aplicar geometría
        self.geometry(f"{self.strAncho}x{self.strAlto}+{x}+{y}")

    def centrarVentanas(self,ventana,ancho,alto):
        screen_width = ventana.winfo_screenwidth()
        screen_height = ventana.winfo_screenheight()
        
        # Calcular posición x, y
        x = (screen_width - ancho) // 2
        y = (screen_height - alto) // 2
        
        # Aplicar geometría
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
    
    def crear_PrincipalFrame(self): #metodo para crear los inicializar los canvas, scrollbar, etc.
        self.frame_principal = tk.Frame(self, bg="#f0f0f0")
        self.frame_principal.pack(fill="both", expand=True, padx=20, pady=20)
        
        self.frame_controles = tk.Frame(self.frame_principal)
        self.frame_controles.pack(pady=10)
        self.canvas = tk.Canvas(self.frame_principal, bg="white")
       
        self.scrollbar = tk.Scrollbar(self.frame_principal, orient=tk.VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Empaquetado
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Frame interior para los botones
        self.frame_interior = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame_interior, anchor="nw")
        
        # Configurar actualización automática del scroll
        self.frame_interior.bind("<Configure>", lambda e: self.actualizar_scrollregion())

        self.menuButon = tk.Menu(self)
        self.menuSesion = tk.Menu(self.menuButon, tearoff=0)
        
        self.menuButon.add_cascade(menu=self.menuSesion, label="Archivo")
        self.menuSesion.add_command(label="textos",accelerator="combiWord",command=self.devolver)
        
        
  
        
        self.config(menu=self.menuButon)
        
    def primerBoton(self):
        self.imagen = tk.PhotoImage(width=50, height=50)
        self.nuevo_boton = tk.Button(
            self.frame_interior,
            text=f"Crear BD \n➕",
            image=self.imagen,
            compound="center",
            width=100,
            
            command=self.agregar_boton
        )
        self.nuevo_boton.imagen = self.imagen 
        self.nuevo_boton.pack(pady=10, anchor="w")

        self.contador[0] += 1  # Actualizar contador
        self.actualizar_scrollregion()
    
    def agregar_boton(self):
        # Crear un nuevo botón y agregarlo al frame interior
        
        nombreExportado = conectSimple.devolverName(None)
        
        if nombreExportado is None:
            nombreExportado="hola"
        elif not nombreExportado:
            nombreExportado="hola"
        else:
            print("hubp error")
        
        self.imagen = tk.PhotoImage(width=60, height=60)
        self.nuevo_boton = tk.Button(
            self.frame_interior,
            text=f" {nombreExportado} {self.contador[0] + 1}",
            image=self.imagen,
            compound="center",
            width=100,
            command=lambda n=self.contador[0]: print(f"Botón {n + 1} clickeado")
        )
        self.nuevo_boton.imagen = self.imagen 
        self.nuevo_boton.pack(pady=10, anchor="w")

        self.contador[0] += 1  # Actualizar contador
        self.actualizar_scrollregion()

    def actualizar_scrollregion(self):
    # Actualizar el área de desplazamiento
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def cargar_botones(self):
        
        for _ in range(0):
            self.agregar_boton()
            
    def auto_btn(self):
        self.btn_agregar = tk.Button(
        self.frame_controles,
        text="➕ Agregar Botón",
        command=self.llamarVentanaExterna,
        bg="lightblue",
        fg="black"
        )
        self.btn_agregar.pack()
    def ventanaLogin(self):
        anchoHere=150
        altoHere=60
        self.loginFrame = tk.Toplevel(self.frame_principal)
        self.loginFrame.title("Login")
        self.loginFrame.geometry(f"{anchoHere}x{altoHere}")  # Establece tamaño primero
        self.loginFrame.resizable(False, False)
        
        self.loginFrame.update_idletasks() 
        self.centrarVentanas(self.loginFrame,anchoHere,altoHere)
        self.loginFrame.transient(self.frame_principal)
        self.loginFrame.protocol("WM_DELETE_WINDOW", self.destroy)
        self.loginFrame.configure(takefocus=True)
        self.loginFrame.grab_set()
        self.loginFrame.geometry("250x200")
        
        self.labelFast(self.loginFrame,10,10,"Iniciar sesion")
        
        self.labelFast(self.loginFrame,10,35,"Nombre")
        
        self.labelFast(self.loginFrame,10,95,"Contraseña (si la hay)")
        
        self.nameUser = tk.Entry(self.loginFrame)
        self.nameUser.place(width=150,height=20,x=10,y=60)
        
        
        self.passUser = tk.Entry(self.loginFrame)
        self.passUser.place(width=150,height=20,x=10,y=120)
        
        
        
        
        self.btnFast(self.loginFrame,10,150,100,30,"Ingresar",self.comprobarUser)
        self.btnFast(self.loginFrame,140,150,100,30,"Crear Usuario",self.crearUser)
        
    def comprobarUser(self):
        NombreUser=self.nameUser.get()
        passWo=self.passUser.get()
        valorBoo=self.sqlOpera.consultaUser(str(NombreUser),str(passWo))
        
        if(valorBoo):
            
            self.loginFrame.destroy()
            MessageBox.showinfo("Mensanje","Inicio de sesion exitosa")
            
        else:
            MessageBox.showwarning("Error 909","Error de usuario o contraseña ")
    
    def crearUser(self):
        anchoHere=150
        altoHere=60
        self.makeUser = tk.Toplevel(self.frame_principal)
        self.makeUser.title("Login")
        self.makeUser.geometry(f"{anchoHere}x{altoHere}")  # Establece tamaño primero
        self.makeUser.resizable(False, False)
        
        self.makeUser.update_idletasks() 
        self.centrarVentanas(self.makeUser,anchoHere,altoHere)
        self.centrarVentanas(self.makeUser,anchoHere,altoHere)
        self.makeUser.transient(self.frame_principal)
        self.makeUser.protocol("WM_DELETE_WINDOW", self.makeUser.destroy)
        self.makeUser.configure(takefocus=True)
        self.makeUser.grab_set()
        self.makeUser.geometry("250x200")
        
        self.checkValue = tk.BooleanVar(self.makeUser) # Create a BooleanVar
        self.checkValue.set(False)
        
        self.labelFast(self.makeUser,10,10,"Crear nuevo usuario")
        self.labelFast(self.makeUser,10,30,"Nombre:")
        self.labelFast(self.makeUser,10,90,"Contraseña")
        
        self.ingresaName = tk.Entry(self.makeUser)
        self.ingresaName.place(width=150,height=20,x=10,y=60)
        
        self.ingresapassUser = tk.Entry(self.makeUser)
        self.ingresapassUser.place(width=150,height=20,x=10,y=120)
        
        self.btnFast(self.makeUser,140,150,100,30,"Crear Usuario",self.consultaCrearUsuario)
        
        self.checkDefaultpass(self.makeUser,"Sin contraseña",self.checkValue,10,160,self.mesanjePrubea)
        
    def consultaCrearUsuario(self):
        boolean=False
        existe=True
        nombreU=""
        passWord=""
        nombreU=self.ingresaName.get()
        passWord=self.ingresapassUser.get()
        nu1=len(nombreU)
        nu2=len(passWord)
        existe=self.sqlOpera.buscarNameUser(nombreU)
        
        boolean=self.mesanjePrubea()
        try:
            if(existe!=True):
                if(passWord != '' and passWord != ''):
                    self.sqlOpera.insertarUsuarioPerfil(nombreU,passWord)
                    self.makeUser.destroy()
                    MessageBox.showinfo("Usuario","Su usuario se creo correctamente")
                if(passWord == '' and boolean):
                    passWord="admin"
                    self.sqlOpera.insertarUsuarioPerfil(nombreU,passWord)
                    self.makeUser.destroy()
                    MessageBox.showinfo("Usuario","Su usuario se creo correctamente")
                if(passWord == ''):
                    MessageBox.showwarning("Error 908","Agrege la contraseña")
                
            else:
                MessageBox.showwarning("Error 808","El usuario ya existe")
        except:
            MessageBox.showwarning("Error 801","Error al crear al usuario")
            
            self.ingresaName.delete(0, nu1)
            self.ingresapassUser.delete(0, nu2)
            
            
    def labelFast(self,upFrame,xPos,yPos,texto,):
        
        label = tk.Label(upFrame, text=texto).place(x=xPos,y=yPos)
 
    
    def btnFast(self,upFrame,xPos,yPos,entWidth,entHeight,texto,btnFuncion):
        
        botonGenerico = tk.Button(upFrame,text=texto,command=btnFuncion)
        botonGenerico.place(width=entWidth,height=entHeight,x=xPos,y=yPos)
        
    def checkDefaultpass(self,upFrame,texto,varible,xPos,yPos,command):
        checkbox = tk.Checkbutton(upFrame, text=texto, variable=varible, command=self.mesanjePrubea)
        checkbox.place(x=xPos,y=yPos)
        
    
        
    def mesanjePrubea(self):
        if self.checkValue.get():
            return True
        else:
            return False
        
    def devolver(self):
        numero=1
        conectSimple.imprimirdato(numero)
        
    def llamarVentanaExterna(self):
        ventanaInsert=adminGUI(self.frame_principal)
        ventanaInsert.ventCrearTabla()
        
        
    def frameLoop():
        app = MiApp()    # Instanciar la aplicación
    
        app.mainloop() 
class complementos:
    def __init__(self):
        pass
    def btnFast(self,upFrame,xPos,yPos,entWidth,entHeight,texto,btnFuncion):
        
        botonGenerico = tk.Button(upFrame,text=texto,command=btnFuncion)
        botonGenerico.place(width=entWidth,height=entHeight,x=xPos,y=yPos)
'''''''''
if __name__ == "__main__":
    app = MiApp()    # Instanciar la aplicación
    
    app.mainloop()   # Ejecutar el bucle principal
    '''''