from validadores import Validadores
from tabulate import tabulate
#SELECT DATE_FORMAT(fecha, '%d/%m/%Y') AS fecha_formateada FROM tu_tabla;
def acceso_tablas(self):
    
    validacion = Validadores(self.database).validador_login()
    if validacion == "Acceso correcto":
        print("Acceso a tablas")
        while True:
            print("\nMenu:")
            print("1. Crear")
            print("2. Ver")
            print("3. Modificar")
            print("4. Eliminar")
            print("5. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                self.agregar_registro()
            elif opcion == '2':
                self.ver_registros()
            elif opcion == '3':
                self.modificar_registro()
            elif opcion == '4':
                self.eliminar_registro()#verificar regitro que exista con esa fecha y ese monto 
            elif opcion == '5':
                print("Saliendo del menú CRUD.")
                break
            else:
                print("Opción no válida, por favor intente de nuevo.")
    else:
        print("Acceso incorrecto")

    def agregar_registro(self):
        fecha=input('Ingrese Fecha De Registro (año/mes/dia):')
        categoria=input('Ingrese Categoria: ')
        while True:
                try:
                    monto= int(input("Ingrese Monto: "))
                    if monto <= 0 :
                        raise ValueError("Monto debe ser SUPERIOR a 0)")
                    break
                except ValueError as ve:
                    print(f"Error: {ve}")
                except Exception as e:
                    print(f"(INGRESE SOLO NUMEROS!, {e})")
        observacion=input('Ingrese Observacion: ')
        data=(fecha,categoria,monto,observacion)
        sentencia="insert into orianaLagos_GASTOS (Fecha,Categoria,Monto,Observacion) values (%s,%s,%s,%s)"
        self.database.cursor.execute(sentencia,data)
        self.database.connection.commit()

    def ver_registros(self):
        sentencia = "SELECT Fecha,Categoria,Monto,Observacion FROM orianaLagos_GASTOS"
        self.database.cursor.execute(sentencia)
        datos = self.database.cursor.fetchall()
        headers = ['Fecha,Categoria,Monto,Observacion']
        tabla = tabulate(datos, headers=headers, tablefmt="fancy_grid")
        print(tabla) 

    def modifica_registro(self):
        fecha=input('Ingrese fecha del registro a modificar:')
        monto=int(input('Ingrese nuevo monto:'))
        while True:
            try:
                monto= int(input("Ingrese Monto: "))
                if monto <= 0 :
                    raise ValueError("Monto debe ser SUPERIOR a 0)")
                break
            except ValueError as ve:
                print(f"Error: {ve}")
            except Exception as e:
                print(f"(INGRESE SOLO NUMEROS!, {e})")
        sentencia=f"update orianaLagos_GASTOS set fecha='{fecha}' where monto='{monto}'"
        self.database.cursor.execute(sentencia)
        self.database.connection.commit()    

    def eliminar_registro(self):
            fecha=input('Ingrese fecha del registro a eliminar: ')
            monto=input('Ingrese monto del registro a eliminar: ')
            query = f"DELETE FROM orianaLagos_REGISTROS WHERE fecha =%s and monto =%s"
            self.database.cursor.execute(query,(fecha,monto))
            self.database.connection.commit()
            print('Perfil eliminado') 


        