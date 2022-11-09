import pygame
import os
import time
import random
pygame.init()
pygame.font.init()

win = pygame.display.set_mode((1250, 700))
clock = pygame.time.Clock()
STAT_FONT = pygame.font.SysFont("broadway", 25)
title = pygame.font.SysFont("broadway", 75)
run = True

BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("pokertable.jpg")))
backofcard = pygame.transform.scale2x(pygame.image.load(os.path.join("backofcard.png")))
tenofhearts = pygame.image.load(os.path.join("tenofhearts.png"))
sixofclubs = pygame.image.load(os.path.join("sixofclubs.png"))
queenofclubs = pygame.image.load(os.path.join("queenofclubs.png"))
aceofhearts = pygame.image.load(os.path.join("aceofhearts.png"))
sevenofdiamonds = pygame.image.load(os.path.join("sevenofdiamonds.png"))
tenofclubs = pygame.image.load(os.path.join("tenofclubs.png")) 
jackofclubs = pygame.image.load(os.path.join("jackofclubs.png"))
jackofspades = pygame.image.load(os.path.join("jackofspades.png"))
threeofdiamonds = pygame.image.load(os.path.join("threeofdiamonds.png"))
nineofclubs = pygame.image.load(os.path.join("nineofclubs.png"))
queenofhearts = pygame.image.load(os.path.join("queenofhearts.png"))
tenofdiamonds = pygame.image.load(os.path.join("tenofdiamonds.png"))
threeofhearts = pygame.image.load(os.path.join("threeofhearts.png"))
kingofclubs = pygame.image.load(os.path.join("kingofclubs.png")) 
sixofspades = pygame.image.load(os.path.join("sixofspades.png"))
nineofdiamonds = pygame.image.load(os.path.join("nineofdiamonds.png")) 
fourofdiamonds = pygame.image.load(os.path.join("fourofdiamonds.png")) 
eightofclubs = pygame.image.load(os.path.join("eightofclubs.png"))
nineofhearts = pygame.image.load(os.path.join("nineofhearts.png"))
queenofspades = pygame.image.load(os.path.join("queenofspades.png"))
twoofdiamonds = pygame.image.load(os.path.join("twoofdiamonds.png")) 
kingofhearts = pygame.image.load(os.path.join("kingofhearts.png")) 
sixofdiamonds = pygame.image.load(os.path.join("sixofdiamonds.png")) 
threeofspades = pygame.image.load(os.path.join("threeofspades.png")) 
sevenofhearts = pygame.image.load(os.path.join("sevenofhearts.png"))
threeofclubs = pygame.image.load(os.path.join("threeofclubs.png")) 
fiveofclubs = pygame.image.load(os.path.join("fiveofclubs.png"))

pile1A = [tenofhearts, sixofclubs, queenofclubs, aceofhearts, sevenofdiamonds, tenofclubs, jackofclubs, jackofspades, threeofdiamonds]
pile2A = [nineofclubs, queenofhearts, tenofdiamonds, threeofhearts, kingofclubs, sixofspades, nineofdiamonds, fourofdiamonds, eightofclubs]
pile3A = [nineofhearts, queenofspades, twoofdiamonds, kingofhearts, sixofdiamonds, threeofspades, sevenofhearts, threeofclubs, fiveofclubs]

pile1B = [pile3A[6], pile3A[3], pile3A[0], pile2A[6], pile2A[3], pile2A[0], pile1A[6], pile1A[3], pile1A[0]]
pile2B = [pile3A[7], pile3A[4], pile3A[1], pile2A[7], pile2A[4], pile2A[1], pile1A[7], pile1A[4], pile1A[1]]
pile3B = [pile3A[8], pile3A[5], pile3A[2], pile2A[8], pile2A[5], pile2A[2], pile1A[8], pile1A[5], pile1A[2]]

def reveal(card):
	redrawGameWindow()
	y = -200
	while y<175:
		redrawGameWindow5()
		win.blit(pygame.transform.scale2x(card),(525,y))
		y += 3
		pygame.display.update()
	loop = True
	while loop:
		clock.tick(50)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				return run
				loop = False

