import random

couts = [
    [5, 3, 4],
    [6, 7, 2]
]

sol = [
    [3, 5, 0],
    [1, 0, 8]
]

def calcul_cout(sol):
    total = 0

    for i in range(2):
        for j in range(3):
            total += sol[i][j] * couts[i][j]

    return total

def voisin(sol):
    nouv = [ligne[:] for ligne in sol]

    j = random.randint(0, 2)

    if nouv[0][j] > 0:
        nouv[0][j] -= 1
        nouv[1][j] += 1

    return nouv

tabou = []

meilleure_sol = sol
meilleur_cout = calcul_cout(sol)

print("Coût initial :", meilleur_cout)

for i in range(10):
    nouv = voisin(meilleure_sol)

    if str(nouv) not in tabou:
        cout = calcul_cout(nouv)

        if cout < meilleur_cout:
            meilleure_sol = nouv
            meilleur_cout = cout

        tabou.append(str(nouv))

        if len(tabou) > 5:
            tabou.pop(0)

print("Meilleure solution :", meilleure_sol)
print("Meilleur coût :", meilleur_cout)