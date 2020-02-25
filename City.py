class City:
    """ Classe Définissant une ville par :
    - Son numéro (int)
    - Son nom (string)
    - Sa latitude (float)
    - Sa longitude (float)
    - Son état (visité ou non)
    """
    
    def __init__(self, id, name, latitude, longitude):
        """ Constructeur de la classe City"""
        self._id = id
        self._name = name
        self._latitude = latitude
        self._longitude = longitude
        self._visited = False
    
    """ Getter & Setter """
    def get_id(self):
        return self._id
    def get_name(self):
        return self._name
    def get_latitude(self):
        return self._latitude
    def get_longitude(self):
        return self._longitude
    def get_visited(self):
        return self._visited

    """ Property """
    id = property(get_id)
    name = property(get_name)
    latitude = property(get_latitude)
    longitude = property(get_longitude)
    visited = property(get_visited)

    """ ToString """
    def __str__(self):
        if(self._visited):
            return "La ville "+str(self.id)+" a été visité"