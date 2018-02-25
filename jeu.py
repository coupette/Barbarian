import pygame, sys
from pygame.locals import *
from math import sqrt
from random import randint

acote1 = None
acote2 = None
acote3 = None
acote4 = None
acote5 = None
acote6 = None

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class barbare:
    def __init__(self, vie, argent):
        self.vie = vie
        self.argent = argent

    def actualise(self,Evie, Eargent, DISPLAY):

        self.argent += Eargent
        self.vie += Evie
        myfont = pygame.font.SysFont("monospace", 25)

        print("[Compteur] Vie: " + str(self.vie) + " Argent: " + str(self.argent))

        if (self.vie>100):
            self.vie = 100

        if (self.argent>=5000):
            return 1    #Gagné argent

        else:
            if(self.vie<=0):
                return 2    #mort
            else:
                return 0    #Rien ne se passe

class evenement:
    def __init__(self, type):
        self.type = type
        self.annonce = ""
        self.vie = 0
        self.argent = 0

        if(self.type == 1):
            self.annonce = "Vous vous faites voler votre sac"
            self.vie = 0
            self.argent = -100
        elif(self.type == 2):
            self.annonce = "Vous trébuchez"
            self.vie = -5
            self.argent = 0
        elif(self.type == 3):
            self.annonce = "Vous recevez une prime de la banque"
            self.vie = 0
            self.argent = 100
        elif(self.type == 4):
            self.annonce = "Vous trouvez des pièces par terre"
            self.vie = 0
            self.argent = 50
        elif(self.type == 5):
            self.annonce = "Vous vous cassez un bras"
            self.vie = -10
            self.argent = 0
        elif(self.type == 6):
            self.annonce = "Attaque d'indien"
            self.vie = 0
            self.argent = -100
        elif(self.type == 7):
            self.annonce = "Vous trouvez 700 pièces d'or"
            self.vie = 0
            self.argent = 700
        elif(self.type == 8):
            self.annonce = "Vous mangez un mars"
            self.vie = 10
            self.argent = 0
        elif(self.type == 9):
            self.annonce = "Pépite d'or"
            self.vie = 20
            self.argent = 1000
        elif(self.type == 10):
            self.annonce = "Attaque d'ours"
            self.vie = -20
            self.argent = 0
        elif(self.type == 11):
            self.annonce = "Trésor caché"
            self.vie = 50
            self.argent = 2500
        elif(self.type == 12):
            self.annonce = "Vous gagnez la lotterie des nains de la montagne"
            self.vie = 100
            self.argent = 4000
        elif(self.type == 13):
            self.annonce = "Glissement de terrain"
            self.vie = -40
            self.argent = 0
        elif(self.type == 14):
            self.annonce = "Vous tombez de la montagne"
            self.vie = -100
            self.argent = 0
        else:
            print("[Evenement] Erreur: non mappé")

    def annonceEvenement(self):  #Decrit l'évenement
        print("[Evenement] Annonce: " + self.annonce)
        return self.annonce

    def applique(self, personnage, DISPLAY):     #Actualise les stats du personnage
        print("[Evenement] Applique : vie: " + str(self.vie) + " argent: " + str(self.argent))

        return personnage.actualise(self.vie,self.argent, DISPLAY)

