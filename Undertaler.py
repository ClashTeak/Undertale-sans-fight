import pygame, sys
from pygame.locals import *

pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((1000,800))
clock = pygame.time.Clock()

#                                    variable


pygame.mixer.music.load("Data/battle_music.wav")
pygame.mixer.music.queue("Data/battle_music.wav")
pygame.mixer.music.set_volume(70)
pygame.mixer.music.play()


black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
yellow = pygame.Color(255,213,0)
red = pygame.Color(221,0,16)
green = pygame.Color(0,219,42)

select_button = 1
select_act = 1
max_nb_act = 1

act_button_fight = False
act_button_act = False
act_button_item = False
act_button_mercy = False
act_all_button = False
fight_gaster = False
fight_chara = False

police = pygame.font.Font("Data/Mars_Needs_Cunnilingus.ttf",40)
police2 = pygame.font.Font("Data/DTM-Mono.otf",40)

affiche1 = police.render("Chara   LV 99999",1,black)

#                                         Pictures
cadre_img = pygame.transform.scale(pygame.image.load("Data/cadre.png"),(820,250))
cadre_fight = pygame.transform.scale(pygame.image.load("Data/cadre.png"),(850,200))
cadre_bord = pygame.transform.scale(pygame.image.load("Data/cadre_bord.png"),(820,250))
background = pygame.image.load("Data/background.png")
fight_barre = pygame.image.load("Data/fight_joge.png")
fight_bar_img = pygame.image.load("Data/fight_bar.png")

heart = pygame.transform.scale(pygame.image.load("Data/heart.png"),(30,30))

#sound
sound = [
	pygame.mixer.Sound("Data/sound/select_button_sound.wav"),
	pygame.mixer.Sound("Data/sound/unselect_button_sound.wav"),
]


#sprite
gaster_sprite = [
	pygame.transform.scale(pygame.image.load("Data/gaster_sprite_1.png"),(300,400)),
	pygame.transform.scale(pygame.image.load("Data/gaster_sprite_2.png"),(300,400)),
	pygame.transform.scale(pygame.image.load("Data/gaster_sprite_3.png"),(300,400)),
	pygame.transform.scale(pygame.image.load("Data/gaster_sprite_4.png"),(300,400)),
	pygame.transform.scale(pygame.image.load("Data/gaster_sprite2_5.png"),(280,313)),
	pygame.transform.scale(pygame.image.load("Data/gaster_sprite2_6.png"),(280,313)),
	pygame.transform.scale(pygame.image.load("Data/gaster_sprite2_7.png"),(280,313)),
	pygame.transform.scale(pygame.image.load("Data/gaster_sprite2_8.png"),(280,313)),
	pygame.transform.scale(pygame.image.load("Data/gaster_sprite2_bas_5.png"),(300,139)),
	pygame.transform.scale(pygame.image.load("Data/gaster_sprite2_haut_5.png"),(300,192)),
	pygame.transform.scale(pygame.image.load("Data/gaster_sprite2_bas_6.png"),(300,139)),
	pygame.transform.scale(pygame.image.load("Data/gaster_sprite2_haut_6.png"),(300,192)),
	pygame.transform.scale(pygame.image.load("Data/gaster_sprite2_bas_7.png"),(300,139)),
	pygame.transform.scale(pygame.image.load("Data/gaster_sprite2_haut_7.png"),(300,192)),
	pygame.transform.scale(pygame.image.load("Data/gaster_sprite2_bas_8.png"),(300,139)),
	pygame.transform.scale(pygame.image.load("Data/gaster_sprite2_haut_8.png"),(300,192)),
]

hit_sprites = [
	
]


