#Esta es la funcion recursiva para las password
from time import *
from sys import exit
import getpass, sys, signal
from time import localtime, asctime

#Opcion para apretar ctrl_c
def def_handler(sig, frame):
    print("\n\n[!]Saliendo...")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def try_pass(password, usuario, intentos = 3):
    if intentos > 0:#si intentos en mayor que 0
        print("\nIntentos disponibles: {0}".format(intentos))
        entrada_pass = getpass.getpass("Password: ") #aqui ingresamos cantidad de intentos
        print("Comprobando....")
        sleep(3)
        if entrada_pass == password:
            print("Password correcta")
            archivos = open("logs/log.txt", "a")
            archivos.writelines("Intento de ingreso correcto: {0} : {1}\n".format(asctime(localtime()), usuario))
            archivos.close()
        else:
            print("Password incorrecta")
            return try_pass(password, usuario, intentos - 1)
    else:
        print("\n\t[!]Intentos fallidos, se registrara en los logs")
        archivos = open("logs/log.txt", "a")
        archivos.writelines("[!] Intento de ingreso incorrecto: {0} : {1}\n".format(asctime(localtime()), usuario))
        archivos.close()
        exit(1)