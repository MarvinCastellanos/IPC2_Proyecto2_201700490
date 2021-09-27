class Prioridad:
    def __init__(self,linea,componente):
        self.siguiente=None
        self.linea=linea
        self.componente=componente
    
    def getSiguiente(self):
        return self.siguiente

    def getLinea(self):
        return self.linea

    def getComponente(self):
        return self.componente

    def setSiguiente(self,arg):
        self.siguiente=arg

    def setLinea(self,arg):
        self.linea=arg
    
    def setComponente(self,arg):
        self.componente=arg