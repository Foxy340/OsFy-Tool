import os
import time
print("\nInstalando requerimientos...\n")
os.system("apt install python3 -y")
os.system("python3 -m pip install -r requirements.txt")
os.system("chmod 777 osfy.py")
from colorama import init, Fore
GREEN = Fore.GREEN
RED = Fore.RED
RESET = Fore.WHITE
print(Fore.GREEN+"\n\n¡Instalacion completada!")
time.sleep(2)
print(f"\n{GREEN}Ingrese en su terminal: '{RED}python3 osfy.py{GREEN}' para continuar...")
print(GREEN+"\nOh se lo haremos automaticamente, solo ponga si quiere o no:")
time.sleep(1)
peticion = input("Desea abrir automaticamente el script? (yes/no) #>>> ")
if peticion=="yes" or peticion=="y":
	time.sleep(1)
	print(GREEN+"\nOkey abriendo...")
	os.system("python3 osfy.py")
	exit()
elif peticion=="no" or peticion=="n":
	time.sleep(1)
	print(GREEN+"\n¡Okey, adios!\n")
	exit()
else:
	print(f"\n{RED}Opción Incorrecta, {GREEN}vuelva a ejecutar el script.\n")
	time.sleep(1)
	exit()

	
