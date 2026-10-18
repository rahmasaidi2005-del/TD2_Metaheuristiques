import random

grand = 999999

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

def calcul_cout(route):
    total = 0

    for i in range(len(route) - 1):
        total += dist[route[i]-1][route[i+1]-1]

    return total

def creer_route():
    villes = [2, 3, 4, 5, 6, 7, 8]

    random.shuffle(villes)

    return [1] + villes + [1]

population = []

for i in range(6):
    population.append(creer_route())

nb_gen = 10

print("================================")
print("ALGORITHME GENETIQUE")
print("================================")

for gen in range(nb_gen):

    population.sort(key=calcul_cout)

    meilleur = population[0]

    print("\nGeneration", gen + 1)
    print("Meilleure tournée :", meilleur)
    print("Coût :", calcul_cout(meilleur))

    nouvelle_pop = population[:2]

    while len(nouvelle_pop) < 6:

        parent = random.choice(population[:3])

        enfant = parent[:]

        i = random.randint(1, 7)
        j = random.randint(1, 7)

        enfant[i], enfant[j] = enfant[j], enfant[i]

        nouvelle_pop.append(enfant)

    population = nouvelle_pop

population.sort(key=calcul_cout)

print("\nRésultat final :")
print("Meilleure tournée :", population[0])
print("Coût total :", calcul_cout(population[0]))