import pygame, sys, random, time
from pygame.locals import *


#Color
col1 = (214, 67, 67)

#Imágenes

dino1 = pygame.image.load("./imagenes/dino1.png") 
dino2 = pygame.image.load("./imagenes/dino2.png") 
piso = pygame.image.load("./imagenes/piso.png")
pisoroto = pygame.image.load("./imagenes/pisoroto.png")
farol1 = pygame.image.load("./imagenes/farol1.png")
farol2 = pygame.image.load("./imagenes/farol2.png")
farol3 = pygame.image.load("./imagenes/farol3.png")
farol4 = pygame.image.load("./imagenes/farol4.png")
fondo = pygame.image.load("./imagenes/fondo.png")
botonon = pygame.image.load("./imagenes/botonon.png")
botonoff = pygame.image.load("./imagenes/botonoff.png")
menu = pygame.image.load("./imagenes/menu.png")
menuj = pygame.image.load("./imagenes/menujugar.png")
menun = pygame.image.load("./imagenes/menuniveles.png")
menus = pygame.image.load("./imagenes/menuskins.png")
superado = pygame.image.load("./imagenes/superado.png")

#Ventana
pygame.init()
panta = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juegazo")


#Variables
JUEGO = True
reloj = pygame.time.Clock()
paso = 0
muerte = 0.2

