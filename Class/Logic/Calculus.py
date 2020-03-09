from math import sqrt, pi, sin, cos, radians, atan2, floor

def distanceInKm(latitude1, longitude1, latitude2, longitude2):
    """ Calcul de la distance en mètre entre deux coordonnées en prenant en compte que la terre est sphérique 
    param :

    latitude1, longitude1 : latitude et longitude de départ
    latitude2, longitude2 : latitude et longitude d'arrivée
    """
    EARTH_RADIUS = 6378137 # Terre -> sphère de 6378km de rayon
    
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

    return out

def distEarthRadius(start, destination):
        """ Calcul de la distance entre deux villes 
        param :
        
        start : la ville de départ
        destination : la ville d'arrivée
        """
        res = distanceInKm(start.latitude, start.longitude, destination.latitude, destination.longitude)
        return truncate(res, 3)

def dist(start, destination):
    """ Calcul de la distance entre deux villes (avec le théorème de Pythagore)

    param :
    
    start : la ville de départ
    destination : la ville d'arrivée
    """
    return sqrt( (destination.longitude - start.longitude) ** 2 + (destination.latitude - start.latitude) ** 2) * 100 # application du théorème de Pythagore + conversion en km

def truncate(nb, decimals=0):
    """ Permet de tronquer un nombre 
    param :

    nb : le nombre
    decimals : le nombre de décimal
    """
    multiplier = 10 ** decimals
    return int(nb * multiplier) / multiplier


