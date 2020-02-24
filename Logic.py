import Parser as parse

class Logic():
    """ Classe servant à représenter la couche métier. elle contient :
    - Une liste des villes (City)
    """

    def __init__(self):
        """ Constructeur de la classe Logic """
        self._cities = []
    
    def addCity(self, city):
        """ Permet d'ajouter une ville à la liste 
        - city : la ville à ajouter
        """
        self.cities.append(city)

    def addCities(self):
        """ Permet depuis un fichier (définit par l'utilisateur) d'ajouter un ensemble de ville """
        FileParser = parse.Parser()
        FileParser.open()
        FileParser.extractContents()
        self.cities.append(FileParser.createCities())

    def displayCities(self):
        """ Permet d'afficher les informations des villes """
        for li in self.cities:
            for city in li:
                print(city)

    """ Getter & Setter """
    def get_cities(self):
        return self._cities

    def set_cities(self, cities):
        self._cities = cities
    
    """ Property """
    cities = property(get_cities, set_cities)