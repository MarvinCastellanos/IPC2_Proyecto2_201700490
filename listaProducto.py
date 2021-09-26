from nodoProducto import Producto
from PyQt5.QtWidgets import QMessageBox

class listaP:
    def __init__(self):
        self.head=None

    def getHead(self):
        return self.head
    
    def agregaProducto(self,nodo):
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

    def mensaje(self):
        msg=QMessageBox()
        msg.setWindowTitle('Error')
        msg.setText('El producto no ha sido encontrado')
        msg.setIcon(QMessageBox.Critical)
        x=msg.exec_()

    def buscar(self,nombre):
        aux=self.head

        while(True):
            if aux.getNombre()==nombre:
                return aux
            elif aux.getSiguiente()==None:
                self.mensaje()
                break
            else:
                aux=aux.getSiguiente()