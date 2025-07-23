import mysql.connector
import re
class mySQLOperacion:

    def __init__(self):
        #conexicion de la base de datos en el programa
        self.mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="aj1381",
        database='useradmin'
        )
        self.mycursor = self.mydb.cursor()
        
    def mostrarDB(self):
        self.mycursor.execute("SHOW DATABASES")
        listaRetor=[]
        for x in self.mycursor:
            
            listaRetor.append(str(x))
        
        return listaRetor
    def crearDB(self,newDB):
        if not re.match(r'^[a-zA-Z0-9_]+$', newDB):
            raise ValueError("Nombre de base de datos inválido")

    # 2. Escapar manualmente (opcional pero redundante si validamos bien)
        escaped_db = newDB.replace("`", "``")  # Escapa backticks existentes
        query=f"CREATE DATABASE IF NOT EXISTS {escaped_db}"
        self.mycursor.execute(query)
        
    def deleteDB(self,deleteDB):
        if not re.match(r'^[a-zA-Z0-9_]+$', deleteDB):
            raise ValueError("Nombre de base de datos inválido")

    # 2. Escapar manualmente (opcional pero redundante si validamos bien)
        escaped_db = deleteDB.replace("`", "``")  # Escapa backticks existentes
        query=f"DROP DATABASE IF EXISTS  {escaped_db}"
        self.mycursor.execute(query)
    
    def crearUserTablas(self):
        #nombre, apellidos, fecha registrado,
        query="CREATE TABLE  IF NOT EXISTS useradmin.userperfil (userID int AUTO_INCREMENT PRIMARY KEY, userNombre varchar(255)  NOT NULL UNIQUE, contrasena varchar(255))"
        self.mycursor.execute(query)
    
    def insertarUsuarioPerfil(self,nombre,contraseña):
        query=f"INSERT INTO useradmin.userperfil (userNombre,contrasena) VALUES(%s,%s)"
        self.mycursor.execute(query,(nombre,contraseña))
        self.mydb.commit()
    def eliminarTabla(self,nombreTabla,nameDB):
        query=f"DROP TABLE IF EXISTS {nameDB}.{nombreTabla}"

        self.mycursor.execute(query)
        self.mydb.commit()
    
    def consultaUser(self,userNombre,passW):
        
        if(passW==""):
            passW="admin"
        query=f"SELECT * FROM   useradmin.userperfil WHERE userNombre = %s AND contrasena = %s "
        self.mycursor.execute(query,(userNombre,passW))
        myresult = self.mycursor.fetchone()
        
        if myresult is not None:
            return True
        else:
            return False
    def buscarNameUser(self,nameUs):
        query=f"SELECT * FROM  useradmin.userperfil WHERE userNombre = %s"
        self.mycursor.execute(query,(nameUs,))
        myresult = self.mycursor.fetchone()
        
        if myresult is None:
            return False
        
        if myresult[1] == nameUs:
            return True
        else:
            return False


