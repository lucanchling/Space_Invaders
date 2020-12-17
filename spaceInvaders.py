# Header
# Programme principal
# Luc Anchling
# github : https://github.com/lucanchling/Space_Invaders
# 17 Décembre 2020
# To Do :

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
PosX = 0.61*Largeur
PosY = 1.2*Hauteur

def DeplacementVaisseau(event):
    global PosX,Largeur
    touche = event.keysym
    # Vaisseau au milieu
    if PosX+10 < Largeur and PosX-10 > 0:
        # Déplacement à droite
        if touche == 'Right':
            PosX += 5
        # Déplacement à Gauche
        if touche == 'Left':
            PosX -= 5
    # Vaisseau sur le bord droit
    elif PosX+10 == Largeur :
        if touche == 'Left':
            PosX -= 5
    # Vaisseau sur le bord gauche
    elif PosX-10 == 0:
        if touche == 'Right':
            PosX += 5
        # on dessine le Vaisseau � sa nouvelle position
    Canevas.coords(Vaisseau,PosX -10, PosY -10, PosX +10, PosY +10)

# Partie Graphique :

# Création de la fenetre :
fenetre = Tk()
fenetre.title('Space Invaders')

# Zone principale de jeu :
Largeur,Hauteur=580,420
Canevas = Canvas(fenetre, width = Largeur, height = Hauteur, bg='grey')
Vaisseau = Canevas.create_rectangle(PosX-10,PosY-10,PosX+10,PosY+10,width=1,outline='black',fill='red')
Canevas.bind('<Key>',DeplacementVaisseau)
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

# Création de l'objet alien :
alien = Canevas.create_rectangle(X-RAYON,Y-RAYON,X+RAYON,Y+RAYON,width=1,fill='blue')

fenetre.mainloop()