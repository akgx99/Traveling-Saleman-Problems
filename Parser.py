class Parser():
    """ Classe parseur servant à parcourir un fichier pour en extraire des données et créer des objets :
    - file : le fichier à parcourir
    - data : les données triées du fichier

    Les données sont stockées ligne par ligne. Ligne qui contiennent des éléments (ex : la ligne : "35 47.416667 4.366667" contient trois éléments)
    """

    def __init__(self):
        self._file = None
        self._data = []

    def extractContents(self):
        """ Permet d'extraire ligne par ligne sous forme de liste les données """
        try:
            name = input("Nom du fichier : \n")
            self.file = open(name, 'r')
        except IOError:
            print('Cannot open: ', name)
        else:
            with self.file as f:
                for line in f:
                    self._data.append(line)
            self._file.close()

    """ Getter & Setter """
    def get_file(self):
        return self._file

    def set_file(self, file):
        self._file = file
    
    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    """ Property """
    file = property(get_file, set_file)
    data = property(get_data, set_data)