class Des:
    def __init__(self):
        nbFace = 6
    def lancerDouble(self, Hexa):

        DictionnaireSort = {}

        if(Hexa.type == "EAU"):
            print("Lancer de dès en cours pour le type: Eau")

            DictionnaireSort["1,1"] = 5    # - 10 pts de vie
            DictionnaireSort["1,2"] = 5    # - 10 pts de vie
            DictionnaireSort["1,3"] = 6    # - 10 pts de vie
            DictionnaireSort["2,1"] = 6    # - 10 pts de vie
            DictionnaireSort["2,2"] = 6    # - 10 pts de vie
            DictionnaireSort["2,3"] = 7    # + 700 pièces d'or
            DictionnaireSort["3,1"] = 7    # + 700 pièces d'or
            DictionnaireSort["3,2"] = 8    # + 10 pts de vie
            DictionnaireSort["3,3"] = 8    # + 10 pts de vie

            a = randint(1,3)
            b = randint(1,3)

            k = str(a) + "," + str(b)

            #print("[DEBUG] a: " + str(a) + " b: " + str(b) + " event: " + DictionnaireSort[k])
            #print("Evénement: " + DictionnaireSort[k])
            action = evenement(DictionnaireSort[k])
            return(action)

        elif(Hexa.type == "MONTAGNE"):
            print("Lancer de dès en cours pour le type: Montagne")

            DictionnaireSort["1,1"] = 14  #mort
            DictionnaireSort["1,2"] = 13   #-40 pts de vie
            DictionnaireSort["1,3"] = 13   #-40 pts de vie
            DictionnaireSort["2,1"] = 11    # + 2500 pièces d'or + 50 pts de vie
            DictionnaireSort["2,2"] = 9     # + 1000 pièces d'or + 20 pts de vie
            DictionnaireSort["2,3"] = 9    # + 1000 pièces d'or + 20 pts de vie
            DictionnaireSort["3,1"] = 10    # - 20 points de vie
            DictionnaireSort["3,2"] = 9     # + 1000 pièces d'or + 20 pts de vie
            DictionnaireSort["3,3"] = 12    # + 4000 pièces d'or + vie full

            a = randint(1,3)
            b = randint(1,3)

            k = str(a) + "," + str(b)

            #print("[DEBUG] a: " + str(a) + " b: " + str(b) + " event: " + DictionnaireSort[k])
            #print("Evénement: " + DictionnaireSort[k])
            action = evenement(DictionnaireSort[k])
            return(action)
            #return(DictionnaireSort[k])

        elif(Hexa.type == "FORET"):
            print("Lancer de dès en cours pour le type: Foret")

            DictionnaireSort["1,1"] = 5    # - 10 pts de vie
            DictionnaireSort["1,2"] = 5    # - 10 pts de vie
            DictionnaireSort["1,3"] = 6    # - 10 pts de vie
            DictionnaireSort["2,1"] = 6    # - 10 pts de vie
            DictionnaireSort["2,2"] = 6    # - 10 pts de vie
            DictionnaireSort["2,3"] = 7    # + 700 pièces d'or
            DictionnaireSort["3,1"] = 7    # + 700 pièces d'or
            DictionnaireSort["3,2"] = 8    # + 10 pts de vie
            DictionnaireSort["3,3"] = 8    # + 10 pts de vie

            a = randint(1,3)
            b = randint(1,3)

            k = str(a) + "," + str(b)

            #print("[DEBUG] a: " + str(a) + " b: " + str(b) + " event: " + DictionnaireSort[k])
            #print("Evénement: " + DictionnaireSort[k])
            action = evenement(DictionnaireSort[k])
            return(action)

        elif(Hexa.type == "plaine"):
            print("Lancer de dès en cours pour le type: Plaine")

            DictionnaireSort["1,1"] = 1   # -100 pièces d'or
            DictionnaireSort["1,2"] = 1   # -100 pièces d'or
            DictionnaireSort["1,3"] = 3   # +100 pièces d'or
            DictionnaireSort["2,1"] = 2   # -5 pts de vie
            DictionnaireSort["2,2"] = 3   # +100 pièces d'or
            DictionnaireSort["2,3"] = 4   # +50 pièces d'or
            DictionnaireSort["3,1"] = 4   # +50 pièces d'or
            DictionnaireSort["3,2"] = 2   # -5 pts de vie
            DictionnaireSort["3,3"] = 2   # -5 pts de vie

            a = randint(1,3)
            b = randint(1,3)

            k = str(a) + "," + str(b)

            #print("[DEBUG] a: " + str(a) + " b: " + str(b) + " event: " + DictionnaireSort[k])
            #print("Evénement: " + DictionnaireSort[k])
            action = evenement(DictionnaireSort[k])
            return(action)

        else:
            print("Erreur: Type de case non assigné")

