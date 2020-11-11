#! /usr/bin/env python3
# -*- coding: utf-8 -*-
 
""" View
"""
#DEVOIR : REGLER LE PROBLEME DU CLIC LONG
 
from math import *
from tkinter import *
from random import *
 
class View():
    """Description de la classe :
     
    def __init__(self, dimensions, states, set_state, control_variables):
            Creation de la fenetre tkinter et du canvas
            appels des différentes fonctions Placement, remplissageForet, BoutonsEtBoitesEtCurseurs
             
    def Placement(self) :
    Place tous les élements du canvas : la zone de dessins, les boites Controle, Options, Choix et Curseurs, le bouton Quitter, 
     
     
     
    def remplissageForet (self) :
        Cette fonction crée tous les carrés composant la grille du jeu dans le canvas.
        Crée aussi la liste ListeGrille comportant tous les identifiants des carrés du canvas
     
    def BoutonsEtBoitesEtCurseurs(self) :
        Crée tous les boutons, les boites et les curseurs :
     
        Boites :
            Controle : contenant toutes les autres boites
            Choix : avec les radioboutons (cette boite est dans la boite Controle)
            Options : avec les 3 boutons aléatoire, carte vide, pause (cette boite est dans la boite Controle)
            Curseurs : avec les deux curseurs CurseurTaille et CurseurVitesse (cette boite est dans la boite Controle)
     
        Boutons : 
            Les 3 boutons alétoire, carte vide et pause
            Les radioboutons dépendant du jeu sélectionné donc des states et directement placés lors de leurs créations
            Le bouton Quitter : ferme la fenetre lors de son activation
     
        Curseurs :
            CurseurTaille : modifie la plage de coloriage de la souris lors du clic gauche
            CurseurVitesse : modifie la vitesse de propagation lors du jeu
     
    def set_cell_color(self, l, c, color): 
        Change la couleur initiale en la nouvelle couleur (color) de la case indiquée par sa ligne (l) et sa colonne (c).
     
    def clic(self, event) : 
        Trouve la colonne et la ligne associées au clic de position (x,y). Appel la fonction set_cell_color() avec 
        la ligne et la colonne trouvées et de la couleur indiquée par les radioboutons
         
    def clicLong(self, event) :
        Trouve la colonne et la ligne associées au clic de position (x,y). Et lors du déplacement de la souris, colorie 
        toutes les cases autour du carré centrale (l,c) selon la taille donnée par le CurseurTaille
     
     
    def loop(self):
        Affiche la fenetre
     
    def bind_action(self, name, action):
        Lie les différents noms aux actions :
         - le nom Randmap est associé à la création d'une carte aléatoire
         - le nom Clearmap est associé à la remise a zero de la carte
         - le nom Pause : met en pause la propagation
    """
             
  
    def __init__(self, dimensions, states, set_state, control_variables):
        """Initializes the view.
        :param dimensions: the dimensions of the automaton,
        as a pair (width, height)
        :param states: gives the available states.
        It is given as a dictionary whose keys are the names of the states
        and the corresponding entries are the colors.
        :param set_state: the function to call for updating a state
        in the automaton. It takes three arguments, the line, the column, and
        the state to apply (i.e. the key from the dictionary)
        :param control_variables: a dictionary of variables that are shared
        with the controller.
        """
          
        #Creation de la fenetre tkinter
        self.window = Tk()
        self.window.title('Jeu')
         
        #Variables necessaires aux fonctions de la classe
        self.states=states
        self.nombre_carre_largeur = dimensions[0]
        self.nombre_carre_hauteur = dimensions[1] 
          
          
        #Creation de la zone du Canvas
        self.largeur = 400
        self.hauteur = 300
        self.foret=Canvas(self.window, width=self.largeur, height=self.hauteur, bg="white")
         
         
        #Actions associées aux boutons de la souris
        self.foret.bind('<Button-1>', self.clic)
        self.foret.bind('<B1-Motion>', self.clicLong) 
          
        
     
        #Appel de la fonction pour remplir la foret avec les carrés
        self.remplissageForet()
          
        #Appel de la fonction qui crée tous les boutons, curseurs, boites
        self.BoutonsEtBoitesEtCurseur()
        control_variables["speed"]=self.value1
          
        #Bouton pour fermer le programme
        self.fermerlafenetre=Button(command=self.window.destroy, text="Quitter")
         
        #Appel de la fonction qui place tous les éléments de la fenetre
        self.Placement()
        self.set_state= set_state
        
         
    def Placement(self) :
        #Variables définissant les lignes et les colonnes du canvas entier
        ligne = 0
        colonne = 0
        #Variables définissant les lignes et les colonnes au sein de la boîte Controle
        ligneControle = 0
        colonneControle = 0
        #Variables définissant les lignes et les colonnes au sein de la boîte Options
        ligneOptions = 0
        colonneOptions= 0
        #Variables définissant les lignes et les colonnes au sein de la boîte Curseurs
        ligneCurseurs = 0
        colonneCurseurs = 0
         
         
         
        #Placement de la foret
        self.foret.grid(row=ligne, column = colonne)
         
        #Placement des boites
        colonne = colonne + 1
        self.boiteControle.grid(column = colonne , row = ligne )
        self.boiteChoix.grid( column = colonneControle, row = ligneControle)
        ligneControle = ligneControle + 1
        self.boiteOptions.grid( column = colonneControle, row = ligneControle)
        ligneControle = ligneControle + 1
        self.boiteCurseurs.grid(column=colonneControle, row = ligneControle)
       
         
        #DANS LES BOITES : 
            #boite : Controle 
        "Directement placée lors de leurs créations"
             
             
            #boite : Curseurs
        self.curseurVitesse.grid(column= colonneCurseurs, row = ligneCurseurs)
        ligneCurseurs = ligneCurseurs + 1
        self.curseurTaille.grid(column=colonneCurseurs, row = ligneCurseurs)  
         
            #boite : Options (aléatoire, pause et carte vide)
         
        self.Clearmap.grid(column=colonneOptions, row = ligneOptions)
        colonneOptions = colonneOptions + 1
        self.Randmap.grid(column=colonneOptions, row = ligneOptions)
        colonneOptions = colonneOptions + 1
        self.Pause.grid(column=colonneOptions, row = ligneOptions)
        colonneOptions = colonneOptions - 1
        ligneOptions=ligneOptions+1
        self.LifeGame.grid(column=colonneOptions, row = ligneOptions)
        colonneOptions = colonneOptions + 1
        self.Fire.grid(column=colonneOptions, row = ligneOptions)
        
        
        #Placement bouton fermer
        ligne = ligne + 1
        self.fermerlafenetre.grid(column = colonne, row = ligne, sticky = 'e')
        
         
         
         
             
             
     
  
    #Creation de la grille pour notre foret
    def remplissageForet(self) :
        #Liste avec tous les id des carrés :
        #ListeGrille = [[colonne 1 de la ligne 1, colonne 2 de la ligne 1 ...], [colonne 1 de la ligne 2, colonne 2 de la ligne 2]]
        self.ListeGrille= []
        Xcarre = 0
        Ycarre = 0
      
        #Modifier la taille de nos carres ICI :
        self.CoteCarre= 10
      
        #Verification : les carres rentrent dans la zone
        if self.nombre_carre_largeur%self.CoteCarre != 0 or self.nombre_carre_hauteur%self.CoteCarre != 0 :
            return print( "ERREUR : probleme de taille de la zone \n de dessin, pas un multiple des tailles des carres")
  
        #Remplissage 
        for j in range (0, self.nombre_carre_hauteur) :
            for i in range (0, self.nombre_carre_largeur) :
                ident=self.foret.create_rectangle(Xcarre, Ycarre , Xcarre + self.CoteCarre, Ycarre + self.CoteCarre, fill ="white")
                if i == 0 :
                    self.ListeGrille.append([ident])
                else :
                    self.ListeGrille[j].append(ident)
                Xcarre = Xcarre + self.CoteCarre
            Ycarre = Ycarre + self.CoteCarre
            Xcarre = 0
       
    def BoutonsEtBoitesEtCurseur(self):
        #Variables nécessaires au placement des radioboutons dans la boite Choix
        colonneBoutons = 0
        ligneBoutons = 0
        #Creation des boites
        self.boiteControle = LabelFrame(self.window, text='Contrôle', width = 300, height = 400)
        self.boiteChoix = LabelFrame(self.boiteControle, text='Choix')
        self.boiteOptions = LabelFrame(self.boiteControle, text='Options')
        self.boiteCurseurs = LabelFrame(self.boiteControle, width = 300, height = 250, text='Curseurs')
         
        #Creation et placement des radioBoutons
        self.etat = StringVar()
        for cle in self.states :
            self.cle = Radiobutton(self.boiteChoix, text=cle, variable = self.etat, value = cle)
            self.cle.grid(column= colonneBoutons, row = ligneBoutons, sticky='w')
            ligneBoutons = ligneBoutons + 1

          
        #Creation des Boutons aléatoire, pause et carte vide
        self.Clearmap = Button(self.boiteOptions, text='Carte vide')
        self.Randmap = Button(self.boiteOptions, text='Aléatoire')
        self.Pause = Button(self.boiteOptions, text='Pause')
        self.LifeGame=Button(self.boiteOptions, text='LifeGame')
        self.Fire=Button(self.boiteOptions, text='Fire')
          
        
        #Création des Curseurs
        self.value1=IntVar()
        self.value2=IntVar()
        self.curseurVitesse=Scale(self.boiteCurseurs, label = "Vitesse", orient='horizontal', variable=self.value1, troughcolor = 'gray90')
        self.curseurTaille=Scale(self.boiteCurseurs, orient='horizontal', label = 'Taille', variable=self.value2, from_= 0, to = 7, resolution = 1, troughcolor = 'gray90')
        
          
     
    def set_cell_color(self, l, c, color):
        """set_cell_color(self, l, c, color): 
        Change la couleur initiale en la nouvelle couleur (color) de la case indiquée par sa ligne (l) et sa colonne (c)."""
        itemChange = self.ListeGrille[l-1][c-1]
        self.foret.itemconfigure(itemChange,fill=color)
      
      
          
    def clic(self, event) :
        x = event.x
        y = event.y
        ligne = 0
        colonne = 0
        X = 0
        Y = 0
        for i in range (0, self.nombre_carre_largeur) :
            if x > X :
                colonne = colonne + 1
                X = X + self.CoteCarre
        for j in range (0,self.nombre_carre_hauteur):
            if y > Y :
                ligne = ligne + 1
                Y = Y + self.CoteCarre
        
        etat=self.etat.get()
        if etat == '' :
            etat = "empty"
        #TROUVER LA BONNE CONDITION 
        if ligne >= 0 and colonne >= 0  :
            self.set_state(ligne,colonne,etat)
            self.set_cell_color(ligne,colonne,self.states[etat])
     
     
      
    def clicLong(self,event) :
        x = event.x
        y = event.y
        ligne = 0
        colonne = 0
        X = 0
        Y = 0
        etat=self.etat.get()
        if etat == '' :
            etat = "empty"
        for i in range (0, self.nombre_carre_largeur) :
            if x > X :
                colonne = colonne + 1
                X = X + self.CoteCarre
        for j in range (0,self.nombre_carre_hauteur):
            if y > Y :
                ligne = ligne + 1
                Y = Y + self.CoteCarre
 
        if self.value2.get() == 0 :
            self.set_state(ligne,colonne,etat)
            self.set_cell_color(ligne,colonne,self.states[etat])
        #k : crée la plage de valeur autour du carré cliqué à partir de ka valeur donnée par le curseurTaille, pour la ligne
        #K : crée la plage de valeur autour du carré cliqué à partir de ka valeur donnée par le curseurTaille, pour la colonne
        else :
            for k in range (-self.value2.get(),self.value2.get()) :
                for K in range (-self.value2.get(),self.value2.get()) :
                    #Conditions permettant de ne pas colorier des cases de l'autre coté du canevas
                    if ligne + k - 1>= 0  and colonne + K -1 >=0:
                        #Eviter le out of range :
                        if (ligne + k < self.nombre_carre_hauteur +1) and (colonne + K < self.nombre_carre_largeur +1)  :
                            self.set_state(ligne + k,colonne + K,etat)
                            self.set_cell_color(ligne + k,colonne + K,self.states[etat])
  
      
    def loop(self):
        """Starts the mainloop of the GUI."""
        self.window.mainloop()
         
         
         
  
    def bind_action(self, name, action):
         
        if name == "randmap":
            self.Randmap.configure(command=action)
        if name == "clearmap":
            self.Clearmap.configure(command=action)
        if name == "pause":
            self.Pause.configure(command=action)
        if name == "LifeGame":
            self.Pause.configure(command=action)
        if name == "Fire":
            self.Pause.configure(command=action)
              
              
  
    def reset(self, dimensions, states, set_state):
        """Restart the view with new dimensions and states.
  
        The parameters coincide with the parameters of the initializer.
        :param dimensions: the dimensions of the automaton,
        as a pair (width, height)
        :param states: gives the available states.
        It is given as a dictionary whose keys are the names of the states
        and the corresponding entries are the colors.
        :param set_state: the function to call for updating a state
        in the automaton. It takes three arguments, the line, the column, and
        the state to apply (i.e. the key from the dictionary)
        """