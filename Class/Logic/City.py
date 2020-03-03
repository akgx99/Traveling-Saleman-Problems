class City:
    """ Classe Définissant une ville par :
    - Son numéro (int)
    - Son nom (string)
    - Sa latitude (float)
    - Sa longitude (float)
    - Son état (visité ou non)
    """
    
    def __init__(self, id, name, latitude, longitude):
        """ Constructeur de la classe City
        param :
            id
            name : nom de la ville
            latitude
            longitude
        """
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
   
    """ Property """
    id = property(get_id)
    name = property(get_name)
    latitude = property(get_latitude)
    longitude = property(get_longitude)
