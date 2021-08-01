import os
import time
print("\nInstalando requerimientos...\n")
os.system("apt install python3 -y")
os.system("python3 -m pip install -r requirements.txt")
os.system("chmod 777 osfy.py")
print("\n\n¡Instalacion completada!")
time.sleep(2)
print("\ngrese en su terminal: 'python3 osfy.py' para continuar...")
print("\nOh se lo haremos automaticamente, solo ponga si quiere o no:")
time.sleep(1)
peticion = input("Desea abrir automaticamente el script? (yes/no) #>>> ")
if peticion=="yes" or peticion=="y":
	time.sleep(1)
	print("\nOkey abriendo...")
	os.system("python3 osfy.py")
	exit()
elif peticion=="no" or peticion=="n":
	time.sleep(1)
	print("\n¡Okey, adios!\n")
	exit()
else:
	print("\nOpción Incorrecta, vuelva a ejecutar el script.\n")
	time.sleep(1)
	exit()