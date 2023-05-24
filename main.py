#IMPORT
import pygame
import button

pygame.init()

#SCREEN DISPLAY
screen = pygame.display.set_mode((1540, 840))
pygame.display.set_caption("From Dream to Reality")
pygame.init()
window = pygame.display.set_mode((1540, 840))
pygame.display.set_caption("From Dream to Reality")
clock = pygame.time.Clock()

#BACKGROUNDS
background1 = pygame.image.load('bg1.jpg')
background2 = pygame.image.load('bg2.png')
background3 = pygame.image.load('bg_normal.png')
background4 = pygame.image.load('bg_oily.png')
background5 = pygame.image.load('bg_dry.png')
background6 = pygame.image.load('bg_sensitive.png')
background7 = pygame.image.load('bg_combination.png')
background8 = pygame.image.load('normal_dos.png')
background9 = pygame.image.load('normal_donts.png')
background10 = pygame.image.load('oily_dos.png')
background11 = pygame.image.load('oily_donts.png')
background12 = pygame.image.load('dry_dos.png')
background13 = pygame.image.load('dry_donts.png')
background14 = pygame.image.load('sensitive_dos.png')
background15 = pygame.image.load('sensitive_donts.png')
background16 = pygame.image.load('combination_dos.png')
background17 = pygame.image.load('combination_donts.png')
background38 = pygame.image.load('quotebg.jpg')

image1 = pygame.transform.scale(background1, (1540, 840))
image2 = pygame.transform.scale(background2, (1540, 840))
image3 = pygame.transform.scale(background3, (1540, 840))
image4 = pygame.transform.scale(background4, (1540, 840))
image5 = pygame.transform.scale(background5, (1540, 840))
image6 = pygame.transform.scale(background6, (1540, 840))
image7 = pygame.transform.scale(background7, (1540, 840))
image8 = pygame.transform.scale(background8, (1540, 840))
image9 = pygame.transform.scale(background9, (1540, 840))
image10 = pygame.transform.scale(background10, (1540, 840))
image11 = pygame.transform.scale(background11, (1540, 840))
image12 = pygame.transform.scale(background12, (1540, 840))
image13 = pygame.transform.scale(background13, (1540, 840))
image14 = pygame.transform.scale(background14, (1540, 840))
image15 = pygame.transform.scale(background15, (1540, 840))
image16 = pygame.transform.scale(background16, (1540, 840))
image17 = pygame.transform.scale(background17, (1540, 840))
image38 = pygame.transform.scale(background38, (1540, 840))

#ICON
img = pygame.image.load('icon.png')
pygame.display.set_icon(img)

#BACKGROUND MUSIC
file = 'humoresque_bgm.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)

game_paused = False
menu_state = "main"

font = pygame.font.Font("Minecraft.ttf", 30)
TEXT_COL = (0, 0, 0)

#IMAGES
#WELCOME IMAGE
button1_img = pygame.image.load("button1.png").convert_alpha()
button2_img = pygame.image.load("button2.png").convert_alpha()
button3_img = pygame.image.load("button3.png").convert_alpha()

#BACK IMAGE
bckbutton_img = pygame.image.load("bckbutton.png").convert_alpha()

#START IMAGE
start_img = pygame.image.load("start.png").convert_alpha()

#FIVE SKIN TYPE CHOICES IMAGE
maegels1_img = pygame.image.load("maegels1.png").convert_alpha()
maegels2_img = pygame.image.load("maegels2.png").convert_alpha()
maegels3_img = pygame.image.load("maegels3.png").convert_alpha()
maegels4_img = pygame.image.load("maegels4.png").convert_alpha()
maegels5_img = pygame.image.load("maegels5.png").convert_alpha()

#NEXT IMAGE
nextbutton_img = pygame.image.load("nextbutton.png").convert_alpha()
nextbutton1_img = pygame.image.load("nextbutton.png").convert_alpha()

#HOME IMAGE
backtostart_img = pygame.image.load("backtostart.png").convert_alpha()

#WELCOME BUTTON
button1_img = button.Button(454, 20, button1_img, 1)
button2_img = button.Button(440, 250, button2_img, 1)
button3_img = button.Button(440, 500, button3_img, 1)

#BACK BUTTON
bckbutton_img = button.Button(5, 5, bckbutton_img, 0.13)

#START BUTTON
start_img = button.Button(1335, 710, start_img, 0.3)

#FIVE SKIN TYPE CHOICES BUTTON
maegels1_img = button.Button(75, 230, maegels1_img, 0.7)
maegels2__img = button.Button(540, 230, maegels2_img, 0.7)
maegels3_mg = button.Button(1007, 230, maegels3_img, 0.7)
maegels4_img = button.Button(300, 450, maegels4_img, 0.7)
maegels5_img = button.Button(780, 450, maegels5_img, 0.7)

