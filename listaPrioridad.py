from nodoPrioridad import Prioridad

class listaPriori:
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
            else:
                aux=aux.getSiguiente()
    
    def pop(self):
        if self.head==None:
            print('lista Vacia')
        aux=self.head
        self.head=aux.getSiguiente()
        aux=None