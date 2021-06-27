import pygame, sys, random, time
from pygame.locals import *

pygame.init()

#Color
col1 = (78.2, 70, 74.2)
NEGRO = (0,0,0)
GRIS = (77,77,77)

#Imágenes

dino1 = pygame.image.load("./imagenes/dino1.png") 
dino2 = pygame.image.load("./imagenes/dino2.png") 

piso = pygame.image.load("./imagenes/piso.png")
pisobase = pygame.image.load("./imagenes/piso.png")
pisoroto = pygame.image.load("./imagenes/pisoroto.png")

fondo = pygame.image.load("./imagenes/fondo.png")
fondo0 = pygame.image.load("./imagenes/fondonivel0.png")
fondoniveles = pygame.image.load("./imagenes/fondoniveles.png")

botonon = pygame.image.load("./imagenes/botonon.png")
botonoff = pygame.image.load("./imagenes/botonoff.png")

menui = pygame.image.load("./imagenes/menu.png")
menuj = pygame.image.load("./imagenes/menujugar.png")
menun = pygame.image.load("./imagenes/menuniveles.png")
menus = pygame.image.load("./imagenes/menuskins.png")

superado = pygame.image.load("./imagenes/superado.png")
tuto = pygame.image.load("./imagenes/info1.png")
tuto2 = pygame.image.load("./imagenes/info2.png")

botonr = pygame.image.load("./imagenes/botonr.png") #tutorial
botond = pygame.image.load("./imagenes/botond.png")
botonl = pygame.image.load("./imagenes/botonl.png")
botonu = pygame.image.load("./imagenes/botonu.png")
botonE = pygame.image.load("./imagenes/E.png")
flechar = pygame.image.load("./imagenes/flechar.png")

niveles = pygame.image.load("./imagenes/niveles.png")
nivelesselect = pygame.image.load("./imagenes/nivelessel.png")
#Audio

hielo = pygame.mixer.Sound("./audio/hielo.wav")
select = pygame.mixer.Sound("./audio/seleccionar.wav")
reselect = pygame.mixer.Sound("./audio/reselect.wav")

#Fuentes

dafont = pygame.font.SysFont("8bitOperatorPlus8-Regular.ttf", 30) 

#Ventana

panta = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juegazo")


#Variables
JUEGO = True
reloj = pygame.time.Clock()
paso = 0
muerte = 0.2
menu = menui
nosirve=True #Solo para poder esconder una parte


nivtotal = 3 #-1 NIVELES


NIVEL=[]

tutorial = True #para nivel 0
tutorial2 = True #para nivel 2
info = False #para info

NIVELES = False
LIMITADOR = False
LIMITADORALFOMBRA=True
juicio=0 #Para limites

#Fotogramas
foto = 100
selecto = 0.3