class hexagone:
    x = 0
    y = 0
    z = 0
    r = 0
    q = 0
    col = 0
    row = 0
    type = "plaine"
    color = ""
    isBabare = 0
    isACote1 = None
    isACote2= None
    isACote3= None
    isACote4= None
    isACote5= None
    isACote6= None

    def __init__(self, col, row):
        self.col = col
        self.row = row
        if(col == 2 and row == 0):
            self.type = "EAU"
        elif(col == 8 and row == 1):
            self.type = "EAU"
        elif(col == 9 and row == 1):
            self.type = "EAU"
        elif(col == 1 and row == 2):
            self.type = "FORET"
        elif(col == 2 and row == 2):
            self.type = "FORET"
        elif(col == 2 and row == 3):
            self.type = "FORET"
        elif(col == 3 and row == 2):
            self.type = "FORET"
        elif(col == 6 and row == 0):
            self.type = "MONTAGNE"
        elif(col == 6 and row == 1):
            self.type = "MONTAGNE"
        elif(col == 6 and row == 2):
            self.type = "MONTAGNE"

    def drawAxialSelected(self, DISPLAY,tabHex,personnage, annonceEvent):
        size = 83
        for h in tabHex:
            if(h.isBabare == 1):
                h.isBabare = 0
                h.isACote = 1


        self.isBabare = 1
        reDraw(personnage, annonceEvent)
        petitBarbare = pygame.image.load("barbare.png")
        DISPLAY.blit(petitBarbare, (self.x-size/2, self.y-size/2))



    def drawAxialMove(self, DISPLAY):
        size = 83
        height = size * 2
        width = sqrt(3)/2 * height
        blue=(0,0,255)
        pygame.draw.polygon(DISPLAY,blue,[
                                      [self.x+size,self.y],
                                      [self.x+size/2,self.y+width/2],
                                      [self.x-size/2,self.y+width/2],
                                      [self.x-size,self.y],
                                      [self.x-size/2,self.y-width/2],
                                      [self.x+size/2,self.y-width/2]
                                  ], 3)

        pasBarbare = pygame.image.load("feetBarbare.png")
        DISPLAY.blit(pasBarbare, (self.x-size, self.y-size))

    def drawAxial(self, DISPLAY):
        size = 83
        height = size * 2
        width = sqrt(3)/2 * height
        blue=(255,0,0)
        self.x = (self.x)+95
        self.y = (self.y)+226
        pygame.draw.polygon(DISPLAY,blue,[
                                      [self.x+size,self.y],
                                      [self.x+size/2,self.y+width/2],
                                      [self.x-size/2,self.y+width/2],
                                      [self.x-size,self.y],
                                      [self.x-size/2,self.y-width/2],
                                      [self.x+size/2,self.y-width/2]
                                  ], 3)

    def drawAxialUnselect(self, DISPLAY):
        size = 83
        height = size * 2
        width = sqrt(3)/2 * height
        blue=(255,0,0)
        pygame.draw.polygon(DISPLAY,blue,[
                                      [self.x+size,self.y],
                                      [self.x+size/2,self.y+width/2],
                                      [self.x-size/2,self.y+width/2],
                                      [self.x-size,self.y],
                                      [self.x-size/2,self.y-width/2],
                                      [self.x+size/2,self.y-width/2]
                                  ], 3)

    def drawPositionDebut(self, DISPLAY):
        size = 83
        height = size * 2
        width = sqrt(3)/2 * height
        blue=(232,6,42)
        self.x = (self.x)+95
        self.y = (self.y)+226
        pygame.draw.polygon(DISPLAY,blue,[
                                      [self.x+size,self.y],
                                      [self.x+size/2,self.y+width/2],
                                      [self.x-size/2,self.y+width/2],
                                      [self.x-size,self.y],
                                      [self.x-size/2,self.y-width/2],
                                      [self.x+size/2,self.y-width/2]
                                  ])
        petitBarbare = pygame.image.load("barbare.png")
        DISPLAY.blit(petitBarbare, (self.x-size/2, self.y-size/2))

    def OddrToCube(self):
            self.x = self.col
            self.z = self.row - (self.col - (self.col&1)) / 2
            self.y = -self.x-self.z


    def cube_to_axial(self):
        self.q = self.x
        self.r = self.z

    def checkPosition(self, xPos, yPos, DISPLAY, tabHexa):

        distance = sqrt(pow(self.x-xPos, 2) + pow(self.y - yPos, 2))

        if (distance <= 83):
            for h in tabHexa:
                h.drawAxialUnselect(DISPLAY)
            self.isACote = 1
            return self
        else:
            return "null"
            #print(str(distance) + " x:" + str(self.x) + " y:" + str(self.y) + " row: " + str(self.row) + " col: " + str(self.col) + " q:" + str(self.q) + " r:" + str(self.r))

    def hex_neighbor(self, tableau, DISPLAY):
        increment = 0
        for i in range(0, 6):
            if (i == 0):
                ajQ = 0
                ajR = -1
            elif (i == 1):
                ajQ = -1
                ajR = 0
            elif (i == 2):
                 ajQ = -1
                 ajR = 1
            elif (i == 3):
                ajQ = 0
                ajR = 1
            elif (i == 4):
                ajQ = 1
                ajR = 0
            elif (i == 5):
                ajQ = 1
                ajR = -1
            for h in tableau:
                #print(str(increment))
                if (h.q == (self.q + ajQ))and(h.r == (self.r + ajR)):
                    increment = increment + 1
                    h.drawAxialMove(DISPLAY)
                    h.isACote = 1
                    if increment == 1:
                        global acote1
                        acote1 = h
                    if increment ==2:
                        global acote2
                        acote2 = h
                    if increment ==3:
                        global acote3
                        acote3 = h
                    if increment ==4:
                        global acote4
                        acote4 = h
                    if increment ==5:
                        global acote5
                        acote5 = h
                    if increment ==6:
                        global acote6
                        acote6 = h

