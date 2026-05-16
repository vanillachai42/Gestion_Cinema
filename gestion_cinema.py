from film import Film
from salle_cinema import SalleCinema
from salle_de_luxe import SalleDeLuxe


class GestionCinema:
    def __init__(self):
        self.__nom = "CinéMax"
        self.__ventes = 0.0
        self.__lstFilms = []
        self.__lstSalles = []

    # -- Getters --

    def getVentes(self) -> float:
        """Retourne les ventes totales du jour."""
        return self.__ventes

    def getListeFilms(self) -> list:
        """Retourne la liste des films."""
        return self.__lstFilms

    def getListeSalles(self) -> list:
        """Retourne la liste des salles."""
        return self.__lstSalles

    # -- Gestion des films --

    def ajouterFilm(self, film: Film):
        """Ajoute un film au catalogue."""
        self.__lstFilms.append(film)

    def chercherFilmParTitre(self, titre: str) -> Film:
        """
        Cherche et retourne le film correspondant au titre.
        Lève RuntimeError si introuvable.
        """
        for film in self.__lstFilms:
            if film.getTitre() == titre:
                return film
        raise RuntimeError("Ce film n'existe pas")

    def supprimerFilm(self, titre: str):
        """
        Supprime le film correspondant au titre.
        """
        film = self.chercherFilmParTitre(titre)
        self.__lstFilms.remove(film)

    # -- Gestion des salles --

    def ajouterSalle(self, salle):
        if not isinstance(salle, SalleCinema):
            raise TypeError("Le paramètre doit être de type SalleCinema ou SalleDeLuxe")
        self.__lstSalles.append(salle)

    def chercherSalleParNum(self, numero: int):
        for salle in self.__lstSalles:
            if salle.getNumeroSalle() == numero:
                return salle
        raise RuntimeError("Ce numéro de salle n'existe pas")

    def chercherSallesSansFilm(self) -> list:
        """Retourne la liste des salles sans film attribué"""
        return [salle for salle in self.__lstSalles if salle.getFilm() is None]

    # -- Gestion des revenus --

    def ajouterVentes(self, montant: float):
        self.__ventes += montant

    # -- Affichage --

    def afficherCinema(self):
        print(self.__nom)
        print("=" * 16)
        print(f"Nombre de films : {len(self.__lstFilms)}")
        print(f"Total des ventes : {self.__ventes}$")
        print("-" * 26)
        for salle in self.__lstSalles:
            salle.afficher()