def roundThree(pile1D, pile2D, pile3D):
	redrawGameWindow()
	loop = True
	while loop:
		clock.tick(50)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				return run
				loop = False
		text = STAT_FONT.render("Row 1", 1, (255, 255, 255))
		win.blit(text, (25, 75))
		text = STAT_FONT.render("Row 2", 1, (255, 255, 255))
		win.blit(text, (25, 275))
		text = STAT_FONT.render("Row 3", 1, (255, 255, 255))
		win.blit(text, (25, 475))
		pygame.display.update()
		x2 = 1250
		x = 130
		while x2>x:
			redrawGameWindow4()
			win.blit(pile1D[0],(x2,50)), win.blit(pile1D[1],(x2+(1*125),50)), win.blit(pile1D[2],(x2+(2*125),50)), win.blit(pile1D[3],(x2+(3*125),50)), win.blit(pile1D[4],(x2+(4*125),50)), win.blit(pile1D[5],(x2+(5*125),50)), win.blit(pile1D[6],(x2+(6*125),50)), win.blit(pile1D[7],(x2+(7*125),50)), win.blit(pile1D[8],(x2+(8*125),50))
			win.blit(pile2D[0],(x2,250)), win.blit(pile2D[1],(x2+(1*125),250)), win.blit(pile2D[2],(x2+(2*125),250)), win.blit(pile2D[3],(x2+(3*125),250)), win.blit(pile2D[4],(x2+(4*125),250)), win.blit(pile2D[5],(x2+(5*125),250)), win.blit(pile2D[6],(x2+(6*125),250)), win.blit(pile2D[7],(x2+(7*125),250)), win.blit(pile2D[8],(x2+(8*125),250))
			win.blit(pile3D[0],(x2,450)), win.blit(pile3D[1],(x2+(1*125),450)), win.blit(pile3D[2],(x2+(2*125),450)), win.blit(pile3D[3],(x2+(3*125),450)), win.blit(pile3D[4],(x2+(4*125),450)), win.blit(pile3D[5],(x2+(5*125),450)), win.blit(pile3D[6],(x2+(6*125),450)), win.blit(pile3D[7],(x2+(7*125),450)), win.blit(pile3D[8],(x2+(8*125),450))
			x2 -= 10
			pygame.display.update()
		text = title.render("Which row has your card?", 1, (255, 255, 255))
		win.blit(text, (100, 600))
		pygame.display.update()
		loop2 = True
		while loop2:
			clock.tick(50)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
					return run
					loop2 = False
			keys = pygame.key.get_pressed()
			if keys[pygame.K_1]:
				run = reveal(pile1D[6])
				return run
			elif keys[pygame.K_2]:
				run = reveal(pile2D[6])
				return run 
			elif keys[pygame.K_3]:
				run = reveal(pile3D[6])
				return run 

