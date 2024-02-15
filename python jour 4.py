# https://www.sharemycode.fr/pythonj4


# dice : exemple de tests unitaires --------------------------------------

import dice
import pytest


parameters_creation = [
    (1, 6),
    (2, 2),
    (6, 6),
    (100, 100),
    (101, 6),
    ("Bob", 6)
]

@pytest.mark.parametrize("nb_faces_init,expected",parameters_creation)
def test_eval_dice(nb_faces_init, expected):
    dice_to_test = dice.Dice(nb_faces_init)
    assert dice_to_test.nb_faces == expected

@pytest.mark.parametrize("nb_faces_init,expected",parameters_creation)
def test_eval_luckydice(nb_faces_init, expected):
    dice_to_test = dice.LuckyDice(nb_faces_init)
    assert dice_to_test.nb_faces == expected



# dice : héritage ----------------------------------

"""
Créé le 1er février 2024

@author : Grace Delouis

Module contenant des classes relatives à des dés :
   * Dice : dé simple avec un nombre de faces réglable
"""
import random


class Dice:
    """Classe modélisant un dé simple avec
    un nombre de faces réglable"""

    def __init__(self, nb_faces_init: int = 6) -> None:
        """Constructeur de la classe Dice"""
        self.nb_faces = nb_faces_init

    @property
    def nb_faces(self) -> int:
        """accesseur du nombre de faces"""
        return self._nb_faces

    @nb_faces.setter
    def nb_faces(self, value: int) -> None:
        """
        mutateur du nombre de faces
        Valeur valide : entier entre 2 et 100
        Si valeur invalide : valeur fixée à 6 par défaut
        """
        if isinstance(value, int) and 2 <= value <= 100:
            self._nb_faces = value
        else:
            print("valeur invalide, nb de faces fixé à 6")
            self._nb_faces = 6

    def est_reussite_critique(self, resultat: int) -> bool:
        """
        renvoie True si le résultat du lancer
        est une réussite critique (on tombe sur le max)
        """
        return resultat == self.nb_faces

    def est_echec_critique(self, resultat: int) -> bool:
        """
        renvoie True si le résultat du lancer
        est un échec critique (on tombe sur 1)
        """
        return resultat == 1

    def lancer(self) -> int:
        """lance le dé et renvoie le résultat"""
        resultat = random.randint(1, self.nb_faces)
        return resultat

    def lancer_avec_message(self) -> int:
        """lance le dé et renvoie le résultat, avec messages dans la
        console"""
        resultat = self.lancer()
        if self.est_reussite_critique(resultat):
            print("réussite critique ! ", end=" ")
        elif self.est_echec_critique(resultat):
            print("oups... échec critique", end=" ")
        return resultat


class LuckyDice(Dice):
    """
    Classe permettant de créer un dé chanceux.
    Un dé chanceux est relancé une fois si on tombe
    sur un échec critique (1)
    """

    def lancer(self) -> int:
        """lancer avec un dé chanceux : on relance une fois
        si on tombe  sur un échec critique (1)"""
        resultat = super().lancer()
        if super().est_echec_critique(resultat):
            print("je relance...", end=" ")
            resultat = super().lancer()
        return resultat


if __name__ == '__main__':
    print("test : dé à 6 faces")
    de_6 = LuckyDice()
    print(de_6.nb_faces)
    for i in range(10):
        print(de_6.lancer_avec_message(), end=" ")
    print("\n")

    print("test : dé à 20 faces")
    de_20 = LuckyDice(-20)
    print(de_20.nb_faces)
    for i in range(10):
        print(de_20.lancer_avec_message(), end=" ")
    print()


