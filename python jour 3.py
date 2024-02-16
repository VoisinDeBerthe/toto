# https://www.sharemycode.fr/pythonj3

# T : Léa, Allaric
# HP : Sophie, Bruno, Lucas
# SW : Laurent, David

# bases de données exo avec bonus execute

import sqlite3


database_name = "my_database.db"
sql_create = """ CREATE TABLE IF NOT EXISTS books(
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_name TXT, 
    author TXT);
    """

with sqlite3.connect(database_name) as conn:
    cursor = conn.cursor()
    cursor.execute(sql_create) # creation table

    # insertions
    cursor.execute("""INSERT INTO books(book_name, author)
    VALUES("Lord of the rings 1 : the fellowship of the ring",
     "J.R.R. Tolkien");""")

    reference = ("Lord of the rings 2 : the two towers", "J.R.R. Tolkien")
    cursor.execute("""INSERT OR IGNORE INTO books (book_name, author)
      VALUES(?, ?)""", reference)

    reference = ("Lord of the rings 3 : the return of the king", "J.R.R. Tolkien")
    cursor.execute("""INSERT OR IGNORE INTO books (book_name, author)
      VALUES(?, ?)""", reference)

    list_of_references = [
        ("Harry Potter 1", "J. K. Rowling"),
        ("Harry Potter 2", "J. K. Rowling"),
        ("Harry Potter 3", "J. K. Rowling"),
        ("Harry Potter 4", "J. K. Rowling"),
        ("Harry Potter 5", "J. K. Rowling"),
        ("Harry Potter 6", "J. K. Rowling"),
        ("Harry Potter 7", "J. K. Rowling"),

    ]
    sql_insert = """INSERT OR IGNORE INTO books (book_name, author)
      VALUES(?, ?)"""
    cursor.executemany(sql_insert, list_of_references)

    # affichage de la table entière
    cursor.execute("""SELECT * FROM books """) # selection
    rows = cursor.fetchall()
    for row in rows:
        print(row)




# bases de données démo avec mot-clé with ----------------------

import sqlite3


database_name = "my_database.db"
sql_create = """ CREATE TABLE IF NOT EXISTS contacts (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       nom TEXT,
       age INT,
       job TXT); 
    """

with sqlite3.connect(database_name) as conn:
    cursor = conn.cursor()
    cursor.execute(sql_create) # creation table

    # insertions
    cursor.execute("""INSERT OR IGNORE INTO contacts (nom, age, job)
      VALUES("Monty", 42, "humoriste")""")

    reference = ("Python", 33, "dev")
    cursor.execute("""INSERT OR IGNORE INTO contacts (nom, age, job)
      VALUES(?, ?, ?)""", reference)

    # affichage de la table entière
    cursor.execute("""SELECT * FROM contacts """) # selection
    rows = cursor.fetchall()
    for row in rows:
        print(row)





# fichiers json exo --------------------------

import json


def save_dico(dico_to_save, output_filename):
    """
    sauvegarde les données du dictionnaire
    dans un fichier json
    """
    with open(output_filename, "w") as json_file:
      json.dump(dico_to_save, json_file, indent=4)


def load_dico(input_filename):
    """
    charge les données du fichier json dans
    un dictionnaire
    """
    with open(input_filename, "r") as json_file:
      dico_to_create = json.load(json_file)
    return dico_to_create


if __name__ == '__main__':
    mon_dico = {"nom": "Monty", "age": 42}
    filename = "demo.txt"

    save_dico(mon_dico, filename)
    dico_loaded = load_dico(filename)
    print(dico_loaded)

# fichiers json
import json

filename = "demo.txt"

data_dict = {
    "Monty": {
        "Job": "Humourist",
        "Age": 42
    },
    "Python": {
        "Job": "Dev",
        "Age": 42,
        "languages": ["Python", "Java", "C"]
    },
}

# sérialisation (dico vers json)
with open(filename, "w") as json_file:
  json.dump(data_dict, json_file, indent=4)

# désérialisation (json vers dico)
with open(filename, "r") as json_file:
  data_dict = json.load(json_file)

print(data_dict)
print(type(data_dict))




