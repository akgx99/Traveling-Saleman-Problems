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
        """ Construteur de la classe logic 
        param:
            vertex : les sommets à visiter
            start : le sommet de départ
        """
        self._visited = []
        self._vertex = vertex
        self._start = start
        self._costs = 0.00

    def increasingTour(self):
        """ Algo de parcours des villes une à une par ordre croissant de leur position """
        for current in self._vertex:
            self._visited.append(current)
            next = self._vertex[+1]

            self._costs += calc.dist(current, next)

    def randomTour(self):
        """ Algo de parcours aléatoire des villes à visiter """
        current = self._start
        self.visited.append(current)

        while len(self._visited) < len(self._vertex):
            rand = rnd.randrange(1, len(self._vertex)) # numéro ville au hasard
            
            next = self._vertex[rand]

            if next not in self._visited: # si la ville suivante n'a pas déjà été visitée
                self.visited.append(next)
                self._costs += calc.dist(current, next)
                current = next # la ville d'arrivée depuis la ville de départ une fois visitée

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
            current = next # la ville d'arrivée depuis la ville de départ une fois visitée


    """ Getter & Setter """
    def get_vertex(self):
        return self._vertex
    def get_start(self):
        return self._start
    def get_costs(self):
        return "Le coût est de "+str(self._costs)+" km"
    def get_visited(self):
        return self._visited
            
    """ Property """
    start = property(get_start)
    vertex = property(get_vertex)
    costs = property(get_costs)
    visited = property(get_visited)