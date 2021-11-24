# Consola interactiva del usuario administrador
import sys
from os import system
from sys import argv
from time import sleep
from UserList import existe_usuario
import UserList
from getpass import getpass

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

        else:
            print("[!] Comando no reconocido\n")

def console(name):
    while True:
        prompt = name+">> "
        console = str(input(prompt))

        if console == "exit" or console == "quit" or console == "salir":
            sys.exit(0)
        
        elif console == "whoami":
            print(name)

        elif console == "clear":
            system("cls")# Limpieza de terminal

        elif console == "buycompany":
            #va todo lo que estan haciendo ustedes
            pass

        else:
            print("[!] Comando no reconocido\n")