def roundTwo(pile1C, pile2C, pile3C):
	redrawGameWindow()
	loop = True
	while loop:
		clock.tick(50)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				return run
				loop = False
		text = STAT_FONT.render("Row 1", 1, (255, 255, 255))
		win.blit(text, (25, 75))
		text = STAT_FONT.render("Row 2", 1, (255, 255, 255))
		win.blit(text, (25, 275))
		text = STAT_FONT.render("Row 3", 1, (255, 255, 255))
		win.blit(text, (25, 475))
		pygame.display.update()
		x2 = 1250
		x = 130
		while x2>x:
			redrawGameWindow4()
			win.blit(pile1C[0],(x2,50)), win.blit(pile1C[1],(x2+(1*125),50)), win.blit(pile1C[2],(x2+(2*125),50)), win.blit(pile1C[3],(x2+(3*125),50)), win.blit(pile1C[4],(x2+(4*125),50)), win.blit(pile1C[5],(x2+(5*125),50)), win.blit(pile1C[6],(x2+(6*125),50)), win.blit(pile1C[7],(x2+(7*125),50)), win.blit(pile1C[8],(x2+(8*125),50))
			win.blit(pile2C[0],(x2,250)), win.blit(pile2C[1],(x2+(1*125),250)), win.blit(pile2C[2],(x2+(2*125),250)), win.blit(pile2C[3],(x2+(3*125),250)), win.blit(pile2C[4],(x2+(4*125),250)), win.blit(pile2C[5],(x2+(5*125),250)), win.blit(pile2C[6],(x2+(6*125),250)), win.blit(pile2C[7],(x2+(7*125),250)), win.blit(pile2C[8],(x2+(8*125),250))
			win.blit(pile3C[0],(x2,450)), win.blit(pile3C[1],(x2+(1*125),450)), win.blit(pile3C[2],(x2+(2*125),450)), win.blit(pile3C[3],(x2+(3*125),450)), win.blit(pile3C[4],(x2+(4*125),450)), win.blit(pile3C[5],(x2+(5*125),450)), win.blit(pile3C[6],(x2+(6*125),450)), win.blit(pile3C[7],(x2+(7*125),450)), win.blit(pile3C[8],(x2+(8*125),450))
			x2 -= 10
			pygame.display.update()
		text = title.render("Which row has your card?", 1, (255, 255, 255))
		win.blit(text, (100, 600))
		pygame.display.update()
		loop2 = True
		while loop2:
			clock.tick(50)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
					return run
					loop2 = False
			keys = pygame.key.get_pressed()
			if keys[pygame.K_1]:
				pile1D = [pile3C[6], pile3C[3], pile3C[0], pile2C[6], pile2C[3], pile2C[0], pile1C[6], pile1C[3], pile1C[0]]
				pile2D = [pile3C[7], pile3C[4], pile3C[1], pile2C[7], pile2C[4], pile2C[1], pile1C[7], pile1C[4], pile1C[1]]
				pile3D = [pile3C[8], pile3C[5], pile3C[2], pile2C[8], pile2C[5], pile2C[2], pile1C[8], pile1C[5], pile1C[2]]
				run = roundThree(pile1D, pile2D, pile3D)
				return run 
			elif keys[pygame.K_2]:
				pile1D = [pile3C[6], pile3C[3], pile3C[0], pile1C[6], pile1C[3], pile1C[0], pile2C[6], pile2C[3], pile2C[0]]
				pile2D = [pile3C[7], pile3C[4], pile3C[1], pile1C[7], pile1C[4], pile1C[1], pile2C[7], pile2C[4], pile2C[1]]
				pile3D = [pile3C[8], pile3C[5], pile3C[2], pile1C[8], pile1C[5], pile1C[2], pile2C[8], pile2C[5], pile2C[2]]
				run = roundThree(pile1D, pile2D, pile3D)
				return run
			elif keys[pygame.K_3]:
				pile1D = [pile2C[6], pile2C[3], pile2C[0], pile1C[6], pile1C[3], pile1C[0], pile3C[6], pile3C[3], pile3C[0]]
				pile2D = [pile2C[7], pile2C[4], pile2C[1], pile1C[7], pile1C[4], pile1C[1], pile3C[7], pile3C[4], pile3C[1]]
				pile3D = [pile2C[8], pile2C[5], pile2C[2], pile1C[8], pile1C[5], pile1C[2], pile3C[8], pile3C[5], pile3C[2]]
				run = roundThree(pile1D, pile2D, pile3D)
				return run 