#Inicio
while JUEGO:
	
	panta.blit(menu, (0,0))
	pygame.display.flip()
	
	#Declarar niveles como falsos
	for i in range(nivtotal):
		NIVEL.append(i)
		NIVEL[i] = False
		
	
	for evento in pygame.event.get():
		
		if evento.type == MOUSEBUTTONDOWN:


			if (291<=evento.pos[0]<=554) and (280<=evento.pos[1]<=314): #Jugar
				panta.blit(menuj, (0,0))
				#pygame.mixer.Sound.play(select)
				#time.sleep(selecto)
				pygame.display.flip()
				time.sleep(0.3)
				menu = menui
				NIVEL[0] = True
			else:
				if (291<=evento.pos[0]<=554) and (368<=evento.pos[1]<=402): #Niveles
					panta.blit(menun, (0,0))
					#pygame.mixer.Sound.play(select)
					#time.sleep(selecto)
					pygame.display.flip()
					time.sleep(0.3)
					NIVELES = True
				else:
					if (291<=evento.pos[0]<=554) and (457<=evento.pos[1]<=491): #Skins (Todavía no hace nada)
						menu = menus
						#pygame.mixer.Sound.play(select)
						#time.sleep(selecto)
						pygame.display.flip()
						
			
		if evento.type == KEYDOWN:
			
			if evento.key == K_ESCAPE:
				JUEGO = False
	
	while NIVELES:
		
		
		#Defino los niveles
		
		cantidaddeniveles=3
		
		levels=[]
		
		for i in range(cantidaddeniveles):
			levels.append(i)
		
		#Ubicación
		
		nivx=[]
		nivy=[]
		xn1=180
		yn1=200
		
		for i in range(cantidaddeniveles):
			nivx.append(i)
			nivy.append(i)
		
		for i in range(cantidaddeniveles):
			nivx[i]= xn1 + (i*150)
			nivy[i]= yn1
		
		#Números
		
		Números=[]
		
		for i in range(cantidaddeniveles):
			Números.append(i)
			Números[i] = dafont.render(f"{Números[i]}",1,(col1)) #no lee la fuente que elegí
		
		
		#Bliteo
		
		panta.blit(fondoniveles,(0,0))
		
		for i in range(cantidaddeniveles):
			panta.blit(niveles, (nivx[i],nivy[i]))
			panta.blit(Números[i], ((nivx[i]+57),(nivy[i]+15)))
		
		
		pygame.display.flip()
		
		for evento in pygame.event.get():
			if evento.type == MOUSEBUTTONDOWN:
				for i in range(cantidaddeniveles):
					if ((nivx[i] <= evento.pos[0] <= (nivx[i]+125)) and ((nivy[i] <= evento.pos[1] <= (nivy[i]+50)))):
						NIVEL[i]=True
						NIVELES=False
						panta.blit(nivelesselect, (nivx[i],nivy[i]))
						panta.blit(Números[i], ((nivx[i]+57),(nivy[i]+15)))
						pygame.display.flip()
						time.sleep(0.3)
						
			if evento.type == KEYDOWN:
				if evento.key == K_ESCAPE:
					NIVELES=False


	while NIVEL[0]:
		
		if nosirve: #Reseteo de variables
			
			
			#Número mágico
			toty = 6
			 
			#Posición Inicial de Dino y Variables de movimiento
			dinos = dino1
			dinoy = 407
			dinox = 0
			mov = 50
			sumax = 0
			sumay = 0
			VOLVER = True
			
			#Variable para roto
			roto = []
			
			for i in range(toty):
				roto.append(i)
				roto[i]=False
			
			
			#reseteo de conta pasos
			paso = [] 
			
			for i in range(toty):
				paso.append(i)
				paso[i]=0
			
			
			#Variables de Finalización
			final = 0
			prendido1 = False
			prendido2 = False
			
			
			#Botones
			bot1x=300
			bot1y=357
			bot2x=300
			bot2y=407
			boton1 = botonoff
			boton2 = botonoff
			
			
			#Definir lista de pisos
			
			px=[]
			py=[]
			
			for i in range (toty):
				px.append(i)
				py.append(i)
			
			
 
			
			#Variablens para Fila
			
			#fila1
			
			fila1y= 357
			fila1x= 150 #esto es lo que va a arrancar la fila
			pisos_fila1 = 3 #Número de pisos de la fila
			
			for i in range (pisos_fila1):
				px[i]= fila1x + (i*50)
				py[i]= fila1y
			
			
			#fila2
			fila2y= 407
			fila2x= 150 #esto es lo que va a arrancar la fila
			pisos_fila2 = pisos_fila1 + 3 #Número de pisos de la fila
			
			for i in range (pisos_fila1, pisos_fila2):
				px[i]= fila2x + ((i-pisos_fila1)*50)
				py[i]= fila2y
			
		
		
		while VOLVER: #Ciclo del nivel
			
			
			#time.sleep(0.1)
			reloj.tick(foto)
			panta.blit(fondo0, (0,0))
			
			#Botones
			panta.blit(boton1,(bot1x, bot1y))
			panta.blit(boton2,(bot2x, bot2y))
			
			
			#Pisos bliteados
			for i in range(toty):
				panta.blit(pisobase,(px[i],py[i]))
			
			
			for evento in pygame.event.get(): 
				
				if evento.type == MOUSEBUTTONDOWN:
					if (12 <= evento.pos[0] <= 54) and (13 <= evento.pos[1] <= 54):
						tutorial = True
				
				if evento.type == pygame.KEYDOWN: #Teclado
					
					if evento.key == pygame.K_ESCAPE: #Apagado
						VOLVER = False
						NIVEL[0] = False
						panta.blit(menu, (0,0))
						pygame.display.flip()
						dinox=1000



					if evento.key == pygame.K_RIGHT: #DERECHA
						sumax = mov
						dinos = dino1
						for i in range(toty):
							if dinox == (px[i]-50) and dinoy == (py[i]):
								paso[i] += 1
								final += 1
								roto[i]= True



					if evento.key == pygame.K_LEFT and (dinox != 0):  #IZQUIERDA
						sumax = (-mov)
						dinos = dino2
						for i in range(toty):
							if dinox == (px[i]+50) and dinoy == (py[i]):
								paso[i] += 1
								final += 1
								roto[i]= True



					if evento.key == pygame.K_DOWN:  #ABAJO
						sumay = mov
						for i in range(toty):
							if dinoy == (py[i]-50) and dinox == (px[i]):
								paso[i] += 1
								final += 1
								roto[i]= True
 
 

					if evento.key == pygame.K_UP:  #ARRIBA
						sumay = (-mov)
						for i in range(toty):
							if dinoy == (py[i]+50) and dinox == (px[i]):
								paso[i] += 1
								final += 1
								roto[i]= True
							



					if evento.key == pygame.K_e and (dinox == bot1x) and (dinoy == bot1y) and (final == toty):
						boton1 = botonon
						prendido1 = True
						panta.blit(boton1,(bot1x, bot1y))
					else:
						if evento.key == pygame.K_e and (dinox == bot2x) and (dinoy == bot2y) and (final == toty):
							boton2 = botonon
							panta.blit(boton2,(bot2x, bot2y))
							prendido2 = True



			
			#Para rompero el piso
			for i in range(toty): 
				if roto[i]:
					panta.blit(pisoroto, (px[i],py[i]))
					
					#pygame.mixer.Sound.play(hielo)
			
			
			#LIMITADOR TRUE OR FALSE
			
			if dinox >= 150:
				LIMITADOR=True
				LIMITADORALFOMBRA=False
			else:
				LIMITADORALFOMBRA=True
				LIMITADOR=False
			
			
			
			#Para la alfombra
			if LIMITADORALFOMBRA:
				if dinox < 150 and dinoy == 407 and sumay > 0:
					sumay = 0
				else:
					if dinox < 150 and dinoy == 357 and sumay < 0:
						sumay = 0
						
			
			#Limitador para botones
			if (((dinox+sumax) == bot1x and bot1y == (dinoy+sumay)) or ((dinox+sumax) == bot2x and bot2y == (dinoy+sumay))): #Varia según donde pongas los botones, o al menos eso creo xD
				LIMITADOR = False
			
			
			#LIMITADOR
			
			juicio = 0
			
			if LIMITADOR:
				for i in range(toty):
					
					if ((dinox+sumax) == px[i] and (dinoy+sumay) == py[i]) :
						juicio += 1
						
				
				if juicio != 1:
					sumax=0
					sumay=0
			
			
			
			dinoy = sumay + dinoy
			dinox = sumax + dinox
			panta.blit(dinos,(dinox, dinoy))
			
			pygame.display.flip()
			
			sumax = 0
			sumay = 0
			
			
			 #Perder
			for i in range(toty):
				if (paso[i] == 2):
					time.sleep(0.3)
					VOLVER = False
			
			
			 #final
			if (prendido1 == 1) and (prendido2 == 1):
				pygame.display.flip()
				time.sleep(0.3)
				panta.blit(superado, (200, 150)) 
				pygame.display.flip()
				PREGUNTA = True
				while PREGUNTA:
					print()
					for evento in pygame.event.get(): # (Segur no funciona todavía)
						if evento.type == MOUSEBUTTONDOWN:
							if (270 <= evento.pos[0] <= 356) and (365 <= evento.pos[1] <= 387):
								PREGUNTA = False
								VOLVER = False
								NIVEL[0] = False
							if (433 <= evento.pos[0] <= 548) and (365 <= evento.pos[1] <= 387):
								PREGUNTA = False
								VOLVER = False
								NIVEL[0] = False
								NIVEL[1] = True
			
			
			#print(f"DINO: {dinox} dinoy:{dinoy} prendido1: {prendido1}" ) #Esto es para ver mejor coordenadas y detectar errores.
			
			
			while tutorial:
				panta.blit(tuto, (200, 150))
				pygame.display.flip()
				for evento in pygame.event.get(): # (Segur no funciona todavía) 570 180
						if evento.type == MOUSEBUTTONDOWN:
							if (560 <= evento.pos[0] <= 580) and (170 <= evento.pos[1] <= 190):
								tutorial = False
						if evento.type == pygame.KEYDOWN:
							if evento.key == K_ESCAPE:
								tutorial = False


	while NIVEL[1]:
		
		if nosirve: #Reseteo de variables
			
			
			#Número mágico
			toty = 22
			 
			#Posición Inicial de Dino y Variables de movimiento
			dinos = dino1
			dinoy = 407
			dinox = 0
			mov = 50
			sumax = 0
			sumay = 0
			VOLVER = True
			
			#Variable para roto
			roto = []
			
			for i in range(toty):
				roto.append(i)
				roto[i]=False
			
			
			#reseteo de conta pasos
			paso = [] 
			
			for i in range(toty):
				paso.append(i)
				paso[i]=0
			
			
			#Variables de Finalización
			final = 0
			prendido1 = False
			prendido2 = False
			
			
			
			#Botones
			bot1x=500
			bot1y=357
			bot2x=500
			bot2y=407
			boton1 = botonoff
			boton2 = botonoff
			
			
			
			
			#Definir lista de pisos
			
			px=[]
			py=[]
			
			for i in range (toty):
				px.append(i)
				py.append(i)
			
			
 
			
			#Variablens para Fila
			
			#fila1
			
			fila1y= 307
			fila1x= 300 #esto es lo que va a arrancar la fila
			pisos_fila1 = 4 #Número de pisos de la fila
			
			for i in range (pisos_fila1):
				px[i]= fila1x + (i*50)
				py[i]= fila1y
			
			
			#fila2
			fila2y= 357
			fila2x= 150 #esto es lo que va a arrancar la fila
			pisos_fila2 = pisos_fila1 + 7 #Número de pisos de la fila
			
			for i in range (pisos_fila1, pisos_fila2):
				px[i]= fila2x + ((i-pisos_fila1)*50)
				py[i]= fila2y
			
			
			#fila3
			fila3y= 407
			fila3x= 150 #esto es lo que va a arrancar la fila
			pisos_fila3 = pisos_fila2 + 7 #Número de pisos de la fila
			
			for i in range (pisos_fila2, pisos_fila3):
				px[i]= fila3x + ((i-pisos_fila2)*50)
				py[i]= fila3y
			
			
			#fila4
			fila4y= 457 #Altura
			fila4x= 300 #esto es lo que va a arrancar la fila
			pisos_fila4 = pisos_fila3 + 4 #Número de pisos de la fila
			
			for i in range (pisos_fila3, pisos_fila4):
				px[i]= fila4x + ((i-pisos_fila3)*50)
				py[i]= fila4y
		
		
		
		while VOLVER: #Ciclo del nivel
			
			#time.sleep(0.1)
			reloj.tick(foto)
			panta.blit(fondo, (0,0))



			#Botones
			panta.blit(boton1,(bot1x, bot1y))
			panta.blit(boton2,(bot2x, bot2y))



			#Pisos bliteados
			for i in range(toty):
				panta.blit(pisobase,(px[i],py[i]))




			for evento in pygame.event.get():
				
				if evento.type == MOUSEBUTTONDOWN:
					if (12 <= evento.pos[0] <= 54) and (13 <= evento.pos[1] <= 54):
						info = True



				if evento.type == pygame.KEYDOWN: #Teclado
					
					if evento.key == pygame.K_ESCAPE: #Apagado
						VOLVER = False
						NIVEL[1] = False
						panta.blit(menu, (0,0))
						pygame.display.flip()
						dinox=1000



					if evento.key == pygame.K_RIGHT: #DERECHA
						sumax = mov
						dinos = dino1
						for i in range(toty):
							if dinox == (px[i]-50) and dinoy == (py[i]):
								paso[i] += 1
								final += 1
								roto[i]= True



					if evento.key == pygame.K_LEFT and (dinox != 0):  #IZQUIERDA
						sumax = (-mov)
						dinos = dino2
						for i in range(toty):
							if dinox == (px[i]+50) and dinoy == (py[i]):
								paso[i] += 1
								final += 1
								roto[i]= True



					if evento.key == pygame.K_DOWN:  #ABAJO
						sumay = mov
						for i in range(toty):
							if dinoy == (py[i]-50) and dinox == (px[i]):
								paso[i] += 1
								final += 1
								roto[i]= True
 
 

					if evento.key == pygame.K_UP:  #ARRIBA
						sumay = (-mov)
						for i in range(toty):
							if dinoy == (py[i]+50) and dinox == (px[i]):
								paso[i] += 1
								final += 1
								roto[i]= True
							



					if evento.key == pygame.K_e and (dinox == bot1x) and (dinoy == bot1y) and (final == toty):
						boton1 = botonon
						prendido1 = True
						panta.blit(boton1,(bot1x, bot1y))
					else:
						if evento.key == pygame.K_e and (dinox == bot2x) and (dinoy == bot2y) and (final == toty):
							boton2 = botonon
							panta.blit(boton2,(bot2x, bot2y))
							prendido2 = True



			#Para rompero el piso
			
			for i in range(toty): 
				if roto[i]:
					panta.blit(pisoroto, (px[i],py[i]))
					
					#pygame.mixer.Sound.play(hielo)
			



			#LIMITADOR TRUE OR FALSE
			
			if dinox >= 150:
				LIMITADOR=True
				LIMITADORALFOMBRA=False
			else:
				LIMITADORALFOMBRA=True
				LIMITADOR=False
			
			
			#Para la alfombra
			if LIMITADORALFOMBRA:
				if dinox < 150 and dinoy == 407 and sumay > 0:
					sumay = 0
				else:
					if dinox < 150 and dinoy == 357 and sumay < 0:
						sumay = 0
			
			
			#Limitador para botones
			if (((dinox+sumax) == bot1x and bot1y == (dinoy+sumay)) or ((dinox+sumax) == bot2x and bot2y == (dinoy+sumay))): #Varia según donde pongas los botones, o al menos eso creo xD
				LIMITADOR = False
				
			
			
			#LIMITADOR
			juicio = 0
			if LIMITADOR:
				for i in range(toty):
					
					if ((dinox+sumax) == px[i] and (dinoy+sumay) == py[i]) :
						juicio += 1
						
				if juicio != 1:
					sumax=0
					sumay=0



			dinoy = sumay + dinoy
			dinox = sumax + dinox
			panta.blit(dinos,(dinox, dinoy))
			
			pygame.display.flip()
			
			sumax = 0
			sumay = 0



			 #Perder
			for i in range(toty):
				if (paso[i] == 2):
					time.sleep(0.3)
					VOLVER = False



			 #final
			if (prendido1 == True) and (prendido2 == True):
				pygame.display.flip()
				time.sleep(0.3)
				panta.blit(superado, (200, 150)) 
				pygame.display.flip()
				PREGUNTA = True
				while PREGUNTA:
					print()
					for evento in pygame.event.get(): # (Seguir no funciona todavía)
						if evento.type == MOUSEBUTTONDOWN:
							if (270 <= evento.pos[0] <= 356) and (365 <= evento.pos[1] <= 387):
								PREGUNTA = False
								VOLVER = False
								NIVEL[1] = False
							if (433 <= evento.pos[0] <= 548) and (365 <= evento.pos[1] <= 387):
								PREGUNTA = False
								VOLVER = False
								NIVEL[1] = False
								NIVEL[2] = True

			#print(f"DINO: {dinox} dinoy:{dinoy} prendido1: {prendido1} pregunta: {PREGUNTA}" ) #Esto es para ver mejor coordenadas y detectar errores.

			while info:
				panta.blit(tuto, (200, 150))
				pygame.display.flip()
				for evento in pygame.event.get(): # (Segur no funciona todavía) 570 180
						if evento.type == MOUSEBUTTONDOWN:
							if (560 <= evento.pos[0] <= 580) and (170 <= evento.pos[1] <= 190):
								info = False
						if evento.type == pygame.KEYDOWN:
							if evento.key == K_ESCAPE:
								info = False


	while NIVEL[2]:
	
		if nosirve: #Reseteo de variables
			
			
			#Trampita
			
			trampita = random.randint(0,1) 
			
			#Número mágico
			
			toty = random.randint(27,28) #Variación en el mapa, dependiendo de que número salga el mapa va a ser de una forma o otra.
			
			 
			#Posición Inicial de Dino y Variables de movimiento
			dinos = dino1
			dinoy = 407
			dinox = 0
			mov = 50
			sumax = 0
			sumay = 0
			VOLVER = True
			
			#Variable para roto
			roto = []
			
			for i in range(toty):
				roto.append(i)
				roto[i]=False
			
			
			#reseteo de conta pasos
			paso = [] 
			
			for i in range(toty):
				paso.append(i)
				paso[i]=0
			
			
			#Variables de Finalización
			final = 0
			prendido1 = False
			prendido2 = False
			
			
			
			#Botones
			bot1x=500
			bot1y=257
			bot2x=500
			bot2y=507
			boton1 = botonoff
			boton2 = botonoff
			
			
			
			
			#Definir lista de pisos
			
			px=[]
			py=[]
			
			for i in range (toty):
				px.append(i)
				py.append(i)
			
			

			
			#Variablens para Fila
			
			#fila1
			
			fila1y= 257
			fila1x= 300 #esto es lo que va a arrancar la fila
			pisos_fila1 = 4 #Número de pisos de la fila
			
			for i in range (pisos_fila1):
				px[i]= fila1x + (i*50)
				py[i]= fila1y


			#fila2
			fila2y= 307
			fila2x= 300 #esto es lo que va a arrancar la fila
			if toty == 28:
				pisos_fila2 = pisos_fila1 + 5 
			else:
				if toty == 27 and trampita == 0:
					pisos_fila2 = pisos_fila1 + 4 
				else:
					pisos_fila2 = pisos_fila1 + 5
			
			for i in range (pisos_fila1, pisos_fila2):
				px[i]= fila2x + ((i-pisos_fila1)*50)
				py[i]= fila2y


			#fila3
			fila3y= 357
			fila3x= 150 #esto es lo que va a arrancar la fila
			pisos_fila3 = pisos_fila2 + 5 #Número de pisos de la fila
			
			for i in range (pisos_fila2, pisos_fila3):
				px[i]= fila3x + ((i-pisos_fila2)*50)
				py[i]= fila3y


			#fila4
			fila4y= 407 #Altura
			fila4x= 150 #esto es lo que va a arrancar la fila
			pisos_fila4 = pisos_fila3 + 5 #Número de pisos de la fila
			
			for i in range (pisos_fila3, pisos_fila4):
				px[i]= fila4x + ((i-pisos_fila3)*50)
				py[i]= fila4y
				
			#fila5
			fila5y= 457 #Altura
			fila5x= 300 #esto es lo que va a arrancar la fila
			
			if toty == 28:
				pisos_fila5 = pisos_fila4 + 5 
			if toty == 27 and trampita == 1:
				pisos_fila5 = pisos_fila4 + 4 #Número de pisos de la fila
			else:
				pisos_fila5 = pisos_fila4 + 5 
			
			for i in range (pisos_fila4, pisos_fila5):
				px[i]= fila5x + ((i-pisos_fila4)*50)
				py[i]= fila5y



			#fila6
			fila6y= 507 #Altura
			fila6x= 300 #esto es lo que va a arrancar la fila
			pisos_fila6 = pisos_fila5 + 4 #Número de pisos de la fila
			
			for i in range (pisos_fila5, pisos_fila6):
				px[i]= fila6x + ((i-pisos_fila5)*50)
				py[i]= fila6y
			
			
			
			
			
			
		while VOLVER: #Ciclo del nivel
			
			#time.sleep(0.1)
			reloj.tick(foto)
			panta.blit(fondo, (0,0))



			#Botones
			panta.blit(boton1,(bot1x, bot1y))
			panta.blit(boton2,(bot2x, bot2y))



			#Pisos bliteados
			for i in range(toty):
				panta.blit(pisobase,(px[i],py[i]))




			for evento in pygame.event.get():
				
				if evento.type == MOUSEBUTTONDOWN:
					if (12 <= evento.pos[0] <= 54) and (13 <= evento.pos[1] <= 54):
						info = True



				if evento.type == pygame.KEYDOWN: #Teclado
					
					if evento.key == pygame.K_ESCAPE: #Apagado
						VOLVER = False
						NIVEL[2] = False
						panta.blit(menu, (0,0))
						pygame.display.flip()
						dinox=1000



					if evento.key == pygame.K_RIGHT: #DERECHA
						sumax = mov
						dinos = dino1
						for i in range(toty):
							if dinox == (px[i]-50) and dinoy == (py[i]):
								paso[i] += 1
								final += 1
								roto[i]= True



					if evento.key == pygame.K_LEFT and (dinox != 0):  #IZQUIERDA
						sumax = (-mov)
						dinos = dino2
						for i in range(toty):
							if dinox == (px[i]+50) and dinoy == (py[i]):
								paso[i] += 1
								final += 1
								roto[i]= True



					if evento.key == pygame.K_DOWN:  #ABAJO
						sumay = mov
						for i in range(toty):
							if dinoy == (py[i]-50) and dinox == (px[i]):
								paso[i] += 1
								final += 1
								roto[i]= True
 
 

					if evento.key == pygame.K_UP:  #ARRIBA
						sumay = (-mov)
						for i in range(toty):
							if dinoy == (py[i]+50) and dinox == (px[i]):
								paso[i] += 1
								final += 1
								roto[i]= True
							



					if evento.key == pygame.K_e and (dinox == bot1x) and (dinoy == bot1y):  #En este nivel se tiene que activar la e sin haber presionado todo
						boton1 = botonon
						prendido1 = True
						panta.blit(boton1,(bot1x, bot1y))
					else:
						if evento.key == pygame.K_e and (dinox == bot2x) and (dinoy == bot2y):
							boton2 = botonon
							panta.blit(boton2,(bot2x, bot2y))
							prendido2 = True



			#Para rompero el piso
			
			for i in range(toty): 
				if roto[i]:
					panta.blit(pisoroto, (px[i],py[i]))
					
					#pygame.mixer.Sound.play(hielo)
			



			#LIMITADOR TRUE OR FALSE
			
			if dinox >= 150:
				LIMITADOR=True
				LIMITADORALFOMBRA=False
			else:
				LIMITADORALFOMBRA=True
				LIMITADOR=False
			
			
			#Para la alfombra
			if LIMITADORALFOMBRA:
				if dinox < 150 and dinoy == 407 and sumay > 0:
					sumay = 0
				else:
					if dinox < 150 and dinoy == 357 and sumay < 0:
						sumay = 0
			
			
			#Limitador para botones
			if (((dinox+sumax) == bot1x and bot1y == (dinoy+sumay)) or ((dinox+sumax) == bot2x and bot2y == (dinoy+sumay))): #Varia según donde pongas los botones, o al menos eso creo xD
				LIMITADOR = False
				
			
			
			#LIMITADOR
			juicio = 0
			if LIMITADOR:
				for i in range(toty):
					
					if ((dinox+sumax) == px[i] and (dinoy+sumay) == py[i]) :
						juicio += 1

				
				if juicio != 1:
					sumax=0
					sumay=0



			dinoy = sumay + dinoy
			dinox = sumax + dinox
			panta.blit(dinos,(dinox, dinoy))
			
			pygame.display.flip()
			
			sumax = 0
			sumay = 0



			 #Perder
			for i in range(toty):
				if (paso[i] == 2):
					time.sleep(0.3)
					VOLVER = False



			 #final
			if (prendido1 == True) and (prendido2 == True) and (final == toty):
				pygame.display.flip()
				time.sleep(0.3)
				panta.blit(superado, (200, 150)) 
				pygame.display.flip()
				PREGUNTA = True
				while PREGUNTA:
					print()
					for evento in pygame.event.get(): # (Seguir no funciona todavía)
						if evento.type == MOUSEBUTTONDOWN:
							if (270 <= evento.pos[0] <= 356) and (365 <= evento.pos[1] <= 387):
								PREGUNTA = False
								VOLVER = False
								NIVEL[2] = False

			#print(f"DINO: {dinox} dinoy:{dinoy} prendido1: {prendido1} pregunta: {PREGUNTA}" ) #Esto es para ver mejor coordenadas y detectar errores.

			while info:
				panta.blit(tuto2, (200, 150))
				pygame.display.flip()
				for evento in pygame.event.get(): # (Segur no funciona todavía) 570 180
						if evento.type == MOUSEBUTTONDOWN:
							if (560 <= evento.pos[0] <= 580) and (170 <= evento.pos[1] <= 190):
								info = False
						if evento.type == pygame.KEYDOWN:
							if evento.key == K_ESCAPE:
								info = False

			while tutorial2:
				panta.blit(tuto2, (200, 150))
				pygame.display.flip()
				for evento in pygame.event.get(): # (Segur no funciona todavía) 570 180
						if evento.type == MOUSEBUTTONDOWN:
							if (560 <= evento.pos[0] <= 580) and (170 <= evento.pos[1] <= 190):
								tutorial2 = False
						if evento.type == pygame.KEYDOWN:
							if evento.key == K_ESCAPE:
								tutorial2 = False
			
