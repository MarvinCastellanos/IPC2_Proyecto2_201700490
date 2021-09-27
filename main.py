# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QFileDialog
import xml.etree.ElementTree as ET
import re
import graphviz
import codecs
import webbrowser

from nodoLinea import Linea
from nodoProducto import Producto
from nodoPrioridad import Prioridad
from nodoDestino import Destino
from nodoLineaReporte import LineaR
from nodoReporte import Reporte

from listaLinea import listaL
from listaProducto import listaP
from listaPrioridad import listaPriori
from listaDestino import listaD
from listaLineaReporte import listaLR
from listaReporte import listaT

lineaMaquinas=listaL()
productosDisponibles=listaP()
TablaReporte=listaT()
time=0


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 507)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 50, 191, 22))
        self.comboBox.setMaxVisibleItems(30)
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 50, 161, 31))
        self.pushButton.setObjectName("pushButton")

        self.pushButtonActualiza = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonActualiza.setGeometry(QtCore.QRect(520, 50, 161, 31))
        self.pushButtonActualiza.setObjectName("pushButtonActualiza")

        self.labelProducto = QtWidgets.QLabel(self.centralwidget)
        self.labelProducto.setGeometry(QtCore.QRect(20, 70, 361, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.labelProducto.setFont(font)
        self.labelProducto.setText("")
        self.labelProducto.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProducto.setObjectName("labelProducto")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(270, 160, 411, 291))
        self.tableView.setObjectName("tableView")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 140, 411, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionCargar_m_quinas = QtWidgets.QAction(MainWindow)
        self.actionCargar_m_quinas.setObjectName("actionCargar_m_quinas")
        self.actionCargar_Simulaci_n = QtWidgets.QAction(MainWindow)
        self.actionCargar_Simulaci_n.setObjectName("actionCargar_Simulaci_n")
        self.actionInformaci_n_de_estudiante = QtWidgets.QAction(MainWindow)
        self.actionInformaci_n_de_estudiante.setObjectName("actionInformaci_n_de_estudiante")
        self.actionGenerar_reporte = QtWidgets.QAction(MainWindow)
        self.actionGenerar_reporte.setObjectName("actionGenerar_reporte")
        self.menuFile.addAction(self.actionCargar_m_quinas)
        self.menuFile.addAction(self.actionCargar_Simulaci_n)
        self.menuEdit.addAction(self.actionGenerar_reporte)
        self.menuAyuda.addAction(self.actionInformaci_n_de_estudiante)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 360, 271, 21))
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(70, 380, 111, 61))
        self.lcdNumber.setObjectName("lcdNumber")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionInformaci_n_de_estudiante.triggered.connect(self.datosEstudiante)
        self.actionCargar_m_quinas.triggered.connect(lambda: cargarMaquinas(QFileDialog.getOpenFileName()))
        #self.actionCargar_m_quinas.triggered.connect(self.rellenaComboBox)
        self.actionCargar_Simulaci_n.triggered.connect(lambda:cargarSimulacion(QFileDialog.getOpenFileName()))
        self.actionGenerar_reporte.triggered.connect(generarReporte)
        self.pushButtonActualiza.clicked.connect(self.rellenaComboBox)
        self.pushButton.clicked.connect(self.simulaProducto)
        self.actionGenerar_reporte.triggered.connect(self.reportes)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Proyecto 2"))
        self.pushButton.setText(_translate("MainWindow", "Simular"))
        self.pushButtonActualiza.setText(_translate("MainWindow", "Actualizar ventana"))
        self.label.setText(_translate("MainWindow", "Productos disponibles."))
        self.label_2.setText(_translate("MainWindow", "Tabla de simulación."))
        self.menuFile.setTitle(_translate("MainWindow", "Archivo"))
        self.menuEdit.setTitle(_translate("MainWindow", "Reportes"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create a new file"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save a file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setStatusTip(_translate("MainWindow", "Copy a file"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setStatusTip(_translate("MainWindow", "Paste a file"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionCargar_m_quinas.setText(_translate("MainWindow", "Cargar máquinas"))
        self.actionCargar_m_quinas.setStatusTip(_translate("MainWindow", "Carga archivo XML de máquinas"))
        self.actionCargar_Simulaci_n.setText(_translate("MainWindow", "Cargar Simulación"))
        self.actionCargar_Simulaci_n.setStatusTip(_translate("MainWindow", "Carga archivo de sumulación de varias máquinas"))
        self.actionInformaci_n_de_estudiante.setText(_translate("MainWindow", "Información de estudiante"))
        self.actionInformaci_n_de_estudiante.setStatusTip(_translate("MainWindow", "Muestra información de estudiante"))
        self.actionGenerar_reporte.setText(_translate("MainWindow", "Generar reporte"))
        self.actionGenerar_reporte.setStatusTip(_translate("MainWindow", "Genera Reportes"))
        self.label_3.setText(_translate("MainWindow", "Tiempo de ensamblaje"))

    def reportes(self):
        generaGraphviz(productosDisponibles.buscar(self.comboBox.currentText()))
        generaHTML(productosDisponibles.buscar(self.comboBox.currentText()))



    def simulaProducto(self):
        global time
        t=ensamblar(productosDisponibles.buscar(self.comboBox.currentText())) 
        self.lcdNumber.setProperty("value", t)

    def rellenaComboBox(self):
        aux=productosDisponibles.getHead()
        self.comboBox.clear()
        while(True):
            if aux is not None:
                self.comboBox.addItem(aux.getNombre())
            else:
                break
            if aux.getSiguiente()==None:
                break
            aux=aux.getSiguiente()

    def datosEstudiante(self):
        msg=QMessageBox()
        msg.setWindowTitle('Datos de estudiante')
        msg.setText('Marvin Daniel Castellanos Castillo\n201700490\nIPC2')
        msg.setIcon(QMessageBox.Information)
        x=msg.exec_()
    
def generaHTML(producto):
    global TablaReporte
    html='''
    
    <!DOCTYPE html>
 <html lang="es">
 <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <title>Reportes</title>
 </head>
 <body>
    <h1>'''
    html+=producto.getNombre()+'</h1><table>'
    html+='''<tr><th>Segundo</th><th>Linea</th><th>Accion<tr></th>'''
    
    aux=TablaReporte.getHead()
    n=1
    while(True):
        aux2=aux.getListaLineas().getHead()
        while(True):
            
            if aux2==None:
                #aux2=aux.getListaLineas().getHead()
                break
            
            html+='<tr><th>S'+str(n)+'</th>'
            html+='<th>'+str(aux2.getLinea())+'</th>'
            html+='<th>'+aux2.getMensaje()+'</th></tr>'
            aux2=aux2.getSiguiente()
            continue

        if aux.getSiguiente()==None:
            html+='<tr></tr>'
            break
        else:
            aux=aux.getSiguiente()
            n+=1
            continue
    n+=1
    html+='</tr></table></body></html>'
            
    file=codecs.open("Reporte.html","w",'utf-8')
    file.write(html)
    file.close()
    webbrowser.open_new_tab('Reporte.html')



def generaGraphviz(producto):

    dot = graphviz.Digraph(comment='The Round Table')
    lineas=re.findall('L[0-9]+p?C[0-9]+',producto.getListaPrioridad())
    LPrioridad=listaPriori()
    for linea in lineas:
        L =re.search('L[0-9]+',linea).group()
        L =re.search('[0-9]+',L).group()

        C=re.search('C[0-9]+',linea).group()
        C=re.search('[0-9]+',C).group()

        LPrioridad.agregaComponente(Prioridad(L,C))

    aux=LPrioridad.getHead()
    n=0
    while (True):
        txt='L'+aux.getLinea()+'C'+aux.getComponente()
        nactual=str(n)
        nsiguiente=str(n+1)
        dot.node(nactual,txt)
        if aux.getSiguiente()==None:
            break
        else:
            dot.edge(nactual, nsiguiente, constraint='false')
            aux=aux.getSiguiente()
            n+=1
    dot.render('grafica', view=True)

def ensamblar(producto):
    global TablaReporte

    TablaReporte=listaT()

    lineas=re.findall('L[0-9]+p?C[0-9]+',producto.getListaPrioridad())
    LPrioridad=listaPriori()
    for linea in lineas:
        L =re.search('L[0-9]+',linea).group()
        L =re.search('[0-9]+',L).group()

        C=re.search('C[0-9]+',linea).group()
        C=re.search('[0-9]+',C).group()

        LPrioridad.agregaComponente(Prioridad(L,C))

    #rellena listas de destino de cada linea de ensamblaje
    auxL=lineaMaquinas.getHead() #auxiliar de lineas
    while(True):  
        auxP=LPrioridad.getHead() #auxiliar de lista de prioridad
        while(True):
            if int(auxP.getLinea())==int(auxL.getNLinea()):
                auxL.getListaDestino().agregaComponente(Destino(int(auxP.getComponente())))
                #print('linea '+auxP.getLinea()+', componente '+auxP.getComponente())
            
            if auxP.getSiguiente()==None:
                break
            else:
                auxP=auxP.getSiguiente()
        
        if auxL.getSiguiente()==None:
            break
        else:
            auxL=auxL.getSiguiente()
    #print('agregados')

    time=0
    auxL=lineaMaquinas.getHead()
    while(True):
        ListaReporte=listaLR()
        if auxL==None:
            auxL=lineaMaquinas.getHead()
            time+=1
        if LPrioridad.getHead()==None:
            break
        elif auxL.getListaDestino().getHead()==None:
            ListaReporte.agregaLinea(LineaR(auxL.getNLinea(),'No hace nada'))
            pass
        elif int(auxL.getListaDestino().getHead().getComponente())==int(auxL.getNPosicion()):
            if int(auxL.getNLinea())==int(LPrioridad.getHead().getLinea()):
                #ensamblar
                if int(auxL.getTiempo()) == int(auxL.getTTiempo()):
                    #se ensambla
                    ListaReporte.agregaLinea(LineaR(auxL.getNLinea(),'Ensambla'))
                    auxL.setTiempo(auxL.getTTiempo()+1)
                else:
                    LPrioridad.pop()
                    auxL.getListaDestino().pop()
            else:
                #no hacer nada
                ListaReporte.agregaLinea(LineaR(auxL.getNLinea(),'No hace nada'))
                pass
        elif int(auxL.getListaDestino().getHead().getComponente())<int(auxL.getNPosicion()):
            #se mueve hacia atras
            auxL.setNPosicion(auxL.getNPosicion()-1)
            ListaReporte.agregaLinea(LineaR(auxL.getNLinea(),'Se mueve hacia atras'))
            #print(auxL.getNPosicion())
        elif int(auxL.getListaDestino().getHead().getComponente())>int(auxL.getNPosicion()):
            #se mueve hacia adelante
            auxL.setNPosicion(auxL.getNPosicion()+1)
            ListaReporte.agregaLinea(LineaR(auxL.getNLinea(),'Se mueve hacia adelante'))
            #print(auxL.getNPosicion())
        auxL=auxL.getSiguiente()
        TablaReporte.agregaSegundo(Reporte(ListaReporte))
    lineaMaquinas.reset()
    return(time)
    
def cargarMaquinas(direccion):
    tree=ET.parse(direccion[0])
    root=tree.getroot()

    for lineas in root.findall('ListadoLineasProduccion'):
        for linea in lineas.findall('LineaProduccion'):

            numero=linea[0].text
            numero= numero.replace('\t',"")
            numero= numero.replace('\n',"")
            numero= numero.replace(' ',"")

            cantidad=linea[1].text
            cantidad= cantidad.replace('\t',"")
            cantidad= cantidad.replace('\n',"")
            cantidad= cantidad.replace(' ',"")

            tiempo=linea[2].text
            tiempo= tiempo.replace('\t',"")
            tiempo= tiempo.replace('\n',"")
            tiempo= tiempo.replace(' ',"")

            #print(numero)

            lineaMaquinas.agregaLinea(Linea(int(tiempo),int(cantidad),int(numero)))
        mensajeDatosGuardados('lineas de produccion')

    for productos in root.findall('ListadoProductos'):
        for producto in productos.findall('Producto'):

            nombre=producto[0].text
            nombre= nombre.replace('\t',"")
            nombre= nombre.replace('\n',"")
            nombre= nombre.replace(' ',"")

            elaboracion=producto[1].text
            elaboracion= elaboracion.replace('\t',"")
            elaboracion= elaboracion.replace('\n',"")
            elaboracion= elaboracion.replace(' ',"")

            productosDisponibles.agregaProducto(Producto(nombre,elaboracion))
        mensajeDatosGuardados('productos')

def mensajeDatosGuardados(mensaje):
    msg=QMessageBox()
    msg.setWindowTitle('Datos guardados')
    msg.setText('Datos de '+mensaje+' guardados con éxito')
    msg.setIcon(QMessageBox.Information)
    x=msg.exec_()

def cargarSimulacion(direccion):
    print(direccion)

def generarReporte(self):
    pass
    #print('generarReporte')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
