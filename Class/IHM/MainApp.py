import Class.Logic.CitiesManager as CitiesManager
import Class.Logic.Calculus as Calc
import Class.Logic.Algo as Algo
import tkinter as tk
from tkinter.filedialog import askopenfilename

class MainApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="alice blue")
        self.master = master
        self.master.title("TP - RO") # titre de la fenêtre
        self.master.geometry("400x500")
        self.master['bg'] = "alice blue"
        self.pack()

        # affichage du coût
        self._displayCosts = tk.Label(self, bg="alice blue", text="Aucun algorithme choisi...")
        self._displayCosts.pack(side="top", pady="10")

        # algo a utiliser
        self._chosenAlgo = None

        #boutton algo 1 : Tournéé croissante
        self._buttonAlgo1 = tk.Button(self, text="Tournée Croissante", command=lambda name="IncreasingTour":self.LaunchAlgorithm(name), width=15, height=1, bg="dodger blue", fg="light cyan", activebackground="lightgray")
        self._buttonAlgo1.pack(side="bottom",  pady="10")

        # boutton algo 2 : Tournéé random
        self._buttonAlgo2 = tk.Button(self, text="Au hasard", command=lambda name="RandomTour":self.LaunchAlgorithm(name), width=15, height=1, bg="dodger blue", fg="light cyan", activebackground="lightgray")
        self._buttonAlgo2.pack(side="bottom",  pady="10")

         # boutton algo 2 : Tournéé random
        self._buttonAlgo3 = tk.Button(self, text="Proche voisin", command=lambda name="closeNeighbor":self.LaunchAlgorithm(name), width=15, height=1, bg="dodger blue", fg="light cyan", activebackground="lightgray")
        self._buttonAlgo3.pack(side="bottom",  pady="10")

        # affichage la liste des villes visitées
        self._displayRes = tk.Listbox(self, width=30, height=20)
        self._displayRes.pack(side="left", fill="y")
        
        scrollBar = tk.Scrollbar(self, bg="alice blue", orient="vertical")
        scrollBar.config(command=self._displayRes.yview)
        scrollBar.pack(side="right", fill="y")
        
        self._displayRes.config(yscrollcommand=scrollBar.set)

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
                elif self._chosenAlgo == "RandomTour":
                    self.algo.randomTour() # lance l'algo de parcours RandomTour
                elif self._chosenAlgo == "closeNeighbor":
                    self.algo.closeNeighbor() # lance l'algo de parcours closeNeighbor
                    
                self.viewRes() # affiche les résultat dans la liste
                self.viewCosts() # affiche le coût de l'algo

    def clearList(self):
        """ Permet d'effacer le contenu de la listBox """
        self._displayRes.delete(0, tk.END)

    def viewRes(self):
        """ Affiche les villes visitées dans la liste """
        for i in range(0, len(self.algo.visited)):
            out = str(self.algo.visited[i].name)+" ("+ str(self.algo.visited[i].id) +") a été visité"
            self._displayRes.insert(i, out)
            
    def viewCosts(self):
        self._displayCosts['text'] = self._displayCosts['text'] = str(Calc.costTour(self.algo.visited, self.algo.start))+" km parcouru"
