# https://www.sharemycode.fr/pythonj2

# T : Léa, Allaric
# HP : Sophie, Bruno
# SW : Laurent


import random

# pile ou face, exemple de base
choix = input("pile ou face ? : ")
liste_faces = ["pile", "face"]

lancer = random.choice(liste_faces)
if choix == lancer:
    print("Bravo, vous avez gagné !")
else:
    print("dommage...")

# pile ou face : version 2
# nettoyage de la saisie (minuscules + espaces)
# redemande en cas de saisie incorrecte

choix = None
liste_faces = ["pile", "face"]
while choix not in liste_faces:
    choix = input("pile ou face ? : ").strip().lower()

lancer = random.choice(liste_faces)
if choix == lancer:
    print("Bravo, vous avez gagné !")
else:
    print("dommage...")

# pile ou face version 3 :
# fonction pour une partie
# redemander à l'utilisateur

def partie_pile_ou_face():
    """
    lance une partie de pile ou face
    """
    choix = None
    liste_faces = ["pile", "face"]
    while choix not in liste_faces:
        choix = input("pile ou face ? : ").strip().lower()

    lancer = random.choice(liste_faces)
    if choix == lancer:
        print("Bravo, vous avez gagné !")
    else:
        print("dommage...")


# code principal
rejouer = "oui"

while rejouer == "oui":
    partie_pile_ou_face()
    rejouer = input("rejouer ? (oui/non): ").strip().lower()

print("au revoir :)")


# imports de modules v3
from time import sleep


for i in range(10, 0, -1):
    print(i)
    sleep(1)
print("Bonne année")


# imports de modules v2
import time as ti


for i in range(10, 0, -1):
    print(i)
    ti.sleep(1)
print("Bonne année")

# imports de modules v1
import time


for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
print("Bonne année")


# lancement des tests  :
pytest .\test_main.py 

# exemple pytest : test_main.py
import main


def test_ma_division_10_4():
    assert main.ma_division(10, 4) == 2.5

def test_ma_division_10_0():
    assert main.ma_division(10, 0) == None
    

# exemple pytest : main.py
def ma_division(num, denom):
    """
    implémentation maison d'une
    division de deux nombres
    """
    resultat = None
    if denom != 0:
        resultat = num / denom
    return resultat



# exo debug

def est_bissextile(annee):
    if annee % 4 == 0 :
        if annee % 100 == 0
            if annee // 400 == 0:
                return True
            else:
                return False
        else:
        return True
    else:
        return false

print(est_bissextile(2000))



# fonctions exo paramètres optionnels
def calculer_moyenne(nb_1: float, nb_2: float, *numbers: float) -> float:
    """
    Calcule la moyenne de tous les nombres passés en argument
    :param nb_1: 1er nombre obligatoire
    :param nb_2: 2d nombre obligatoire
    :param numbers: les nombres optionnels
    :return: la moyenne
    """
    somme = nb_1 + nb_2 + sum(numbers)
    total = 2 + len(numbers)
    return somme / total


# Exemple d'utilisation 1
print(calculer_moyenne(10, 20))

# Exemple d'utilisation 2
print(calculer_moyenne(10, 20, 30.0))

# Exemple d'utilisation 3
calculer_moyenne(10)


# paramètres optionnels
def print_test_var_args(first_arg, *args):
    """affiche l'argument obligatoire, puis les
    arguments optionnels s'il y en a"""
    print("Argument obligatoire : ", first_arg)
    print(args)
    for arg in args:
        print("autre arg via *args : ", arg)


print_test_var_args('Monty', 'python', '42', 'test')
print()
print_test_var_args('Monty')
# print_test_var_args()


# fonctions et types mutables :
# passage par référence
def modifier_liste(ma_liste):
    """Modifie la première valeur de la
    liste et la renvoie"""
    ma_liste[0] = 42
    return ma_liste


liste_init = [1, 2]
liste_copie = liste_init.copy()
liste_fin = modifier_liste(liste_init)
print("liste initiale : ", liste_init)
print("liste copie : ", liste_copie)
print("liste finale : ", liste_fin)
print(liste_init is liste_fin)
print(liste_init is liste_copie)

