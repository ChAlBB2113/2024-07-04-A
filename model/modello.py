from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodi=[]
        self._archi=[]
        self._grafo=nx.DiGraph()


    def getAnni(self):
        return DAO.getAnni()
    def getForme(self, a):
        return DAO.getShape(a)

    def creaGrafo(self,annoDato, formaData):
        self._nodi.clear()
        self._archi.clear()
        self._grafo.clear()

        avvistamenti=DAO.get_all_sightings()
        for avvistamento in avvistamenti:
            if avvistamento.shape==formaData and avvistamento.datetime.strftime("%Y")==annoDato:
                print(avvistamento.shape, formaData, avvistamento.datetime.strftime("%Y"), annoDato)
                self._nodi.append(avvistamento)

        self._grafo.add_nodes_from(self._nodi)
        print(len(self._nodi))


        for a1 in self._nodi:
            for a2 in self._nodi:
                if a1.id!=a2.id and a1.state==a2.state:
                    print((a1,a2))
                    if a1.datetime.strftime("%Y-%m-%d %H:%M:%S")<a2.datetime.strftime("%Y-%m-%d %H:%M:%S"):
                        #if (a1,a2) not in self._archi: (non serve, doppi archi direzionati a stesso modo pure non li conta il digraph)
                            self._archi.append((a1,a2))
                            print((a1,a2))
                    if a1.datetime.strftime("%Y-%m-%d %H:%M:%S")>a2.datetime.strftime("%Y-%m-%d %H:%M:%S"):
                        #if (a1, a2) not in self._archi: (idem di qua sopra)
                            self._archi.append((a2,a1))
                            print((a2,a1))


        print(len(self._archi))

        self._grafo.add_edges_from(self._archi)


        #altrimenti me la potevo cavare con una query come fatto per tema esame luglio C dove preso da db
        #ogni coppia di avvistamenti diversi (diverso id) con quella forma e quell anno e rispettive longitudini in tuple da 4 elementi,
        #(qui avrei preso rispettive date, non longitudini ) per poi fare confronto longitudini (date in sto caso) e
        #costruire opportuno arco per ciascuna di quelle tuple (tranne per quelle in cui differenza longitudini era nulla, come
        #qui non penso si debba considerare caso di datetime uguale)


