class Parser():
    """ Classe parseur servant à parcourir un fichier pour en extraire des données :
    - file : le fichier à parcourir
    """

    def __init__(self):
        self._file = None

    def open(self):
        """ Permet d'ouvir un fichier """
        try:
            name = input("Nom du fichier : \n")
            self.file = open(name, 'r')
        except IOError:
            print('Cannot open : ', name)
        self.file.close()

    

    """ Getter & Setter """
    def get_file(self):
        return self._file

    def set_file(self, file):
        self._file = file

    """ Property """
    file = property(get_file, set_file)