def hex_to_pixel(hex):
    size = 83
    hex.x = size * 3/2 * hex.q
    hex.y = size * sqrt(3) * (hex.r + hex.q/2)

def reDraw(personnage, annonceEvent):
    bg = pygame.image.load("mapandgame.PNG")
    DISPLAY=pygame.display.set_mode(bg.get_rect().size,RESIZABLE)
    myfont = pygame.font.SysFont("monospace", 25)

    DISPLAY.blit(bg, (0, 0))
    WHITE=(255,255,255)
    blue=(0,0,255)
    myfont = pygame.font.SysFont("monospace", 25)
    tabHexa = []

    compteur_vie = myfont.render("Vie: " + str(personnage.vie), 10, (0,0,255))
    compteur_argent = myfont.render("Argent: " + str(personnage.argent), 10, (0,0,255))
    annonce = myfont.render("Annonce: " + str(annonceEvent), 10, (0,0,255))

    DISPLAY.blit(compteur_vie, (70, 830))
    DISPLAY.blit(compteur_argent, (200, 830))
    DISPLAY.blit(annonce, (400, 830))


    for i in range(0, 11):
      for k in range(0,5):
          hex = hexagone(i,k-1)
          hex.OddrToCube()
          hex.cube_to_axial()
          hex_to_pixel(hex)
          hex.drawAxial(DISPLAY)
          label = myfont.render(str(hex.col) + ' ' + str(hex.row), 1, (0,0,255))
          DISPLAY.blit(label, (hex.x, hex.y))
          tabHexa.append(hex)


def main():
    pygame.init()

    # Inside of the game loop

    bg = pygame.image.load("mapandgame.PNG")
    width = bg.get_width()
    height = bg.get_height()
    DISPLAY=pygame.display.set_mode([width,height+50],RESIZABLE)

    annonceEvent = ""
    d = Des()
    bar = barbare(100,0)
    DISPLAY.blit(bg, (0, 0))
    WHITE=(255,255,255)
    blue=(0,0,255)
    myfont = pygame.font.SysFont("monospace", 25)
    tabHexa = []

    compteur_vie = myfont.render("Vie: " + str(bar.vie) , 10, (0,0,255))
    compteur_argent = myfont.render("Argent: " + str(bar.argent), 10, (0,0,255))
    annonce = myfont.render("Annonce: " + str(annonceEvent), 10, (0,0,255))

    DISPLAY.blit(compteur_vie, (70, 830))
    DISPLAY.blit(compteur_argent, (200, 830))
    DISPLAY.blit(annonce, (400, 830))

    randomI = randint(0, 11)
    randomK = randint(0, 5)

    hexadebut = 0

    for i in range(0, 11):
      for k in range(0,5):
          hex = hexagone(i,k-1)
          hex.OddrToCube()
          hex.cube_to_axial()
          hex_to_pixel(hex)
          if(i == randomI and k == randomK):
            hexadebut = hex
            hex.drawPositionDebut(DISPLAY)
            hex.isBabare = 1
          else:
            hex.drawAxial(DISPLAY)
          label = myfont.render(str(hex.col) + ' ' + str(hex.row), 1, (0,0,255))
          DISPLAY.blit(label, (hex.x, hex.y))
          tabHexa.append(hex)

    hexadebut.hex_neighbor(tabHexa,DISPLAY)

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                Mouse_x, Mouse_y = pygame.mouse.get_pos()
                for h in tabHexa:
                    if (h.checkPosition(Mouse_x, Mouse_y,DISPLAY, tabHexa)!="null"):
                        move = 0
                        if(acote1 != None and acote1.col == h.col and acote1.row == h.row):
                            move = 1
                        if(acote2 != None and acote2.col == h.col and acote2.row == h.row):
                            move = 1
                        if(acote3 != None and acote3.col == h.col and acote3.row == h.row):
                            move = 1
                        if(acote4 != None and acote4.col == h.col and acote4.row == h.row):
                            move = 1
                        if(acote5 != None and acote5.col == h.col and acote5.row == h.row):
                            move = 1
                        if(acote6 != None and acote6.col == h.col and acote6.row == h.row):
                            move = 1
                        if(move == 1):

                            action = d.lancerDouble(h)
                            annonceEvent = action.annonceEvenement()
                            etat = action.applique(bar, DISPLAY)

                            if (etat == 1):
                                print("gagné")
                            elif (etat ==2):
                                print("mort")
                            else:
                                print("la partie continue")


                            h.drawAxialSelected(DISPLAY, tabHexa, bar, annonceEvent)
                            h.hex_neighbor(tabHexa,DISPLAY)
        pygame.display.update()
main()
