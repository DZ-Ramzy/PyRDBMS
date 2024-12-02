class DBManager:
    def __init__(self, db_config):
      
        self.db_config = db_config  # Instance de DBConfig
        self.databases = {}  # Dictionnaire pour stocker les bases de données (nom -> Database)
        self.active_database = None  # Base de données couramment active    # l'attribut self.active_database est défini,il ne prend pas simplement le nom de la base de données courante, mais une référence à l'instance de la classe Database représentant la base active.
                                                                              
                                                                              
    def CreateDatabase(self, nom_bdd):
    #Crée une nouvelle base de données avec le nom spécifié.
          if nom_bdd in self.databases:
          raise ValueError(f"La base de données '{nom_bdd}' existe déjà.")
    # Ajouter une nouvelle base de données (instance de Database) au dictionnaire
       self.databases[nom_bdd] = Database(nom_bdd)
           print(f"Base de données '{nom_bdd}' créée avec succès.")

    def SetCurrentDatabase(self, nom_bdd):
    # Active la base de données spécifiée par son nom.
        if nom_bdd not in self.databases:
        raise ValueError(f"La base de données '{nom_bdd}' n'existe pas.")
    # Définir la base de données active
    self.active_database = self.databases[nom_bdd]
    print(f"Base de données active : '{nom_bdd}'.")

    def AddTableToCurrentDatabase(self, tab):
    #Ajoute une table à la base de données active.
        if not self.active_database:
            raise ValueError("Aucune base de données active. Veuillez activer une base de données avant d'ajouter une table.")
        table_name = tab.relationName  # Nom de la table à partir de l'instance Relation
        if table_name in self.active_database.tables: 
            raise ValueError(f"La table '{table_name}' existe déjà dans la base de données active.")
    # Ajout de la table dans la base active
        self.active_database.tables[table_name] = tab
        print(f"Table '{table_name}' ajoutée à la base de données '{self.active_database.name}'.")

    def GetTableFromCurrentDatabase(self, nom_table):
    #Retourne l'instance de Relation correspondant à nomTable dans la base de données active.
        if not self.active_database:
            raise ValueError("Aucune base de données active.")
        if nom_table not in self.active_database.tables:
            raise ValueError(f"La table '{nom_table}' n'existe pas dans la base de données active.")
        return self.active_database.tables[nom_table]

    def RemoveTableFromCurrentDatabase(self, nom_table):
    #Supprime la table correspondant à nomTable dans la base de données active.
        if not self.active_database:
            raise ValueError("Aucune base de données active.")
        if nom_table not in self.active_database.tables:
            raise ValueError(f"La table '{nom_table}' n'existe pas dans la base de données active.")
        del self.active_database.tables[nom_table] #Supression
        print(f"La table '{nom_table}' a été supprimée de la base de données '{self.active_database.name}'.")


    def RemoveDatabase(self, nomBdd):
    #Supprime la base de données correspondant à nomBdd.
        if nomBdd not in self.databases:
            raise ValueError(f"La base de données '{nomBdd}' n'existe pas.")
     #DESACTIVER LA BASE DE DONNES AVANT LA SUPRESSION 
        if self.active_database and self.active_database.name == nomBdd: #verifier si elle est active et c'est bien la BDD qu'on veut supprimer 
            self.active_database = None  # Désactiver la base 
        del self.databases[nomBdd]
        print(f"La base de données '{nomBdd}' a été supprimée.")

    def RemoveTablesFromCurrentDatabase(self):
    #Supprime toutes les tables de la base de données active en utilisant clear().
        if not self.active_database:
            raise ValueError("Aucune base de données active.")
    
        self.active_database.tables.clear()
        print(f"Toutes les tables de la base de données '{self.active_database.name}' ont été supprimées.")

    def RemoveDatabases(self):
    #Supprime toutes les bases de données en utilisant clear() et désactive la base active.
        self.databases.clear()
        self.active_database = None #desactiver la reference car y aura aucune BDD active 
        print("Toutes les bases de données ont été supprimées.")

    def ListDatabases(self):
    #Affiche les noms de toutes les bases de données existantes, une par ligne.
        if not self.databases:
            print("Aucune base de données existante.")
        else:
            print("Bases de données existantes :")
            for db_name in self.databases.keys(): #liste des clés de bases de données qui existent 
                print(db_name)

    def ListTablesInCurrentDatabase(self):
    #Affiche les noms et les schémas (noms et types des colonnes) de toutes les tables de la base de données couramment active, une table par ligne.
        if not self.active_database:
            raise ValueError("Aucune base de données active.")
        if not self.active_database.tables:
            print(f"La base de données '{self.active_database.name}' ne contient aucune table.")
            return
        print(f"Tables dans la base de données '{self.active_database.name}':")
        for table_name, relation in self.active_database.tables.items(): # parcourir le dictionnaire pour avoir des paires (clé,valeur) sous forme de tuples 
        # Construire le schéma à partir des colonnes de la relation
            schema = ", ".join(relation.colInfoList) #concaténer les éléments de la liste en la sépareant par , 
            print(f"CREATE TABLE {table_name} ({schema})")




