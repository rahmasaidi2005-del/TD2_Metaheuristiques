

# EXERCICE 3 : PROBLEME DU VOYAGEUR DE COMMERCE (TSP)
# METHODE : RECUIT SIMULE


import random
import math


# Valeur très grande utilisée lorsqu'il n'existe pas
# de liaison directe entre deux villes


grand = 999999


# Matrice des distances


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


# Fonction qui calcule le coût d'une tournée


def calcul_cout(route):

    total = 0

    for i in range(len(route) - 1):

        ville_depart = route[i] - 1
        ville_arrivee = route[i + 1] - 1

        total += dist[ville_depart][ville_arrivee]

    return total


# Solution initiale imposée par l'énoncé


solution_courante = [1, 2, 3, 4, 5, 6, 7, 8, 1]

# Meilleure solution connue
meilleure_solution = solution_courante[:]
# Température initiale


temperature = 100

# Nombre d'itérations demandé
iterations = 5

print("===================================")
print("RECUIT SIMULE")
print("===================================")

print("Solution initiale :", solution_courante)
print("Coût initial :", calcul_cout(solution_courante))


# Début de l'algorithme


for i in range(iterations):

    # Création d'un voisin
    voisin = solution_courante[:]

    # Choix de deux villes aléatoires
    a = random.randint(1, 7)
    b = random.randint(1, 7)

    while a == b:
        b = random.randint(1, 7)

    # Échange des villes
    voisin[a], voisin[b] = voisin[b], voisin[a]

    # Calcul des coûts
    cout_courant = calcul_cout(solution_courante)
    cout_voisin = calcul_cout(voisin)

    # Différence entre les coûts
    delta = cout_voisin - cout_courant

    print("\nIteration", i + 1)
    print("Température =", temperature)
    print("Voisin =", voisin)
    print("Coût voisin =", cout_voisin)


    # Si le voisin est meilleur


    if delta < 0:

        solution_courante = voisin[:]

        print("Solution améliorée acceptée")


    # Si le voisin est moins bon


    else:

        probabilite = math.exp(-delta / temperature)

        aleatoire = random.random()

        print("Probabilité =", probabilite)

        if aleatoire < probabilite:

            solution_courante = voisin[:]

            print("Solution moins bonne acceptée")

        else:

            print("Solution rejetée")

    # Mise à jour de la meilleure solution

    if calcul_cout(solution_courante) < calcul_cout(meilleure_solution):
        meilleure_solution = solution_courante[:]

    # Diminution progressive de la température
    temperature = temperature * 0.8



print("Meilleure tournée trouvée :")
print(meilleure_solution)

print("Coût final :")
print(calcul_cout(meilleure_solution))