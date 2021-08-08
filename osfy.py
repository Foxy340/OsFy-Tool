
try:
        import os
        import time
        import platform
        import webbrowser as web
        from colorama import init, Fore
except ModuleNotFoundError:
        print("Requerimientos no instalados, por favor ingrese en su terminal: 'python3 install.py' ")
init(autoreset=True)
YELLOW = Fore.YELLOW
RED = Fore.RED
CYAN = Fore.CYAN
BLUE = Fore.BLUE
RESET = Fore.WHITE
GREEN = Fore.GREEN
PURPLE = Fore.MAGENTA
banner = RED+'''
▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒
▒▒█▒▒▒▄██████████▄▒▒▒▒
▒█▐▒▒▒████████████▒▒▒▒
▒▌▐▒▒██▄▀██████▀▄██▒▒▒
▐┼▐▒▒██▄▄▄▄██▄▄▄▄██▒▒▒
▐┼▐▒▒██████████████▒▒▒
▐▄▐████─▀▐▐▀█─█─▌▐██▄▒
▒▒█████──────────▐███▌
▒▒█▀▀██▄█─▄───▐─▄███▀▒
▒▒█▒▒███████▄██████▒▒▒
▒▒▒▒▒██████████████▒▒▒
▒▒▒▒▒█████████▐▌██▌▒▒▒
▒▒▒▒▒▐▀▐▒▌▀█▀▒▐▒█▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▌▒▒▒▒▒

'''
def clear():
        if platform.system() == "Windows":
                os.system("cls")
        else:
                os.system("clear")
def menu():
        clear()
        print(f"\n\n{YELLOW}========================")
        print(banner)
        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
        print(f"{YELLOW}\n========================\n")
        print(f"\t{BLUE}--{GREEN}CATEGÓRIAS{BLUE}--\n")
        print(f"{BLUE}[ {PURPLE}1 {BLUE}] {RESET}- {CYAN}Phishing")
        print(f"{BLUE}[ {PURPLE}2 {BLUE}] {RESET}- {CYAN}Attack Ddos")
        print(f"{BLUE}[ {PURPLE}3 {BLUE}] {RESET}- {CYAN}OSINT")
        print(f"{BLUE}[ {PURPLE}4 {BLUE}] {RESET}- {CYAN}Lenguajes de programación(Install)")
        print(f"{BLUE}[ {PURPLE}5 {BLUE}] {RESET}- {CYAN}Vulnerability Scanners")
        print(f"{BLUE}[ {PURPLE}6 {BLUE}] {RESET}- {CYAN}Brute Force")
        print(f"{BLUE}[ {PURPLE}7 {BLUE}] {RESET}- {CYAN}Instalar paquetes({RED}100MB{GREEN})")
        print(f"{BLUE}[ {PURPLE}X {BLUE}] {RESET}- {CYAN}Volver\n")
        m1 = input("Ingrese una opción #>>> ")
        if m1=="1":
                opcion1()
        elif m1=="x" or m1=="X":
                time.sleep(1)
                clear()
                print(f"\n\n{YELLOW}========================")
                print(banner)
                print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                print(f"\n{YELLOW}========================\n")
                print(GREEN+"Volviendo...")
                time.sleep(2)
        elif m1=="2":
                opcion2()

        elif m1=="3":
                opcion3()
        elif m1=="4":
                opcion4()
        elif m1=="5":
                opcion5()
        elif m1=="6":
                opcion6()
        elif m1=="7":
                opcion7()
        else:
                clear()
                print(f"\n\n{YELLOW}========================")
                print(banner)
                print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                print(f"\n\n{YELLOW}========================\n")
                print(RED+"Opción invalida...\n")
                time.sleep(1)
                print(GREEN+"Volviendo...")
                time.sleep(6)
