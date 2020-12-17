# Header
# Programme principal
# Luc Anchling
# github : https://github.com/lucanchling/Space_Invaders
# 17 Décembre 2020
# To Do :

# Importation des modules :
from tkinter import *

LARGEUR = 480
HAUTEUR = 320
RAYON = 20
X = LARGEUR/2
Y = HAUTEUR/2
DX = 1

def deplacement():
    global X,Y,DX,DY,RAYON,LARGEUR,HAUTEUR
    # Gestion bord droit
    if X+RAYON+DX > LARGEUR:
        X = 2*(LARGEUR-RAYON)-X
        DX = -DX
    # Gestion bord gauche
    if X-RAYON+DX < 0:
        X = 2*RAYON-X
        DX = -DX
    X = X+DX
    canevas.coords(alien,X-RAYON,Y-RAYON,X+RAYON,Y+RAYON)
    fenetre.after(15,deplacement)
    buttonStart.destroy()

# Partie Graphique :

# Création de la fenetre :
fenetre = Tk()
fenetre.title('Space Invaders')

# Zone principale de jeu :
LARGEUR,HAUTEUR=580,420
canevas = Canvas(fenetre, width = LARGEUR, height = HAUTEUR, bg='grey')
canevas.pack(side = 'left')

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
alien = canevas.create_rectangle(X-RAYON,Y-RAYON,X+RAYON,Y+RAYON,width=1,fill='blue')

fenetre.mainloop()