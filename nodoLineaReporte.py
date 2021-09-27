from listaDestino import listaD
class LineaR:
    def __init__(self,linea,mensaje):
        self.siguiente=None
        self.linea=linea
        self.mensaje=mensaje

    def getSiguiente(self):
        return self.siguiente
    
    def getLinea(self):
        return self.linea

    def getMensaje(self):
        return self.mensaje

    def setSiguiente(self,arg):
        self.siguiente=arg

    def setLinea(self,arg):
        self.linea=arg

    def setMensaje(self,arg):
        self.mensaje=arg