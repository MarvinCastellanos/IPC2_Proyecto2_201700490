from nodoDestino import Destino

class listaT:
    def __init__(self):
        self.head=None

    def getHead(self):
        return self.head
    
    def agregaComponente(self,nodo):
        aux=self.head

        while(True):
            if self.head==None:
                self.head=nodo
                break
            elif aux.getSiguiente()==None:
                aux.setSiguiente(nodo)
                break
            elif aux.getSiguiente().getNLinea()>=nodo.getNLinea():
                nodo.setSiguiente(aux.getSiguiente())
                aux.setSiguiente(nodo)
                break
            else:
                aux=aux.getSiguiente()