def opcion1():
        while True:
                time.sleep(1)
                clear()
                print(f"\n\n{YELLOW}========================")
                print(banner)
                print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                print(f"\n{YELLOW}========================\n")
                print(f"{GREEN}Herramientas de '{RED}Phishing{GREEN}'{RESET}:\n")
                print(f"{BLUE}[ {PURPLE}1 {BLUE}] {RESET}- {CYAN}AIOPhish")
                print(f"{BLUE}[ {PURPLE}2 {BLUE}] {RESET}- {CYAN}SocialSploit")
                print(f"{BLUE}[ {PURPLE}3 {BLUE}] {RESET}- {CYAN}Predator-Phishing")
                print(f"{BLUE}[ {PURPLE}4 {BLUE}] {RESET}- {CYAN}Zphisher")
                print(f"{BLUE}[ {PURPLE}5 {BLUE}] {RESET}- {CYAN}Dark-Phish")
                print(f"{BLUE}[ {PURPLE}X {BLUE}] {RESET}- {CYAN}Volver\n")
                time.sleep(1)
                p1 = input("Ingrese una opción #>>> ")
                if p1=="1":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(RESET+'''Herramienta: "AIOPhish"
Cómo su nombre lo indica es una herramienta de Phising, que nos permite editarla a nuestro gusto para agregarle creibilidad.

COMANDOS TERMUX

apt install git -y

git clone https://github.com/DeepSociety/AIOPhish

cd AIOPhish

bash install-termux.sh

bash aiophish.sh

Autor del Script: "DeepSociety"''')
                        print("\n")
                        time.sleep(10)
                        print(GREEN+"Instalando...\n")
                        os.system("git clone https://github.com/Cesar-Hack-Gray/SocialSploit")
                        time.sleep(1)
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"¡Instalacion completada!")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(2)
                elif p1=="2":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(RESET+'''Herramienta: "SocialSploit"
SocialSploit es un framework de phishing que nos ayuda a hackear con ngrok y serveo, se trata de ingeniería social.

COMANDOS TERMUX

 apt install git -y

 git clone https://github.com/Cesar-Hack-Gray/SocialSploit

 cd SocialSploit

 ls

 bash install.sh

 ./Sploit

Autor del Script: "Cesar Hack Gray"''')
                        print("\n")
                        time.sleep(10)
                        print(GREEN+"Instalando...\n")
                        os.system("git clone https://github.com/Cesar-Hack-Gray/SocialSploit")
                        time.sleep(1)
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"¡Instalacion completada!")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(2)
                elif p1=="3":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(RESET+'''Herramienta: "Predator-Phising"
Herramienta profesional.
Phishing con más de 40 plantillas.
Funcionalidad: Todas pueden subirlas a un hosting.
Port forwarding: localhost.run/serveo/ngrok, pueden elegir el puerto que quieran.
Personalización: Pueden insertar títulos, fotos, descripciones, mini url y redireccionar a la víctima, además soporta Telegram.
Cóctel thelinuxchoice: Combinación de scripts de IP, cámara y ubicación en una sola página.
Email Spoofing: 3 plantillas HTML personalizables para enviar desde esta tool o con SET.
Idioma: Todas las plantillas en español.

COMANDOS TERMUX

apt install git -y

git clone https://github.com/tony23x/Predator-Phish.git

cd Predator-Phish

bash install.sh

bash predator-phish.sh

Autor del Script "tony23x"''')
                        time.sleep(10)
                        print(GREEN+"\nInstalando...\n")
                        os.system("git clone https://github.com/tony23x/Predator-Phish.git")
                        time.sleep(1)
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"¡Instalacion completada!")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(2)
                elif p1=="4":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(RESET+'''Herramienta: "zphisher"
Herramienta más usada en Phising
Páginas de inicio de sesión más recientes y actualizadas.
Soporte de URL de máscara
Amigable para principiantes.
Varias opciones de tunelización Localhost Ngrok (con o sin hotspot)

COMANDOS TERMUX

apt install git -y

git clone https//github.com/htr-tech/zphisher.git

cd zphisher

bash zphisher.sh

zphisher.sh

Autor del Script: "htr-tech" ''')
                        time.sleep(10)
                        print(GREEN+"\nInstalando...\n")
                        os.system("git clone https://github.com/htr-tech/zphisher")
                        time.sleep(1)
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"¡Instalacion completada!")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(2)
                elif p1=="5":
                        clear()
                        print(f"\n\n========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n========================\n")
                        print('''Herramienta: "Dark-Phish"
Está herramienta de Phising es una herramienta muy buena ya que cuenta con 29 páginas de Phising y un customizador.

COMANDOS TERMUX

apt install python3

apt install curl

apt install php

apt install git -y

git clone https://github.com/Cyber-Anonymous/Dark-Phish.git

pip3 install requests

pip3 install wget

cd Dark-Phish

python3 dark-phish.py

Autor del Script: "Cyber-Anonymous"''')
                        time.sleep(10)
                        print(GREEN+"\nInstalando...\n")
                        os.system("git clone https://github.com/Cyber-Anonymous/Dark-Phish.git")
                        time.sleep(1)
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"¡Instalacion completada!")
                        time.sleep(2)
                        print(GREEN+"Volviendo...")
                        time.sleep(2)
                elif p1=="X" or p1=="x":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"Volviendo...")
                        time.sleep(2)
                        break
                else:
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(RED+"Opción invalida...\n")
                        time.sleep(1)
                        print(GREEN+"Volviendo...")
                        time.sleep(6)
