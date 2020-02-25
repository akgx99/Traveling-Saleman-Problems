import Class.Logic.CitiesManager as CitiesManager
import Class.Logic.Algo as Algo
import tkinter as tk
from tkinter.filedialog import askopenfilename

class MainApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("TP - RO") # titre de la fenêtre
        self.master.geometry("300x450") # taille de la fenêtre
        self.pack()

        # affichage du coût
        self._displayCosts = tk.Label(self, text="Aucun algorithme choisi...")
        self._displayCosts.pack(side="bottom")

        # algo a utiliser
        self._chosenAlgo = None
        self._labelAlgo = tk.Label(self, text="Algo :")
        self._labelAlgo.pack(side="top")

        # boutton algo 1 : Tournéé croissante
        self._buttonAlgo1 = tk.Button(self, text="Tournée Croissante", command=lambda name="IncreasingTour":self.LaunchAlgorithm(name), width=15, height=1, bg="darkgray", fg="black", activebackground="lightgray")
        self._buttonAlgo1.pack(side="top")

        # affichage la liste des villes visitées
        self._displayRes = tk.Listbox(self, width=30, height=20)
        self._displayRes.pack()

        # affichage du coût
        self._displayCosts = tk.Label(self, text="Aucun algorithme choisi...")
        self._displayCosts.pack(side="bottom")

    def LaunchAlgorithm(self, name):
        """ Permet de lancer l'algorithme choisi """
        self._chosenAlgo = name
        self.openFile()

    def openFile(self):
        """ Ouvre un fichier avec une interface graphique pour choisir le fichier """
        self.filePath = askopenfilename(filetypes =(("TSP File", "*.tsp"),("TSP File","*.TSP")), title = "Choose a TSP file") # ouvre une fenêtre de choix de fichier .tsp ou .TSP
        self.clearList()

        if(self.filePath != ""):
            if self._chosenAlgo != None:
                self.process(self.filePath, self._chosenAlgo)     

    def process(self, file, algo):
        """ Fait le lien entre l'interface graphique et la couche métier """
        self.manager = CitiesManager.CitiesManager() # construteur du CitiesManager
        self.manager.addCities(file) # ajouter des villes a partir d"un fichier

        if(len(self.manager.cities) > 0): # si plus d'une ville existe
            self.algo = Algo.Algo(self.manager.cities, self.manager.cities[0]) # définit les villes comme sommets et un sommet de départ

            if self._chosenAlgo != None:
                if self._chosenAlgo == "IncreasingTour":
                    self.algo.increasingTour() # lance l'algo de parcours IncreasingTour
                    
                self.viewRes() # affiche les résultat dans la liste
                self.viewCosts() # affiche le coût de l'algo

    def clearList(self):
        """ Permet d'effacer le contenu de la listBox """
        self._displayRes.delete(0, tk.END)

    def viewRes(self):
        """ Affiche les villes visitées dans la liste """
        for i in range(0, len(self.manager.cities)):
            self._displayRes.insert(i, self.manager.cities[i])
    
    def viewCosts(self):
        self._displayCosts['text'] = self.algo.costs
