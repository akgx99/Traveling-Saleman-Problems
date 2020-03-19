from math import sqrt, pi, sin, cos, radians, atan2
import random as rnd
import Class.Logic.Calculus as calc

class Algo():
    """ Classe contenant les différents algorithmes du plus court chemin. Elle contient :
    - Une liste des sommets
    - Un sommet de départ
    - un coût (coût du déplacement)
    """

    def __init__(self, vertex, start):
        """ Constructeur de la classe Algo 
        param:
            vertex : les sommets à visiter
            start : le sommet de départ
        """
        self._visited = []
        self._vertex = vertex
        self._start = start
        self._costs = 0
        self._cliDisplay = []

    def increasingTour(self):
        """ Algo de parcours des villes une à une par ordre croissant de leur position """
        i = 0
        for current in self._vertex:
            self._visited.append(current)
            self._cliDisplay.append(current.id)
            if len(self._visited) < len(self._vertex):
                next = self._vertex[i+1]
                self._costs += calc.dist(current, next)
                i= i+1
            elif len(self._vertex) > 2:
                next = self._start
                self._costs += calc.dist(current, next)
    
        print(self._cliDisplay)

    def randomTour(self):
        """ Algo de parcours aléatoire des villes à visiter """
        
        rnd.shuffle(self._vertex) # trie aléatoirement la liste de ville
        self.increasingTour() # parcours la liste dans l'ordre aléatoire 
        
    def findNearestNeighbor(self, city):
        """ Algo qui permet de trouver le plus proche de voisin d'une ville

        city : la depuis laquelle on doit trouver le plus proche voisin

        return : La ville la plus proche
        """
        min = float("inf") # nombre infini 

        for next in self._vertex:
            if next not in self._visited: # si la ville n'a pas été visitée
                if calc.dist(city, next) < min: # si la distance est inférieur à la plus petite distance précédente
                    # alors elle devient la ville la plus proche
                    min = calc.dist(city, next) 
                    res = next
        return res

    def closeNeighbor(self):
        current = self._start
        self.visited.append(current)

        while len(self._visited) < len(self._vertex):
            next = self.findNearestNeighbor(current) # la suivante est la ville la plus proche
            self.visited.append(next) # la ville suivante à été visitée
            self._costs += calc.dist(current, next)
            self._cliDisplay.append(current.id)
            current = next # la ville d'arrivée depuis la ville de départ une fois visitée
        self._costs += calc.dist(current, self._start)
        print(self._cliDisplay)

    """ Getter & Setter """
    def get_vertex(self):
        return self._vertex
    def get_start(self):
        return self._start
    def get_costs(self):
        return "Le coût est de "+str(self._costs)+" km"
    def get_visited(self):
        return self._visited
    def get_getDisplay(self):
        return self._visited
            
    """ Property """
    start = property(get_start)
    vertex = property(get_vertex)
    cliDisplay = property(get_getDisplay)
    costs = property(get_costs)
    visited = property(get_visited)