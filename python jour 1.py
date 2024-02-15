# https://www.sharemycode.fr/pythonj1


# while d�mo -------------------------------------

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

# while d�mo ------------------
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
    print("r�duction")
else:
    print("tarif plein")

# if d�mo -----------------------------------------
note = 19

if note == 20:
    print("Fantastique !")
    print("C'est parfait !")
elif note >= 10:
    print("Super, tu peux passer � la suite !")
else:
    print("A revoir")

# strings : d�mo -----------------
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
ma_chaine = " - bonjour � tous - "

print(ma_chaine)
# retirer les espaces aux extr�mit�s (d�faut)
print(ma_chaine.strip())

# retirer tous les espaces et tous les tirets aux extr�mit�s
# attention : ce n'est pas le motif
print(ma_chaine.strip(" -"))
# rstrip() : retire � la fin (� droite) les espaces et les \n

# remplacer un motif par un autre
print(ma_chaine.replace("bonjour", "bonsoir"))

# d�couper la chaine par rapport aux espaces (d�faut)
print(ma_chaine.split())

# d�couper la chaine par rapport � un motif
print(ma_chaine.split("ou"))

# chainer les fonctions de string
print(ma_chaine.strip(" -").capitalize())

# tuples : cr�ation -------------
mon_tuple_vide = ()
mon_tuple_v1 = (12, 42, 13)
mon_tuple_v2 = 12, 42, 13

print(mon_tuple_vide, mon_tuple_v1, mon_tuple_v2)

# tuples : acc�s
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


# dicos : cr�ation ----------------------------

mon_dico_vide = {}  # ou dict()
mon_dico = {
    "cle 1": "valeur 1",
    "cle 2": "valeur 2",
    404: "not found",
    "admin": True
}

print(mon_dico_vide, mon_dico)

# dicos : acc�s
print(mon_dico["cle 1"])

# dicos : modification
mon_dico["admin"] = False
print(mon_dico)

# dicos : ajout
mon_dico[418] = "I'm a teapot"
print(mon_dico)

# dicos : suppression d'un indice, m�thode 1
del mon_dico[418]
print(mon_dico)

# dicos : suppression d'un indice, m�thode 2
ma_valeur = mon_dico.pop("admin")
print(mon_dico)
print(ma_valeur)

# dicos : r�cup�rer toutes les cl�s
print(mon_dico.keys())

# dicos : r�cup�rer toutes les valeurs
print(mon_dico.values())

# dicos : r�cup�rer tous les couples cl�-valeur
print(mon_dico.items())

# listes exo 1 ------------------------------

colors = ["bleu clair", "bleu fonc�", "vert"]

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

# listes : cr�ation ----------------------------------
ma_liste_vide = []  # ou list()
ma_liste = [12, 42, 13]
ma_liste_mix = ["Monty", True, 3.14, 42]

print(ma_liste_vide, ma_liste, ma_liste_mix)

# listes : acc�s
print(ma_liste[0])

# listes : modifications
ma_liste[0] = 2
print(ma_liste)

# listes : longueur de la liste
n = len(ma_liste)
# print(ma_liste[n]) : IndexError: list index out of range
print(n, ma_liste[n - 1])

# listes : ajouter un �l�ment � la fin de la liste
ma_liste.append(51)
print(ma_liste)

# listes : ins�rer � une position x donn�e
x = 0
ma_liste.insert(x, 88)
print(ma_liste)

# listes : concat�nation
ma_liste = ma_liste + ma_liste_mix
print(ma_liste)

# listes : suppression � un indice donn�
del ma_liste[0]
print(ma_liste)

# listes : supprimer une valeur donn�e (premi�re occurence uniquement)
ma_liste.remove(42)
print(ma_liste)

# correction exo input ---------------------------
prenom = input("Votre prenom : ")
print("Bonjour", prenom)

# input d�mo
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