#Buttons Pictures
buttons_fight = [
	pygame.transform.scale(pygame.image.load("Data/button_fight.png"),(170,70)),
	pygame.transform.scale(pygame.image.load("Data/button_fight_select.png"),(170,70)),
	pygame.transform.scale(pygame.image.load("Data/button_fight_appuyer.png"),(170,70)),
]
buttons_act = [
	pygame.transform.scale(pygame.image.load("Data/button_act.png"),(170,70)),
	pygame.transform.scale(pygame.image.load("Data/button_act_select.png"),(170,70)),
	pygame.transform.scale(pygame.image.load("Data/button_act_appuyer.png"),(170,70)),
]
buttons_item = [
	pygame.transform.scale(pygame.image.load("Data/button_item.png"),(170,70)),
	pygame.transform.scale(pygame.image.load("Data/button_item_select.png"),(170,70)),
	pygame.transform.scale(pygame.image.load("Data/button_item_appuyer.png"),(170,70)),
]
buttons_mercy = [
	pygame.transform.scale(pygame.image.load("Data/button_mercy.png"),(170,70)),
	pygame.transform.scale(pygame.image.load("Data/button_mercy_select.png"),(170,70)),
	pygame.transform.scale(pygame.image.load("Data/button_mercy_appuyer.png"),(170,70)),
]




#                                    Fonction
def test_enter_key():
	global act_button_fight
	global act_button_act
	global act_button_item
	global act_button_mercy
	global act_all_button
	
	if select_button == 1:
		act_all_button = True
		act_button_fight = True
		act_button_act = False
		act_button_item = False
		act_button_mercy =	False
	elif select_button == 2:
		act_all_button = True
		act_button_fight = False
		act_button_act = True
		act_button_item = False
		act_button_mercy =	False
	elif select_button == 3:
		act_all_button = True
		act_button_fight = False
		act_button_act = False
		act_button_item = True
		act_button_mercy =	False
	elif select_button == 4:
		act_all_button = True
		act_button_fight = False
		act_button_act = False
		act_button_item = False
		act_button_mercy =	True





#                                     class
class Cadre(pygame.sprite.Sprite):
	
	def __init__(self):
		
		self.x = 90
		self.y = 350
		
		self.image = cadre_img
		self.bord = cadre_bord
		
		pygame.sprite.Sprite.__init__(self)
	
	def update(self):
		
		
		self.rect = (self.x,self.y,self.image.get_width(),self.image.get_height())
		self.mask = pygame.mask.from_surface(self.bord)



class Button_fight:
	
	def __init__(self):
		
		self.x,self.y = 60,700
		self.image = buttons_fight[2]
		
		self.update()
	
	def update(self):
		
		self.rect = (self.x,self.y,self.image.get_width(),self.image.get_height())
		
		if select_button == 1:
			self.image = buttons_fight[2]
		else:
			self.image = buttons_fight[0]


class Button_act:
	
	def __init__(self):
		
		self.x,self.y = 300,700
		self.image = buttons_act[0]
		
		self.update()
	
	def update(self):
		
		self.rect = (self.x,self.y,self.image.get_width(),self.image.get_height())
		
		if select_button == 2:
			self.image = buttons_act[2]
		else:
			self.image = buttons_act[0]


class Button_item:
	
	def __init__(self):
		
		self.x,self.y = 540,700
		self.image = buttons_item[0]
		
		self.update()
	
	def update(self):
		
		self.rect = (self.x,self.y,self.image.get_width(),self.image.get_height())
		
		if select_button == 3:
			self.image = buttons_item[2]
		else:
			self.image = buttons_item[0]


class Button_mercy:
	
	def __init__(self):
		
		self.x,self.y = 780,700
		self.image = buttons_mercy[0]
		
		self.update()
	
	def update(self):
		
		self.rect = (self.x,self.y,self.image.get_width(),self.image.get_height())
		
		if select_button == 4:
			self.image = buttons_mercy[2]
		else:
			self.image = buttons_mercy[0]
		

