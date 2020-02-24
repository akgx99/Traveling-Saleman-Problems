from math import sqrt

class Logic():
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
        
    def increasingTour(self):
        """ Algo de parcours des villes une à une par odre croissant de leur position """
        self.start.visited = True

        for vector in self._vectors:
            vector.visited = True
            suivant = self._vectors[+1]

            # calcul de distance de coordonnées selon le thèoréme de Pythagore
            self._costs += sqrt( (suivant.longitude - vector.latitude) ** 2 + (suivant.latitude - vector.longitude) ** 2) 

    """ Getter & Setter """
    def get_vectors(self):
        return self._vectors
    def get_start(self):
        return self._start
    def get_costs(self):
        return self._costs
    
    """ Property """
    start = property(get_start)
    vectors = property(get_vectors)
    costs = property(get_costs)

    