import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self._idMap = {}

    @staticmethod
    def getMetodi():
        return DAO.getMethods()

    def buildGraph(self, anno, metodo):
        self._graph.clear()
        self._idMap.clear()
        nodi = DAO.getNodi(anno, metodo)
        self._graph.add_nodes_from(nodi)
        for nodo in self._graph.nodes:
            self._idMap[nodo.Product_number] = nodo


    def getGraphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()