#NEXT BUTTON
nextbutton_img = button.Button(1460, 5, nextbutton_img, 0.13)
nextbutton1_img = button.Button(75, 8, nextbutton1_img, 0.12)

#HOME BUTTON
backtostart_img = button.Button(1470, 5, backtostart_img, 0.18)

#NORMAL SKIN CARE PRODUCTS
background18 = pygame.image.load('normalcleanserbg.png')
background19 = pygame.image.load('normaltonerbg.png')
background20 = pygame.image.load('normalmoisturizerbg.png')
background21 = pygame.image.load('normalsunscreenbg.png')

image18 = pygame.transform.scale(background18, (1540, 840))
image19 = pygame.transform.scale(background19, (1540, 840))
image20 = pygame.transform.scale(background20, (1540, 840))
image21 = pygame.transform.scale(background21, (1540, 840))

normcleanser_img = pygame.image.load("normcleanser.png").convert_alpha()
normtoner_img = pygame.image.load("normtoner.png").convert_alpha()
normmoisturizer_img = pygame.image.load("normmoisturizer.png").convert_alpha()
normsunscreen_img = pygame.image.load("normsunscreen.png").convert_alpha()

normcleanser_img = button.Button(200, 250, normcleanser_img, 0.5)
normtoner_img = button.Button(550, 240, normtoner_img, 0.5)
normmoisturizer_img = button.Button(850, 250, normmoisturizer_img, 0.5)
normsunscreen_img = button.Button(1200, 250, normsunscreen_img, 0.5)

#OILY SKIN CARE PRODUCTS
background30 = pygame.image.load('oilycleanserbg.jpeg')
background31 = pygame.image.load('oilytonerbg.jpeg')
background32 = pygame.image.load('oilymoisturizerbg.jpeg')
background33 = pygame.image.load('oilysunscreenbg.jpeg')

image30 = pygame.transform.scale(background30, (1540, 840))
image31 = pygame.transform.scale(background31, (1540, 840))
image32 = pygame.transform.scale(background32, (1540, 840))
image33 = pygame.transform.scale(background33, (1540, 840))

oilycleanser_img = pygame.image.load("oilycleanser.png").convert_alpha()
oilytoner_img = pygame.image.load("oilytoner.png").convert_alpha()
oilymoisturizer_img = pygame.image.load("oilymoisturizer.png").convert_alpha()
oilysunscreen_img = pygame.image.load("oilysunscreen.png").convert_alpha()

oilycleanser_img = button.Button(200, 250, oilycleanser_img, 0.5)
oilytoner_img = button.Button(550, 270, oilytoner_img, 0.5)
oilymoisturizer_img = button.Button(850, 270, oilymoisturizer_img, 0.5)
oilysunscreen_img = button.Button(1200, 250, oilysunscreen_img, 0.5)

#DRY SKIN CARE PRODUCTS
background34 = pygame.image.load('drycleanserbg.png')
background35 = pygame.image.load('drytonerbg.png')
background36 = pygame.image.load('drymoisturizerbg.png')
background37 = pygame.image.load('drysunscreenbg.png')

image34 = pygame.transform.scale(background34, (1540, 840))
image35 = pygame.transform.scale(background35, (1540, 840))
image36 = pygame.transform.scale(background36, (1540, 840))
image37 = pygame.transform.scale(background37, (1540, 840))

drycleanser_img = pygame.image.load("drycleanser.png").convert_alpha()
drytoner_img = pygame.image.load("drytoner.png").convert_alpha()
drymoisturizer_img = pygame.image.load("drymoisturizer.png").convert_alpha()
drysunscreen_img = pygame.image.load("drysunscreen.png").convert_alpha()

drycleanser_img = button.Button(200, 270, drycleanser_img, 0.5)
drytoner_img = button.Button(550, 240, drytoner_img, 0.5)
drymoisturizer_img = button.Button(850, 250, drymoisturizer_img, 0.5)
drysunscreen_img = button.Button(1200, 250, drysunscreen_img, 0.5)

#SENSITIVE SKIN CARE PRODUCTS
background22 = pygame.image.load('sencleanserbg.png')
background23 = pygame.image.load('sentonerbg.png')
background24 = pygame.image.load('senmoisturizerbg.png')
background25 = pygame.image.load('sensunscreenbg.png')

image22 = pygame.transform.scale(background22, (1540, 840))
image23 = pygame.transform.scale(background23, (1540, 840))
image24 = pygame.transform.scale(background24, (1540, 840))
image25 = pygame.transform.scale(background25, (1540, 840))

