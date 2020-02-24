import CitiesManager
import Logic

def main():
   manager = CitiesManager.CitiesManager()
   manager.addCities()

   algo = Logic.Logic(manager.cities, manager.cities[0])
   algo.increasingTour()

   manager.displayCities()
   print("Le coût est de "+ str(algo.costs)+" Km")

if __name__ == "__main__":
   main()