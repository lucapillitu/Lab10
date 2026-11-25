import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    """
           Funzione che controlla prima se il valore dell'importo inserito sia valido (es. non deve essere una stringa) e
           poi popola "self._view.lista_visualizzazione" con le seguenti info
           * Numero di Filiali presenti
           * Numero di Collegamenti
           * Lista di Collegamenti che superano l'importo indicato come soglia
           """
    def mostra_collegamenti(self, e):
        valore = self._view.importo_medio_minimo.value

        if (valore is None or not int(valore) or valore<=0):
            self._view.show_alert("inserisci un valore adeguato ad un bonifico")
            return





