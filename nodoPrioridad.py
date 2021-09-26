class Prioridad:
    def __init__(self,componente):
        self.siguiente=None
        self.componente=componente
    
    def getSiguiente(self):
        return self.siguiente

    def getComponente(self):
        return self.Componente

    def setSiguiente(self,arg):
        self.siguiente=arg

    def setComponente(self,arg):
        self.componente=arg