# heritage démo -------------------------------------
class Contact:
    """Classe modélisant un contact simple avec un nom
    et un age"""

    def __init__(self, nom_init="Monty", age_init=42):
        """constructeur de la classe Contact"""
        self.nom = nom_init
        self.age = age_init



    @property
    def age(self):
        """accesseur (getter) de l'attribut age"""
        return self._age

    @age.setter
    def age(self, value):
        """mutateur (setter) de l'attribut age"""
        if value >= 0:
            self._age = value
        else:
            print("age invalide, age fixé à 42 ans")
            self._age = 42

    def afficher_infos(self):
        """affiche les infos du contact"""
        print("Informations :")
        print(f"  * nom : {self.nom}")
        print(f"  * age : {self.age}")

    def renvoyer_age_dans_x_ans(self, x_ans=10):
        """renvoie l'age du contact dans x_ans"""
        age_dans_x_ans = self.age + x_ans
        return age_dans_x_ans


class Ami(Contact):
    """Classe Ami, héritant de la classe Contact
    info supplémentaire : anniversaire
    """

    def __init__(self, nom_init="Monty", age_init=42, anniv_init="01/01/1970"):
        """constructeur de la classe Ami"""
        super().__init__(nom_init, age_init)
        self.anniv = anniv_init

    def afficher_infos(self):
        """affiche les infos de l'Ami"""
        super().afficher_infos()
        print(f"  * anniv : {self.anniv}")


if __name__ == '__main__':
    contact_1 = Ami()
    print(contact_1.nom, contact_1.age)
    contact_2 = Ami("Bob", -12)
    contact_2.afficher_infos()
    contact_2.age = -165
    contact_2.afficher_infos()
    print(contact_2.renvoyer_age_dans_x_ans(100))

# classe Dice : encapsulation

"""
Créé le 1er février 2024

@author : Grace Delouis

Module contenant des classes relatives à des dés :
   * Dice : dé simple avec un nombre de faces réglable
"""
import random


class Dice:
    """Classe modélisant un dé simple avec
    un nombre de faces réglable"""

    def __init__(self, nb_faces_init: int = 6) -> None:
        """Constructeur de la classe Dice"""
        self.nb_faces = nb_faces_init

    @property
    def nb_faces(self) -> int:
        """accesseur du nombre de faces"""
        return self._nb_faces

    @nb_faces.setter
    def nb_faces(self, value: int) -> None:
        """
        mutateur du nombre de faces
        Valeur valide : entier entre 2 et 100
        Si valeur invalide : valeur fixée à 6 par défaut
        """
        if isinstance(value, int) and 2 <= value <= 100:
            self._nb_faces = value
        else:
            print("valeur invalide, nb de faces fixé à 6")
            self._nb_faces = 6

    def est_reussite_critique(self, resultat: int) -> bool:
        """
        renvoie True si le résultat du lancer
        est une réussite critique (on tombe sur le max)
        """
        return resultat == self.nb_faces

    def est_echec_critique(self, resultat: int) -> bool:
        """
        renvoie True si le résultat du lancer
        est un échec critique (on tombe sur 1)
        """
        return resultat == 1

    def lancer(self) -> int:
        """lance le dé et renvoie le résultat"""
        resultat = random.randint(1, self.nb_faces)
        return resultat

    def lancer_avec_message(self) -> int:
        """lance le dé et renvoie le résultat, avec messages dans la
        console"""
        resultat = self.lancer()
        if self.est_reussite_critique(resultat):
            print("réussite critique ! ", end=" ")
        elif self.est_echec_critique(resultat):
            print("oups... échec critique", end=" ")
        return resultat


if __name__ == '__main__':
    print("test : dé à 6 faces")
    de_6 = Dice()
    print(de_6.nb_faces)
    for i in range(10):
        print(de_6.lancer_avec_message(), end=" ")
    print("\n")

    print("test : dé à 20 faces")
    de_20 = Dice(-20)
    print(de_20.nb_faces)
    for i in range(10):
        print(de_20.lancer_avec_message(), end=" ")
    print()


