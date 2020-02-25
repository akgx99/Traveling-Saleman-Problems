# Traveling Saleman Problems

## Introduction

Il s'agit d"un projet permettant de tester les applications d'algorithmes du plus court chemin 
dans le cadre du cours de recherche opérationnelle
de DUT informatique.

## Dépendances 

- Un environnement prolog (https://www.swi-prolog.org/)
- Python3 (https://www.python.org/download/releases/3.0/)
- La librairie Python Tkinter (https://docs.python.org/fr/3/library/tkinter.html)

## Quick start

### CLI

Dans un fichier ou directement depuis la console python exécutez le code suivant :

```python
import CitiesManager
import Logic

def main():
   manager = CitiesManager.CitiesManager() # construteur du CitiesManager
   manager.addCities("fileName") # ajouter des villes a partir d"un fichier

   if(len(manager.cities) > 0): # si plus d'une ville existe
      
      # définit les villes comme sommets et un sommet de départ
      algo = Logic.Logic(manager.cities, manager.cities[0]) 
      algo.increasingTour() # lance l'algoo de parcours IncreasingTour

      manager.displayCities() # Affiche les villes qui ont été visité ou non
      print(algo.costs) # affiche le côut

if __name__ == "__main__":
   main()
```

### GUI

Lancer le fichier ```main.py```

Le programme pour fonctionner à besoin d'un fichier, renseignez un des fichiers suivants (ou créer le votre) :

```
villes.tsp, villes2.tsp, villes5.tsp
```

Une fois exécuté le programme vous proposera une sortie comme celle-ci :

```
La ville 1 a été visité
La ville 2 a été visité
Le coût est de 17.73 km
```

Pour aller plus loin se référer à la documentation technique (pas encore disponible)

## Notes

A l'heure actuelle le projet comporte :

- Un algo de tournée croissante (par numéro de ville)
- Une interface console (CLI)
