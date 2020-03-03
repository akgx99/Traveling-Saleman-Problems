class Parser():
    """ Classe parseur servant à parcourir un fichier pour en extraire des données et créer des objets :
    - file : le fichier à parcourir
    - data : les données triées du fichier

    Les données sont stockées ligne par ligne. Ligne qui contiennent des éléments (ex : la ligne : "35 47.416667 4.366667" contient trois éléments)
    """

    def __init__(self):
        self._file = None
        self._data = []

    def extractContents(self, file):
        """ Permet d'extraire ligne par ligne sous forme de liste les données 
        param: 
            file : le fichier à parcourir
        """
        try:
            self._file = open(file, 'r')
        except IOError:
            print('Cannot open: ', file)
        else:
            with self._file as f:
                for line in f:
                    self._data.append(line)
            self._file.close()

    """ Getter & Setter """
    def get_data(self):
        return self._data

    """ Property """
    data = property(get_data)