def opcion2():
        while True:
                time.sleep(1)
                clear()
                print(f"\n\n{YELLOW}========================")
                print(banner)
                print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                print(f"\n{YELLOW}========================\n")
                print(f"{GREEN}Herramientas de '{RED}Ddos'{RESET}:\n")
                print(f"{BLUE}[ {PURPLE}1 {BLUE}] {RESET}- {CYAN}Hammer")
                print(f"{BLUE}[ {PURPLE}2 {BLUE}] {RESET}- {CYAN}LiteDdos")
                print(f"{BLUE}[ {PURPLE}3 {BLUE}] {RESET}- {CYAN}Planetwork-Ddos")
                print(f"{BLUE}[ {PURPLE}4 {BLUE}] {RESET}- {CYAN}Hulk")
                print(f"{BLUE}[ {PURPLE}5 {BLUE}] {RESET}- {CYAN}SlowLoris")
                print(f"{BLUE}[ {PURPLE}X {BLUE}] {RESET}- {CYAN}Volver\n")
                p2 = input("Ingrese una opción #>>> ")
                if p2=="1":
                        time.sleep(1)
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(RESET+'''Herramienta: "Hammer"
Herramienta de ddos muy usada.
Hammer necesita la IP del sitio web que desea atacar.
Para obtener la IP del sitio web simplemente
 escriba
nmap ejemplo.com
Anote la dirección IP de ese sitio web.
Y inicie el ataque ddos

COMANDOS TERMUX

apt install python

apt install git -y

apt install dnsutils

git clone https://github.com/rk1342k/Hammer

cd Hammer

python hammer.py -s [ip a atacar] -t 135

ejemplo:

python hammer.py -s 123.45.67.89 -t 135

Autor del Script: "rk1342k"''')
                        time.sleep(10)
                        print(GREEN+"\nInstalando...")
                        os.system("git clone https://github.com/rk1342k/Hammer")
                        time.sleep(1)
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"¡Instalacion completada!")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(6)
                elif p2=="2":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n\n{YELLOW}========================\n")
                        print(RESET+'''Herramienta: "LITEDDOS"
Es una de las usadas.
Esta herramienta es compatible con actividades DDOS, la forma de ejecutar es escribiendo los siguientes comandos: $ python2 islddos.py <ip> <puerto> <paquete> ejemplo: $ python2 islddos.py 104.27.190.77 8080100 IP objetivo: 104.27.190.77 puerto: 8080 paquete : 100 Hecho en indonesia Indonesia Security Lite

COMANDOS TERMUX

apt install python2 -y

apt install git -y

apt install dnsutils

git clone https://github.com/4L13199/LITEDDOS

cd LITEDDOS

python2 LITEDDOS.py <IP> <puerto> <paquetes>

ejemplo

python2 LITEDDOS.py 123.45.67.80 80 150

Autor del Script: "4L13199"''')
                        time.sleep(10)
                        print(GREEN+"\nInstalando...\n")
                        os.system("git clone https://github.com/4L13199/LITEDDOS")
                        time.sleep(1)
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"¡Instalacion completada!")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(6)
                elif p2=="3":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(RESET+'''Herramienta: "Planetwork-DDOS"
Herramienta de DDOS muy usada.
Esta herramienta tiene una velocidad increíble para poder hacer DDOS, envía 4200 solicitudes de paquetes en 3 segundos. Es una de las mejores herramientas de ddos que eh probado.

COMANDOS TERMUX

apt install python2 -y

apt install git -y

apt install dnsutils

git clone https://github.com/Hydra7/Planetwork-DDOS

cd Planetwork-DDOS

python2 pntddos.py <IP> <puerto> <paquetes>

ejemplo

python2 pntddos.py 123.45.67.80 80 150

Autor del Script: "Hydra7"''')
                        time.sleep(10)
                        print(GREEN+"\nInstalando...\n")
                        os.system("git clone https://github.com/Hydra7/Planetwork-DDOS")
                        time.sleep(1)
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"¡Instalacion completada!")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(6)
                elif p2=="4":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(RESET+'''Herramienta: "Hulk"
Esta herramienta está destinada a las pruebas de estrés y puede que realmente caiga el servidor mal configurado o la aplicación mal hecha. Úselo con cuidado.

COMANDOS TERMUX

apt install git -y

apt install python2 -y

git clone https://github.com/grafov/hulk

cd hulk

chmod +x *

python2 hulk.py ejemplo.com

Autor del Script: "grafov"''')
                        time.sleep(10)
                        print(GREEN+"\nInstalando...")
                        os.system("git clone https://github.com/grafov/hulk")
                        time.sleep(1)
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"¡Instalacion completada!")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(2)

                elif p2=="5":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(RESET+'''Herramienta: "Slowloris"
Slowloris es básicamente un ataque de denegación de servicio HTTP que afecta a los servidores con subprocesos. Funciona así:

Comenzamos a hacer muchas solicitudes HTTP.
Enviamos encabezados periódicamente (cada ~ 15 segundos) para mantener abiertas las conexiones.
Nunca cerramos la conexión a menos que el servidor lo haga. Si el servidor cierra una conexión, creamos una nueva y seguimos haciendo lo mismo.
Esto agota el grupo de subprocesos de los servidores y el servidor no puede responder a otras personas.

COMANDOS TERMUX

apt install python3 -y

apt install git -y

git clone https://github.com/gkbrk/slowloris.git

cd slowloris

python3 slowloris.py ejemplo.com

Autor del Script: "gkbrk"''') 
                        time.sleep(10)
                        print(GREEN+"\nInstalando...")
                        os.system("git clone https://github.com/gkbrk/slowloris.git")
                        print(GREEN+"\n¡Instalacion completada!")
                        time.sleep(2)
                        time.sleep(1)
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"¡Instalacion completada!")
                        time.sleep(2)
                elif p2=="x" or p2=="X":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"Volviendo...")
                        time.sleep(2)
                        break
                else:
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(RED+"Opción invalida...\n")
                        time.sleep(1)
                        print(GREEN+"Volviendo...")
                        time.sleep(6)
