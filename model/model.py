from database.dao import DAO
import networkx as nx


class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()


    def popola(self):
        if self._edges is None:
            self._edges = DAO.get_archi()
        if self._nodes is None:
            self._nodes = DAO.get_nodi()

    def filiale(self,id):#da cambiare in un dizionario
        for f in self._nodes:
            if f.id == id:
                return f
        return None


    def costruisci_grafo(self, threshold):

        """
        Costruisce il grafo (self.G) inserendo tutte le Filiali (i nodi) presenti e filtrando i Collegamenti con
        importo medio per bonifico >= threshold (euro)
        """
        self.popola()
        self.G.clear()

        for f in self._nodes:
            self.G.add_node(f)

        #aggiungo tutti i nodi filtrati
        for a in self._edges:
            if a[2] >= threshold:
                self.G.add_edge(self.filiale(a[0]),self.filiale(a[1]), weight=a[2])




    def get_num_edges(self):
        return self.G.number_of_edges()


    def get_num_nodes(self):
        return self.G.number_of_nodes()


    def get_all_edges(self):
        return self.G.edges(data=True)
