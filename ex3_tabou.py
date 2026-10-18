
# EXERCICE 3 : PROBLEME DU VOYAGEUR DE COMMERCE (TSP)
# METHODE : RECHERCHE TABOU


import random

#
# La variable "grand" représente une distance très élevée.
# Elle est utilisée lorsqu'il n'existe pas de liaison
# directe entre deux villes.


grand = 999999


# Matrice des distances entre les villes
# Les villes sont numérotées de 1 à 8


dist = [
    [0, 14, 15, grand, grand, grand, grand, 17],
    [14, 0, 13, 14, 20, grand, grand, 21],
    [15, 13, 0, 11, 21, 17, 9, 9],
    [grand, 14, 11, 0, 11, 10, 8, 20],
    [grand, 20, 21, 11, 0, 15, 18, grand],
    [grand, grand, 17, 10, 15, 0, 9, grand],
    [grand, grand, 9, 8, 18, 9, 0, 13],
    [17, 21, 9, 20, grand, grand, 13, 0]
]

# ----------------------------------------------------------
# Solution initiale imposée par l'énoncé
# ----------------------------------------------------------

route = [1, 2, 3, 4, 5, 6, 7, 8, 1]

# ----------------------------------------------------------
# Fonction de calcul du coût d'une tournée
# ----------------------------------------------------------

def calcul_cout(route):

    total = 0

    for i in range(len(route) - 1):

        ville_depart = route[i] - 1
        ville_arrivee = route[i + 1] - 1

        total += dist[ville_depart][ville_arrivee]

    return total


# ----------------------------------------------------------
# Affichage de la solution initiale
# ----------------------------------------------------------

cout_initial = calcul_cout(route)

print("===================================")
print("SOLUTION INITIALE")
print("===================================")

print("Tournée :", route)
print("Coût initial :", cout_initial)

# ----------------------------------------------------------
# Liste tabou
# Elle mémorise les solutions déjà visitées
# ----------------------------------------------------------

liste_tabou = []

# ----------------------------------------------------------
# Meilleure solution courante
# ----------------------------------------------------------

meilleure_route = route[:]
meilleur_cout = calcul_cout(meilleure_route)

# ----------------------------------------------------------
# Nombre d'itérations
# ----------------------------------------------------------

nb_iterations = 20


# Début de la recherche tabou


for iteration in range(nb_iterations):

    # Copier la meilleure tournée actuelle
    voisin = meilleure_route[:]

    # Choisir deux positions aléatoires
    i = random.randint(1, 7)
    j = random.randint(1, 7)

    # Éviter d'échanger la même position
    while i == j:
        j = random.randint(1, 7)

    # Échange de deux villes
    voisin[i], voisin[j] = voisin[j], voisin[i]

    # Vérifier que la solution n'est pas tabou
    if str(voisin) not in liste_tabou:

        cout_voisin = calcul_cout(voisin)

        print("\nIteration", iteration + 1)
        print("Voisin généré :", voisin)
        print("Coût :", cout_voisin)

        # Mise à jour de la meilleure solution
        if cout_voisin < meilleur_cout:

            meilleure_route = voisin[:]
            meilleur_cout = cout_voisin

            print(">>> Nouvelle meilleure solution trouvée")

        # Ajouter la solution dans la liste tabou
        liste_tabou.append(str(voisin))

        # Taille maximale de la liste tabou = 5
        if len(liste_tabou) > 5:
            liste_tabou.pop(0)




print("Meilleure tournée trouvée :")
print(meilleure_route)

print("Meilleur coût trouvé :")
print(meilleur_cout)