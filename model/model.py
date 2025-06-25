import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self._idMap = {}

    @staticmethod
    def getMetodi():
        return DAO.getMethods()

    def buildGraph(self, anno, metodo, s):
        self._graph.clear()
        self._idMap.clear()
        s = 1 + float(s)
        nodi = DAO.getNodi(anno, metodo)
        self._graph.add_nodes_from(nodi)
        for nodo in self._graph.nodes:
            self._idMap[nodo.Product_number] = nodo
            for nodo2 in self._graph.nodes:
                if nodo2 != nodo and float(nodo.VenditaTot) > s*float(nodo2.VenditaTot):
                    self._graph.add_edge(nodo2, nodo)

    def getGraphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def prodottiRedditizzi(self):
        lista = []
        for nodo in self._graph.nodes:
            suc = list(self._graph.successors(nodo))
            pre = list(self._graph.predecessors(nodo))
            if len(suc) == 0:
                lista.append((nodo, len(pre)))
        listaOrdinata = sorted(lista, key=lambda x: x[1], reverse=True)
        listaFinale = []
        i = 0
        for e in listaOrdinata:
            if i < 5:
                listaFinale.append(e)
                i += 1
        return listaFinale