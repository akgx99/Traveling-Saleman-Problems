import City as c

class Logic():
    """ Classe servant à représenter la couche métier. elle contient :
    - Une liste des villes (City)
    """

    def __init__(self):
        self._cities = []

    
    """ Getter & Setter """
    def get_cities(self):
        return self._cities

    def set_cities(self, cities):
        self._cities = cities
    
    """ Property """
    cities = property(get_cities, set_cities)