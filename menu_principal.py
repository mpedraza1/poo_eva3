from validadores import Validadores
from tabulate import tabulate
from menu import *
class Menu_Principal():
    

    def __init__(self,Database):
        self.database = Database
   
    def acceso_tablas(self):
        validacion = Validadores(self.database).validador_login()

        if validacion == "Acceso correcto":
            print("Acceso al Menú Principal")
            while True:
                print("\nMenu:")
                print("1. Acceso Menu Gastos")
                print("2. Acceso Menu Ingresos")
                print("3. Salir")           
                
                opcion = input("Seleccione una opción: ")
                
                if opcion == '1':
                    self.agregar_registro()
                elif opcion == '2':
                    self.ver_registros()
                elif opcion == '3':
                    self.modificar_registro()
                elif opcion == '4':
                    self.eliminar_registro()
                elif opcion == '5':
                    print("Saliendo del menú")
                    break
                else:
                    print("Opción no válida, por favor intente de nuevo.")
        else:
            print("Acceso incorrecto")
     

