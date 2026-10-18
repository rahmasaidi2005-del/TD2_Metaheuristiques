# TD2 - Métaheuristiques

## Réalisé par

**Rahma Saidi**

---

# Introduction

Ce travail a pour objectif d'étudier l'utilisation des métaheuristiques pour résoudre des problèmes d'optimisation combinatoire.

Les méthodes utilisées sont :

- Recherche Tabou
- Recuit Simulé
- Algorithme Génétique

Ces algorithmes ont été appliqués au :

- Problème de Transport
- Problème du Voyageur de Commerce (TSP)

---

# Exercice 2 : Problème de Transport

## Description du problème

Une entreprise possède deux dépôts :

- D1 : 8 conteneurs
- D2 : 9 conteneurs

Trois magasins doivent être approvisionnés :

- M1 : 4 conteneurs
- M2 : 5 conteneurs
- M3 : 8 conteneurs

L'objectif est de satisfaire toutes les demandes tout en minimisant le coût de transport.

---

## Conception du problème

```text
                DEPOTS

             D1       D2
            (8)      (9)

             |\      /|
             | \    / |
             |  \  /  |

            M1 M2 M3

             4  5  8
```

---

## Matrice des coûts

| Dépôt | M1 | M2 | M3 |
|---------|---------|---------|---------|
| D1 | 5 | 3 | 4 |
| D2 | 6 | 7 | 2 |

---

## Modélisation

Une solution est représentée par une matrice indiquant le nombre de conteneurs transportés entre les dépôts et les magasins.

Exemple :

```text
        M1 M2 M3
D1      3  5  0
D2      1  0  8
```

---

## Fonction Objectif

```text
Minimiser :

Coût Total = Σ (Quantité × Coût Unitaire)
```

---

## Solution obtenue

```text
D1 → M1 = 3

D1 → M2 = 5

D1 → M3 = 0

D2 → M1 = 1

D2 → M2 = 0

D2 → M3 = 8
```

---

## Calcul du coût

```text
D1 → M1 : 3 × 5 = 15

D1 → M2 : 5 × 3 = 15

D2 → M1 : 1 × 6 = 6

D2 → M3 : 8 × 2 = 16
```

```text
Coût Total = 52
```

---



# Exercice 3 : Problème du Voyageur de Commerce

## Description du problème

Le voyageur doit visiter toutes les villes une seule fois puis revenir à la ville de départ.

Le but est de minimiser la distance totale parcourue.

---

## Conception du problème

```text
          (1)
         /   \
        /     \
      (2)     (8)
       |       |
       |       |
      (3)     (7)
       |       |
       |       |
      (4)----(6)
         \   /
          (5)
```

---

## Solution initiale

```text
1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 1
```

---

## Calcul du coût initial

```text
1 → 2 = 14

2 → 3 = 13

3 → 4 = 11

4 → 5 = 11

5 → 6 = 15

6 → 7 = 9

7 → 8 = 13

8 → 1 = 17
```

```text
Coût Initial = 103
```

---

# Recherche Tabou

## Principe

La recherche tabou consiste à explorer le voisinage d'une solution afin d'en trouver une meilleure.

Une liste tabou est utilisée pour empêcher le retour vers des solutions déjà explorées.

---

## Étapes

1. Partir d'une solution initiale.
2. Générer un voisin.
3. Évaluer son coût.
4. Comparer les solutions.
5. Mettre à jour la liste tabou.
6. Répéter plusieurs itérations.

---



# Recuit Simulé

## Principe

Le recuit simulé est inspiré du refroidissement des métaux.

Il accepte toujours les meilleures solutions mais peut également accepter certaines solutions moins bonnes afin d'éviter les minima locaux.

---

## Paramètres utilisés

```text
Température initiale = 100

Nombre d'itérations = 5

Refroidissement :

T = T × 0.8
```

---

## Étapes

1. Générer un voisin.
2. Calculer la différence de coût.
3. Accepter ou refuser la solution.
4. Réduire la température.
5. Continuer jusqu'à la dernière itération.

---



# Algorithme Génétique

## Principe

L'algorithme génétique s'inspire du principe de sélection naturelle.

Chaque solution représente un individu d'une population.

L'objectif est de faire évoluer la population afin de trouver les meilleures tournées.

---

## Étapes

### Génération initiale

Création d'une population de solutions aléatoires.

### Évaluation

Calcul de la qualité de chaque solution.

### Sélection

Conservation des meilleurs individus.

### Mutation

Modification aléatoire d'une solution.

### Nouvelle génération

Création d'une nouvelle population.



# Comparaison des Méthodes

## Recherche Tabou

### Avantages

- Simple à implémenter.
- Utilise une mémoire des solutions déjà visitées.
- Évite les cycles.

### Inconvénients

- Peut rester bloquée dans certaines zones de recherche.

---

## Recuit Simulé

### Avantages

- Permet d'éviter les minima locaux.
- Offre une bonne exploration.

### Inconvénients

- Dépend fortement du choix de la température.

---

## Algorithme Génétique

### Avantages

- Explore simultanément plusieurs solutions.
- Très bonne diversification.
- Adapté aux grands espaces de recherche.

### Inconvénients

- Temps d'exécution plus élevé.
- Plus grand nombre de paramètres.

---

## Tableau Comparatif

| Critère | Recherche Tabou | Recuit Simulé | Algorithme Génétique |
|----------|----------|----------|----------|
| Mémoire | Oui | Non | Non |
| Population | Non | Non | Oui |
| Évite les minima locaux | Moyen | Bon | Très bon |
| Diversification | Moyenne | Bonne | Très bonne |
| Complexité | Faible | Moyenne | Élevée |

---

## Analyse

La recherche tabou améliore progressivement une solution grâce à l'utilisation d'une mémoire.

Le recuit simulé accepte parfois des solutions moins performantes afin d'explorer davantage l'espace de recherche.

L'algorithme génétique travaille sur une population complète de solutions et offre généralement une meilleure capacité d'exploration.

---

# Structure du Projet

```text
TD2_Metaheuristiques
│
├── images
│   ├── resultat_ex2.png
│   ├── resultat_genetique.png
│   ├── resultat_recuit.png
│   ├── resultat_recuit2.png
│   ├── resultat_tabou.png
│   ├── resultat_tabou2.png
│   └── resultat_tabou3.png
│
├── ex2_transport_tabou.py
├── ex3_tabou.py
├── ex3_recuit_simule.py
├── ex3_genetique.py
└── README.md
```

---



# Conclusion

Dans ce travail, trois métaheuristiques ont été étudiées afin de résoudre des problèmes d'optimisation.

La Recherche Tabou repose sur une mémoire appelée liste tabou.

Le Recuit Simulé utilise une température permettant d'accepter temporairement des solutions moins bonnes.

L'Algorithme Génétique fait évoluer une population de solutions à travers la sélection et la mutation.

Ces approches permettent de résoudre efficacement des problèmes complexes tels que le transport et le voyageur de commerce.
