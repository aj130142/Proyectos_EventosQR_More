import tkinter as tk

class MiApp(tk.Tk):
    def __init__(self):
        super().__init__()  # Inicializar la clase padre (tk.Tk)
        contador=[0]
        # Configuración inicial de la ventana
        self.strAlto="600"
        self.strAncho="600"
        self.title("Botones Dinámicos con Scroll")          # Título
        self.centrarventanaPrincipal()      # Tamaño (ancho x alto)
        self.resizable(True, False)     # Permitir redimensionar (ancho, alto)
        self.contador= contador
        #otra parte del codigo
        self.crear_PrincipalFrame()
        self.agregar_boton()
        self.cargar_botones()
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

    def agregar_boton(self):
        # Crear un nuevo botón y agregarlo al frame interior
        self.imagen = tk.PhotoImage(width=50, height=50)
        self.nuevo_boton = tk.Button(
            self.frame_interior,
            text=f"Hola {self.contador[0] + 1}",
            image=self.imagen,
            compound="center",
            width=50,
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
        
        for _ in range(5):
            self.agregar_boton()
            
    def auto_btn(self):
        self.btn_agregar = tk.Button(
        self.frame_controles,
        text="➕ Agregar Botón",
        command=self.agregar_boton,
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
        
        self.btnFast(self.loginFrame,10,150,100,30,"Ingresar",self.loginFrame.destroy)
        self.btnFast(self.loginFrame,140,150,100,30,"Crear Usuario",self.crearUser)
    
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
        self.labelFast(self.makeUser,10,30,"Nombre")
        self.labelFast(self.makeUser,10,90,"Contraseña")
        
        self.nameUser = tk.Entry(self.makeUser)
        self.nameUser.place(width=150,height=20,x=10,y=60)
        
        self.passUser = tk.Entry(self.makeUser)
        self.passUser.place(width=150,height=20,x=10,y=120)
        
        self.checkDefaultpass(self.makeUser,"Opcion",self.checkValue,10,160,self.mesanjePrubea)
    
    def labelFast(self,upFrame,xPos,yPos,texto,):
        
        label = tk.Label(upFrame, text=texto)
        label.place(x=xPos,y=yPos)
    
    def btnFast(self,upFrame,xPos,yPos,entWidth,entHeight,texto,btnFuncion):
        
        botonGenerico = tk.Button(upFrame,text=texto,command=btnFuncion)
        botonGenerico.place(width=entWidth,height=entHeight,x=xPos,y=yPos)
        
    def checkDefaultpass(self,upFrame,texto,varible,xPos,yPos,command):
        checkbox = tk.Checkbutton(upFrame, text=texto, variable=varible, command=self.mesanjePrubea)
        checkbox.place(x=xPos,y=yPos)
        
    def mesanjePrubea(self):
        if self.checkValue.get():
            print("encendido")
        else:
            print("apagado")
        
    def iniciar(self):
        self.vista.mainloop()

if __name__ == "__main__":
    app = MiApp()    # Instanciar la aplicación
    
    app.mainloop()   # Ejecutar el bucle principal