sencleanser_img = pygame.image.load("sencleanser.png").convert_alpha()
sentoner_img = pygame.image.load("sentoner.png").convert_alpha()
senmoisturizer_img = pygame.image.load("senmoisturizer.png").convert_alpha()
sensunscreen_img = pygame.image.load("sensunscreen.png").convert_alpha()

sencleanser_img = button.Button(200, 250, sencleanser_img, 0.5)
sentoner_img = button.Button(550, 240, sentoner_img, 0.5)
senmoisturizer_img = button.Button(850, 250, senmoisturizer_img, 0.5)
sensunscreen_img = button.Button(1200, 250, sensunscreen_img, 0.5)

#COMBINATION SKIN CARE PRODUCTS
background26 = pygame.image.load('combicleanserbg.png')
background27 = pygame.image.load('combidoublebg.png')
background28 = pygame.image.load('combimoisturizerbg.png')
background29 = pygame.image.load('combisunscreenbg.png')

image26 = pygame.transform.scale(background26, (1540, 840))
image27 = pygame.transform.scale(background27, (1540, 840))
image28 = pygame.transform.scale(background28, (1540, 840))
image29 = pygame.transform.scale(background29, (1540, 840))

combicleanser_img = pygame.image.load("combicleanser.png").convert_alpha()
combimoisturizer_img = pygame.image.load("combimoisturizer.png").convert_alpha()
combidouble_img = pygame.image.load("combidouble.png").convert_alpha()
combisunscreen_img = pygame.image.load("combisunscreen.png").convert_alpha()

combicleanser_img = button.Button(200, 250, combicleanser_img, 0.5)
combimoisturizer_img = button.Button(550, 240, combimoisturizer_img, 0.5)
combidouble_img = button.Button(850, 250, combidouble_img, 0.5)
combisunscreen_img = button.Button(1200, 250, combisunscreen_img, 0.5)

#TEXT
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