def roundOne():
	redrawGameWindow()
	loop = True
	while loop:
		clock.tick(50)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				return run
				loop = False
		text = STAT_FONT.render("Row 1", 1, (255, 255, 255))
		win.blit(text, (25, 75))
		text = STAT_FONT.render("Row 2", 1, (255, 255, 255))
		win.blit(text, (25, 275))
		text = STAT_FONT.render("Row 3", 1, (255, 255, 255))
		win.blit(text, (25, 475))
		pygame.display.update()
		x2 = 1250
		x = 130
		while x2>x:
			redrawGameWindow4()
			win.blit(pile1B[0],(x2,50)), win.blit(pile1B[1],(x2+(1*125),50)), win.blit(pile1B[2],(x2+(2*125),50)), win.blit(pile1B[3],(x2+(3*125),50)), win.blit(pile1B[4],(x2+(4*125),50)), win.blit(pile1B[5],(x2+(5*125),50)), win.blit(pile1B[6],(x2+(6*125),50)), win.blit(pile1B[7],(x2+(7*125),50)), win.blit(pile1B[8],(x2+(8*125),50))
			win.blit(pile2B[0],(x2,250)), win.blit(pile2B[1],(x2+(1*125),250)), win.blit(pile2B[2],(x2+(2*125),250)), win.blit(pile2B[3],(x2+(3*125),250)), win.blit(pile2B[4],(x2+(4*125),250)), win.blit(pile2B[5],(x2+(5*125),250)), win.blit(pile2B[6],(x2+(6*125),250)), win.blit(pile2B[7],(x2+(7*125),250)), win.blit(pile2B[8],(x2+(8*125),250))
			win.blit(pile3B[0],(x2,450)), win.blit(pile3B[1],(x2+(1*125),450)), win.blit(pile3B[2],(x2+(2*125),450)), win.blit(pile3B[3],(x2+(3*125),450)), win.blit(pile3B[4],(x2+(4*125),450)), win.blit(pile3B[5],(x2+(5*125),450)), win.blit(pile3B[6],(x2+(6*125),450)), win.blit(pile3B[7],(x2+(7*125),450)), win.blit(pile3B[8],(x2+(8*125),450))
			x2 -= 10
			pygame.display.update()
		text = title.render("Which row has your card?", 1, (255, 255, 255))
		win.blit(text, (100, 600))
		pygame.display.update()
		loop2 = True
		while loop2:
			clock.tick(50)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
					return run
					loop2 = False
			keys = pygame.key.get_pressed()
			if keys[pygame.K_1]:
				pile1C = [pile1A[8], pile2A[8], pile3A[8], pile1A[7], pile2A[7], pile3A[7], pile1A[6], pile2A[6], pile3A[6]]
				pile2C = [pile1A[5], pile2A[5], pile3A[5], pile1A[4], pile2A[4], pile3A[4], pile1A[3], pile2A[3], pile3A[3]]
				pile3C = [pile1A[2], pile2A[2], pile3A[2], pile1A[1], pile2A[1], pile3A[1], pile1A[0], pile2A[0], pile3A[0]]
				run = roundTwo(pile1C, pile2C, pile3C)
				return run
			elif keys[pygame.K_2]:
				pile1C = [pile1A[8], pile2A[8], pile3A[8], pile1A[6], pile2A[6], pile3A[6], pile1A[7], pile2A[7], pile3A[7]]
				pile2C = [pile1A[5], pile2A[5], pile3A[5], pile1A[3], pile2A[3], pile3A[3], pile1A[4], pile2A[4], pile3A[4]]
				pile3C = [pile1A[2], pile2A[2], pile3A[2], pile1A[0], pile2A[0], pile3A[0], pile1A[1], pile2A[1], pile3A[1]]
				run = roundTwo(pile1C, pile2C, pile3C)
				return run
			elif keys[pygame.K_3]:
				pile1C = [pile1A[7], pile2A[7], pile3A[7], pile1A[6], pile2A[6], pile3A[6], pile1A[8], pile2A[8], pile3A[8]]
				pile2C = [pile1A[4], pile2A[4], pile3A[4], pile1A[3], pile2A[3], pile3A[3], pile1A[5], pile2A[5], pile3A[5]]
				pile3C = [pile1A[1], pile2A[1], pile3A[1], pile1A[0], pile2A[0], pile3A[0], pile1A[2], pile2A[2], pile3A[2]]
				run = roundTwo(pile1C, pile2C, pile3C)
				return run

