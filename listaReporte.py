from nodoReporte import Reporte

class listaT:
    def __init__(self):
        self.head=None

    def getHead(self):
        return self.head
    
    def agregaSegundo(self,nodo):
        aux=self.head

        while(True):
            if self.head==None:
                self.head=nodo
                break
            elif aux.getSiguiente()==None:
                aux.setSiguiente(nodo)
                break
            else:
                aux=aux.getSiguiente()