# classe Contact : ecapsulation
class Contact:
    """Classe modélisant un contact simple avec un nom
    et un age"""

    def __init__(self, nom_init="Monty", age_init=42):
        """constructeur de la classe Contact"""
        self.nom = nom_init
        self.age = age_init

    @property
    def age(self):
        """accesseur (getter) de l'attribut age"""
        return self._age

    @age.setter
    def age(self, value):
        """mutateur (setter) de l'attribut age"""
        if value >= 0:
            self._age = value
        else:
            print("age invalide, age fixé à 42 ans")
            self._age = 42

    def afficher_infos(self):
        """affiche les infos du contact"""
        print("Informations :")
        print(f"  * nom : {self.nom}")
        print(f"  * age : {self.age}")

    def renvoyer_age_dans_x_ans(self, x_ans=10):
        """renvoie l'age du contact dans x_ans"""
        age_dans_x_ans = self.age + x_ans
        return age_dans_x_ans


if __name__ == '__main__':
    contact_1 = Contact()
    print(contact_1.nom, contact_1.age)
    contact_2 = Contact("Bob", -12)
    contact_2.afficher_infos()
    contact_2.age = -165
    contact_2.afficher_infos()
    print(contact_2.renvoyer_age_dans_x_ans(100))

# classe Etudiant -------------------------------------------------
class Etudiant:

    def __init__(self, nom_init="Monty",
                 prenom_init="Python", liste_de_notes_init=[]):
        """constructeur de la classe Etudiant"""
        self.nom = nom_init
        self.prenom = prenom_init
        self.liste_de_notes = liste_de_notes_init

    def ajouter_note(self, note_a_ajouter):
        """ajouter une note"""
        self.liste_de_notes.append(note_a_ajouter)
        print(f"note ajoutée : {note_a_ajouter}")

    def ajouter_notes(self, *notes_a_ajouter):
        """ajoute plusieurs notes d'un coup
        notes notées dans les parenthèses"""
        self.liste_de_notes = self.liste_de_notes + list(notes_a_ajouter)
        print(f"notes ajoutées : {notes_a_ajouter}")

    def calculer_moyenne(self):
        """renvoie a moyenne des notes"""
        moyenne = None
        if len(self.liste_de_notes) >= 1:
            somme = sum(self.liste_de_notes)
            total = len(self.liste_de_notes)
            moyenne = round(somme / total, 2)
        else:
            print("pas de notes, pas de moyennes")
        return moyenne

    def __str__(self):
        """formattage du print"""
        message_to_print = (f"Informations :\n"
                            f"  * nom : {self.nom}\n"
                            f"  * prenom : {self.prenom}\n"
                            f"  * notes : {self.liste_de_notes}\n")
        return message_to_print


if __name__ == '__main__':
    etudiant_1 = Etudiant()
    etudiant_1.ajouter_note(10)
    etudiant_1.ajouter_notes(15, 20)
    print(etudiant_1)
    print(etudiant_1.calculer_moyenne())



# Exo Dice ----------------------------------------------
"""
Créé le 1er février 2024

@author : Grace Delouis

Module contenant des classes relatives à des dés :
   * Dice : dé simple avec un nombre de faces réglable
"""
import random


class Dice:
    """Classe modélisant un dé simple avec
    un nombre de faces réglable"""

    def __init__(self, nb_faces_init=6):
        """Constructeur de la classe Dice"""
        self.nb_faces = nb_faces_init

    def lancer(self):
        """lance le dé et renvoie le résultat"""
        resultat = random.randint(1, self.nb_faces)
        return resultat


if __name__ == '__main__':
    print("test : dé à 6 faces")
    de_6 = Dice()
    print(de_6.nb_faces)
    for i in range(10):
        print(de_6.lancer(), end=" ")
    print("\n")

    print("test : dé à 20 faces")
    de_20 = Dice(20)
    print(de_20.nb_faces)
    for i in range(10):
        print(de_20.lancer(), end=" ")
    print()