def choice():
	y = 125
	loop = True
	while loop:
		clock.tick(50)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				return run
				loop = False
		win.blit(backofcard, (200,125))
		text = STAT_FONT.render("Pile 1", 1, (255, 255, 255))
		win.blit(text, (260,425))
		win.blit(backofcard, (500,125))
		text = STAT_FONT.render("Pile 2", 1, (255, 255, 255))
		win.blit(text, (560,425))
		win.blit(backofcard, (800,125))
		text = STAT_FONT.render("Pile 3", 1, (255, 255, 255))
		win.blit(text, (860,425))
		text = title.render("CHOOSE A PILE OF CARDS", 1, (255, 255, 255))
		win.blit(text, (115,525))
		pygame.display.update()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_1]:
			while y<200:
				win.blit(backofcard, (200,y))
				win.blit(backofcard, (500,125))
				text = STAT_FONT.render("Pile 2", 1, (255, 255, 255))
				win.blit(text, (560,425))
				win.blit(backofcard, (800,125))
				text = STAT_FONT.render("Pile 3", 1, (255, 255, 255))
				win.blit(text, (860,425))
				text = title.render("CHOOSE A PILE OF CARDS", 1, (255, 255, 255))
				win.blit(text, (115,525))
				pygame.display.update()
				redrawGameWindow1()
				y += 1
			while y>-500:
				win.blit(backofcard, (200,y))
				win.blit(backofcard, (500,125))
				text = STAT_FONT.render("Pile 2", 1, (255, 255, 255))
				win.blit(text, (560,425))
				win.blit(backofcard, (800,125))
				text = STAT_FONT.render("Pile 3", 1, (255, 255, 255))
				win.blit(text, (860,425))
				text = title.render("CHOOSE A PILE OF CARDS", 1, (255, 255, 255))
				win.blit(text, (115,525))
				pygame.display.update()
				redrawGameWindow1()
				y -= 7
			y2 = 700
			while y2>75:
				redrawGameWindow()
				x2 = 50
				for i in range(9):
					win.blit(pile1A[i], (x2,y2))
					pygame.display.update()
					x2 += 150
				y2 -= 7
			text = title.render("Choose and remember", 1, (255, 255, 255))
			win.blit(text, (150,300))
			text = title.render("one of these cards!", 1, (255, 255, 255))
			win.blit(text, (250,400))
			text = STAT_FONT.render("Press spacebar to continue", 1, (255, 255, 255))
			win.blit(text, (425,550))
			pygame.display.update()
			loop2 = True
			while loop2:
				clock.tick(50)
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						run = False
						return run
						loop2 = False
				keys = pygame.key.get_pressed()
				if keys[pygame.K_SPACE]:
					run = roundOne() 
					return run

		if keys[pygame.K_2]:
			while y<200:
				win.blit(backofcard, (500,y))
				win.blit(backofcard, (200,125))
				text = STAT_FONT.render("Pile 1", 1, (255, 255, 255))
				win.blit(text, (260,425))
				win.blit(backofcard, (800,125))
				text = STAT_FONT.render("Pile 3", 1, (255, 255, 255))
				win.blit(text, (860,425))
				text = title.render("CHOOSE A PILE OF CARDS", 1, (255, 255, 255))
				win.blit(text, (115,525))
				pygame.display.update()
				redrawGameWindow2()
				y += 1
			while y>-500:
				win.blit(backofcard, (500,y))
				win.blit(backofcard, (200,125))
				text = STAT_FONT.render("Pile 1", 1, (255, 255, 255))
				win.blit(text, (260,425))
				win.blit(backofcard, (800,125))
				text = STAT_FONT.render("Pile 3", 1, (255, 255, 255))
				win.blit(text, (860,425))
				text = title.render("CHOOSE A PILE OF CARDS", 1, (255, 255, 255))
				win.blit(text, (115,525))
				pygame.display.update()
				redrawGameWindow2()
				y -= 7
			y2 = 700
			while y2>75:
				redrawGameWindow()
				x2 = 50
				for i in range(9):
					win.blit(pile2A[i], (x2,y2))
					pygame.display.update()
					x2 += 150
				y2 -= 7
			text = title.render("Choose and remember", 1, (255, 255, 255))
			win.blit(text, (150,300))
			text = title.render("one of these cards!", 1, (255, 255, 255))
			win.blit(text, (250,400))
			text = STAT_FONT.render("Press spacebar to continue", 1, (255, 255, 255))
			win.blit(text, (425,550))
			pygame.display.update()
			loop2 = True
			while loop2:
				clock.tick(50)
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						run = False
						return run
						loop2 = False
				keys = pygame.key.get_pressed()
				if keys[pygame.K_SPACE]:
					run = roundOne() 
					return run				

		if keys[pygame.K_3]:
			while y<200:
				win.blit(backofcard, (800,y))
				win.blit(backofcard, (200,125))
				text = STAT_FONT.render("Pile 1", 1, (255, 255, 255))
				win.blit(text, (260,425))
				win.blit(backofcard, (500,125))
				text = STAT_FONT.render("Pile 2", 1, (255, 255, 255))
				win.blit(text, (560,425))
				text = title.render("CHOOSE A PILE OF CARDS", 1, (255, 255, 255))
				win.blit(text, (115,525))
				pygame.display.update()
				redrawGameWindow3()
				y += 1
			while y>-500:
				win.blit(backofcard, (800,y))
				win.blit(backofcard, (200,125))
				text = STAT_FONT.render("Pile 1", 1, (255, 255, 255))
				win.blit(text, (260,425))
				win.blit(backofcard, (500,125))
				text = STAT_FONT.render("Pile 2", 1, (255, 255, 255))
				win.blit(text, (560,425))
				text = title.render("CHOOSE A PILE OF CARDS", 1, (255, 255, 255))
				win.blit(text, (115,525))
				pygame.display.update()
				redrawGameWindow3()
				y -= 7
			y2 = 700
			while y2>75:
				redrawGameWindow()
				x2 = 50
				for i in range(9):
					win.blit(pile3A[i], (x2,y2))
					pygame.display.update()
					x2 += 150
				y2 -= 7
			text = title.render("Choose and remember", 1, (255, 255, 255))
			win.blit(text, (150,300))
			text = title.render("one of these cards!", 1, (255, 255, 255))
			win.blit(text, (250,400))
			text = STAT_FONT.render("Press spacebar to continue", 1, (255, 255, 255))
			win.blit(text, (425,550))
			pygame.display.update()
			loop2 = True
			while loop2:
				clock.tick(50)
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						run = False
						return run
						loop2 = False
				keys = pygame.key.get_pressed()
				if keys[pygame.K_SPACE]:
					run = roundOne() 
					return run		

