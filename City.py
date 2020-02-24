class City:
    """ Classe Définissant une ville par :
    - Son numéro (int)
    - Son nom (string)
    - Sa latitude (float)
    - Sa longitude (float)
    """
    
    def __init__(self, id, name, latitude, longitude):
        """ Constructeur de la classe City"""
        self._id = id
        self._name = name
        self._latitude = latitude
        self._longitude = longitude
    
    """ Getter & Setter """
    def get_id(self):
        return self._id
    def get_name(self):
        return self._name
    def get_latitude(self):
        return self._latitude
    def get_longitude(self):
        return self._longitude

    def set_id(self, id):
        self._id = id 
    def set_name(self, name):
        self._name = name     
    def set_latitude(self, latitude):
        self._latitude = latitude
    def set_longitude(self, longitude):
        self._longitude = longitude  

    """ Property """
    id = property(get_id, set_id)
    name = property(get_name, set_name)
    latitude = property(get_latitude, set_latitude)
    longitude = property(get_longitude, set_longitude)

    """ ToString """
    def __str__(self):
        return "La ville "+str(self.id)+" du nom de "+self.name+" se trouve en position "+str(self._latitude)+"::"+str(self.longitude)