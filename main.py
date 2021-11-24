#Carga principal, este ejecuta todo lo demas
import argparse, sys, signal
from InterAdmin import console, console_admin
from logins import try_pass
import UserList

UserList.lista
UserList.userlist()

#Opcion para apretar ctrl_c
def def_handler(sig, frame):
    print("\n\n[!]Saliendo...")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

parser = argparse.ArgumentParser(description="Opciones para el sistema de gestion de compras")
parser.version = 'Beta 1.0'
parser.add_argument('--version', action='version')
parser.add_argument(
                    '-l', '--login',
                    type=str,
                    choices = UserList.lista,
                    help="Ingresa usuario a logear",
)

args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Aqui van los login de los usuarios

#Administrador
if args.login == "Administrador":
    try_pass("admin123", "Administrador")
    print("+++++++++++++++++Bienvenido administrador+++++++++++++++++")
    console_admin()

#Pepito
if args.login == "Pepito":
    try_pass("123", "Pepito")
    print("Ingresaste como Pepito")
    console("PEPITO")