def redrawGameWindow1():
	win.blit(BG_IMG, (0,0))
	win.blit(backofcard, (500,125))
	text = STAT_FONT.render("Pile 2", 1, (255, 255, 255))
	win.blit(text, (560,425))
	win.blit(backofcard, (800,125))
	text = STAT_FONT.render("Pile 3", 1, (255, 255, 255))
	win.blit(text, (860,425))
	text = title.render("CHOOSE A PILE OF CARDS", 1, (255, 255, 255))
	win.blit(text, (115,525))
	pygame.display.update()
def redrawGameWindow2():
	win.blit(BG_IMG, (0,0))
	win.blit(backofcard, (200,125))
	text = STAT_FONT.render("Pile 1", 1, (255, 255, 255))
	win.blit(text, (260,425))
	win.blit(backofcard, (800,125))
	text = STAT_FONT.render("Pile 3", 1, (255, 255, 255))
	win.blit(text, (860,425))
	text = title.render("CHOOSE A PILE OF CARDS", 1, (255, 255, 255))
	win.blit(text, (115,525))
	pygame.display.update()
def redrawGameWindow3():
	win.blit(BG_IMG, (0,0))
	win.blit(backofcard, (200,125))
	text = STAT_FONT.render("Pile 1", 1, (255, 255, 255))
	win.blit(text, (260,425))
	win.blit(backofcard, (500,125))
	text = STAT_FONT.render("Pile 2", 1, (255, 255, 255))
	win.blit(text, (560,425))
	text = title.render("CHOOSE A PILE OF CARDS", 1, (255, 255, 255))
	win.blit(text, (115,525))
	pygame.display.update()

def redrawGameWindow4():
	win.blit(BG_IMG, (0,0))
	text = STAT_FONT.render("Row 1", 1, (255, 255, 255))
	win.blit(text, (25, 75))
	text = STAT_FONT.render("Row 2", 1, (255, 255, 255))
	win.blit(text, (25, 275))
	text = STAT_FONT.render("Row 3", 1, (255, 255, 255))
	win.blit(text, (25, 475))
	pygame.display.update()

def redrawGameWindow5():
	win.blit(BG_IMG, (0,0))
	text = title.render("Is this your card?", 1, (255, 255, 255))
	win.blit(text, (300, 475))
	pygame.display.update()

def redrawGameWindow():
	win.blit(BG_IMG, (0,0))
	pygame.display.update()

loop = True
while loop:
	clock.tick(50)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			loop = False
	text = title.render("MAGIC PREDICTION", 1, (255, 255, 255))
	win.blit(text, (240,50))
	text = STAT_FONT.render("Card Trick by Ryan Hayashi", 1, (255, 255, 255))
	win.blit(text, (450,200))
	text = STAT_FONT.render("Programmed by Matthew Kalichman and Mikayla Anders", 1, (255, 255, 255))
	win.blit(text, (250,275))
	text = title.render("PRESS SPACEBAR", 1, (255, 255, 255))
	win.blit(text, (300,500))
	pygame.display.update()
	keys = pygame.key.get_pressed()
	if keys[pygame.K_SPACE]:
		loop = False

while run:
	clock.tick(50)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	redrawGameWindow()
	run = choice()

pygame.quit()