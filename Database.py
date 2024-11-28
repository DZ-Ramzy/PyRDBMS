class Database:
    def __init__(self, name):
        self.name = name
        # Dictionnaire pour stocker les tables
        # Clé : Nom de la table, Valeur : Instance de la classe Relation
        self.tables = {}


     # Getter pour le nom de la base de données
    def get_name(self):
        return self.name

    # Setter pour le nom de la base de données
    def set_name(self, name):
        if not name:
            raise ValueError("Le nom de la base de données ne peut pas être vide.")
        self.name = name

    # Getter pour les tables
    def get_tables(self):
        return self.tables

    # Setter pour les tables (rarement utilisé, mais disponible si nécessaire)
    def set_tables(self, tables):
        if not isinstance(tables, dict):
            raise ValueError("Les tables doivent être un dictionnaire.")
        self.tables = tables


  #########################################################UN PLUS ################################################################

    def create_table(self, table_name, columns, taille_var=False):
        """Créer une nouvelle table."""
        if table_name in self.tables:
            raise ValueError(f"La table '{table_name}' existe déjà dans la base de données '{self.name}'.")
        self.tables[table_name] = Relation(
            relationName=table_name,
            nbCollumn=len(columns),
            colInfoList=columns,
            tailleVar=taille_var,
            bufferManager=None,  # À adapter si nécessaire
            headerPageId=None    # À adapter si nécessaire
        )
        print(f"Table '{table_name}' créée dans la base de données '{self.name}'.")

    def drop_table(self, table_name):
        """Supprimer une table."""
        if table_name not in self.tables:
            raise ValueError(f"La table '{table_name}' n'existe pas dans la base de données '{self.name}'.")
        del self.tables[table_name]
        print(f"Table '{table_name}' supprimée de la base de données '{self.name}'.")

    def list_tables(self):
        """Lister les tables de la base de données."""
        if not self.tables:
            print(f"Aucune table dans la base de données '{self.name}'.")
        else:
            print(f"Tables dans la base de données '{self.name}':")
            for table_name, relation in self.tables.items():
                print(f"- {table_name} : {relation.getCol_info_list()}")
