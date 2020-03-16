import Class.Logic.Parser as parse
import Class.Logic.City as City

class CitiesManager():
    """ Classe servant à gérer les villes à visiter. elle contient :
    - Une liste des villes (City)
    """

    def __init__(self):
        """ Constructeur de la classe Logic """
        self._cities = []
    
    def addCity(self, city):
        """ Permet d'ajouter une ville à la liste 
        param :
            city : la ville à ajouter
        """
        self._cities.append(city)

    def addCities(self, file):
        """ Permet depuis un fichier (définit par l'utilisateur) d'ajouter un ensemble de ville 
        
        param :
            file : le fichier à parcourir
        """
        FileParser = parse.Parser()
        FileParser.extractContents(file)
        for x in FileParser.data:
            ele = x.split(" ", 3) # liste des éléments (id, latitude et longitude) contenus dans chaque jeu de données
            city = City.City(int(ele[0]), float(ele[1]), float(ele[2])) # construteur de la ville avec les éléments précédents
            self._cities.append(city)

            for i in range(0, len(self._cities)):
                FileParser.extractName()
                Names = FileParser.name
                ele = Names[i].split(" ")
                city.name = ele[1]

  
    """ Getter & Setter """
    def get_cities(self):
        return self._cities
    def set_cities(self, cities):
        self._cities = cities
    
    """ Property """
    cities = property(get_cities, set_cities)