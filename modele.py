#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from random import*


"""Module Modele: contains all the elements that acts \
on the cellular Automaton.
"""



class Automaton():
    """All data about the board and its evolution.

    This is the main class of this file.
    """

    def __init__(self, dimensions, ruleset):
        """Initializes the automaton.

        :param dimensions: the dimensions of the automaton, as a pair
        (width, height)
        :param ruleset: a ruleset, as a string. 
        If the string is not acceptable or implemented, makes an automaton with the ruleset "Fire".
        """
        self.dimensions = dimensions
        self.largeur = dimensions[0]
        self.hauteur = dimensions[1]
        self.ruleset=ruleset
        
        if self.ruleset == "Fire" :
            self.state = {'fire' : 'red', 'tree' : 'green', 'ashes' : 'grey', 'empty' :'white'}
        if self.ruleset == "LifeGame" :
            self.state = {'alive': 'red', 'empty': 'white'}
    
        self.createListeModele()
        
        
        
    def empty_board(self):
        for l in range (0, len(self.ListeModele)):
            for c in range (0, len(self.ListeModele[l])):
                self.set_cell(l, c,'empty')
                
        """Empty the current board.

        Acts by side-effect on the automaton.
        """
        

    def random_board(self):
        if self.ruleset=="Fire":
            L =['empty','tree']
            feuListeLigne=[]
            feuListeColonne=[]
            for l in range (0, len(self.ListeModele)):
                feuListeLigne.append(l)
                for c in range (0, len(self.ListeModele[l])):
                    aleatoire = choice(L)
                    self.set_cell(l, c,aleatoire)
                    if l == 0 : 
                        feuListeColonne.append(c)
                    
                
            feuLigne = choice(feuListeLigne)
            feuColonne = choice(feuListeColonne)
            self.set_cell(feuLigne, feuColonne,'fire')
            
        if self.ruleset=="LifeGame":
            L = ["alive", "empty"]
            for l in range (0, len(self.ListeModele)):
                for c in range (0, len(self.ListeModele[l])):
                    aleatoire = choice(L)
                    self.set_cell(l, c,aleatoire)
        """Fills the current board with random states appropriate for the rules.

        Acts by side-effect on the automaton.
        """
        
    def createListeModele(self) :
        self.ListeModele= []
        for i in range (0, self.hauteur) :
            for j in range (0, self.largeur) :
                if j == 0 :
                    self.ListeModele.append(['empty'])
                else :
                    self.ListeModele[i].append('empty')
        


    def get_cell_color(self, l, c):
        for cle in self.state :
            if self.ListeModele[l-1][c-1] == cle :
                return(self.state[cle])
    
    
    def set_cell(self, l, c, state):
        self.ListeModele[l-1][c-1] = state
        """self.get_cell_color(l-1,c-1)"""
        
        """Updates the cell l,c to state corresponding to the key "state".

        Is used in particular for editing the board from the controller.
        :param l,c: line and column for the edition of the board. They range from 0 to height-1 or width-1
        :param state: a state as the key in the association form get_states.
        """

    def compute_step(self, feedback=(lambda l, c, color: None)):
        """ Applies one step to every square on the board.

        :param feedback: a function on three arguments, l, c, color, 
        that is used to notify the controller that a change of color 
        is needed on the cell at position l,c (into the given color).
        :returns: a boolean,  True if at least one cell changed of state.
        """
        
        if self.ruleset=="Fire":
            cpt_ligne=0
            cpt_colonne=0
            cpt_Ligne=-1
            cpt_Colonne=-1
            ListeFire = []
            for i in self.ListeModele:
                cpt_Ligne=cpt_Ligne+1
                cpt_Colonne=-1
                for j in i:
                    cpt_Colonne=cpt_Colonne+1
                    if j=="fire":
                        ListeFire.append((cpt_Colonne,cpt_Ligne))
            for i in ListeFire :
                cpt_colonne = i[0]
                cpt_ligne = i[1]
                self.ListeModele[cpt_ligne][cpt_colonne] = "ashes"
                print(self.ListeModele[cpt_ligne][cpt_colonne])
                feedback(cpt_ligne+1,cpt_colonne+1,'grey')
                if self.ListeModele[cpt_ligne][cpt_colonne-1] == "tree" and cpt_colonne > 0 :
                    self.ListeModele[cpt_ligne][cpt_colonne-1]="fire"
                    feedback(cpt_ligne+1,cpt_colonne,'red')
                if cpt_colonne<39 and self.ListeModele[cpt_ligne][cpt_colonne+1] == "tree":
                    self.ListeModele[cpt_ligne][cpt_colonne+1]="fire"
                    feedback(cpt_ligne+1,cpt_colonne+2,'red')
                if self.ListeModele[cpt_ligne-1][cpt_colonne] == "tree" and cpt_ligne > 0 :
                    self.ListeModele[cpt_ligne-1][cpt_colonne]="fire"
                    feedback(cpt_ligne,cpt_colonne+1,'red')
                if cpt_ligne<29 and self.ListeModele[cpt_ligne+1][cpt_colonne] == "tree":
                    self.ListeModele[cpt_ligne+1][cpt_colonne]="fire"
                    feedback(cpt_ligne+2,cpt_colonne+1,'red')
                    
        if self.ruleset == "LifeGame":
            compteurMort=0
            cptLigne = -1
            cptColonne = 0
            compteurVivant = 0
            for i in range (1, len(self.ListeModele)-1):
                for j in range (1,len(self.ListeModele[i])-1) :
                    """if self.ListeModele[i][j] == "empty" :
                        compteurMort=-1
                        for k in range (j -1, j + 2) :
                            for K in range(i -1, i +2) :
                                if self.ListeModele[K][k] == "empty" :
                                    compteurMort = compteurMort +1
                        if 8 - compteurMort == 3 :
                            self.ListeModele[i][j] = "alive"
                            feedback(i+1,j+1,'red')"""
                    if self.ListeModele[i][j] == "alive" : 
                        compteurVivant = -1
                        for k in range (j -1, j + 2) :
                            for K in range(i -1, i +2) :
                                if self.ListeModele[K][k] == "alive" :
                                    compteurVivant = compteurVivant +1
                        print(compteurVivant)
                        if  compteurVivant == 0 or compteurVivant == 1 or compteurVivant == 4 or  compteurVivant == 5 or compteurVivant == 6 or compteurVivant == 7 or compteurVivant == 8 :
                            self.ListeModele[i][j] = "empty"
                            feedback(i+1,j+1,'white')
                        
    
           
           
            
        
                    
       
        """feedback(l,c,'red') est equivalent à dire; je veux colorier la case l,c en red."""
            
        return True         
            
            
        
    def get_states(self):
        
        return self.state

