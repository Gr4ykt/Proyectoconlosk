from os import close
from time import *
from sys import exit
from time import localtime, asctime

#abrir archivos //// archivos = open("Inventariocompras.txt", "w")
#escribir /// archivos.write("hola mundo\n")


def Inventario(name):
    
    nombre_archivo = "inventarios/Inventario_{}.txt".format(name)
    validacion = int(input("1. Comprar productos\n2. Inventario de compras\n3. Salir: \n{0}>>> ".format(name)))

    if (validacion == 1):
        print ("introduzca el producto a agregar: ")
        producto = str(input(" \n >>> "))
        archivos = open(nombre_archivo, "a")
        archivos.write("producto: {}".format(producto))
        
        print("Ingrese cantidad de productos :")
        cantidadproductos = str(input(">>> "))
        archivos.writelines("   ///   cantidad: {}    ///    {}\n".format(cantidadproductos, asctime(localtime())))
        archivos.close()


        archivo_admin = open("inventarios/Admin_inventario.txt", "a")
        archivo_admin.writelines("{}:{}:{}:{} \n".format(name, producto, cantidadproductos, asctime(localtime())))
        archivo_admin.close()

        return Inventario(name)

    if (validacion == 2):

        archivo2 = open(nombre_archivo, "r")
        print(archivo2.readlines())
        archivo2.close()

        return Inventario(name)

    else:
        close