# fichiers textes exos
def exercice_1():
    """
    Écriture : à l'aide d'une boucle pour,
    écrire les lignes suivantes dans un fichier

    Lecture: lire les lignes du fichier et
    les afficher dans la console
    """
    filename = "demo.txt"
    nb_lines = 5

    # ecriture
    with open(filename, "w", encoding="utf-8") as file:
        for i in range(1, nb_lines + 1):
            line = f"line {i}\n"
            file.write(line)

    # lecture
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
        # bonus : transformer en liste
        content = content.split("\n")
        content = content[:-1] # retirer la dernière case, vide
        print(content)


def exo_2_dico_to_file(dico_to_save, output_filename):
    """
    sauvegarde le dictionnaire dans un fichier
    format : une ligne = un couple clé valeur

    :param dico_to_save: le dictionnaire à sauvegarder
    :param output_filename: le fichier de sauvegarde
    :return: None
    """
    with open(output_filename, "w", encoding="utf-8") as file:
        for key, value in dico_to_save.items():
            line = f"{key}: {value}\n"
            file.write(line)


def exo_2_file_to_dico(input_filename):
    """
    charge les données du fichier dans un dictionnaire
    format : une ligne = un couple clé valeur

    :param output_filename: le fichier de sauvegarde
    :return: un dictionnaire
    """
    dico_to_create = {}
    with open(input_filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.rstrip()
            key, value = line.split(": ")
            # pour convertir l'age en entier
            if value.isnumeric():
                value = int(value)
            dico_to_create[key] = value
    return dico_to_create


if __name__ == '__main__':
    # test exo 1
    exercice_1()

    # tests exo 2
    filename = "demo.txt"

    mon_dico = {
        "nom": "Monty",
        "age": 42,
        "job": "humoriste"
    }

    exo_2_dico_to_file(mon_dico, filename)
    dico_2 = exo_2_file_to_dico(filename)
    print(dico_2)


# fichiers textes démo ----------------------------
filename = "demo.txt"

# ouverture en écriture avec écrasement
with open(filename, "w", encoding="utf-8") as file:
    prenom = "Monty"
    line = f"Bonjour {prenom}\n"
    file.write(line)

# ouverture en écriture avec ajout à la fin
with open(filename, "a", encoding="utf-8") as file:
    age = str(42)
    file.write(age)

# ouverture en lecture : tout d'un coup
with open(filename, "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
    print(type(content))

# ouverture en lecture : ligne à ligne
with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        # nettoyer les espaces et les \n à la fin de la ligne
        line = line.rstrip()
        # remplacer Monty par Python
        line = line.replace("Monty", "Python")
        # découper la chaine (défaut : espaces)
        line = line.split()
        print(line)

# création de modules : mon_module.py

"""
Créé le 31/01/2024

@author: G. Delouis

Module de démo sur la création des modules
"""


def renvoyer_addition(nb_1, nb_2):
    """renvoie la somme de nb_1 et nb_2"""
    return nb_1 + nb_2


print(f"__name__ dans mon_module.py : {__name__}")
# si ce fichier est exécuté, joue les lignes suivantes
# sinon ignore les lignes suivantes
if __name__ == "__main__":
    print(renvoyer_addition(40, 2))


# création de modules : utilisation_de_mon_module.py
import mon_module as mm

print(f"__name__ dans utilisation_de_mon_module.py : {__name__}")

print(mm.renvoyer_addition(10, 3))


# exo regexp d'Allaric
# -------------------------------------------------Exercice module regex

#--------------------------------------------------La fonction
def valide_date(date_texte: str) -> (int, int, int):
    """
    Décompose une date si elle est valide
    :param date_texte: date en texte à la française
    :return: le tupple (jour, mois, année) si OK, None sinon
    """
    match = re.search(r"^(\d\d)/(\d\d)/(\d{4})$", date_texte)

    if match:
        day = int(match.group(1))
        month = int(match.group(2))
        year = int(match.group(3))

        match month:
            case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                max_day = 31

            case 4 | 6 | 9 | 11:
                max_day = 30

            case 2:
                max_day = 29 if est_bissextile2(year) else 28

            case _:
                return None

        if 0 < day <= max_day:
            return day, month, year

    return None

#--------------------------------------------------Les test unitaires
valide_date_data = [
    ("31/02/2024", None),
    ("31/04/2024", None),
    ("32/01/2024", None),
    ("29/02/2025", None),
    ("00/02/2025", None),
    ("tata", None),
    (" 31/01/2024", None),
    ("31/01/2024 ", None),
    ("31/01/2024", (31, 1, 2024)),
    ("28/02/2024", (28, 2, 2024)),
    ("30/05/2024", (30, 5, 2024))
]


@pytest.mark.parametrize("annee, expected", valide_date_data)
def test_valide_date(annee, expected):
    assert main.valide_date(annee) == expected

#------------------------------------------------Fin exercice module regex


# sys correction exo ------------------
import sys


def sys_exercice_1():
    """
    Rédiger un script à lancer depuis un terminal qui affiche:
       * Le nom du script
       * La liste des arguments passés en ligne de commande
    Prendre en compte le cas où aucun argument nest passé en ligne de commande
    """
    nom_script = sys.argv[0]
    print(f"nom du script : {nom_script}")
    if len(sys.argv) < 2:
        print("pas d'argument")
    else:
        print("liste des arguments :")
        for arg in sys.argv[1:]:
            print(f"   * {arg}")
    print()


def sys_exercice_1_bonus_stdout():
    """
    Rédiger un script à lancer depuis un terminal qui affiche:
       * Le nom du script
       * La liste des arguments passés en ligne de commande
    Prendre en compte le cas où aucun argument nest passé en ligne de commande
    ÉCRIT SUR LA SORTIE STANDARD
    """
    nom_script = sys.argv[0]
    sys.stdout.write(f"nom du script : {nom_script}\n")
    if len(sys.argv) < 2:
        sys.stdout.write("pas d'argument\n")
    else:
        sys.stdout.write("liste des arguments :\n")
        for arg in sys.argv[1:]:
            sys.stdout.write(f"   * {arg}\n")
    sys.stdout.write("\n")


def sys_exercice_2():
    """Rédiger un script à lancer depuis un terminal qui affiche:
        * La version de Python
        * L'OS de python
    """
    print(f"version de python : {sys.version_info.major}.{sys.version_info.minor}")
    print("OS : ", sys.platform)

    print()


def sys_exercice_3():
    """
    Rédiger un script à lancer depuis un terminal qui :
        Récupère deux nombres en ligne de commande
        Quitte le programme si le nombre d'arguments est insuffisant
        Fait la division du premier par le second

    """
    if len(sys.argv) < 3:
        print("nombre d'argument insuffisants")
        sys.exit()
    num = float(sys.argv[1])
    denom = float(sys.argv[2])

    print("resultat :", num / denom)

    print()


# exécution des exos
sys_exercice_1()
sys_exercice_1_bonus_stdout()
sys_exercice_2()
sys_exercice_3()


# sys.argv démo

import sys

print(sys.argv)

if len(sys.argv) < 2:
    print("précisez le fichier")
    print(sys.exit("fermeture du programme"))
fichier_a_traiter = sys.argv[1]

# traitement du fichier
print(f"traitement du fichier {fichier_a_traiter}...")
print("fichier traité")

# datetime exo --------------
import datetime as dt


# datetime exo 1
def date_rendu_livre():
    """demande à l'utilisateur la date d'emprunt et affiche la
    date de retour de l'ouvrage (date limite : 3 semaines
    après la date d'emprunt)"""

    today = dt.date.today()
    print("today : ", today)
    duree_emprunt = dt.timedelta(weeks=3)
    date_rendu = today + duree_emprunt
    # bonus : formatage de la date avec strftime()
    date_rendu_formatee = date_rendu.strftime("%A %y-%m-%d")
    print("book borrowed until : ", date_rendu_formatee)


# datetime exo 1 bonus
def date_rendu_livre_avec_saisie():
    """demande à l'utilisateur la date d'emprunt et affiche la
    date de retour de l'ouvrage (date limite : 3 semaines
    après la date d'emprunt)"""
    annee, mois, jour = input("today (format aaaa-mm-jj) : ").split("-")
    annee = int(annee)
    mois = int(mois)
    jour = int(jour)

    today = dt.date(annee, mois, jour)
    duree_emprunt = dt.timedelta(weeks=3)
    date_rendu = today + duree_emprunt
    print("book borrowed until : ", date_rendu)

# exercice 2
def nb_jours_avant_nouvelle_annee():
    """affiche le nombre de jours restants avant la nouvelle année"""
    today = dt.date.today()
    next_year = dt.date(today.year + 1, 1, 1)
    print(next_year - today)


date_rendu_livre()
nb_jours_avant_nouvelle_annee()
