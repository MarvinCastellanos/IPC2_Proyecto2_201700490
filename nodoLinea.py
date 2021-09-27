from listaDestino import listaD
class Linea:
    def __init__(self,tiempo,cantidad,nLinea):
        self.siguiente=None
        self.tiempo=tiempo
        self.cantidad=cantidad
        self.nLinea=nLinea
        self.listaDestino=listaD()
        self.nPosicion=0
        self.tTiempo=0
    
    def getSiguiente(self):
        return self.siguiente

    def getTiempo(self):
        return self.tiempo
    
    def getCantidad(self):
        return self.cantidad

    def getNLinea(self):
        return self.nLinea
    
    def getListaDestino(self):
        return self.listaDestino
    
    def getNPosicion(self):
        return self.nPosicion

    def getTTiempo(self):
        return self.tTiempo

    def setSiguiente(self,arg):
        self.siguiente=arg

    def setTiempo(self,arg):
        self.tiempo=arg

    def setCantidad(self,arg):
        self.cantidad=arg

    def setNLinea(self,arg):
        self.nLinea=arg

    def setListaDestino(self,arg):
        self.listaDestino=arg

    def setNPosicion(self,arg):
        self.nPosicion=arg

    def setTTiempo(self,arg):
        self.tTiempo=arg