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

        cityOne = rnd.randrange(1, len(self._vertex)) # numéro ville 1 au hasard
        next = self._vertex[cityOne]
        self.visited.append(next)

        while next is not self._vertex[len(self._vertex)- 1]:
            randX = rnd.randrange(1, len(self._vertex)) # numéro ville X au hasard
            randY = rnd.randrange(1, len(self._vertex)) # numéro ville Y au hasard
            
            current = self._vertex[randX]
            self.visited.append(current)

            next = self._vertex[randY]
            self.visited.append(next)

            self._costs += self.distanceInKm(current.latitude, current.longitude, next.latitude, next.longitude)

        self._costs += self.distanceInKm(current.latitude, current.longitude, next.latitude, next.longitude)
            
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