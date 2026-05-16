import random
from film import Film


class SalleCinema:
    _numeros_utilises = set()
    def __init__(self):
        numero = random.randint(1, 15)
        while numero in SalleCinema._numeros_utilises:
            numero = random.randint(1, 15)
        SalleCinema._numeros_utilises.add(numero)
        self.__numeroSalle = numero
        self.__nbPlacesMax = random.randint(50, 150)
        self.__nbPlacesDispos = 0 
        self.__film_a_projeter = None
        self.__venteOuverte = False

    # -- Getters --

    def getNumeroSalle(self) -> int:
        """Retourne le numéro de la salle."""
        return self.__numeroSalle

    def getFilm(self) -> Film:
        """Retourne le film attribué, ou None si aucun."""
        return self.__film_a_projeter

    # -- Gestion de la vente --

    def reinitialiserVente(self):
        """Ouvre la vente et rend toutes les places disponibles."""
        self.__venteOuverte = True
        self.__nbPlacesDispos = self.__nbPlacesMax

    def attribuerFilm(self, film: Film):
        """Attribue un film à la salle et réinitialise la vente."""
        self.__film_a_projeter = film
        self.reinitialiserVente()
        print("Film attribué avec succès")

    def fermerVente(self):
        """Ferme la vente de billets."""
        self.__venteOuverte = False

    def vendreBillets(self, nbBillets: int) -> float:
        """
        Vend des billets et retourne le montant de la transaction.

        Lève RuntimeError si :
          - la vente est fermée
          - nbBillets dépasse la capacité maximale
          - nbBillets dépasse les places disponibles
        """
        if not self.__venteOuverte:
            raise RuntimeError("La vente n'est présentement pas accessible pour ce film")

        if nbBillets > self.__nbPlacesMax:
            raise RuntimeError("Le nombre de billets dépasse la capacité maximale de la salle")

        if nbBillets > self.__nbPlacesDispos:
            raise RuntimeError("Il ne reste plus assez de places disponibles")

        # Ajustement des places disponibles
        self.__nbPlacesDispos -= nbBillets

        # Fermeture automatique si salle complète
        if self.__nbPlacesDispos == 0:
            print("Complet !")
            self.fermerVente()

        # Calcul et retour du montant
        return nbBillets * self.__film_a_projeter.getPrix()

    # -- Affichage --

    def afficher(self):
        if self.__film_a_projeter is None:
            print(f"SALLE {self.__numeroSalle} \u2013 Aucun film à l'affiche")
        elif not self.__venteOuverte:
            print(f"SALLE {self.__numeroSalle} \u2013 {self.__film_a_projeter.getTitre()}, vente terminée")
        else:
            print(f"SALLE {self.__numeroSalle} \u2013 {self.__film_a_projeter.getTitre()}, places disponibles : {self.__nbPlacesDispos}")