class Gaster:
	
	cpt1 = 0
	cpt2 = 0
	
	def __init__(self):
		
		self.x,self.y = 320,0
		self.image = gaster_sprite[8]
		self.image2 = gaster_sprite[9]
		
		self.name = "* Gaster"
		self.hp = 800
		self.mhp = 1000
		
		self.affiche = police2.render(self.name+"         "+str(self.hp)+"/"+str(self.mhp),1,white)
		
		self.update()
	
	def update(self):
		self.cpt1 += 1
		self.cpt2 += 1
		
		if self.cpt2 == 40:
			self.image2 = gaster_sprite[9]
		if self.cpt2 == 80:
			self.image2 = gaster_sprite[11]
		if self.cpt2 == 120:
			self.image2 = gaster_sprite[13]
		if self.cpt2 == 160:
			self.image2 = gaster_sprite[15]
			self.cpt2 = 0
		
		if self.cpt1 == 10:
			self.image = gaster_sprite[8]
		if self.cpt1 == 20:
			self.image = gaster_sprite[10]
		if self.cpt1 == 30:
			self.image = gaster_sprite[12]
		if self.cpt1 == 40:
			self.image = gaster_sprite[14]
			self.cpt1 = 0
		
		self.rect = (self.x,self.y,self.image.get_width(),self.image.get_height())
		self.affiche = police2.render(self.name+"         "+str(self.hp)+"/"+str(self.mhp),1,white)
	
	
		
	
	def blit(self):
		
		window.blit(self.image,(self.x+20,self.y+210))
		window.blit(self.image2,(self.x+20,self.y+20))


class Chara(pygame.sprite.Sprite):
	
	def __init__(self):
		
		self.x = 500
		self.y = 400
		self.lx = 500
		self.ly = 400
		self.vx = 0
		self.vy = 0
		self.hp = 1000
		
		self.image = heart
		
		pygame.sprite.Sprite.__init__(self)
		self.update()
	
	def update(self):
		
		self.lx = self.x
		self.ly = self.y
		
		self.x += self.vx
		self.y += self.vy
		
		
		self.rect = (self.x,self.y,self.image.get_width(),self.image.get_height())
		self.mask = pygame.mask.from_surface(self.image)


class Chara_heart_menu:
	
	def __init__(self):
		
		self.x = 70
		self.y = 720
		
		self.image = heart
	
	def update(self):
		
		if act_all_button == False:
			if select_button == 1:
				self.x = 70
				self.y = 720
			if select_button == 2:
				self.x = 310
				self.y = 720
			if select_button == 3:
				self.x = 550
				self.y = 720
			if select_button == 4:
				self.x = 790
				self.y = 720
		
		elif act_all_button:
			if select_act == 1:
				self.x = 130
				self.y = 380
			if select_act == 2:
				self.x = 130
				self.y = 480
			
		
		self.rect = (self.x,self.y,self.image.get_width(),self.image.get_height())
	

class Fight_bar(pygame.sprite.Sprite):
	
	def __init__(self):
		
		self.x,self.y = 150,380
		self.vx = 7
		self.retour = 0
		
		self.image = fight_bar_img
		
		pygame.sprite.Sprite.__init__(self)
	
	def update(self):
		
		self.x += self.vx
		
		self.rect = (self.x,self.y,self.image.get_width(),self.image.get_height())
		self.mask = pygame.mask.from_surface(self.image)
		
		
		




cadre = Cadre()
button_fight = Button_fight()
button_act = Button_act()
button_item = Button_item()
button_mercy = Button_mercy()
gaster = Gaster()
chara = Chara()
chara_heart_menu = Chara_heart_menu()
fight_bar = Fight_bar()


class Fight_choice:
	
	def __init__(self):
		
		self.x = 180
		self.y = 370
		self.affiche_choice1 = gaster.affiche
		self.choice = ""
		
	
	def blit(self):
		self.calcul_heal = gaster.mhp/150
		pygame.draw.rect(window, red,(410,380,150,30))
		pygame.draw.rect(window, green,(410,380,gaster.hp/self.calcul_heal,30))
		window.blit(self.affiche_choice1,(self.x,self.y))
		

