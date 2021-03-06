# Header
# Programme principal
# Luc Anchling
# github : https://github.com/lucanchling/Space_Invaders
# 17 Décembre 2020
# To Do : Essayer d'intégrer des classes

# Importation des modules :
from tkinter import Tk, Canvas, Label, Button, Menu, PhotoImage,messagebox
from random import randint
from os import path

# Dimension :
largeur = 580
hauteur = 420
RAYON = 20

delta = 85
# Coordonnées aliens :
X = [largeur/2,largeur/2+delta,largeur/2-delta,largeur/2+2*delta,largeur/2-2*delta,largeur/2+3*delta,largeur/2-3*delta]
Y = hauteur/2

# Déplacements horizontaux des ennemis 
DX = 0.5   # Classique
DXx= 1.5   # Bonus
nbVie = 3  # Nombre de vie de l'user
vieIlot = [3,3]   # nombre de vie des ilots de protection
deplacementVertical = 10
alienBonusVie = True   # Etat de l'ennemi bonus (True : vivant - False : Dead)
score = 0

# position initiale et dimension du Vaisseau
PosX = int(0.5*largeur)
PosY = int(0.95*hauteur)
tailleVaiss = 15

# dimension et vitesse des Missiles :
tailleMissile = 15
vitMissile = 3

