class Reporte:
    def __init__(self,listaLineas):
        self.siguiente=None #segundo
        self.listaLineas=listaLineas
    
    def getSiguiente(self):
        return self.siguiente

    def getListaLineas(self):
        return self.listaLineas

    def setSiguiente(self,arg):
        self.siguiente=arg

    def setListaLineas(self,arg):
        self.listaLineas=arg