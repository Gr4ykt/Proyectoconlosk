#Esta es la funcion recursiva para las password
from time import *
from sys import exit
import getpass
from time import localtime, asctime

def try_pass(password, intentos = 3):
    if intentos > 0:#si intentos en mayor que 0
        print("\nIntentos disponibles: {0}".format(intentos))
        entrada_pass = getpass.getpass("Password: ") #aqui ingresamos cantidad de intentos
        print("Comprobando....")
        sleep(3)
        if entrada_pass == password:
            print("Password correcta")
            archivos = open("logs/log_password.txt", "a")
            archivos.writelines("Intento de ingreso correcto: {0} : {1}\n".format(asctime(localtime()), entrada_pass))
            archivos.close()
        else:
            print("Password incorrecta")
            return try_pass(password, intentos - 1)
    else:
        print("\n\t[!]Intentos fallidos, se registrara en los logs")
        exit(1)