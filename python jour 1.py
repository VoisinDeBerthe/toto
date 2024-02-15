# https://www.sharemycode.fr/pythonj1


# while démo -------------------------------------

i = 1
phrase = "bonjour :)"

while i <= 10:
    print(i, phrase)
    i += 1

# while exo 2

quitter = "non"

while quitter != "oui":
    quitter = input("quitter ? (oui/non) : ")

# while exo 3

quitter = "non"

while quitter != "oui":
    quitter = input("quitter ? (oui/non) : ").strip().lower()

# while exo 4

quitter = "non"
liste_choix_autorises = ["oui", "o", "yes", "y"]

while quitter not in liste_choix_autorises:
    quitter = input("quitter ? : ").strip().lower()

# while démo ------------------
i = 0

while i < 2:
    print(i)
    i += 1



# if exo 1 -----------------------
age = int(input("age : "))

if age < 18:
    print("mineur")
else:
    print("majeur")

# bonus ternaire
print("mineur" if age < 18 else "majeur")

# if exo 2
age = int(input("age : "))

if 12 <= age <= 27:
    print("réduction")
else:
    print("tarif plein")

# if démo -----------------------------------------
note = 19

if note == 20:
    print("Fantastique !")
    print("C'est parfait !")
elif note >= 10:
    print("Super, tu peux passer à la suite !")
else:
    print("A revoir")

# strings : démo -----------------
prenom = "moNTy"

print(prenom[0])
# prenom[0] = "P" : TypeError: 'str' object does not support item assignment


# strings et casse
print(prenom.lower())
print(prenom.upper())
print(prenom.capitalize())
print(prenom)
prenom = prenom.capitalize()
print(prenom)

# string et autres manipulations
ma_chaine = " - bonjour à tous - "

print(ma_chaine)
# retirer les espaces aux extrémités (défaut)
print(ma_chaine.strip())

# retirer tous les espaces et tous les tirets aux extrémités
# attention : ce n'est pas le motif
print(ma_chaine.strip(" -"))
# rstrip() : retire à la fin (à droite) les espaces et les \n

# remplacer un motif par un autre
print(ma_chaine.replace("bonjour", "bonsoir"))

# découper la chaine par rapport aux espaces (défaut)
print(ma_chaine.split())

# découper la chaine par rapport à un motif
print(ma_chaine.split("ou"))

# chainer les fonctions de string
print(ma_chaine.strip(" -").capitalize())

# tuples : création -------------
mon_tuple_vide = ()
mon_tuple_v1 = (12, 42, 13)
mon_tuple_v2 = 12, 42, 13

print(mon_tuple_vide, mon_tuple_v1, mon_tuple_v2)

# tuples : accès
print(mon_tuple_v1[0])

# tuples : modification
# mon_tuple_v1[0] = 2 : TypeError: 'tuple' object does not support item assignment


# destructuration (unpack)
# marche aussi avec les listes
a, b = 4, 8.3

# dicos exo 1 ---------------------
dico_prenoms_metiers = {
    "Monty": "humoriste",
    "Bob": "artiste"
}

print(dico_prenoms_metiers)

dico_prenoms_metiers["Bob"] = "bricoleur"
print(dico_prenoms_metiers)

dico_prenoms_metiers["Python"] = "dev"
print(dico_prenoms_metiers)

# dicos exo 4
dico_prenoms_complet = {
    "Monty": {
        "Age": 42,
        "Job": "humoriste"
    },
    "Bob": {
        "Age": 24,
        "Job": "bricoleur"
    },
    "Python": {
        "Age": 33,
        "Job": "dev"
    },
}
print(dico_prenoms_complet)
print(dico_prenoms_complet["Monty"])
print(dico_prenoms_complet["Monty"]["Age"])


# dicos : création ----------------------------

mon_dico_vide = {}  # ou dict()
mon_dico = {
    "cle 1": "valeur 1",
    "cle 2": "valeur 2",
    404: "not found",
    "admin": True
}

print(mon_dico_vide, mon_dico)

# dicos : accès
print(mon_dico["cle 1"])

# dicos : modification
mon_dico["admin"] = False
print(mon_dico)

# dicos : ajout
mon_dico[418] = "I'm a teapot"
print(mon_dico)

# dicos : suppression d'un indice, méthode 1
del mon_dico[418]
print(mon_dico)

# dicos : suppression d'un indice, méthode 2
ma_valeur = mon_dico.pop("admin")
print(mon_dico)
print(ma_valeur)

# dicos : récupérer toutes les clés
print(mon_dico.keys())

# dicos : récupérer toutes les valeurs
print(mon_dico.values())

# dicos : récupérer tous les couples clé-valeur
print(mon_dico.items())

# listes exo 1 ------------------------------

colors = ["bleu clair", "bleu foncé", "vert"]

colors.append("jaune")
colors.insert(0, "rose")
colors_to_add = ["orange", "rouge"]
colors = colors + colors_to_add
print(colors)

# listes exo 3
matrice = [
    [1, 0, 0],
    [0, 1, 42],
    [0, 0, 1]
]

print(matrice)
print(matrice[1])
print(matrice[1][2])

# listes : création ----------------------------------
ma_liste_vide = []  # ou list()
ma_liste = [12, 42, 13]
ma_liste_mix = ["Monty", True, 3.14, 42]

print(ma_liste_vide, ma_liste, ma_liste_mix)

# listes : accès
print(ma_liste[0])

# listes : modifications
ma_liste[0] = 2
print(ma_liste)

# listes : longueur de la liste
n = len(ma_liste)
# print(ma_liste[n]) : IndexError: list index out of range
print(n, ma_liste[n - 1])

# listes : ajouter un élément à la fin de la liste
ma_liste.append(51)
print(ma_liste)

# listes : insérer à une position x donnée
x = 0
ma_liste.insert(x, 88)
print(ma_liste)

# listes : concaténation
ma_liste = ma_liste + ma_liste_mix
print(ma_liste)

# listes : suppression à un indice donné
del ma_liste[0]
print(ma_liste)

# listes : supprimer une valeur donnée (première occurence uniquement)
ma_liste.remove(42)
print(ma_liste)

# correction exo input ---------------------------
prenom = input("Votre prenom : ")
print("Bonjour", prenom)

# input démo
age = input("Votre age : ")
print("Vous avez", age, " ans")
print(type(age))

age = int(input("Votre age : "))
print("Vous avez", age, " ans")
print(type(age))

# print
x = 3
y = 5
z = 7

print("contenu de x :")
print(x)
print("Contenu de y :", y)
print("Contenu de y :", y, sep="...")
print("Contenu de z :  {:.2f}".format(z))
print(f"Les trois : {x}, {y:.2f}, {z}")
print("Les trois : {x}, {y:.2f}, {z}")



# typage en python
age = 42
print(age, type(age))

age = str(age)
print(age, type(age))

age = float(age)
print(age, type(age))

age = int(age)
print(age, type(age))


# variables

ma_variable = "valeur"
print(ma_variable)

x = y = 7
print(x, y)

a, b = 4, 8.3
print(a, b)