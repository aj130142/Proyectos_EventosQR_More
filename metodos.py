import tkinter as tk
from tkinter import ttk


class metodos(tk.Toplevel):
    en_uso = False
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.config(width=300, height=200)
        self.title("Ventana secundaria")
        self.butto()
        self.focus()
            # Indicar que está en uso luego de crearse.
        self.__class__.en_uso = True
        
    def butto(self):
        self.boton_cerrar = ttk.Button(
            self,
            text="Cerrar ventana",
            command=self.destroy
            )
        self.boton_cerrar.place(x=75, y=75)
    
    def destroy(self):
        # Restablecer el atributo al cerrarse.
        self.__class__.en_uso = False
        return super().destroy()

class VentanaPrincipal(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=400, height=300)
        self.maxsize(width=400,height=300)
        self.minsize(width=400,height=300)
        self.title("Ventana principal")
        
        self.menu()
        #boton de prueba
        #self.boton1()
    def boton1(self):
        self.boton_abrir = ttk.Button(
            self,
            text="Abrir ventana secundaria",
            command=self.abrir_ventana_secundaria
        )
        self.boton_abrir.place(x=10, y=10)
    def abrir_ventana_secundaria(self):
        if not metodos.en_uso:
            self.ventana_secundaria = metodos()
    def menu(self):
        self.menuMain = tk.Menu()
        self.MenuPrincipal = tk.Menu(self.menuMain, tearoff=False)
        self.menuMain.add_cascade(label="Menu",menu=self.MenuPrincipal)
        self.MenuPrincipal.add_command(label="Funcion1",command=self.abrir_ventana_secundaria)
        self.config(menu=self.menuMain)
#instancias principales
ventana_principal = VentanaPrincipal()
ventana_principal.mainloop()