def opcion3():
        while True:
                time.sleep(1)
                clear()
                print(f"\n\n{YELLOW}========================")
                print(banner)
                print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                print(f"\n{YELLOW}========================\n")
                print(f"{GREEN}Herramientas de '{RED}OSINT{GREEN}'{RESET}:\n")
                print(f"{BLUE}[ {PURPLE}1 {BLUE}] {RESET}- {CYAN}infork-beta")
                print(f"{BLUE}[ {PURPLE}2 {BLUE}] {RESET}- {CYAN}PhoneInfoga")
                print(f"{BLUE}[ {PURPLE}3 {BLUE}] {RESET}- {CYAN}Sherlock")
                print(f"{BLUE}[ {PURPLE}4 {BLUE}] {RESET}- {CYAN}DoxWeb")
                print(f"{BLUE}[ {PURPLE}5 {BLUE}] {RESET}- {CYAN}IP-TRACER")
                print(f"{BLUE}[ {PURPLE}X {BLUE}] {RESET}- {CYAN}Volver\n")
                d1 = input("Ingrese una opción #>>> ")
                if d1=="1":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(RESET+'''Herramienta: "Infork-beta"
Herramienta dedicada a la recopilacion de información, este scripts esta en su version BETA, hay cosas que agregar y que veran en la siguiente "actualización", es multiplataforma: (COMPUTADORAS Y CELULARES).

COMANDOS TERMUX

apt install git -y

apt install python -y

git clone https://github.com/triway340/infork-beta

cd infork-beta

python3 install.py

python3 infork-beta.py

Elegir opciones y completar datos.''')
                        time.sleep(10)
                        print(GREEN+"\nInstalando...")
                        os.system("git clone https://github.com/triway340/infork-beta")
                        time.sleep(1)
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"¡Instalacion completada!")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(2)
                elif d1=="2":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(RESET+'''Herramienta: "PhoneInfoga"
Está herramienta sirve para tener información de un número es mayormente utilizada para el Doxing.
Está herramienta brinda información como país, provincia,compañía, zona horaria. Del número que ingresaste 

COMANDOS TERMUX

apt install python -y

apt install python2 -y

pkg install pip

pkg install git -y

git clone https://github.com/abhinavkavuri/PhoneInfoga

cd PhoneInfoga

mv config.example.py config.py

python3 -m pip install -r requirements.txt

python3 phoneinfoga.py

python3 phoneinfoga.py -n (número)

Autor del Script: "abhinavkavuri"''')
                        time.sleep(10)
                        print(GREEN+"\nInstalando...")
                        os.system("git clone https://github.com/abhinavkavuri/PhoneInfoga")
                        time.sleep(1)
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"¡Instalacion completada!")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(2)
                elif d1=="3":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(RESET+'''Herramienta: "Sherlock"
Sherlock es una herramienta que nos facilita el trabajo de andar buscando los users de cada plataforma. Lo que hace este script es darnos los links de los users que busquemos.

COMANDOS TERMUX

apt install python3 -y

apt install git -y

git clone https://github.com/sherlock-project/sherlock.git

cd sherlock

python3 -m pip install -r requirements.txt

python3 sherlock username

Autor del Script: "sherlock-project"''')
                        time.sleep(10)
                        print(GREEN+"\nInstalando...")
                        os.system("git clone https://github.com/sherlock-project/sherlock.git")
                        time.sleep(1)
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"¡Instalacion completada!")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(2)
                elif d1=="5":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(RESET+'''Herramienta: "IP-Tracer"
IP-Tracer se utiliza para rastrear una dirección IP. IP-Tracer está desarrollado para sistemas basados ​​en Termux y Linux. Puede recuperar fácilmente la información de la dirección IP utilizando IP-Tracer. IP-Tracer usa ip-api para rastrear la dirección IP.

COMANDOS TERMUX

apt install git -y

git clone https://github.com/rajkumardusad/IP-Tracer.git

cd IP-Tracer

chmod +x install

sh install o ./install

Autor del Script: "rajkumardusad"''')
                        time.sleep(10)
                        print(GREEN+"\nInstalando...")
                        os.system("git clone https://github.com/rajkumardusad/IP-Tracer.git")
                        time.sleep(1)
                        clear()
                        print(f"\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n\n{YELLOW}========================\n")
                        print(GREEN+"¡Instalacion completada!")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(2)
                elif d1=="4":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(RESET+'''Herramienta: "DoxWeb"
Herramienta de Doxing que utiliza varios sitios web. Para poder obtener información privada de una persona.

COMANDOS TERMUX

apt install git -y

git clone https://github.com/Darkmux/DoxWeb

chmod 711 DoxWeb.sh

./DoxWeb.sh

Elegir opción y utilizar

Autor del Script: "Darkmux"''')
                        time.sleep(10)
                        print(GREEN+"\nInstalando...")
                        os.system("git clone https://github.com/Darkmux/DoxWeb")
                        time.sleep(1)
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"¡Instalacion completada!")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(2)
                elif d1=="X" or d1=="x":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"Volviendo...")
                        time.sleep(2)
                        break
                else:
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(RED+"Opcion invalida...\n")
                        time.sleep(1)
                        print(GREEN+"Volviendo...")
                        time.sleep(6)
