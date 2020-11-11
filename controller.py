from modele import *
from view import *


class Controleur :

    def __init__(self):
        
        ruleset="Fire"
        self.largeur=40
        self.hauteur=30
        self.etatdico={'fire' : 'red', 'tree' : 'green', 'ashes' : 'grey', 'empty' :'white'}
        self.control_variables = {'speed': 60}
        self.Modele = Automaton((self.largeur,self.hauteur), ruleset)
        self.Vue=View((self.largeur, self.hauteur),self.etatdico,self.Modele.set_cell,self.control_variables)
        self.Vue.bind_action("clearmap", self.Carte_vide)
        self.Vue.bind_action("randmap", self.Aleatoire)
        self.Vue.bind_action("pause", self.pause)
        self.Vue.loop()
        

    def actualisation_View(self):
       for i in range (0, self.hauteur):
           for j in range (0, self.largeur):
               etat_a_changer=self.Modele.ListeModele[i][j]
               couleur_a_changer=self.Modele.get_cell_color(i,j)
               self.Vue.set_cell_color(i,j,couleur_a_changer)
               
           
        
    
    def changement(self):
        self.Modele.compute_step(self.Vue.set_cell_color)
        self.Vue.window.after((101-self.Vue.value1.get())*19, self.changement)
    
    def pause(self):
        self.changement()

    def Aleatoire(self) :
        self.Modele.random_board()
        self.actualisation_View()
        print(self.Vue.value1.get())

    def Carte_vide(self):
        self.Modele.empty_board()
        self.actualisation_View()

   
    
toto=Controleur()


""" Vue : def __init__(self, dimensions, states, set_state, control_variables)
Modele : def __init__(self, dimensions, ruleset)  """
"""def compute_step(self, feedback=(lambda l, c, color: None)):"""
"""  def bind_action(self, name, action):
         
        if name == "randmap":
            self.Randmap.configure(command=action)
        if name == "clearmap":
            self.Clearmap.configure(command=action)
        if name == "pause":
            self.Pause.configure(command=action)"""
            
"""Le contrôleur dessine l'état initial de la grille et fait les différents appels de bind_action, ceci dès l'initialisation. 
En particulier, l'action liée au bouton pose doit lancer la boucle avec le timing. """
"self.Modele.random_board"
