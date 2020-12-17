# Header
# Programme principal
# Luc Anchling
# github : https://github.com/lucanchling/Space_Invaders
# 17 Décembre 2020
# To Do :

# Importation des modules :
from tkinter import Tk, Canvas, Label, Button, Menu


# Partie Graphique

# Création de la fenetre :
fenetre = Tk()
fenetre.title('Space Invaders')

# Zone principale de jeu
canevas = Canvas(fenetre, width = 580, height = 420)
canevas.pack(side = 'left')

# Zone affichant le score
labelScore = Label(fenetre, text='Score :')
labelScore.pack(side = 'top')

# Bouton déclenchant la partie
buttonStart = Button(fenetre, text = 'Start')
buttonStart.pack()

# Bouton permettant de sortir du jeu
buttonQuit = Button(fenetre, text = 'Quit', command = fenetre.destroy)
buttonQuit.pack()

fenetre.mainloop()