# classes : démo ----------------------------------------
class Contact:
    """Classe modélisant un contact simple avec un nom
    et un age"""

    def __init__(self, nom_init="Monty", age_init=42):
        """constructeur de la classe Contact"""
        self.nom = nom_init
        self.age = age_init

    def afficher_infos(self):
        """affiche les infos du contact"""
        print("Informations :")
        print(f"  * nom : {self.nom}")
        print(f"  * age : {self.age}")

    def renvoyer_age_dans_x_ans(self, x_ans=10):
        """renvoie l'age du contact dans x_ans"""
        age_dans_x_ans = self.age + x_ans
        return age_dans_x_ans


if __name__ == '__main__':
    contact_1 = Contact()
    print(contact_1.nom, contact_1.age)
    contact_2 = Contact("Bob", -12)
    contact_2.age = -165
    contact_2.afficher_infos()
    print(contact_2.renvoyer_age_dans_x_ans(100))

# gestion d'exception exos ----------------------------------


def ma_division():
    """
    Faire un script de calcul de division et prenez en compte deux exceptions :
       * division par zéro
       * mauvais type de données

    Bonus : l'écrire sous forme de fonction qui se rappelle quand une exception est gérée
    """

    try:
        num = float(input("numérateur : "))
        denom = float(input("dénominateur : "))

        print(num / denom)
    except ZeroDivisionError:
        print("On ne peut pas diviser par 0")
        ma_division()
    except ValueError:
        print("donnée invalide, entier ou flottant attendu")
        ma_division()


def exo_2_try():
    """
   Soit la liste de dictionnaires ci-dessous.

    Faites un programme qui calcule le nombre total de likes :
       * en passant par un try except <----
       * en passant par un if
    """

    blog_posts = [
        {'Photos': 3, 'Likes': 21, 'Comments': 2},
        {'Likes': 13, 'Comments': 2, 'Shares': 1},
        {'Photos': 5, 'Comments': 8, 'Shares': 3},
    ]

    nb_likes = 0
    for post in blog_posts:
        try:
            nb_likes += post["Likes"]
        except KeyError:
            post["Likes"] = 0
    print(nb_likes)


def exo_2_if():
    """
   Soit la liste de dictionnaires ci-dessous.

    Faites un programme qui calcule le nombre total de likes :
       * en passant par un try except
       * en passant par un if <-------
    """

    blog_posts = [
        {'Photos': 3, 'Likes': 21, 'Comments': 2},
        {'Likes': 13, 'Comments': 2, 'Shares': 1},
        {'Photos': 5, 'Comments': 8, 'Shares': 3},
    ]

    nb_likes = 0
    for post in blog_posts:
        if "Likes" in post.keys():
            nb_likes += post["Likes"]
    print(nb_likes)


def exo_3_file_to_dico(input_filename):
    """
    charge les données du fichier dans un dictionnaire
    format : une ligne = un couple clé valeur

    gérer le cas où le nom de fichier est invalide

    :param output_filename: le fichier de sauvegarde
    :return: un dictionnaire
    """
    dico_to_create = {}
    try:
        with open(input_filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.rstrip()
                key, value = line.split(": ")
                # pour convertir l'age en entier
                if value.isnumeric():
                    value = int(value)
                dico_to_create[key] = value
    except FileNotFoundError:
        print("Nom de fichier invalide")
    return dico_to_create


if __name__ == '__main__':
    # ma_division()
    exo_2_try()
    exo_2_if()
    #
    dico = exo_3_file_to_dico("demofd.txt")
    print(dico)

# gestion d'exception démo ---------------------------

try:
    age = int(input("age : "))
    # age = "bob"

    if age < 18:
        print("mineur")
    else:
        print("majeur")
# except ValueError as err:
#     print("donnée saisie invalide")
#     print(err)
#     print(type(err))
# except TypeError as err:
#     print("donnée invalide")
#     print(err)
#     print(type(err))

except (TypeError, ValueError) as err:
    print("donnée invalide")
    print(err)
    print(type(err))
finally:
    print("au revoir")