fight_choice = Fight_choice()


class Fight_barre:
	
	def __init__(self):
		
		self.x,self.y = 100,200
		
		self.image = fight_barre
	
	def update(self):
		
		self.rect = (self.x,self.y,self.image.get_width(),self.image.get_height())
	

fight_barre = Fight_barre()


#main boucle
continuer = True
while continuer:
	
	music_end = pygame.mixer.music.get_busy()
	
	affiche2 = police.render("HP     "+str(chara.hp)+"/1000",1,black)
	
	for event in pygame.event.get():
		
		if event.type == QUIT:
			pygame.mixer.music.stop()
			pygame.quit()
			sys.exit()
			
		if event.type == KEYDOWN:
			if event.key == K_RIGHT:
				if fight_chara == False or fight_gaster == False:
					if act_all_button == False:
						if select_button < 4:
							sound[1].play()
							select_button += 1
			if event.key == K_LEFT:
				if fight_chara == False or fight_gaster == False:
					if act_all_button == False:
						if select_button > 1:
							sound[1].play()
							select_button -= 1
			if event.key == K_UP:
				if fight_chara == False or fight_gaster == False:
					if act_all_button:
						if select_act > 1:
							sound[1].play()
							select_act -= 1
			if event.key == K_DOWN:
				if fight_chara == False or fight_gaster == False:
					if act_all_button:
						if select_act < max_nb_act:
							sound[1].play()
							select_act += 1
			
			
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
			
			if event.key == K_x:
				if fight_chara == False:
					select_act = 1
					act_all_button = False
					act_button_act = False
					act_button_fight = False
					act_button_item = False
					act_button_mercy = False
			
			if event.key == K_RETURN:
				if fight_chara == False:
					sound[0].play()
					if act_button_fight:
						if select_act == 1:
							fight_choice.choice = "gaster"
							fight_chara = True
							act_button_fight = False
					if act_all_button == False:
						test_enter_key()
				
				elif fight_chara:
					fight_bar.vx = 0
				
	
	
	if music_end == False:
		pygame.mixer.music.play()
	
	
	#class update()
	cadre.update()
	button_fight.update()
	button_act.update()
	button_item.update()
	button_mercy.update()
	gaster.update()
	chara_heart_menu.update()
	fight_barre.update()
	if fight_chara:
		fight_bar.update()
	
	window.fill(white)
	window.blit(background,(50,0))
	window.blit(cadre.image,cadre.rect)
	window.blit(cadre.bord,cadre.rect)
	
	if act_button_fight:
		max_nb_act = 1
		fight_choice.blit()
	if act_button_act:
		max_nb_act = 2
	if act_button_item:
		max_nb_act = 2
	if act_button_mercy:
		max_nb_act = 1
	
	
	if fight_chara:
		window.blit(fight_barre.image,fight_barre.rect)
		window.blit(fight_bar.image,fight_bar.rect)
		if pygame.sprite.collide_mask(cadre,fight_bar) != None:
			if fight_bar.retour == 0:
				fight_bar.retour = 1
				fight_bar.x -= 10
				fight_bar.vx = -7
			elif fight_bar.retour == 1:
				fight_bar.vx = 0
	
	
	#object
	gaster.blit()
	
	#button blit
	window.blit(button_fight.image,button_fight.rect)
	window.blit(button_act.image,button_act.rect)
	window.blit(button_item.image,button_item.rect)
	window.blit(button_mercy.image,button_mercy.rect)
	
	window.blit(affiche1,(50,640))
	window.blit(affiche2,(500,640))
	pygame.draw.rect(window, red,(555,645,55,30))
	
	if fight_chara == False:
		window.blit(chara_heart_menu.image,chara_heart_menu.rect)
	
	if chara.hp/9 > 0:
		pygame.draw.rect(window, yellow,(555,645,chara.hp/18,30))
	
	pygame.display.update()
	clock.tick(60)
	
	
