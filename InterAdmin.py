# Consola interactiva del usuario administrador
import sys
from os import system
from sys import argv
from time import sleep
from UserList import existe_usuario
import UserList

def console_admin():
    while True:
        console = str(input("ADMIN>> "))
        if console == "exit" or console == "quit" or console == "salir":
            sys.exit(0)

        elif console == "clear":
            system("cls")# Limpieza de terminal

        elif console == "ireal":
            user = input("Nombre del usuario: ")
            print("Comprobando...")
            sleep(2)
            existe_usuario(user)

        elif console == "list user":
            print(UserList.lista)

        elif console == "add user":
            user_add = input("Ingrese nuevo usuario: ")
            user_complete = "{}\n".format(user_add)
            archivo = open("usuarios.txt", "a")
            archivo.writelines(user_complete)
            archivo.close()

        else:
            print("[!] Comando no reconocido\n")