#WHILE RUN
run = True
while run:
    
   #MAIN MENU BACKGROUND
    window.blit(image1, (0, 0))

    if game_paused == True:

      #MAIN MENU
      if menu_state == "main":
        if button1_img.draw(screen):
           menu_state 
        if button2_img.draw(screen):
           menu_state 
        if button3_img.draw(screen):
           menu_state
        if start_img.draw(screen):
           menu_state = "start"

      #CHOOSING PHASE
      if menu_state == "start":
         window.blit(image2, (0, 0))

         font2 = pygame.font.Font("Daydream.ttf", 50)
         draw_text("Choose Your Skin Type", font2, TEXT_COL, 300, 130)

         if bckbutton_img.draw(screen):
            menu_state = ("main")
         if maegels1_img.draw(screen):
            menu_state = ("for normal skin")
         if maegels2__img.draw(screen):
            menu_state = ("for oily skin")
         if maegels3_mg.draw(screen):
            menu_state = ("for dry skin")
         if maegels4_img.draw(screen):
            menu_state = ("for sensitive skin")
         if maegels5_img.draw(screen):
            menu_state = ("for combination")

      #NORMAL
      if menu_state == "for normal skin":
         window.blit(image8, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "start"
         if nextbutton_img.draw(screen):
            menu_state = "next"

      if menu_state == "next":
         window.blit(image9, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "for normal skin"
         if nextbutton_img.draw(screen):
            menu_state = "next1"

      if menu_state == "next1":
         window.blit(image3, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next"
         if nextbutton1_img.draw(screen):
            menu_state = "quotenorm"
         if backtostart_img.draw(screen):
            menu_state = "start"
         if normcleanser_img.draw(screen):
            menu_state = "normalcleanser"
         if normtoner_img.draw(screen):
            menu_state = "normaltoner"
         if normmoisturizer_img.draw(screen):
            menu_state = "normalmoisturizer"
         if normsunscreen_img.draw(screen):
            menu_state = "normalsunscreen"

      if menu_state == "quotenorm":
         window.blit(image38, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next1"
      
      if menu_state == "normalcleanser":
         window.blit(image18, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next1"
      if menu_state == "normaltoner":
         window.blit(image19, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next1"
      if menu_state == "normalmoisturizer":
         window.blit(image20, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next1"
      if menu_state == "normalsunscreen":
         window.blit(image21, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next1"
      
      #OILY
      if menu_state == "for oily skin":
         window.blit(image10, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "start"
         if nextbutton_img.draw(screen):
            menu_state = "next2"

      if menu_state == "next2":
         window.blit(image11, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "for oily skin"
         if nextbutton_img.draw(screen):
            menu_state = "next3"

      if menu_state == "next3":
         window.blit(image4, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next2"
         if nextbutton1_img.draw(screen):
            menu_state = "quoteoily"
         if backtostart_img.draw(screen):
            menu_state = "start"
         if oilycleanser_img.draw(screen):
            menu_state = "oilycleanser"
         if oilytoner_img.draw(screen):
            menu_state = "oilytoner"
         if oilymoisturizer_img.draw(screen):
            menu_state = "oilymoisturizer"
         if oilysunscreen_img.draw(screen):
            menu_state = "oilysunscreen"

      if menu_state == "quoteoily":
         window.blit(image38, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next3"

      if menu_state == "oilycleanser":
         window.blit(image30, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next3"
      if menu_state == "oilytoner":
         window.blit(image31, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next3"
      if menu_state == "oilymoisturizer":
         window.blit(image32, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next3"
      if menu_state == "oilysunscreen":
         window.blit(image33, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next3"

      #DRY
      if menu_state == "for dry skin":
         window.blit(image12, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "start"
         if nextbutton_img.draw(screen):
            menu_state = "next4"

      if menu_state == "next4":
         window.blit(image13, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "for dry skin"
         if nextbutton_img.draw(screen):
            menu_state = "next5"

      if menu_state == "next5":
         window.blit(image5, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next4"
         if nextbutton1_img.draw(screen):
            menu_state = "quotedry"
         if backtostart_img.draw(screen):
            menu_state = "start"
         if drycleanser_img.draw(screen):
            menu_state = "drycleanser"
         if drytoner_img.draw(screen):
            menu_state = "drytoner"
         if drymoisturizer_img.draw(screen):
            menu_state = "drymoisturizer"
         if drysunscreen_img.draw(screen):
            menu_state = "drysunscreen"

      if menu_state == "quotedry":
         window.blit(image38, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next5"

      if menu_state == "drycleanser":
         window.blit(image34, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next5"
      if menu_state == "drytoner":
         window.blit(image35, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next5"
      if menu_state == "drymoisturizer":
         window.blit(image36, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next5"
      if menu_state == "drysunscreen":
         window.blit(image37, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next5"

      #SENSITIVE
      if menu_state == "for sensitive skin":
         window.blit(image14, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "start"
         if nextbutton_img.draw(screen):
            menu_state = "next6"

      if menu_state == "next6":
         window.blit(image15, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "for sensitive skin"
         if nextbutton_img.draw(screen):
            menu_state = "next7"

      if menu_state == "next7":
         window.blit(image6, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next6"
         if nextbutton1_img.draw(screen):
            menu_state = "quotesen"
         if backtostart_img.draw(screen):
            menu_state = "start"
         if sencleanser_img.draw(screen):
            menu_state = "sencleanser"
         if sentoner_img.draw(screen):
            menu_state = "sentoner"
         if senmoisturizer_img.draw(screen):
            menu_state = "senmoisturizer"
         if sensunscreen_img.draw(screen):
            menu_state = "sensunscreen"

      if menu_state == "quotesen":
         window.blit(image38, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next7"

      if menu_state == "sencleanser":
         window.blit(image22, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next7"
      if menu_state == "sentoner":
         window.blit(image23, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next7"
      if menu_state == "senmoisturizer":
         window.blit(image24, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next7"
      if menu_state == "sensunscreen":
         window.blit(image25, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next7"

      #COMBINATION
      if menu_state == "for combination":
         window.blit(image16, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "start"
         if nextbutton_img.draw(screen):
            menu_state = "next8"

      if menu_state == "next8":
         window.blit(image17, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "for combination"
         if nextbutton_img.draw(screen):
            menu_state = "next9"

      if menu_state == "next9":
         window.blit(image7, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next8"
         if nextbutton1_img.draw(screen):
            menu_state = "quotecombi"
         if backtostart_img.draw(screen):
            menu_state = "start"
         if combicleanser_img.draw(screen):
            menu_state = "combicleanser"
         if combimoisturizer_img.draw(screen):
            menu_state = "combimoisturizer"
         if combidouble_img.draw(screen):
            menu_state = "combidouble"
         if combisunscreen_img.draw(screen):
            menu_state = "combisunscreen"

      if menu_state == "quotecombi":
         window.blit(image38, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next9"

      if menu_state == "combicleanser":
         window.blit(image26, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next9"
      if menu_state == "combimoisturizer":
         window.blit(image28, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next9"
      if menu_state == "combidouble":
         window.blit(image27, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next9"
      if menu_state == "combisunscreen":
         window.blit(image29, (0, 0))
         if bckbutton_img.draw(screen):
            menu_state = "next9"

    else:
         
         draw_text("PRESS SPACE TO CONTINUE", font, TEXT_COL, 565, 700)
      
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
