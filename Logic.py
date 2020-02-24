import Parser as parse
import City

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
        FileParser.extractContents()
        for x in FileParser.data:
            ele = x.split(" ", 3) # liste des éléments (id, latitude et longitude) contenus dans chaque jeu de données
            city = City.City(int(ele[0]), "None", float(ele[1]), float(ele[2])) # construteur de la ville avec les éléments précédents
            self.cities.append(city)

    def displayCities(self):
        """ Permet d'afficher les informations des villes """
        for city in self.cities:
                print(city)

    """ Getter & Setter """
    def get_cities(self):
        return self._cities

    def set_cities(self, cities):
        self._cities = cities
    
    """ Property """
    cities = property(get_cities, set_cities)