# Système de Gestion de Billets de Cinéma

Travail pratique réalisé dans le cadre du cours **Programmation 2 (420-F16-RO)** au Cégep de Rosemont.

## Description

Simulation d'un système de gestion pour le cinéma fictif **CinéMax**, permettant de gérer les films, les salles et la vente de billets via une interface en ligne de commande.

## Structure du projet

```
TP_GestionCinema/
├── film.py               # Classe Film (titre, catégorie, durée, prix fixe à 13$)
├── salle_cinema.py       # Classe SalleCinema (numéro et capacité aléatoires)
├── salle_de_luxe.py      # Classe SalleDeLuxe (hérite de SalleCinema, ajoute des loges)
├── gestion_cinema.py     # Classe GestionCinema (gère films, salles et revenus)
└── main.py               # Programme principal et menu interactif
```

## Prérequis

- Python 3.x

Aucune bibliothèque externe n'est requise. Les modules `random` et `math` (bibliothèque standard) sont utilisés.

## Installation

```bash
git clone https://github.com/vanillachai42/Gestion_Cinema.git
cd Gestion_Cinema
```

## Utilisation

```bash
python main.py
```

Au démarrage, le programme initialise automatiquement le cinéma avec :
- 4 salles régulières et 2 salles de luxe (numéros et capacités aléatoires)
- 2 films : *Bohemian Rhapsody* (Drame, 123 min) et *Casse-Noisette* (Jeunesse, 94 min)
- *Casse-Noisette* attribué à la première salle

Le menu interactif propose les options suivantes :

| Option | Description |
|--------|-------------|
| 1 | Afficher les informations du cinéma |
| 2 | Ajouter un film |
| 3 | Supprimer un film |
| 4 | Attribuer un film à une salle sans film |
| 5 | Vendre des places (régulières ou loges) |
| 6 | Quitter |

Pour l'option 5, si la salle choisie est une salle de luxe, le programme demande si l'achat concerne des loges (`loge`) ou des places régulières (`regulier`).

## Informations académiques

| Champ | Détail |
|-------|--------|
| Cours | Programmation 2 — 420-F16-RO |
| Établissement | Cégep de Rosemont |
| Auteur | VanillaChai42 |
