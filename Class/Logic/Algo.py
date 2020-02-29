from math import sqrt, pi, sin, cos,radians, atan2
import random as rnd

class Algo():
    """ Classe contenant les différents algorithmes du plus court chemin. Elle contient :
    - Une liste des sommets
    - Un sommet de départ
    - un cout (coût du déplacement)
    """

    def __init__(self, vertex, start):
        """ Construteur de la classe logic """
        self._visited = []
        self._vertex = vertex
        self._start = start
        self._costs = 0.00

    def distanceInKm(self, latitude1, longitude1, latitude2, longitude2):
        """ Calcul de la distance en mètre en prennant en compte que la terre est sphérique """
        EARTH_RADIUS = 6378137; # Terre -> shpère de 6378km de rayon
        
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

        return round(out, 2)

    def increasingTour(self):
        """ Algo de parcours des villes une à une par odre croissant de leur position """
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

            if next not in self._visited:
                self.visited.append(next)
                self._costs += self.distanceInKm(current.latitude, current.longitude, next.latitude, next.longitude)
                current = next          
            
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