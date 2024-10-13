import pymysql
from pymysql import MySQLError

class DataBase():
    def __init__(self, host, user, password, database):
        try: 
            self.connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                port=3306
            )
            self.cursor = self.connection.cursor()
            print("Conexión exitosa")

        except MySQLError as e:
            print(f"Error al conectar a la base de datos: {e}")
            self.connection = None 

    def crear_tablas(self):
        sentencia_USUARIOS='''CREATE TABLE IF NOT EXISTS orianaLagos_USUARIOS
        (Id int auto_increment PRIMARY KEY,Nombre varchar (50) not null,apellido varchar(50) not null, Clave varchar(250) not null)
          '''
        self.cursor.execute(sentencia_USUARIOS)
        self.connection.commit()

        sentencia_GASTOS='''CREATE TABLE IF NOT EXISTS orianaLagos_GASTOS
        (IdUsuario int NOT NULL, Fecha date not null, Categoria VARCHAR(50) not null,Monto int not null, Observacion varchar(200) null,FOREIGN KEY(IdUsuario) references orianaLagos_USUARIOS(Id))
          '''
        self.cursor.execute(sentencia_GASTOS)
        self.connection.commit()

        sentencia_INGRESOS = '''
        CREATE TABLE IF NOT EXISTS orianaLagos_INGRESOS (IdUsuario int NOT NULL , Fecha date not null, Categoria VARCHAR(50) not null,Monto int not null, Observacion varchar(200) null,FOREIGN KEY(IdUsuario) references orianaLagos_USUARIOS(Id))
          '''
        self.cursor.execute(sentencia_INGRESOS)
        self.connection.commit()