def opcion4():
        while True:
                clear()
                print(f"\n\n{YELLOW}========================")
                print(banner)
                print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                print(f"\n{YELLOW}========================\n")
                print(f"{RESET}-{GREEN}Menú de: 'Lenguajes de programación {RED}({GREEN}Install{RED})'{RESET}:")
                print(f"{BLUE}[ {PURPLE}1 {BLUE}] {RESET}- {CYAN}Python ({RED}2{CYAN},{RED}3{CYAN})")
                print(f"{BLUE}[ {PURPLE}2 {BLUE}] {RESET}- {CYAN}Clang")
                print(f"{BLUE}[ {PURPLE}3 {BLUE}] {RESET}- {CYAN}Ruby")
                print(f"{BLUE}[ {PURPLE}4 {BLUE}] {RESET}- {CYAN}PHP")
                print(f"{BLUE}[ {PURPLE}5 {BLUE}] {RESET}- {CYAN}golang")
                print(f"{BLUE}[ {PURPLE}6 {BLUE}] {RESET}- {CYAN}perl ")
                print(f"{BLUE}[ {PURPLE}6 {BLUE}] {RESET}- {CYAN}c++")
                print(f"{BLUE}[ {PURPLE}7 {BLUE}] {RESET}- {CYAN}gcc")
                print(f"{BLUE}[ {PURPLE}X {BLUE}] {RESET}- {CYAN}Volver\n")
                l1 = input("Ingrese una opción #>>> ")
                if l1=="1":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n========================\n")
                        print(f"{GREEN}Instalando: '{RED}Python2{GREEN}'\n")
                        os.system("apt install python2 -y")
                        time.sleep(4)
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n========================\n")
                        print(f"{GREEN}Instalando: '{RED}Python3{GREEN}'\n")
                        os.system("apt install python3 -y")
                        time.sleep(2)
                        print(GREEN+"\nVoliendo...")
                        time.sleep(2)
                elif l1=="2":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(f"{GREEN}Instalando: '{RED}Clang{GREEN}'\n")
                        os.system("apt install clang -y")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(2)
                elif l1=="3":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(f"{GREEN}Instalando: '{RED}Ruby{GREEN}'\n")
                        os.system("apt install ruby -y")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(2)
                elif l1=="4":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(f"{GREEN}Instalando: '{RED}PHP{GREEN}'\n")
                        os.system("apt install php -y")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(2)
                elif l1=="5":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(f"{GREEN}Instalando: '{RED}golang{GREEN}'\n")
                        os.system("apt install golang -y")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(2)
                elif l1=="6":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(f"{GREEN}Instalando: '{RED}perl{GREEN}'\n")
                        os.system("apt install perl -y")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(2)
                elif l1=="7":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(f"{GREEN}Instalando: '{RED}gcc{GREEN}'\n")
                        os.system("apt install gcc -y")
                        time.sleep(2)
                        print(GREEN+"Volviendo...")
                        time.sleep(2)
                elif l1=="x" or l1=="X":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"Volviendo...")
                        time.sleep(2)
                        break
                else:
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(RED+"Opcion invalida...\n")
                        time.sleep(1)
                        print(GREEN+"Volviendo...")
                        time.sleep(6)
