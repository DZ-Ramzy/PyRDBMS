class DBManager:
    def __init__(self, db_config):
        """
        Constructeur de la classe DBManager.
        param db_config: Instance de DBConfig pour la configuration du gestionnaire.
        """
        self.db_config = db_config  # Instance de DBConfig
        self.databases = {}  # Dictionnaire pour stocker les bases de données (nom -> Database)
        self.active_database = None  # Base de données couramment active    # l'attribut self.active_database est défini,il ne prend pas simplement le nom de la base de données courante, mais une référence à l'instance de la classe Database représentant la base active.
                                                                              
                                                                              
    def create_database(self, nom_bdd):
    #Crée une nouvelle base de données avec le nom spécifié.
          if nom_bdd in self.databases:
          raise ValueError(f"La base de données '{nom_bdd}' existe déjà.")
    
    # Ajouter une nouvelle base de données (instance de Database) au dictionnaire
       self.databases[nom_bdd] = Database(nom_bdd)
           print(f"Base de données '{nom_bdd}' créée avec succès.")

    def set_current_database(self, nom_bdd):
    # Active la base de données spécifiée par son nom.
        if nom_bdd not in self.databases:
        raise ValueError(f"La base de données '{nom_bdd}' n'existe pas.")
    
    # Définir la base de données active
    self.active_database = self.databases[nom_bdd]
    print(f"Base de données active : '{nom_bdd}'.")

