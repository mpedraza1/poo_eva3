from base_datos import DataBase
from config import DB_CONFIG
from primer_acceso import Primer_Acceso
from menu_principal import Menu_Principal
#from menu import Menu_Inicio
from validadores import Validadores
from login import login 

def main():
    base_datos = DataBase(**DB_CONFIG)
    base_datos.crear_tablas()
    inicio= Primer_Acceso(base_datos)
    inicio.primer_ingreso()
    menu_prin= Menu_Principal(base_datos)
    menu_prin.acceso_tablas()
    '''if acceso:
        menu_prin = Menu_principal(base_datos)
        menu_prin.opciones(rut,nivel)
    else:
        print ("Usuario y/o contraseña incorrecta")'''


if __name__ == '__main__':
    main()