def opcion5():
        while True:
                clear()
                print(f"\n\n{YELLOW}========================")
                print(banner)
                print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                print(f"\n{YELLOW}========================\n")
                print(f"{RESET}-{GREEN}Menú de: '{RED}Vulnerability Scanners{GREEN}'{RESET}:\n")

                print(f"{BLUE}[ {PURPLE}1 {BLUE}] {RESET}- {CYAN}Golismero")
                print(f"{BLUE}[ {PURPLE}2 {BLUE}] {RESET}- {CYAN}NMAP")
                print(f"{BLUE}[ {PURPLE}3 {BLUE}] {RESET}- {CYAN}Xshell")
                print(f"{BLUE}[ {PURPLE}4 {BLUE}] {RESET}- {CYAN}sqlmap")
                print(f"{BLUE}[ {PURPLE}5 {BLUE}] {RESET}- {CYAN}D-TECT")
                print(f"{BLUE}[ {PURPLE}X {BLUE}] {RESET}- {CYAN}Volver\n")

                v1 = input("Ingrese una opción #>>> ")


                if v1=="1":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(RESET+'''Herramienta: "Golismero"
GoLismero es un marco de código abierto para pruebas de seguridad. Actualmente está orientado a la seguridad web, pero se puede expandir fácilmente a otros tipos de análisis.

COMANDOS TERMUX

apt install python2 -y

pkg install git -y

git clone https://github.com/golismero/golismero

cd golismero

pip install -r requirements.txt

pip install -r requirements_unix.txt

python2 golismero.py y completar con los demás datos.

Autor del Script: "golismero"
''')
                        time.sleep(10)
                        print(GREEN+"\nInstalando...")
                        os.system("git clone https://github.com/golismero/golismero")
                        time.sleep(1)
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"¡Instalacion completada!")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(2)

                elif v1=="2":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print('''Herramienta: "NMAP"
nmap es un programa que sirve para rastrear vulnerabilidades, cómo puertos abiertos y ip de la página web.

COMANDOS TERMUX

pkg install nmap -y

nmap ejemplo.com''')
                        time.sleep(10)
                        print(GREEN+"\nInstalando...")
                        os.system("pkg install nmap -y")
                        time.sleep(1)
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"¡Instalacion completada!")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(2)

                elif v1=="3":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print('''Herramienta: "Xshell"
XShell es una herramienta para encontrar vulnerabilidades.

COMANDOS TERMUX

git clone https://github.com/Manisso/Xshell

cd Xshell

sudo bash install.sh

Autor del Script: "Manisso" ''')
                        time.sleep(10)
                        print(GREEN+"\nInstalando...")
                        os.system("git clone https://github.com/Manisso/Xshell")
                        time.sleep(1)
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"¡Instalacion completada!")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(2)

                elif v1=="4":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print('''Herramienta: "sqlmap"
sqlmap es una herramienta de prueba de penetración de código abierto que automatiza el proceso de detección y explotación de fallas de inyección SQL y la toma de control de los servidores de bases de datos. Viene con un potente motor de detección, muchas funciones de nicho para el mejor probador de penetración y una amplia gama de conmutadores que incluyen huellas dactilares de la base de datos, obtención de datos de la base de datos, acceso al sistema de archivos subyacente y ejecución de comandos en el sistema operativo a través de conexiones de banda.

COMANDOS TERMUX

apt install python -y

apt install git -y

git clone https://github.com/sqlmapproject/sqlmap

cd sqlmap

python sqlmap.py

Y usar las opciones que nos indican.

Autor del Script: "sqlmapproject"
''')
                        time.sleep(10)
                        print(GREEN+"\nInstalando...")
                        os.system("git clone https://github.com/sqlmapproject/sqlmap")
                        time.sleep(1)
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"¡Instalacion completada!")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(2)
                elif v1=="5":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print('''Herramienta: "D-TECT"
D-TECT es una herramienta todo en uno para pruebas de penetración. Esto está especialmente programado para probadores de penetración e investigadores de seguridad para facilitar su trabajo, en lugar de lanzar diferentes herramientas para realizar diferentes tareas. D-TECT proporciona múltiples funciones y funciones de detección que recopilan información del objetivo y encuentran diferentes fallas en ella.

COMANDOS TERMUX

apt install python -y

apt install git -y

git clone https://github.com/shawarkhanethicalhacker/D-TECT-1

cd D-TECT-1

python d-tect.py

Autor del Script: "shawarkhanethicalhacker"
''')
                        time.sleep(10)
                        print(GREEN+"\nInstalando...")
                        os.system("git clone https://github.com/sqlmapproject/sqlmap")
                        time.sleep(1)
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"¡Instalacion completada!")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(2)

                elif v1=="x" or v1=="X":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"Volviendo...")
                        time.sleep(2)
                        break
                else:
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(RED+"Opcion invalida...\n")
                        time.sleep(1)
                        print(GREEN+"Volviendo...")
                        time.sleep(6)
