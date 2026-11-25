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

        if valore is None or not int(valore) or int(valore)<=0:
            self._view.show_alert("inserisci un valore adeguato ad un bonifico")
            return

        self._model.costruisci_grafo(int(valore))#costruisce il grafo effettivo in base al filtro valore

        n_archi = self._model.get_num_edges()
        self._view.lista_visualizzazione.controls.append(
            ft.Text(f"Numero di collegamenti: {n_archi}"))

        n_nodi = self._model.get_num_nodes()
        self._view.lista_visualizzazione.controls.append(
            ft.Text(f"Numero di filiari: {n_nodi}"))

        for f1, f2, attr in self._model.get_all_edges():
            self._view.lista_visualizzazione.controls.append(ft.Text(f"- {f1.nome} [{f1.codice}] -> {f2.nome} [{f2.codice}], con importo bonifico medio : € {attr}"))





