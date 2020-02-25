import CitiesManager
import Logic

def main():
   manager = CitiesManager.CitiesManager() # construteur du CitiesManager
   manager.addCities() # ajouter des villes a partir d"un fichier

   if(len(manager.cities) > 0): # si plus d'une ville existe

      algo = Logic.Logic(manager.cities, manager.cities[0]) # définit les villes comme sommets et un sommet de départ
      algo.increasingTour() # lance l'algoo de parcours IncreasingTour

      manager.displayCities() # Affiche les villes qui ont été visité ou non
      print(algo.costs) # affiche le côut

if __name__ == "__main__":
   main()