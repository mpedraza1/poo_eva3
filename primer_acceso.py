import bcrypt
from validadores import Validadores


class Primer_Acceso():

    def __init__(self,Database):
        self.database = Database

    def primer_ingreso(self):
        nombre= input("Ingrese Nombre: ")
        apellido = input("Ingrese Apellido: ")
        if Validadores.existe_usuario(self,nombre,apellido) == True:
              print ("Usuario ya registrado")
        else:
          clave= (f'{nombre[0]+nombre[1]+nombre[2]}.{apellido[0]+apellido[1]+apellido[2]}')
          print(clave)
          sal= bcrypt.gensalt()
          clave_encriptada= bcrypt.hashpw(clave.encode(),sal)
          data= (nombre,apellido,clave_encriptada)
          sentencia=''' INSERT INTO orianaLagos_USUARIOS (nombre,apellido, clave) 
              values (%s,%s,%s);
            '''
          self.database.cursor.execute(sentencia,data)
          self.database.connection.commit()
          return print("Usuario nuevo creado")
'''    
          else:
            rut= input("Ingrese rut de usuario, sin puntos y con guión: ")
            self.database.cursor.execute('SELECT nombre, apPat, apMat, rut FROM benjaminSalazar_PERFILES where rut = %s', (rut,))
            filas= self.database.cursor.fetchone()
            if filas:
              nombre, apPat, apMat, rut = filas
              clave= (f'{nombre[0]}{apPat[0]}{apMat[0]}{rut}')
              sal= bcrypt.gensalt()
              clave_encriptada= bcrypt.hashpw(clave.encode(),sal)
            contrasena= input ("Ingrese contraseña registrada: ")

            if bcrypt.checkpw(contrasena.encode(), clave_encriptada):
                print ("Acceso correcto")
                validadores = Validadores(self.database)  # Crear una instancia de Validadores
                nivel = validadores.acceso_nivel(rut)   
                return rut, nivel,True
              
            else:
                print("Acceso denegado")


    def primer_ingreso_frases (self):
        self.database.cursor.execute(f"SELECT COUNT(*) FROM benjaminSalazar_FRASES")
        resultado = self.database.cursor.fetchone()[0]
        if resultado == 0: 
          frase1= "No comentes el código malo: reescríbelo. - Brian Kernighan "
          frase2= "Los buenos programadores saben qué escribir. Los grandes saben qué reescribir y reutilizar - Eric S. Raymond"
          frase3= "El código es como el humor. Cuando tienes que explicarlo, es malo. - Cory House"
          frase4= "Programador: Una máquina que convierte el café en código"
          frase5="Primero, resuelve el problema. Después, escribe el código. - John Johnson"
          frases = (frase1, frase2,frase3,frase4,frase5)'''
          #sentencia=''' INSERT INTO benjaminSalazar_FRASES (frases)''' 
          #      VALUES (%s), (%s), (%s), (%s), (%s);
          #  '''
          #self.database.cursor.execute(sentencia,frases)
          #self.database.connection.commit()
        #else:
        #  ()
