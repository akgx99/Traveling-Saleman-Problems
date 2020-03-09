from math import sqrt, pi, sin, cos,radians, atan2
import random as rnd

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

    def distanceInKm(self, latitude1, longitude1, latitude2, longitude2):
        """ Calcul de la distance en mètre en prenant en compte que la terre est sphérique 
        param :

        latitude1, longitude1 : latitude et longitude de départ
        latitude2, longitude2 : latitude et longitude d'arrivée
        """
        EARTH_RADIUS = 6378137 # Terre -> sphère de 6378km de rayon
        
        #degres to radian
        rLat1 = latitude1*(pi/180)  
        rLon1 = longitude1*(pi/180)
        rLon2 = longitude2*(pi/180)
        rLat2 = latitude2*(pi/180)
        degresLo = (rLon2 - rLon1)  / 2
        degresLa = (rLat2 - rLat1)  / 2

        #calcul
        calc = (sin(degresLa) ** 2) + cos(rLat1) * cos(rLat2) * (sin(degresLo) ** 2)
        dist = 2 * atan2(sqrt(calc), sqrt(1-calc))
        out = (EARTH_RADIUS * dist) / 1000

        return round(out, 3)

    def increasingTour(self):
        """ Algo de parcours des villes une à une par ordre croissant de leur position """
        for current in self._vertex:
            self._visited.append(current)
            next = self._vertex[+1]

            self._costs += self.distanceInKm(current.latitude, current.longitude, next.latitude, next.longitude)
            
    def randomTour(self):
        """ Algo de parcours aléatoire des villes à visiter """
        current = self._start
        self.visited.append(current)

        while len(self._visited) < len(self._vertex):
            rand = rnd.randrange(1, len(self._vertex)) # numéro ville au hasard
            
            next = self._vertex[rand]

            if next not in self._visited: # si la ville suivante n'a pas déjà été visitée
                self.visited.append(next)
                self._costs += self.distanceInKm(current.latitude, current.longitude, next.latitude, next.longitude)
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