def opcion6():
        while True:
                clear()
                print(f"\n\n{YELLOW}========================")
                print(banner)
                print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                print(f"\n{YELLOW}========================\n")
                print(f"{RESET}-{GREEN}Menú de: '{RED}Brute Force{GREEN}'{RESET}:\n")
                print(f"{BLUE}[ {PURPLE}1 {BLUE}] {RESET}- {CYAN}John The Ripper")
                print(f"{BLUE}[ {PURPLE}2 {BLUE}] {RESET}- {CYAN}BruteX")
                print(f"{BLUE}[ {PURPLE}3 {BLUE}] {RESET}- {CYAN}Facebook-BruteForce")
                print(f"{BLUE}[ {PURPLE}4 {BLUE}] {RESET}- {CYAN}Bruter19")
                print(f"{BLUE}[ {PURPLE}5 {BLUE}] {RESET}- {CYAN}Brute-Force-Instagram-2021")
                print(f"{BLUE}[ {PURPLE}X {BLUE}] {RESET}- {CYAN}Volver\n")

                b1 = input("Ingrese una opción #>>>> ")


                if b1=="1":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")

                        print('''Herramienta: "John The Ripper"
Esta es la versión "jumbo" mejorada por la comunidad de John the Ripper. Tiene una gran cantidad de código, documentación y datos aportados por los desarrolladores gigantes y la comunidad de usuarios. Es fácil agregar código nuevo a jumbo y los requisitos de calidad son bajos, aunque últimamente hemos comenzado a someter todas las contribuciones a pruebas bastante automatizadas. Esto significa que obtiene una gran cantidad de funciones que no son necesariamente "maduras", lo que a su vez significa que se esperan errores en este código.

COMANDOS TERMUX

apt install git -y

git clone https://github.com/openwall/john

cd john

cd usr

Y ya estaria.

Autor del Script: "openwall" ''')
                        time.sleep(10)
                        print(GREEN+"\nInstalando...")
                        os.system("git clone https://github.com/openwall/john")
                        time.sleep(1)
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"¡Instalacion completada!")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(2)

                elif b1=="2":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")

                        print('''Herramienta: "BruteX"
Fuerza bruta automáticamente todos los servicios que se ejecutan en un objetivo.

COMANDOS TERMUX

apt install git 

git clone https://github.com/1N3/BruteX

cd BruteX

./install.sh

Y disfrutar del Fuerza Bruta

Autor del Script: "1N3"''')
                        time.sleep(10)
                        print(GREEN+"\nInstalando...")
                        os.system("git clone https://github.com/1N3/BruteX")
                        time.sleep(1)
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"¡Instalacion completada!")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(2)

                elif b1=="3":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")

                        print('''Herramienta: "Facebook-BruteForce"
Ataque de fuerza bruta para la cuenta de Facebook

COMANDOS TERMUX

apt install git -y

apt install python -y

git clone https://github.com/IAmBlackHacker/Facebook-BruteForce

cd Facebook-BruteForce
 
python3 -m pip install requests bs4

python3 -m pip install mechanize

python3 fb.py or python fb2.py

Autor del Script: "IAmBlackHacker"''')
                        time.sleep(10)
                        print(GREEN+"\nInstalando...")
                        os.system("git clone  https://github.com/IAmBlackHacker/Facebook-BruteForce")
                        time.sleep(1)
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"¡Instalacion completada!")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(2)
                elif b1=="4":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print('''Herramienta: "Bruter19"
Esta herramienta ha sido desarrollada para que los estudiantes de pirateria informática.

COMANDOS

apt install git -y

apt install python3 -y

git clone https://github.com/AzizKpln/Bruter19

cd Bruter19

chmod +x setup.sh

./setup.sh

python3 bruter19.py''')

                        time.sleep(10)
                        print(GREEN+"\nInstalando...")
                        os.system("git clone https://github.com/AzizKpln/Bruter19")
                        time.sleep(1)
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"¡Instalacion completada!")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(2)
                elif b1=="5":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print('''Herramienta: "Brute-Force-Instagram-2021"
Fuerza bruta de Instagram trabajando en nuevo formato 2021, proxy agregado ^ - ^, código abierto, puede modificarlo.

COMANDOS TERMUX

apt install git -y

apt install python3 -y

git clone https://github.com/0xfff0800/Brute-force-Instagram-2021

pip3 install colorama

cd Brute-force-Instagram-2021

python3 insTof6.py

Autor del Script: "0xfff0800"''')

                        time.sleep(10)
                        print(GREEN+"\nInstalando...")
                        os.system("git clone https://github.com/0xfff0800/Brute-force-Instagram-2021")
                        time.sleep(1)
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"¡Instalacion completada!")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(2)
                elif b1=="x" or b1=="X":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"Volviendo...")
                        time.sleep(2)
                        break
                else:
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(RED+"Opcion invalida...\n")
                        time.sleep(1)
                        print(GREEN+"Volviendo...")
                        time.sleep(6)
