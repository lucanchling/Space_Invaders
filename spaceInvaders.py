# Header
# Programme principal
# Luc Anchling
# github : https://github.com/lucanchling/Space_Invaders
# 17 Décembre 2020
# To Do : à partir de la gestion du missile...

# Importation des modules :
from tkinter import Tk, Canvas, Label, Button, Menu

Largeur = 480
Hauteur = 320
RAYON = 20
X = Largeur/2
Y = Hauteur/2
DX = 1

# Fonction déplaçant les aliens
def deplacement():
    Canevas.focus_set()
    global X,Y,DX,RAYON,Largeur,Hauteur
    # Gestion bord droit
    if X+RAYON+DX > Largeur:
        X = 2*(Largeur-RAYON)-X
        DX = -DX
    # Gestion bord gauche
    if X-RAYON+DX < 0:
        X = 2*RAYON-X
        DX = -DX
    X = X+DX
    Canevas.coords(alien,X-RAYON,Y-RAYON,X+RAYON,Y+RAYON)
    fenetre.after(15,deplacement)
    buttonStart.destroy()


# position initiale du Vaisseau
PosX = int(0.61*Largeur)
PosY = int(1.2*Hauteur)
tailleVaiss = 15

# Missile :
tailleMissile = 15
vitMissile = 5

# Permet de gérer le déplacement du missile
def Deplacementmissile():
    global misX,misY,Hauteur,tailleMissile,tailleVaiss,missile
    misY = misY-vitMissile
    Canevas.coords(missile,misX,misY,misX,misY+tailleMissile)
    if misY < 5:
        Canevas.delete(missile)
    fenetre.after(20,Deplacementmissile)

# FPermet de gérer déplacement du vaisseau
def GestionVaisseau(event):
    global PosX,Largeur,tailleVaiss
    touche = event.keysym
    # Vaisseau au milieu
    if PosX+tailleVaiss < Largeur and PosX-tailleVaiss > 0:
        # Déplacement à droite
        if touche == 'Right':
            PosX += 5
        # Déplacement à Gauche
        if touche == 'Left':
            PosX -= 5
    # Vaisseau sur le bord droit
    elif PosX+tailleVaiss > Largeur :
        if touche == 'Left':
            PosX -= 5
    # Vaisseau sur le bord gauche
    elif PosX-tailleVaiss < tailleVaiss:
        if touche == 'Right':
            PosX += 5
        # on dessine le Vaisseau � sa nouvelle position
    Canevas.coords(Vaisseau,PosX -tailleVaiss, PosY -tailleVaiss, PosX +tailleVaiss, PosY +tailleVaiss)
    if touche == 'space':
        global missile,misX,misY
        missile = Canevas.create_line(PosX,PosY,PosX,PosY-tailleMissile,fill='white')
        misX,misY=PosX,PosY
        Deplacementmissile()


# Partie Graphique :

# Création de la fenetre :
fenetre = Tk()
fenetre.title('Space Invaders')

# Zone principale de jeu :
Largeur,Hauteur=580,420
Canevas = Canvas(fenetre, width = Largeur, height = Hauteur, bg='grey')

Canevas.bind('<Key>',GestionVaisseau)
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
alien = Canevas.create_rectangle(X-RAYON,Y-RAYON,X+RAYON,Y+RAYON,width=1,fill='blue')
Vaisseau = Canevas.create_rectangle(PosX-tailleVaiss,PosY-tailleVaiss,PosX+tailleVaiss,PosY+tailleVaiss,width=1,outline='black',fill='red')

fenetre.mainloop()