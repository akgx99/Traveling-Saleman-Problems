class City:
    """ Classe Définissant une ville par :
    - Son numéro (int)
    - Sa latitude (float)
    - Sa longitude (float)
    - Son nom (string)
    """
    
    def __init__(self, id, latitude, longitude, name='None'):
        """ Constructeur de la classe City
        param :
            id
            latitude
            longitude
            name : nom de la ville
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

    def set_name(self, name):
        self._name = name
   
    """ Property """
    id = property(get_id)
    name = property(get_name, set_name)
    latitude = property(get_latitude)
    longitude = property(get_longitude)