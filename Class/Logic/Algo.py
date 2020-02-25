from math import sqrt, pi, sin, cos,radians, atan2

class Algo():
    """ Classe contenant les différents algorithmes du plus court chemin. Elle contient :
    - Une liste des sommets
    - Un sommet de départ
    - un cout (coût du déplacement)
    """

    def __init__(self, vectors, start):
        """ Construteur de la classe logic """
        self._vectors = vectors
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
        self.start._visited = True

        for current in self._vectors:
            current._visited = True
            next = self._vectors[+1]

            self._costs += self.distanceInKm(current.latitude, current.longitude, next.latitude, next.longitude)
            
    """ Getter & Setter """
    def get_vectors(self):
        return self._vectors
    def get_start(self):
        return self._start
    def get_costs(self):
        return "Le coût est de "+str(self._costs)+" km"
    
    """ Property """
    start = property(get_start)
    vectors = property(get_vectors)
    costs = property(get_costs)