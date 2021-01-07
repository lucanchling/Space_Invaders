# Header
# Programme principal
# Luc Anchling
# github : https://github.com/lucanchling/Space_Invaders
# 17 Décembre 2020
# To Do : 

# Importation des modules :
from tkinter import Tk, Canvas, Label, Button, Menu
from time import time
from random import randint

tic = time()

largeur = 580
hauteur = 420
RAYON = 20
delta = 75
X = [largeur/2,largeur/2+delta,largeur/2-delta,largeur/2+2*delta,largeur/2-2*delta,largeur/2+3*delta,largeur/2-3*delta]
Y = hauteur/2
DX = 0.5

# Fonction déplaçant les aliens
def deplacement():
    Canevas.focus_set()
    global X,Y,DX,RAYON,largeur,hauteur,PosY
    # Gestion bord droit
    for i in range(len(X)):
        if X[i]+RAYON+DX > largeur:
            X[i] = 2*(largeur-RAYON)-X[i]
            DX = -DX
        # Gestion bord gauche avec desccente de l'alien
        if X[i]-RAYON+DX < 0:
            X[i] = 2*RAYON-X[i]
            DX = -DX
            Y += 5
        X[i] = X[i]+DX
        Canevas.coords(alien[i],X[i]-RAYON,Y-RAYON,X[i]+RAYON,Y+RAYON)
        if Y + RAYON >= PosY - tailleVaiss:
            Canevas.delete('all')                
    fenetre.after(15,deplacement)
    buttonStart.destroy()


# position initiale du Vaisseau
PosX = int(0.5*largeur)
PosY = int(0.95*hauteur)
tailleVaiss = 15

# Missile :
tailleMissile = 15
vitMissile = 3

# Permet de gérer le déplacement du missile
def deplacementMissile():
    global misX,misY,hauteur,tailleMissile,tailleVaiss,missile
    misY -= vitMissile
    Canevas.coords(missile,misX,misY,misX,misY+tailleMissile) 
    if misY > 5:
        fenetre.after(15,deplacementMissile)
    # Collision avec le bord haut
    if misY < 5:
        Canevas.delete(missile)
    # Collision avec l'alien
    for i in range(len(X)):
        if misX > X[i] - RAYON and misX < X[i] + RAYON and misY > Y - RAYON and misY < Y + RAYON:
            Canevas.delete(alien[i])
            del alien[i]
            del X[i]
            Canevas.delete(missile)


# Permet de gérer les missiles des aliens
def alienMissile():
    global misAlX,misAlY,misAlien,vitMissile,tailleMissile
    misAlY += vitMissile
    Canevas.coords(misAlien,misAlX,misAlY,misAlX,misAlY+tailleMissile)
    if misAlY < hauteur:
        fenetre.after(15,alienMissile)
    # Collision avec le bord haut
    if misAlY > hauteur - 10:
        Canevas.delete(misAlien)
    # Collision avec le vaisseau
    if misAlX > PosX - tailleVaiss and misAlX < PosX + tailleVaiss and misAlY > PosY - tailleVaiss and misAlY < PosY + tailleVaiss:
        Canevas.delete('all')


# Permet de gérer déplacement du vaisseau
def gestionVaisseau(event):
    global PosX,largeur,tailleVaiss,missile,misX,misY,X,Y,misAlien,misAlX,misAlY
    touche = event.keysym
    # Vaisseau au milieu
    if PosX+tailleVaiss < largeur and PosX-tailleVaiss > 0:
        # Déplacement à droite
        if touche == 'Right':
            PosX += 5
        # Déplacement à Gauche
        if touche == 'Left':
            PosX -= 5
    # Vaisseau sur le bord droit
    elif PosX+tailleVaiss >= largeur :
        if touche == 'Left':
            PosX -= 5
    # Vaisseau sur le bord gauche
    elif PosX-tailleVaiss < tailleVaiss:
        if touche == 'Right':
            PosX += 5
    # on dessine le Vaisseau à sa nouvelle position
    Canevas.coords(Vaisseau,PosX -tailleVaiss, PosY -tailleVaiss, PosX +tailleVaiss, PosY +tailleVaiss)
    if touche == 'space':
        missile = Canevas.create_line(PosX,PosY,PosX,PosY-tailleMissile,fill='white')
        misX,misY=PosX,PosY
        deplacementMissile()
    if touche == 'a':
        misAlX,misAlY=X[randint(0,len(X)-1)],Y
        misAlien = Canevas.create_line(misAlX,misAlY,misAlX,misAlY-tailleMissile,fill='white')
        alienMissile()



# Partie Graphique :

# Création de la fenetre :
fenetre = Tk()
fenetre.title('Space Invaders')

# Zone principale de jeu :
Canevas = Canvas(fenetre, width = largeur, height = hauteur, bg='grey')

Canevas.bind('<Key>',gestionVaisseau)
Canevas.pack(side = 'left')

# Zone affichant le score :
labelScore = Label(fenetre, text='Score :')
labelScore.pack(side = 'top')

# Menu :
menubar = Menu(fenetre)
menu1 = Menu(menubar, tearoff = 0)
menu1.add_command(label = 'New Game')
menu1.add_command(label = 'Quit', command = fenetre.destroy)
menubar.add_cascade(label = 'Partie', menu = menu1)
fenetre.config(menu = menubar)

# Bouton déclenchant la partie :
buttonStart = Button(fenetre, text = 'Start', command = deplacement)
buttonStart.pack()

# Bouton permettant de sortir du jeu :
buttonQuit = Button(fenetre, text = 'Quit', command = fenetre.destroy)
buttonQuit.pack()

# Création de l'objet alien & vaisseau:

alien = []
for i in range(len(X)):
    alien.append(Canevas.create_rectangle(X[i]-RAYON,Y-RAYON,X[i]+RAYON,Y+RAYON,width=1,fill='blue'))
Vaisseau = Canevas.create_rectangle(PosX-tailleVaiss,PosY-tailleVaiss,PosX+tailleVaiss,PosY+tailleVaiss,width=1,outline='black',fill='red')


fenetre.mainloop()