#Fotogramas
foto= 100
PREGUNTA = True
#Inicio
while JUEGO:
    panta.blit(menu, (0,0))
    pygame.display.flip()
	NIVEL2 = False
	for evento in pygame.event.get():
		if evento.type == MOUSEBUTTONDOWN:


			if (291<=evento.pos[0]<=554) and (280<=evento.pos[1]<=314): #Jugar
				panta.blit(menuj, (0,0))
				pygame.display.flip()
				time.sleep(0.5)
				NIVEL2 = True
			else:
				if (291<=evento.pos[0]<=554) and (368<=evento.pos[1]<=402): #Niveles (Todavía no hace nada)
					panta.blit(menun, (0,0))
					pygame.display.flip()
				else:
					if (291<=evento.pos[0]<=554) and (457<=evento.pos[1]<=491): #Skins (Todavía no hace nada)
						panta.blit(menus, (0,0))
						pygame.display.flip()
			
		if evento.type == KEYDOWN:
			
			if evento.key == K_ESCAPE:
				JUEGO = False



	while NIVEL2:
	
		#Posición Inicial de Dino y Variables de movimiento
		dinos = dino1
		dinoy = 407
		dinox = 0
		mov = 50
		sumax = 0
		sumay = 0
		VOLVER = True
		
		#reseteo de conta pasos
		paso1 = 0
		paso2 = 0
		paso3 = 0
		paso4 = 0
		paso5 = 0
		paso6 = 0
		paso7 = 0
		paso8 = 0
		paso9 = 0
		paso10 = 0
		paso11 = 0
		paso12 = 0
		paso13 = 0
		paso14 = 0
		paso15 = 0
		paso16 = 0
		paso17 = 0
		paso18 = 0
		paso19 = 0
		paso20 = 0
		paso21 = 0
		paso22 = 0
		
		#Variables de Finalización
		final = 0
		prendido1 = 0
		prendido2 = 0
		
		
		#resteo de pisos
		piso1 = piso
		piso2 = piso
		piso3 = piso
		piso4 = piso
		piso5 = piso
		piso6 = piso
		piso7 = piso
		piso8 = piso
		piso9 = piso
		piso10 = piso
		piso11 = piso
		piso12 = piso
		piso13 = piso
		piso14 = piso
		piso15 = piso
		piso16 = piso
		piso17 = piso
		piso18 = piso
		piso19 = piso
		piso20 = piso
		piso21 = piso
		piso22 = piso
		
		#Posición de pisos (senda)
		p1x = 150
		p1y = 357
		p2x = 150
		p2y = 407
		p3x = 200
		p3y = 357
		p4x = 200
		p4y = 407
		p5x = 250
		p5y = 357
		p6x = 250
		p6y = 407
		
		#Posición Cuadrado:
		
		# Hileras (vertical) y Filas (horizontal):
		hilera1 = 300
		hilera2 = 350
		hilera3 = 400
		hilera4 = 450
		
		fila1 = 307
		fila2 = 357
		fila3 = 407
		fila4 = 457
		
		#Hilera 1:
		p7x = hilera1
		p7y = fila1
		p8x = hilera1
		p8y = fila2
		p9x = hilera1
		p9y = fila3
		p10x = hilera1
		p10y = fila4
		
		#Hilera 2:
		p11x = hilera2
		p11y = fila1
		p12x = hilera2
		p12y = fila2
		p13x = hilera2
		p13y = fila3
		p14x = hilera2
		p14y = fila4
		
		#Hilera 3:
		p15x = hilera3
		p15y = fila1
		p16x = hilera3
		p16y = fila2
		p17x = hilera3
		p17y = fila3
		p18x = hilera3
		p18y = fila4
		
		#Hilera 4:
		p19x = hilera4
		p19y = fila1
		p20x = hilera4
		p20y = fila2
		p21x = hilera4
		p21y = fila3
		p22x = hilera4
		p22y = fila4
		
		#Botones
		bot1x=500
		bot1y=357
		bot2x=500
		bot2y=407
		boton1 = botonoff
		boton2 = botonoff
		
		#Limitadores
		limite_adelante = 401
		limite_atras = 1
		limite_abajo = 407
		limite_arriba = 357
		
		while VOLVER:
			
			#time.sleep(0.1)
			reloj.tick(foto)
			panta.blit(fondo, (0,0))
			
			#Botones
			panta.blit(boton1,(bot1x, bot1y))
			panta.blit(boton2,(bot2x, bot2y))
			
			#Pisos bliteados
			panta.blit(piso1,(p1x,p1y))
			panta.blit(piso2,(p2x,p2y))
			panta.blit(piso3,(p3x,p3y))
			panta.blit(piso4,(p4x,p4y))
			panta.blit(piso5,(p5x,p5y))
			panta.blit(piso6,(p6x,p6y))
			panta.blit(piso7,(p7x,p7y))
			panta.blit(piso8,(p8x,p8y))
			panta.blit(piso9,(p9x,p9y))
			panta.blit(piso10,(p10x,p10y))
			panta.blit(piso11,(p11x,p11y))
			panta.blit(piso12,(p12x,p12y))
			panta.blit(piso13,(p13x,p13y))
			panta.blit(piso14,(p14x,p14y))
			panta.blit(piso15,(p15x,p15y))
			panta.blit(piso16,(p16x,p16y))
			panta.blit(piso17,(p17x,p17y))
			panta.blit(piso18,(p18x,p18y))
			panta.blit(piso19,(p19x,p19y))
			panta.blit(piso20,(p20x,p20y))
			panta.blit(piso21,(p21x,p21y))
			panta.blit(piso22,(p22x,p22y))
			
			
			for evento in pygame.event.get(): #Teclado
				if evento.type == pygame.KEYDOWN:
					
					if evento.key == pygame.K_ESCAPE: #Apagado
						VOLVER = False
						NIVEL2 = False
						panta.blit(menu, (0,0))
						pygame.display.flip()
						dinox=1000



					if evento.key == pygame.K_RIGHT and (dinox < limite_adelante): #DERECHA
						sumax = mov
						dinos = dino1
						if dinox == (p1x-50) and dinoy == (p1y):
							paso1 += 1
							final += 1
							piso1 = pisoroto
						else:
							if dinox == (p2x-50) and dinoy == (p2y):
								paso2 += 1
								final += 1
								piso2 = pisoroto
							else:
								if dinox == (p3x-50) and dinoy == (p3y):
									paso3 += 1
									final += 1
									piso3 = pisoroto
								else:
									if dinox == (p4x-50) and dinoy == (p4y):
										paso4 += 1
										final += 1
										piso4 = pisoroto
									else:
										if dinox == (p5x-50) and dinoy == (p5y):
											paso5 += 1
											final += 1
											piso5 = pisoroto
										else:
											if dinox == (p6x-50) and dinoy == (p6y):
												paso6 += 1
												final += 1
												piso6 = pisoroto
											else:
												if dinox == (p7x-50) and dinoy == (p7y):
													paso7 += 1
													final += 1
													piso7 = pisoroto
												else:
													if dinox == (p8x-50) and dinoy == (p8y):
														paso8 += 1
														final += 1
														piso8 = pisoroto
													else:
														if dinox == (p9x-50) and dinoy == (p9y):
															paso9 += 1
															final += 1
															piso9 = pisoroto
														else:
															if dinox == (p10x-50) and dinoy == (p10y):
																paso10 += 1
																final += 1
																piso10 = pisoroto
															else:
																if dinox == (p11x-50) and dinoy == (p11y):
																	paso11 += 1
																	final += 1
																	piso11 = pisoroto
																else:
																	if dinox == (p12x-50) and dinoy == (p12y):
																		paso12 += 1
																		final += 1
																		piso12 = pisoroto
																	else:
																		if dinox == (p13x-50) and dinoy == (p13y):
																			paso13 += 1
																			final += 1
																			piso13 = pisoroto
																		else:
																			if dinox == (p14x-50) and dinoy == (p14y):
																				paso14 += 1
																				final += 1
																				piso14 = pisoroto
																			else:
																				if dinox == (p15x-50) and dinoy == (p15y):
																					paso15 += 1
																					final += 1
																					piso15 = pisoroto
																				else:
																					if dinox == (p16x-50) and dinoy == (p16y):
																						paso16 += 1
																						final += 1
																						piso16 = pisoroto
																					else:
																						if dinox == (p17x-50) and dinoy == (p17y):
																							paso17 += 1
																							final += 1
																							piso17 = pisoroto
																						else:
																							if dinox == (p18x-50) and dinoy == (p18y):
																								paso18 += 1
																								final += 1
																								piso18 = pisoroto
																							else:
																								if dinox == (p19x-50) and dinoy == (p19y):
																									paso19 += 1
																									final += 1
																									piso19 = pisoroto
																								else:
																									if dinox == (p20x-50) and dinoy == (p20y):
																										paso20 += 1
																										final += 1
																										piso20 = pisoroto
																									else:
																										if dinox == (p21x-50) and dinoy == (p21y):
																											paso21 += 1
																											final += 1
																											piso21 = pisoroto
																										else:
																											if dinox == (p22x-50) and dinoy == (p22y):
																												paso22 += 1
																												final += 1
																												piso22 = pisoroto



					if evento.key == pygame.K_LEFT and (dinox > limite_atras):  #IZQUIERDA
						sumax = (-mov)
						dinos = dino2
						if dinox == (p1x+50) and dinoy == (p1y):
							paso1 += 1
							final += 1
							piso1 = pisoroto
						else:
							if dinox == (p2x+50) and dinoy == (p2y):  
								paso2 += 1
								final += 1
								piso2 = pisoroto
							else:
								if dinox == (p3x+50) and dinoy == (p3y):
									paso3 += 1
									final += 1
									piso3 = pisoroto
								else:
									if dinox == (p4x+50) and dinoy == (p4y):
										paso4 += 1
										final += 1
										piso4 = pisoroto
									else:
										if dinox == (p5x+50) and dinoy == (p5y):
											paso5 += 1
											final += 1
											piso5 = pisoroto
										else:
											if dinox == (p6x+50) and dinoy == (p6y):
												paso6 += 1
												final += 1
												piso6 = pisoroto
											else:
												if dinox == (p7x+50) and dinoy == (p7y):
													paso7 += 1
													final += 1
													piso7 = pisoroto
												else:
													if dinox == (p8x+50) and dinoy == (p8y):
														paso8 += 1
														final += 1
														piso8 = pisoroto
													else:
														if dinox == (p9x+50) and dinoy == (p9y):
															paso9 += 1
															final += 1
															piso9 = pisoroto
														else:
															if dinox == (p10x+50) and dinoy == (p10y):
																paso10 += 1
																final += 1
																piso10 = pisoroto
															else:
																if dinox == (p11x+50) and dinoy == (p11y):
																	paso11 += 1
																	final += 1
																	piso11 = pisoroto
																else:
																	if dinox == (p12x+50) and dinoy == (p12y):
																		paso12 += 1
																		final += 1
																		piso12 = pisoroto
																	else:
																		if dinox == (p13x+50) and dinoy == (p13y):
																			paso13 += 1
																			final += 1
																			piso13 = pisoroto
																		else:
																			if dinox == (p14x+50) and dinoy == (p14y):
																				paso14 += 1
																				final += 1
																				piso14 = pisoroto
																			else:
																				if dinox == (p15x+50) and dinoy == (p15y):
																					paso15 += 1
																					final += 1
																					piso15 = pisoroto
																				else:
																					if dinox == (p16x+50) and dinoy == (p16y):
																						paso16 += 1
																						final += 1
																						piso16 = pisoroto
																					else:
																						if dinox == (p17x+50) and dinoy == (p17y):
																							paso17 += 1
																							final += 1
																							piso17 = pisoroto
																						else:
																							if dinox == (p18x+50) and dinoy == (p18y):
																								paso18 += 1
																								final += 1
																								piso18 = pisoroto
																							else:
																								if dinox == (p19x+50) and dinoy == (p19y):
																									paso19 += 1
																									final += 1
																									piso19 = pisoroto
																								else:
																									if dinox == (p20x+50) and dinoy == (p20y):
																										paso20 += 1
																										final += 1
																										piso20 = pisoroto
																									else:
																										if dinox == (p21x+50) and dinoy == (p21y):
																											paso21 += 1
																											final += 1
																											piso21 = pisoroto
																										else:
																											if dinox == (p22x+50) and dinoy == (p22y):
																												paso22 += 1
																												final += 1
																												piso22 = pisoroto



					if evento.key == pygame.K_DOWN and (dinoy < limite_abajo):  #ABAJO
						sumay = mov
						if dinoy == (p1y-50) and dinox == (p1x):
							paso1 += 1
							final += 1
							piso1 = pisoroto
						else:
							if dinoy == (p2y-50) and dinox == (p2x):
								paso2 += 1
								final += 1
								piso2 = pisoroto
							else:
								if dinoy == (p3y-50) and dinox == (p3x):
									paso3 += 1
									final += 1
									piso3 = pisoroto
								else:
									if dinoy == (p4y-50) and dinox == (p4x):
										paso4 += 1
										final += 1
										piso4 = pisoroto
									else:
										if dinoy == (p5y-50) and dinox == (p5x):
											paso5 += 1
											final += 1
											piso5 = pisoroto
										else:
											if dinoy == (p6y-50) and dinox == (p6x):
												paso6 += 1
												final += 1
												piso6 = pisoroto
											else:
												if dinoy == (p7y-50) and dinox == (p7x):
													paso7 += 1
													final += 1
													piso7 = pisoroto
												else:
													if dinoy == (p8y-50) and dinox == (p8x):
														paso8 += 1
														final += 1
														piso8 = pisoroto
													else:
														if dinoy == (p9y-50) and dinox == (p9x):
															paso9 += 1
															final += 1
															piso9 = pisoroto
														else:
															if dinoy == (p10y-50) and dinox == (p10x):
																paso10 += 1
																final += 1
																piso10 = pisoroto
															else:
																if dinoy == (p11y-50) and dinox == (p11x):
																	paso11 += 1
																	final += 1
																	piso11 = pisoroto
																else:
																	if dinoy == (p12y-50) and dinox == (p12x):
																		paso12 += 1
																		final += 1
																		piso12 = pisoroto
																	else:
																		if dinoy == (p13y-50) and dinox == (p13x):
																			paso13 += 1
																			final += 1
																			piso13 = pisoroto
																		else:
																			if dinoy == (p14y-50) and dinox == (p14x):
																				paso14 += 1
																				final += 1
																				piso14 = pisoroto
																			else:
																				if dinoy == (p15y-50) and dinox == (p15x):
																					paso15 += 1
																					final += 1
																					piso15 = pisoroto
																				else:
																					if dinoy == (p16y-50) and dinox == (p16x):
																						paso16 += 1
																						final += 1
																						piso16 = pisoroto
																					else:
																						if dinoy == (p17y-50) and dinox == (p17x):
																							paso17 += 1
																							final += 1
																							piso17 = pisoroto
																						else:
																							if dinoy == (p18y-50) and dinox == (p18x):
																								paso18 += 1
																								final += 1
																								piso18 = pisoroto
																							else:
																								if dinoy == (p19y-50) and dinox == (p19x):
																									paso19 += 1
																									final += 1
																									piso19 = pisoroto
																								else:
																									if dinoy == (p20y-50) and dinox == (p20x):
																										paso20 += 1
																										final += 1
																										piso20 = pisoroto
																									else:
																										if dinoy == (p21y-50) and dinox == (p21x):
																											paso21 += 1
																											final += 1
																											piso21 = pisoroto
																										else:
																											if dinoy == (p22y-50) and dinox == (p22x):
																												paso22 += 1
																												final += 1
																												piso22 = pisoroto



					if evento.key == pygame.K_UP and (dinoy > limite_arriba):  #ARRIBA
						sumay = (-mov)
						if dinoy == (p1y+50) and dinox == (p1x):
							paso1 += 1
							final += 1
							piso1 = pisoroto
						else:
							if dinoy == (p2y+50) and dinox == (p2x):
								paso2 += 1
								final += 1
								piso2 = pisoroto
							else:
								if dinoy == (p3y+50) and dinox == (p3x):
									paso3 += 1
									final += 1
									piso3 = pisoroto
								else:
									if dinoy == (p4y+50) and dinox == (p4x):
										paso4 += 1
										final += 1
										piso4 = pisoroto
									else:
										if dinoy == (p5y+50) and dinox == (p5x):
											paso5 += 1
											final += 1
											piso5 = pisoroto
										else:
											if dinoy == (p6y+50) and dinox == (p6x):
												paso6 += 1
												final += 1
												piso6 = pisoroto
											else:
												if dinoy == (p7y+50) and dinox == (p7x):
													paso7 += 1
													final += 1
													piso7 = pisoroto
												else:
													if dinoy == (p8y+50) and dinox == (p8x):
														paso8 += 1
														final += 1
														piso8 = pisoroto
													else:
														if dinoy == (p9y+50) and dinox == (p9x):
															paso9 += 1
															final += 1
															piso9 = pisoroto
														else:
															if dinoy == (p10y+50) and dinox == (p10x):
																paso10 += 1
																final += 1
																piso10 = pisoroto
															else:
																if dinoy == (p11y+50) and dinox == (p11x):
																	paso11 += 1
																	final += 1
																	piso11 = pisoroto
																else:
																	if dinoy == (p12y+50) and dinox == (p12x):
																		paso12 += 1
																		final += 1
																		piso12 = pisoroto
																	else:
																		if dinoy == (p13y+50) and dinox == (p13x):
																			paso13 += 1
																			final += 1
																			piso13 = pisoroto
																		else:
																			if dinoy == (p14y+50) and dinox == (p14x):
																				paso14 += 1
																				final += 1
																				piso14 = pisoroto
																			else:
																				if dinoy == (p15y+50) and dinox == (p15x):
																					paso15 += 1
																					final += 1
																					piso15 = pisoroto
																				else:
																					if dinoy == (p16y+50) and dinox == (p16x):
																						paso16 += 1
																						final += 1
																						piso16 = pisoroto
																					else:
																						if dinoy == (p17y+50) and dinox == (p17x):
																							paso17 += 1
																							final += 1
																							piso17 = pisoroto
																						else:
																							if dinoy == (p18y+50) and dinox == (p18x):
																								paso18 += 1
																								final += 1
																								piso18 = pisoroto
																							else:
																								if dinoy == (p19y+50) and dinox == (p19x):
																									paso19 += 1
																									final += 1
																									piso19 = pisoroto
																								else:
																									if dinoy == (p20y+50) and dinox == (p20x):
																										paso20 += 1
																										final += 1
																										piso20 = pisoroto
																									else:
																										if dinoy == (p21y+50) and dinox == (p21x):
																											paso21 += 1
																											final += 1
																											piso21 = pisoroto
																										else:
																											if dinoy == (p22y+50) and dinox == (p22x):
																												paso22 += 1
																												final += 1
																												piso22 = pisoroto



					if evento.key == pygame.K_e and (dinox == 500) and (dinoy == 357) and (prendido1 < 1):
						boton1 = botonon
						prendido1 += 1
						panta.blit(boton1,(bot1x, bot1y))
					else:
						if evento.key == pygame.K_e and (dinox == 500) and (dinoy == 407) and (prendido2 < 1):
							boton2 = botonon
							panta.blit(boton2,(bot2x, bot2y))
							prendido2 += 1



			if (dinox == 300): #Cambio de Limite para cuadrado
				limite_abajo = 457
				limite_arriba = 307 
			if (dinox == 250):
				limite_abajo = 407
				limite_arriba = 357
			
			
			if dinox == 300 and sumax < 0 and (dinoy != 407) and (dinoy != 357): #Limites extra adelante
				sumax = 0
			else:
				if dinox == 450 and sumax > 0:
					if dinoy == 457 or dinoy == 307:
						sumax = 0
			
			
			if final == 22 and dinox == 450: #Para el final
				limite_adelante = 500
				limite_abajo = 407
				limite_arriba = 357
			
			dinoy = sumay + dinoy
			dinox = sumax + dinox
			panta.blit(dinos,(dinox, dinoy))
			pygame.display.flip() 
			
			sumax = 0
			sumay = 0
			
			if (paso1 == 2): #Perder
				time.sleep(0.3)
				VOLVER = False
			else:
				if (paso2 == 2):
					time.sleep(muerte)
					VOLVER = False
				else:
					if (paso3 == 2):
						time.sleep(muerte)
						VOLVER = False
					else:
						if (paso4 == 2):
							time.sleep(muerte)
							VOLVER = False
						else:
							if (paso5 == 2):
								time.sleep(muerte)
								VOLVER = False
							else:
								if (paso6 == 2):
									time.sleep(muerte)
									VOLVER = False
								else:
									if (paso7 == 2):
										time.sleep(0.3)
										VOLVER = False
									else:
										if (paso8 == 2):
											time.sleep(muerte)
											VOLVER = False
										else:
											if (paso9 == 2):
												time.sleep(muerte)
												VOLVER = False
											else:
												if (paso10 == 2):
													time.sleep(muerte)
													VOLVER = False
												else:
													if (paso11 == 2):
														time.sleep(muerte)
														VOLVER = False
													else:
														if (paso12 == 2):
															time.sleep(muerte)
															VOLVER = False
														else:
															if (paso13 == 2):
																time.sleep(muerte)
																VOLVER = False
															else:
																if (paso14 == 2):
																	time.sleep(muerte)
																	VOLVER = False
																else:
																	if (paso15 == 2):
																		time.sleep(muerte)
																		VOLVER = False
																	else:
																		if (paso16 == 2):
																			time.sleep(muerte)
																			VOLVER = False
																		else:
																			if (paso17 == 2):
																				time.sleep(muerte)
																				VOLVER = False
																			else:
																				if (paso18 == 2):
																					time.sleep(muerte)
																					VOLVER = False
																				else:
																					if (paso19 == 2):
																						time.sleep(muerte)
																						VOLVER = False
																					else:
																						if (paso20 == 2):
																							time.sleep(muerte)
																							VOLVER = False
																						else:
																							if (paso21 == 2):
																								time.sleep(muerte)
																								VOLVER = False
																							else:
																								if (paso22 == 2):
																									time.sleep(muerte)
																									VOLVER = False

			
			if (prendido1 == 1) and (prendido2 == 1): #final
				pygame.display.flip()
				time.sleep(0.3)
				panta.blit(superado, (200, 150)) 
				pygame.display.flip()
				PREGUNTA = True
				while PREGUNTA:
					#print()
					for evento in pygame.event.get(): # (Segur no funciona todavía)
						if evento.type == MOUSEBUTTONDOWN:
							if (270 <= evento.pos[0] <= 356) and (365 <= evento.pos[1] <= 387):
								PREGUNTA = False
								VOLVER = False
								NIVEL2 = False

			#print(f"Preg: {PREGUNTA}     Volver:{VOLVER}     Nivel2: {NIVEL2}" ) #Esto es para ver mejor coordenadas y detectar errores.

