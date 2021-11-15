lista = []

def userlist():
    usuarios = open("usuarios.txt", 'r+')
    for linea in usuarios:
        lista.extend(linea.split())

def lista_usuarios():
    return lista          

def existe_usuario(usuario):
    for i in lista:
        if i == usuario:
            print("[*] existe el usuario", i)