# Début de la partie avec création des aliens, des ilots & du vaisseau:
def debut():
    Canevas.delete('all')
    global X,Y,Vaisseau,alien,missile,affVieIlot,bonusX,bonusY,alienBonus,bonusX,bonusY
    Canevas.create_image(10,10,image = background)
    Y = hauteur/2  # Réinitialisation de la hauteur des ennemis
    alien = []
    bonusX,bonusY = largeur/2, hauteur/2 - 100    
    alienBonus = Canevas.create_rectangle(bonusX-RAYON,bonusY-RAYON,bonusX+RAYON,bonusY+RAYON,width=1,fill='orange')
    for i in range(len(X)):
        alien.append(Canevas.create_rectangle(X[i]-RAYON,Y-RAYON,X[i]+RAYON,Y+RAYON,width=1,fill='blue'))
    Vaisseau = Canevas.create_rectangle(PosX-tailleVaiss,PosY-tailleVaiss,PosX+tailleVaiss,PosY+tailleVaiss,width=1,outline='black',fill='red')
    ilot = []
    affVieIlot = []
    for i in range(1,4,2):
        ilot.append(Canevas.create_rectangle(i*largeur/5,hauteur-50-RAYON,(i+1)*largeur/5,hauteur-50,width=1,fill='grey'))
        # Affichage des vies de chaque ilot :
        affVieIlot.append(Canevas.create_text((i+.5)*largeur/5,hauteur-50-.5*RAYON,text =str(vieIlot[(i-1)//2]), fill ="white", font="Arial 15 bold"))
    deplacementAlien()
    deplacementAlienBonus()

# Gestion de fin de partie avec écriture du score dans un .txt:
def fin():
    Canevas.destroy()
    if path.exists('score.txt') == False :  # Test de l'existence du fichier 'score.txt'
        initDoc()
    doc = open('score.txt','a')
    if nbVie > 1:
        labelScore['text'] = 'Score : ' + str(score*nbVie) + 'pts'
        doc.write('\n'+str(score*nbVie))
    else:
        doc.write('\n'+str(score))
    doc.close()

# permet de gérer le nombre de vie du joueur en relançant ou non la partie si il reste des vies 
def gestionVie():
    global nbVie
    if nbVie > 0 :
        fenetre.after(1000)
        Canevas.delete('all')
        nbVie -= 1
        labelVie['text'] = 'Nombre de vie(s) restante(s) : ' + str(nbVie)
        debut()
    else:
        fin()


# Fonction initialisant le document contenant les scores avec un record par défaut à 100 pts
def initDoc():
    doc = open('score.txt','w')
    doc.write("100")
    doc.close()

# Gestion du score
def scorePlayer(ennemi):
    global labelScore,score
    l_alien = ['alien','alienBonus']
    l_score = [50,150]
    # Permet de savoir quel ennemi a été tué
    for indice,valeur in enumerate(l_alien):
        if ennemi == valeur:
            score += l_score[indice]
    labelScore['text'] = 'Score : ' + str(score) + 'pts'

# Fonction affichant le record actuel
def record():
    doc = open('score.txt','r')
    lscore = doc.readlines()
    print(lscore,max(lscore))
    messagebox.showinfo("Record", 'Le record est de : '+ str(max(lscore).strip()) + 'pts')
    doc.close()

# Fonction gérant le déplacement et l'envoi des missiles des aliens
def deplacementAlien():
    Canevas.focus_set()
    global X,Y,DX,PosY,misAlien,misAlX,misAlY
    # Gestion bord droit
    for i in range(len(X)):
        if X[i]+RAYON+DX > largeur:
            X[i] = 2*(largeur-RAYON)-X[i]
            DX = -DX
    # Gestion bord gauche avec desccente de l'alien
        if X[i]-RAYON+DX < 0:
            X[i] = 2*RAYON-X[i]
            DX = -DX
            Y += deplacementVertical
        X[i] = X[i]+DX
        Canevas.coords(alien[i],X[i]-RAYON,Y-RAYON,X[i]+RAYON,Y+RAYON)
    # Mort du joueur - Alien en bas
        if Y + RAYON >= PosY - tailleVaiss:
            gestionVie()
    fenetre.after(20,deplacementAlien)
    buttonStart.destroy()
    # Envoi du Missile des aliens (à un tps aléatoire)
    if randint(0,3500) < 5:
        misAlX,misAlY=X[randint(0,len(X)-1)],Y
        misAlien = Canevas.create_line(misAlX,misAlY,misAlX,misAlY-tailleMissile,fill='white')
        alienMissile()

# Foncttion gérant le déplacement et l'envoi de missile de l'alien bonus
def deplacementAlienBonus():
    Canevas.focus_set()
    global bonusX,bonusY,alienBonus,DXx,misAlien,misAlX,misAlY
    if alienBonusVie == True: 
        # Gestion bord droit
        if bonusX+RAYON+DXx > largeur:
            bonusX = 2*(largeur-RAYON)-bonusX
            DXx = -DXx
            bonusY += 5
        # Gestion bord gauche avec desccente de l'alien
        if bonusX-RAYON+DX < 0:
            bonusX = 2*RAYON-bonusX
            DXx = -DXx
            bonusY += 5
        bonusX = bonusX+DXx
        Canevas.coords(alienBonus,bonusX-RAYON,bonusY-RAYON,bonusX+RAYON,bonusY+RAYON)
        # Mort du joueur - Alien en bas
        if bonusY + RAYON >= PosY - tailleVaiss:
            gestionVie()
        fenetre.after(20,deplacementAlienBonus)
        buttonStart.destroy()
        # Envoi du Missile des aliens (à un tps aléatoire)
        if randint(0,1500) < 5:
            misAlX,misAlY=bonusX,bonusY
            misAlien = Canevas.create_line(misAlX,misAlY,misAlX,misAlY-tailleMissile,fill='white')
            alienMissile()
    else :
        Canevas.delete(alienBonus)

# Permet de gérer le déplacement du missile
def deplacementMissile():
    global misX,misY,missile,bonusX,bonusY,alienBonus,alienBonusVie
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
            misX,misY=0,0
            scorePlayer('alien')
    # Collision avec l'alien bonus
    if misX > bonusX - RAYON and misX < bonusX + RAYON and misY > bonusY - RAYON and misY < bonusY + RAYON:
            Canevas.delete(alienBonus)
            Canevas.delete(missile)
            misX,misY=0,0
            scorePlayer('alienBonus')
            alienBonusVie = False
    # Lorsque tous les aliens sont tués
    if alienBonusVie == False and len(X) == 0:
        fin()


# Permet de gérer les missiles des aliens
def alienMissile():
    global misAlX,misAlY,misAlien,labelVie,nbVie,vieIlot,affVieIlot
    misAlY += vitMissile
    Canevas.coords(misAlien,misAlX,misAlY,misAlX,misAlY+tailleMissile)
    if misAlY < hauteur:
        fenetre.after(15,alienMissile)
    # Collision avec le bord bas
    if misAlY > hauteur - 10:
        Canevas.delete(misAlien)
    # Collision avec le vaisseau
    if misAlX > PosX - tailleVaiss and misAlX < PosX + tailleVaiss and misAlY > PosY - tailleVaiss and misAlY < PosY + tailleVaiss:
        misAlX,misAlY=0,0
        gestionVie()
    # Collision avec les ilots :
    for i in range(1,4,2):
        if misAlX > i*largeur/5 and misAlX < (i+1)*largeur/5 and misAlY > hauteur-50-RAYON and vieIlot[(i-1)//2] > 0:
            misAlX,misAlY=0,0
            Canevas.delete(misAlien)
            vieIlot[(i-1)//2] -= 1
            Canevas.itemconfigure(affVieIlot[(i-1)//2], text = str(vieIlot[(i-1)//2]))


# Permet de gérer déplacement du vaisseau
def gestionVaisseau(event):
    global PosX,missile,misX,misY,X,Y,misAlien,misAlX,misAlY,Vaisseau
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

# Page à propos
def about():
    messagebox.showinfo("A propos", 'Ce jeu reprend le principe du fameux jeu "Space Invaders"' + '\n' + 'Développé par Luc Anchling')

# Partie Graphique :

# Création de la fenetre :
fenetre = Tk()
fenetre.title('Space Invaders')

# Zone principale de jeu avec fond d'écran:
Canevas = Canvas(fenetre, width = largeur, height = hauteur, bg='grey')
Canevas.bind('<Key>',gestionVaisseau)
Canevas.pack(side = 'left')
background = PhotoImage(file = "background.gif")
Canevas.create_image(10,10,image = background)

# Zone affichant le score :
labelScore = Label(fenetre, text='Score : 0')
labelScore.pack(side = 'top')

# Zone affichant le nombre de vie(s) restante(s):
labelVie = Label(fenetre, text='Nombre de vie(s) restante(s) : 3')
labelVie.pack(side = 'top')

# Menu :
menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff = 0)
menu1.add_command(label = 'Quit', command = fenetre.destroy)
menubar.add_cascade(label = 'Partie', menu = menu1)

menu2 = Menu(menubar, tearoff = 0)
menu2.add_command(label = 'High Score',command = record)
menu2.add_command(label = 'A Propos', command = about)
menubar.add_cascade(label = 'Infos', menu = menu2)
fenetre.config(menu = menubar)

# Bouton déclenchant la partie :
buttonStart = Button(fenetre, text = 'Start', command = debut)
buttonStart.pack()

fenetre.mainloop()