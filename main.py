from film import Film
from salle_cinema import SalleCinema
from salle_de_luxe import SalleDeLuxe
from gestion_cinema import GestionCinema


# -- Affichage du menu --

def menu() -> str:
    print("=" * 60)
    print("    1) Afficher les informations du cinéma")
    print("    2) Ajouter un film")
    print("    3) Supprimer un film")
    print("    4) Attribuer un film à une salle")
    print("    5) Vendre des places de cinéma")
    print("    6) Quitter")
    print("=" * 60)
    return input("Entrez votre choix : ")


# -- Options --

def option1(cinema: GestionCinema):
    """Affiche les informations du cinéma."""
    cinema.afficherCinema()


def option2(cinema: GestionCinema):
    """Demande les infos d'un nouveau film, le crée et l'ajoute au cinéma."""
    try:
        titre = input("Titre du film : ")
        categorie = input("Catégorie : ")
        duree = int(input("Durée (en minutes) : "))
        cinema.ajouterFilm(Film(titre, categorie, duree))
        print("Film ajouté avec succès.")
    except ValueError as e:
        print(f"Erreur : {e}")


def option3(cinema: GestionCinema):
    """Demande un titre et supprime le film correspondant."""
    try:
        titre = input("Titre du film à supprimer : ")
        cinema.supprimerFilm(titre)
        print("Film supprimé avec succès.")
    except RuntimeError as e:
        print(f"Erreur : {e}")


def option4(cinema: GestionCinema):
    """Affiche les salles libres, demande un numéro de salle et un titre de film, puis attribue."""
    try:
        salles_libres = cinema.chercherSallesSansFilm()
        if not salles_libres:
            print("Toutes les salles ont déjà un film attribué.")
            return

        print("\nSalles sans film :")
        for salle in salles_libres:
            salle.afficher()

        numero = int(input("\nNuméro de la salle choisie : "))
        salle = cinema.chercherSalleParNum(numero)

        print("\nFilms disponibles :")
        for film in cinema.getListeFilms():
            print(film)

        titre = input("\nTitre du film à attribuer : ")
        film = cinema.chercherFilmParTitre(titre)
        salle.attribuerFilm(film)

    except (RuntimeError, ValueError) as e:
        print(f"Erreur : {e}")


def option5(cinema: GestionCinema):
    """
    Gère la vente de billets ou de loges.
    """
    try:
        cinema.afficherCinema()

        titre = input("\nQuel film voulez-vous regarder ? ")
        cinema.chercherFilmParTitre(titre)

        numero = int(input("Numéro de la salle : "))
        salle = cinema.chercherSalleParNum(numero)

        nb = int(input("Nombre de billets / personnes : "))

        if isinstance(salle, SalleDeLuxe):
            # Salle de luxe : choix entre loge et places régulières
            choix_type = input("Loge ou places régulières ? (loge/regulier) : ")
            if choix_type.strip().lower() == "loge":
                montant = salle.calculerVentesLoges(nb)
            else:
                montant = salle.vendreBillets(nb)
        else:
            montant = salle.vendreBillets(nb)

        cinema.ajouterVentes(montant)
        print(f"Vente réussie. Montant : {montant}$")

    except (RuntimeError, ValueError) as e:
        print(f"Erreur : {e}")


def option6():
    """Affiche le message de fin et quitte."""
    print("Programme réalisé par : VanillaChai42")


# -- Initialisation --

cinema = GestionCinema()

# 4 salles régulières + 2 salles de luxe
for _ in range(4):
    cinema.ajouterSalle(SalleCinema())
for _ in range(2):
    cinema.ajouterSalle(SalleDeLuxe())

# 2 films requis par l'énoncé
film1 = Film("Bohemian Rhapsody", "Drame", 123)
film2 = Film("Casse-Noisette", "Jeunesse", 94)
cinema.ajouterFilm(film1)
cinema.ajouterFilm(film2)

cinema.getListeSalles()[0].attribuerFilm(film2)


# -- Boucle Principale --

while True:
    choix = menu()

    try:
        choix = int(choix)
    except ValueError:
        print("Choix invalide — entrez un chiffre entre 1 et 6.")
        continue

    if   choix == 1: option1(cinema)
    elif choix == 2: option2(cinema)
    elif choix == 3: option3(cinema)
    elif choix == 4: option4(cinema)
    elif choix == 5: option5(cinema)
    elif choix == 6: option6(); break
    else: print("Choix invalide — entrez un chiffre entre 1 et 6.")