def downloads():
        try:
                os.system("apt update")
                os.system("pkg install mc ")
                os.system("pkg install python2 -y")
                os.system("pkg install ruby -y")
                os.system("pkg install cmatrix -y")
                os.system("pkg install nano -y")
                os.system("pkg install php -y")
                os.system("pkg install wget -y")
                os.system("pkg install curl -y")
                os.system("pkg install  weechat-python-plugin -y")
                os.system("pkg install irssi -y")
                os.system("pkg install root-repo ")
                os.system("pkg install x11-repo ")
                os.system("pkg install cat -y")
                os.system("pkg install unstable-repo")
                os.system("pkg update ")
                os.system("nmap -y")
                os.system("pkg install openssh -y")
        except KeyboardInterrupt:
                clear()
                print(f"\n\n{YELLOW}========================")
                print(banner)
                print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                print(f"\n{YELLOW}========================\n")
                print(f"{GREEN}Has salido. {GREEN}Volviendo...")
                time.sleep(5)
def opcion7():
        while True:
                clear()
                print(f"\n\n{YELLOW}========================")
                print(banner)
                print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                print(f"\n{YELLOW}========================\n")
                print(f"{GREEN}Estas apunto de instalar mas de {RED}100mb {GREEN}de paquetes.\nPara continuar escriba {CYAN}(yes/no).")
                print(f"{BLUE}[ {PURPLE}X {BLUE}] {RESET}- {CYAN}Volver\n")
                u1 = input("Ingrese una opción #>>> ")

                if u1=="yes" or u1=="y":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"Okey instalando...\n\n")
                        downloads()
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"¡Instalacion completada!")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(2)
                elif u1=="no" or u1=="n":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(f"{GREEN}Okey {RED}NO {GREEN}se instalaran.")
                        time.sleep(2)
                        print(GREEN+"\nVolviendo...")
                        time.sleep(2)
                        break
                elif u1=="x" or u1=="X":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"Volviendo...")
                        time.sleep(2)
                        break
                else:
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(RED+"Opcion invalida...\n")
                        time.sleep(1)
                        print(GREEN+"Volviendo...")
                        time.sleep(6)
def contactos():
        while True:
                clear()
                print(f"\n\n{GREEN}========================")
                print(banner)
                print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                print(f"\n{GREEN}========================\n")
                print(f"{GREEN}Autores de esta tool: {RED}Osay y Foxy\n")
                print(f"{BLUE}[ {PURPLE}1 {BLUE}] {RESET}- {CYAN}Contactos de Osay")
                time.sleep(1)
                print(f"{BLUE}[ {PURPLE}2 {BLUE}] {RESET}- {CYAN}Contactos de Foxy")
                time.sleep(1)
                print(f"{BLUE}[ {PURPLE}X {BLUE}] {RESET}- {CYAN}Volver\n")
                c1 = input("Ingrese una opción #>>> ")
                if c1=="1":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(f"{GREEN}Telegram: {RESET}https://t.me/triway340")
                        time.sleep(1)
                        print(f"{GREEN}WhatsApp: {RESET}https://tiktok.com/@triwaytri")
                        time.sleep(1)
                        print(f"{GREEN}Discord: {RESET}triway340#9421")
                        time.sleep(1)
                        print(f"{GREEN}Github: {RESET}https://github.com/triway340")
                        time.sleep8(1)
                        extra1 = input("\nPresione enter para continuar... ")
                elif c1=="2":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(f"{GREEN}Telegram: {RESET}https://t.me/foxito_1")
                        time.sleep(1)
                        print(f"{GREEN}WhatsApp: {RESET}https://tiktok.com/@....foxy_0")
                        time.sleep(1)
                        print(f"{GREEN}Github: {RESET}https://github.com/Foxy340")
                        time.sleep(1)
                        extra2 = input("\nPresione enter para continuar... ")
                elif c1=="x" or c1=="X":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"Volviendo...")
                        time.sleep(2)
                        break
                else:
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(RED+"Opcion invalida...\n")
                        time.sleep(1)
                        print(GREEN+"Volviendo...")
                        time.sleep(6)

def home():
        while True:
                clear()
                print(f"\n\n{YELLOW}========================")
                print(banner)
                print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                print(f"{YELLOW}========================\n")
                print(f"{BLUE}[ {PURPLE}1 {BLUE}] {RESET}- {CYAN}Categorias")
                print(f"{BLUE}[ {PURPLE}2 {BLUE}] {RESET}- {CYAN}Contactos")
                print(f"{BLUE}[ {PURPLE}X {BLUE}] {RESET}- {CYAN}Salir\n")
                peticion1 = input("Ingrese una opción #>>> ")
                if peticion1=="1":
                        menu()
                elif peticion1=="2":
                        contactos()
                elif peticion1=="x" or peticion1=="X":
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(GREEN+"Saliendo...\n")
                        print(GREEN+"¡Adios, vuelve pronto!\n")
                        exit()
                else:
                        clear()
                        print(f"\n\n{YELLOW}========================")
                        print(banner)
                        print(f"{BLUE}--{GREEN}Os{RED}Fy{RESET}-{GREEN}Tool{BLUE}--")
                        print(f"\n{YELLOW}========================\n")
                        print(RED+"Opcion invalida...\n")
                        time.sleep(1)
                        print(GREEN+"Volviendo...")
                        time.sleep(6)
home()


