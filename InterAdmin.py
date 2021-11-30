# Consola interactiva del usuario administrador
import sys
from os import system
from sys import argv
from time import sleep
from UserList import existe_usuario
import UserList
from getpass import getpass
from InventarioFunc import Inventario

def console_admin():
    while True:
        console = str(input("ADMIN>> "))
        if console == "exit" or console == "quit" or console == "salir":
            sys.exit(0)

        elif console == "clear":
            system("cls")# Limpieza de terminal

        elif console == "whoami":
            print("Administrador")

        elif console == "ireal":
            user = input("Nombre del usuario: ")
            print("Comprobando...")
            sleep(2)
            existe_usuario(user)

        elif console == "list user":
            print(UserList.lista)

        elif console == "add user":
            user_add = input("Ingrese nuevo usuario: ")
            user_complete = "{}".format(user_add)
            archivo = open("usuarios.txt", "a")
            archivo.writelines(user_complete+"\n")
            archivo.close()
            add_password = getpass("Ingrese la password: ")
            main_py = open("main.py", "a")
            my_user_new = ("""
#{0}
if args.login == "{1}":
    try_pass("{2}", "{3}")
    print("Ingresaste como {4}")
    console("{5}")
""".format(user_add, user_add, add_password, user_add, user_add, user_add.upper()))
            main_py.writelines(my_user_new)
            main_py.close()
            print("\t[!] Creando usuario...")
            sleep(3)
            print("[!] Se ha creado el nuevo usuario")
            UserList.lista.extend(user_complete)

        elif console == "help":
            print_help = """
            exit/quit/salir     Cierra el programa
            clear               Limpia la terminal
            whoami              Imprime el usuario que se esta utilizando
            ireal               Dice si un usuario existe
            list user           lista a los usuarios existentes
            add user            agregar nuevo usuario(solo disponible para el admin)
            """
            print(print_help)

        else:
            print("[!] Comando no reconocido\n")

def console(name):
    #poc( Prueba de concepto )
    # Pepito_inventario.txt
    # open(name+"_inventario.txt", "a")

    # open("Admin_inventario.txt", "a")

    while True:
        #PEPITO>> 
        prompt = name+">> "
        console = str(input(prompt))

        if console == "exit" or console == "quit" or console == "salir":
            sys.exit(0)
        
        elif console == "whoami":
            print(name)

        elif console == "clear":
            system("cls")# Limpieza de terminal

        elif console == "help":
            print_help = """
            exit/quit/salir     Cierra el programa
            clear               Limpia la terminal
            whoami              Imprime el usuario que se esta utilizando
            buycompany          Comprar o listar las compras del usuario
            """
            print(print_help)

        elif console == "buycompany":
            #va todo lo que estan haciendo ustedes
            Inventario(name)

        else:
            print("[!] Comando no reconocido\n")