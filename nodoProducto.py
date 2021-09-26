class Producto:
    def __init__(self,nombre,listaPrioridad):
        self.siguiente=None
        self.nombre=nombre
        self.listaPrioridad=listaPrioridad
    
    def getSiguiente(self):
        return self.siguiente

    def getNombre(self):
        return self.nombre
    
    def getListaPrioridad(self):
        return self.listaPrioridad

    def setSiguiente(self,arg):
        self.siguiente=arg

    def setNombre(self,arg):
        self.nombre=arg

    def setListaPrioridad(self,arg):
        self.listaPrioridad=arg