# fonctions et types non nutables :
# passage par valeur
def modifier_nombre(nb):
    """modifie la variable nb par la
    valeur 42 et la renvoie"""
    nb = 42
    return nb


nb_init = 1
nb_fin = modifier_nombre(nb_init)
print("nb initial : ", nb_init)
print("nb final : ", nb_fin)
print(nb_init is nb_fin)


# fonctions exo 1
def renvoyer_parite(nb):
    """
    renvoie :
       * "pair" si le nombre est pair (divisible par 2)
       * "impair" sinon
    """
    if nb % 2 == 0:
        parite = "pair"
    else:
        parite = "impair"
    return parite


nb = 5
for i in range(1, nb + 1):
    parite_nb = renvoyer_parite(i)
    print(i, parite_nb)


# for exo 2
def table_multi(nb):
    """affiche la table de multiplication du nombre nb"""
    for i in range(1, 11):
        print(f"{nb:>2} x {i:>2} = {nb * i:<2}")
    print()


nb = 5
table_multi(nb)


# for exo 7
def table_multi(nb, start=1, stop=10):
    """affiche la table de multiplication du nombre nb"""
    print("la nouvelle")
    for i in range(start, stop + 1):
        print(f"{nb:>2} x {i:>2} = {nb * i:<2}")
    print()


nb = 5
table_multi(nb)
table_multi(nb, 2, 4)

# fonctions : création ----------------------
def renvoyer_addition(nb_1, nb_2):
    """renvoie la somme de nb_1 et nb_2"""
    resultat = nb_1 + nb_2
    return resultat

def afficher_addition(nb_1, nb_2):
    """affiche la somme de nb_1 et nb_2"""
    resultat = nb_1 + nb_2
    print(resultat)
    # return None


# fonctions : utilisation avec return
somme = renvoyer_addition(40, 2)
print(somme)
print(renvoyer_addition(nb_2=10, nb_1=3))

# fonctions : utilisation sans return
afficher_addition(40, 2)
afficher_addition(nb_2=10, nb_1=3)

# bonus listes en intention
ma_liste = []
for i in range(0, 11):
    if i % 2 == 0:
        ma_liste.append(i)

print(ma_liste)

ma_liste_v2 = [i for i in range(0, 11) if i % 2 == 0]
print(ma_liste)


# bonus enumerate
ma_liste = [1, 2, 42]
for i in range(len(ma_liste)):
    print(i, ma_liste[i])

ma_liste = [1, 2, 42]
for index, item in enumerate(ma_liste):
    print(index, item)

ma_liste = [1, 2, 42]
for index, item in enumerate(ma_liste, start=1):
    print(index, item)

# for exo 1 ---------------------------------
phrase = "bonjour :)"

for i in range(1, 10):
    print(i, phrase)


# for exo 2
liste_exo_2 = [13, 42, 33, 4, 5]

for nb in liste_exo_2:
    print(nb)

# for exo 3
for i in range(10, -1, -1):
    print(i)
print("Bonne année :)")

# for exo 4

liste_exo_4 = [11, 22, 42, 87, 89, 46]

for nb in liste_exo_4:
    if nb % 2 == 0:
        parite = "pair"
    else:
        parite = "impair"
    print(f"{nb} est {parite}")

# for exo 5
dico_personnage = {
    "nom": "Monty",
    "age": 42
}
print()
for key, value in dico_personnage.items():
    print(f"{key=}, {value=}")


# for démo : liste ------------------------

ma_liste = [12, 42, 13]
for nb in ma_liste:
    print(nb)
print()

# for et range avec une valeur
# de 0 inclus à 5 exclus
for i in range(5):
    print(i)
print()

# for et range avec deux valeurs
# de 1 inclus à 5 exclus
for i in range(1, 5):
    print(i)
print()

# for et range avec trois valeurs
# de 1 inclus à 5 exclus par pas de 2
for i in range(1, 5, 2):
    print(i)
print()
# for et range avec trois valeurs et pas négatif
# de 1 inclus à 5 exclus par pas de -2
# attention à l'ordre !
print("avec un pas négatif")
for i in range(5, 1, -2):
    print(i)
print()
