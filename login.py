from base_datos import DataBase
import bcrypt

class login ():
    def __init__(self,Database):
        self.database = Database

    def validador_login(self):
        nombre= input("Ingrese nombre de usuario: ")
        self.database.cursor.execute('SELECT nombre, apellido FROM orianaLagos_USUARIOS where nombre= %s', (nombre))
        filas= self.database.cursor.fetchone()
        if filas:
            nombre,apellido = filas
            clave= (f'{nombre[0]+nombre[1]+nombre[2]}.{apellido[0]+apellido[1]+apellido[2]}')
            sal= bcrypt.gensalt()
            clave_encriptada= bcrypt.hashpw(clave.encode(),sal)
        contrasena= input ("Ingrese contraseña registrada: ")
        if bcrypt.checkpw(contrasena.encode(), clave_encriptada):
            respuesta = print ("Acceso correcto")  
        else:
            respuesta = print("Acceso denegado") 
        return respuesta