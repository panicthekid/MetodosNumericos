# -*- coding: utf-8 -*-
"""
Created on Thu May 21 23:14:16 2020

@author: Colin Hernandez R. Akzayakatl
"""
import sys
import math
import cmath
import os
from subprocess import call
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5.uic import loadUi



class VentanaPrincipal(QMainWindow):#se tiene que modificar si es un dialogo

    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('mainMetodos.ui', self)#carga la ventana conversor
        self.temasBtn.clicked.connect(self.abrirVentana)
    def abrirVentana(self):
        self.close()
        otraVentana = VentanaTemas(self)
        otraVentana.show()
    #si se tuvieran mas botones se abriria toda  aqui

                
class VentanaTemas(QDialog):
    
    def __init__(self, parent=None):
        super(VentanaTemas, self).__init__(parent)
        loadUi('ventanaTemas.ui', self)
        self.simpsonBtn.clicked.connect(self.abrirVentanaSimpsonFun)
        self.simpsonTabBtn.clicked.connect(self.abrirSimpson)
        self.lagrangeBtn.clicked.connect(self.abrirLagrange)
        self.trapecioBtn.clicked.connect(self.abrirTrapecio)
        self.newtonBtn.clicked.connect(self.abrirNewton)
        self.inicioBtn.clicked.connect(self.abrirVentanaPrincipal)
        self.puntoBtn.clicked.connect(self.abrirPuntoFijo)
        
    def abrirPuntoFijo(self):
        self.close()
        otraVentana = PuntoFijo(self)
        otraVentana.show()
    
    def abrirVentanaSimpsonFun(self):
        self.close()
        otraVentana = SimpsonFun(self)
        otraVentana.show()
    def abrirNewton(self):
        self.close()
        otraVentana = Newton(self)
        otraVentana.show()
    def abrirSimpson(self):
        self.close()
        otraVentana = Simpson(self)
        otraVentana.show()
    def abrirLagrange(self):
        self.close()
        otraVentana = CodeLagrange(self)
        otraVentana.show()
    def abrirTrapecio(self):
        self.close()
        otraVentana = Trapecio(self)
        otraVentana.show()
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()
        
class CodeLagrange(QDialog):
    
    def __init__(self, parent=None):
        super(CodeLagrange, self).__init__(parent)
        loadUi('codeLagrange.ui', self)
        
        self.crearBtn.clicked.connect(self.visibilidad)
        self.calcBtn.clicked.connect(self.calcular)
        self.inicioBtn.clicked.connect(self.abrirVentanaPrincipal)
        self.x0.setVisible(False)
        self.x1.setVisible(False)
        self.x2.setVisible(False)
        self.x3.setVisible(False)
        self.x4.setVisible(False)
        self.x5.setVisible(False)
        self.x6.setVisible(False)
        self.x7.setVisible(False)
        self.x8.setVisible(False)
        self.x9.setVisible(False)
        self.y0.setVisible(False)
        self.y1.setVisible(False)
        self.y2.setVisible(False)
        self.y3.setVisible(False)
        self.y4.setVisible(False)
        self.y5.setVisible(False)
        self.y6.setVisible(False)
        self.y7.setVisible(False)
        self.y8.setVisible(False)
        self.y9.setVisible(False)
        self.labelx0.setVisible(False)
        self.labelx1.setVisible(False)
        self.labelx2.setVisible(False)
        self.labelx3.setVisible(False)
        self.labelx4.setVisible(False)
        self.labelx5.setVisible(False)
        self.labelx6.setVisible(False)
        self.labelx7.setVisible(False)
        self.labelx8.setVisible(False)
        self.labelx9.setVisible(False)
        
        
        self.labely0.setVisible(False)
        self.labely1.setVisible(False)
        self.labely2.setVisible(False)
        self.labely3.setVisible(False)
        self.labely4.setVisible(False)
        self.labely5.setVisible(False)
        self.labely6.setVisible(False)
        self.labely7.setVisible(False)
        self.labely8.setVisible(False)
        self.labely9.setVisible(False)
        


        
    #aqui van las dunciones
    
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()    
    def visibilidad(self):
        n = (self.nBox.value())
       
        if (n==2):
            
            self.x0.setVisible(True)
            self.x1.setVisible(True)
            self.x2.setVisible(False)
            self.x3.setVisible(False)
            self.x4.setVisible(False)
            self.x5.setVisible(False)
            self.x6.setVisible(False)
            self.x7.setVisible(False)
            self.x8.setVisible(False)
            self.x9.setVisible(False)
            
            
            self.y0.setVisible(True)
            self.y1.setVisible(True)
            self.y2.setVisible(False)
            self.y3.setVisible(False)
            self.y4.setVisible(False)
            self.y5.setVisible(False)
            self.y6.setVisible(False)
            self.y7.setVisible(False)
            self.y8.setVisible(False)
            self.y9.setVisible(False)
            
            self.labelx0.setVisible(True)
            self.labelx1.setVisible(True)
            self.labelx2.setVisible(False)
            self.labelx3.setVisible(False)
            self.labelx4.setVisible(False)
            self.labelx5.setVisible(False)
            self.labelx6.setVisible(False)
            self.labelx7.setVisible(False)
            self.labelx8.setVisible(False)
            self.labelx9.setVisible(False)
            
            self.labely0.setVisible(True)
            self.labely1.setVisible(True)
            self.labely2.setVisible(False)
            self.labely3.setVisible(False)
            self.labely4.setVisible(False)
            self.labely5.setVisible(False)
            self.labely6.setVisible(False)
            self.labely7.setVisible(False)
            self.labely8.setVisible(False)
            self.labely9.setVisible(False)
        elif (n==3):
            self.x0.setVisible(True)
            self.x1.setVisible(True)
            self.x2.setVisible(True)
            self.x3.setVisible(False)
            self.x4.setVisible(False)
            self.x5.setVisible(False)
            self.x6.setVisible(False)
            self.x7.setVisible(False)
            self.x8.setVisible(False)
            self.x9.setVisible(False)
            
            
            
            self.y0.setVisible(True)
            self.y1.setVisible(True)
            self.y2.setVisible(True)
            self.y3.setVisible(False)
            self.y4.setVisible(False)
            self.y5.setVisible(False)
            
            self.y6.setVisible(False)
            self.y7.setVisible(False)
            self.y8.setVisible(False)
            self.y9.setVisible(False)
            
            self.labelx0.setVisible(True)
            self.labelx1.setVisible(True)
            self.labelx2.setVisible(True)
            self.labelx3.setVisible(False)
            self.labelx4.setVisible(False)
            self.labelx5.setVisible(False)
            self.labelx6.setVisible(False)
            self.labelx7.setVisible(False)
            self.labelx8.setVisible(False)
            self.labelx9.setVisible(False)
            self.labely0.setVisible(True)
            self.labely1.setVisible(True)
            self.labely2.setVisible(True)
            self.labely3.setVisible(False)
            self.labely4.setVisible(False)
            self.labely5.setVisible(False)
            self.labely6.setVisible(False)
            self.labely7.setVisible(False)
            self.labely8.setVisible(False)
            self.labely9.setVisible(False)
        elif(n==4):
            self.x0.setVisible(True)
            self.x1.setVisible(True)
            self.x2.setVisible(True)
            self.x3.setVisible(True)
            self.x4.setVisible(False)
            self.x6.setVisible(False)
            self.x7.setVisible(False)
            self.x8.setVisible(False)
            self.x9.setVisible(False)
            
            self.y0.setVisible(True)
            self.y1.setVisible(True)
            self.y2.setVisible(True)
            self.y3.setVisible(True)
            self.y4.setVisible(False)
            self.y5.setVisible(False)
            self.y6.setVisible(False)
            self.y7.setVisible(False)
            self.y8.setVisible(False)
            self.y9.setVisible(False)
            
            self.labelx0.setVisible(True)
            self.labelx1.setVisible(True)
            self.labelx2.setVisible(True)
            self.labelx3.setVisible(True)
            self.labelx4.setVisible(False)
            self.labelx5.setVisible(False)
            self.labelx6.setVisible(False)
            self.labelx7.setVisible(False)
            self.labelx8.setVisible(False)
            self.labelx9.setVisible(False)
            
            self.labely0.setVisible(True)
            self.labely1.setVisible(True)
            self.labely2.setVisible(True)
            self.labely3.setVisible(True)
            self.labely4.setVisible(False)
            self.labely5.setVisible(False)
            self.labely6.setVisible(False)
            self.labely7.setVisible(False)
            self.labely8.setVisible(False)
            self.labely9.setVisible(False)
        elif (n==5):
            self.x0.setVisible(True)
            self.x1.setVisible(True)
            self.x2.setVisible(True)
            self.x3.setVisible(True)
            self.x4.setVisible(True)
            self.x6.setVisible(False)
            self.x7.setVisible(False)
            self.x8.setVisible(False)
            self.x9.setVisible(False)
            
            self.y0.setVisible(True)
            self.y1.setVisible(True)
            self.y2.setVisible(True)
            self.y3.setVisible(True)
            self.y4.setVisible(True)
            self.y5.setVisible(False)
            self.y6.setVisible(False)
            self.y7.setVisible(False)
            self.y8.setVisible(False)
            self.y9.setVisible(False)
            
            self.labelx0.setVisible(True)
            self.labelx1.setVisible(True)
            self.labelx2.setVisible(True)
            self.labelx3.setVisible(True)
            self.labelx4.setVisible(True)
            self.labelx5.setVisible(False)
            self.labelx6.setVisible(False)
            self.labelx7.setVisible(False)
            self.labelx8.setVisible(False)
            self.labelx9.setVisible(False)
            
            self.labely0.setVisible(True)
            self.labely1.setVisible(True)
            self.labely2.setVisible(True)
            self.labely3.setVisible(True)
            self.labely4.setVisible(True)
            self.labely6.setVisible(False)
            self.labely7.setVisible(False)
            self.labely8.setVisible(False)
            self.labely9.setVisible(False)
        elif (n==6):
            self.x0.setVisible(True)
            self.x1.setVisible(True)
            self.x2.setVisible(True)
            self.x3.setVisible(True)
            self.x4.setVisible(True)
            self.x6.setVisible(True)
            self.x7.setVisible(False)
            self.x8.setVisible(False)
            self.x9.setVisible(False)
            
            self.y0.setVisible(True)
            self.y1.setVisible(True)
            self.y2.setVisible(True)
            self.y3.setVisible(True)
            self.y4.setVisible(True)
            self.y5.setVisible(True)
            self.y6.setVisible(False)
            self.y7.setVisible(False)
            self.y8.setVisible(False)
            self.y9.setVisible(False)
            
            self.labelx0.setVisible(True)
            self.labelx1.setVisible(True)
            self.labelx2.setVisible(True)
            self.labelx3.setVisible(True)
            self.labelx4.setVisible(True)
            self.labelx5.setVisible(True)
            self.labelx6.setVisible(False)
            self.labelx7.setVisible(False)
            self.labelx8.setVisible(False)
            self.labelx9.setVisible(False)
            
            
            self.labely0.setVisible(True)
            self.labely1.setVisible(True)
            self.labely2.setVisible(True)
            self.labely3.setVisible(True)
            self.labely4.setVisible(True)
            self.labely5.setVisible(True)
            self.labely6.setVisible(False)
            self.labely7.setVisible(False)
            self.labely8.setVisible(False)
            self.labely9.setVisible(False)
        elif (n==7):
            self.x0.setVisible(True)
            self.x1.setVisible(True)
            self.x2.setVisible(True)
            self.x3.setVisible(True)
            self.x4.setVisible(True)
            self.x5.setVisible(True)
            self.x6.setVisible(True)
            self.x7.setVisible(False)
            self.x8.setVisible(False)
            self.x9.setVisible(False)
            
            self.y0.setVisible(True)
            self.y1.setVisible(True)
            self.y2.setVisible(True)
            self.y3.setVisible(True)
            self.y4.setVisible(True)
            self.y5.setVisible(True)
            self.y6.setVisible(True)
            self.y7.setVisible(False)
            self.y8.setVisible(False)
            self.y9.setVisible(False)
            
            self.labelx0.setVisible(True)
            self.labelx1.setVisible(True)
            self.labelx2.setVisible(True)
            self.labelx3.setVisible(True)
            self.labelx4.setVisible(True)
            self.labelx5.setVisible(True)
            self.labelx6.setVisible(True)
            self.labelx7.setVisible(False)
            self.labelx8.setVisible(False)
            self.labelx9.setVisible(False)
            
            self.labely0.setVisible(True)
            self.labely1.setVisible(True)
            self.labely2.setVisible(True)
            self.labely3.setVisible(True)
            self.labely4.setVisible(True)
            self.labely6.setVisible(True)
            self.labely7.setVisible(False)
            self.labely8.setVisible(False)
            self.labely9.setVisible(False)
        elif (n==8):
            self.x0.setVisible(True)
            self.x1.setVisible(True)
            self.x2.setVisible(True)
            self.x3.setVisible(True)
            self.x4.setVisible(True)
            self.x5.setVisible(True)
            self.x6.setVisible(True)
            self.x7.setVisible(True)
            self.x8.setVisible(False)
            self.x9.setVisible(False)
            
            self.y0.setVisible(True)
            self.y1.setVisible(True)
            self.y2.setVisible(True)
            self.y3.setVisible(True)
            self.y4.setVisible(True)
            self.y5.setVisible(True)
            self.y6.setVisible(True)
            self.y7.setVisible(True)
            self.y8.setVisible(False)
            self.y9.setVisible(False)
            
            self.labelx0.setVisible(True)
            self.labelx1.setVisible(True)
            self.labelx2.setVisible(True)
            self.labelx3.setVisible(True)
            self.labelx4.setVisible(True)
            self.labelx5.setVisible(True)
            self.labelx6.setVisible(True)
            self.labelx7.setVisible(True)
            self.labelx8.setVisible(False)
            self.labelx9.setVisible(False)
            
            self.labely0.setVisible(True)
            self.labely1.setVisible(True)
            self.labely2.setVisible(True)
            self.labely3.setVisible(True)
            self.labely4.setVisible(True)
            self.labely6.setVisible(True)
            self.labely7.setVisible(True)
            self.labely8.setVisible(False)
            self.labely9.setVisible(False)
        elif (n==9):
            self.x0.setVisible(True)
            self.x1.setVisible(True)
            self.x2.setVisible(True)
            self.x3.setVisible(True)
            self.x4.setVisible(True)
            self.x5.setVisible(True)
            self.x6.setVisible(True)
            self.x7.setVisible(True)
            self.x8.setVisible(True)
            self.x9.setVisible(False)
            
            
            self.y0.setVisible(True)
            self.y1.setVisible(True)
            self.y2.setVisible(True)
            self.y3.setVisible(True)
            self.y4.setVisible(True)
            self.y5.setVisible(True)
            self.y6.setVisible(True)
            self.y7.setVisible(True)
            self.y8.setVisible(True)
            self.y9.setVisible(False)
            
            
            self.labelx0.setVisible(True)
            self.labelx1.setVisible(True)
            self.labelx2.setVisible(True)
            self.labelx3.setVisible(True)
            self.labelx4.setVisible(True)
            self.labelx5.setVisible(True)
            self.labelx6.setVisible(True)
            self.labelx7.setVisible(True)
            self.labelx8.setVisible(True)
            self.labelx9.setVisible(False)
            
            self.labely0.setVisible(True)
            self.labely1.setVisible(True)
            self.labely2.setVisible(True)
            self.labely3.setVisible(True)
            self.labely4.setVisible(True)
            self.labely5.setVisible(True)
            self.labely6.setVisible(True)
            self.labely7.setVisible(True)
            self.labely8.setVisible(True)
            self.labely9.setVisible(False)
        elif (n==10):
            self.x0.setVisible(True)
            self.x1.setVisible(True)
            self.x2.setVisible(True)
            self.x3.setVisible(True)
            self.x4.setVisible(True)
            self.x5.setVisible(True)
            self.x6.setVisible(True)
            self.x7.setVisible(True)
            self.x8.setVisible(True)
            self.x9.setVisible(True)
            
            
            self.y0.setVisible(True)
            self.y1.setVisible(True)
            self.y2.setVisible(True)
            self.y3.setVisible(True)
            self.y4.setVisible(True)
            self.y5.setVisible(True)
            self.y6.setVisible(True)
            self.y7.setVisible(True)
            self.y8.setVisible(True)
            self.y9.setVisible(True)
            
            
            self.labelx0.setVisible(True)
            self.labelx1.setVisible(True)
            self.labelx2.setVisible(True)
            self.labelx3.setVisible(True)
            self.labelx4.setVisible(True)
            self.labelx5.setVisible(True)
            self.labelx6.setVisible(True)
            self.labelx7.setVisible(True)
            self.labelx8.setVisible(True)
            self.labelx9.setVisible(True)
            
            self.labely0.setVisible(True)
            self.labely1.setVisible(True)
            self.labely2.setVisible(True)
            self.labely3.setVisible(True)
            self.labely4.setVisible(True)
            self.labely5.setVisible(True)
            self.labely6.setVisible(True)
            self.labely7.setVisible(True)
            self.labely8.setVisible(True)
            self.labely9.setVisible(True)
        
            
            
            
            
            
    def calcular(self):
        n = (self.nBox.value())
       
        #declaracion de las listas con las que se calcuara el polinomio
        listax = [] 
        listay = []
        
        if (self.x0.text()!=""):
            listax.append(float(self.x0.text()))
        if (self.x1.text()!=""):
            listax.append(float(self.x1.text()))
        if (self.x2.text()!=""):
            listax.append(float(self.x2.text()))
        if (self.x3.text()!=""):
            listax.append(float(self.x3.text()))
        if (self.x4.text()!=""):
            listax.append(float(self.x4.text()))
        if (self.x5.text()!=""):
            listax.append(float(self.x5.text()))
        if (self.x6.text()!=""):
            listax.append(float(self.x6.text()))
        if (self.x4.text()!=""):
            listax.append(float(self.x7.text()))
        if (self.x4.text()!=""):
            listax.append(float(self.x8.text()))
        if (self.x4.text()!=""):
            listax.append(float(self.x9.text()))

        if (self.y0.text()!=""):
            listay.append(float(self.y0.text()))
        if (self.y1.text()!=""):
            listay.append(float(self.y1.text()))
        if (self.y2.text()!=""):
            listay.append(float(self.y2.text()))
        if (self.y3.text()!=""):
            listay.append(float(self.y3.text()))
        if (self.y4.text()!=""):
            listay.append(float(self.y4.text()))
        if (self.y5.text()!=""):
            listay.append(float(self.y5.text()))
        if (self.y6.text()!=""):
            listay.append(float(self.y6.text()))
        if (self.y7.text()!=""):
            listay.append(float(self.y7.text()))
        if (self.y8.text()!=""):
            listay.append(float(self.y8.text()))
        if (self.y9.text()!=""):
            listay.append(float(self.y9.text()))
        
        x = np.array(listax)
        y = np.array(listay)
        #da el polinomio
        poly = lagrange(x,y)
        poly_st= str(poly)
        print("el polinomio es: ",poly)
         
        self.resultTxt.setText(poly_st)
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()

class Simpson(QDialog):
    
    def __init__(self, parent=None):
        super(Simpson, self).__init__(parent)
        loadUi('simpson.ui', self)
        
        self.crearBtn.clicked.connect(self.visibilidad)
        self.calcBtn.clicked.connect(self.calcular)
        self.inicioBtn.clicked.connect(self.abrirVentanaPrincipal)
        self.x0.setVisible(False)
        self.x1.setVisible(False)
        self.x2.setVisible(False)
        self.x3.setVisible(False)
        self.x4.setVisible(False)
        self.x5.setVisible(False)
        self.x6.setVisible(False)
        self.x7.setVisible(False)
        self.x8.setVisible(False)
        self.x9.setVisible(False)
        self.y0.setVisible(False)
        self.y1.setVisible(False)
        self.y2.setVisible(False)
        self.y3.setVisible(False)
        self.y4.setVisible(False)
        self.y5.setVisible(False)
        self.y6.setVisible(False)
        self.y7.setVisible(False)
        self.y8.setVisible(False)
        self.y9.setVisible(False)
        self.labelx0.setVisible(False)
        self.labelx1.setVisible(False)
        self.labelx2.setVisible(False)
        self.labelx3.setVisible(False)
        self.labelx4.setVisible(False)
        self.labelx5.setVisible(False)
        self.labelx6.setVisible(False)
        self.labelx7.setVisible(False)
        self.labelx8.setVisible(False)
        self.labelx9.setVisible(False)
        
        
        self.labely0.setVisible(False)
        self.labely1.setVisible(False)
        self.labely2.setVisible(False)
        self.labely3.setVisible(False)
        self.labely4.setVisible(False)
        self.labely5.setVisible(False)
        self.labely6.setVisible(False)
        self.labely7.setVisible(False)
        self.labely8.setVisible(False)
        self.labely9.setVisible(False)
        


        
    #aqui van las dunciones
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()
    def visibilidad(self):
        n = (self.nBox.value())
       
        if (n==2):
            
            self.x0.setVisible(True)
            self.x1.setVisible(True)
            self.x2.setVisible(False)
            self.x3.setVisible(False)
            self.x4.setVisible(False)
            self.x5.setVisible(False)
            self.x6.setVisible(False)
            self.x7.setVisible(False)
            self.x8.setVisible(False)
            self.x9.setVisible(False)
            
            
            self.y0.setVisible(True)
            self.y1.setVisible(True)
            self.y2.setVisible(False)
            self.y3.setVisible(False)
            self.y4.setVisible(False)
            self.y5.setVisible(False)
            self.y6.setVisible(False)
            self.y7.setVisible(False)
            self.y8.setVisible(False)
            self.y9.setVisible(False)
            
            self.labelx0.setVisible(True)
            self.labelx1.setVisible(True)
            self.labelx2.setVisible(False)
            self.labelx3.setVisible(False)
            self.labelx4.setVisible(False)
            self.labelx5.setVisible(False)
            self.labelx6.setVisible(False)
            self.labelx7.setVisible(False)
            self.labelx8.setVisible(False)
            self.labelx9.setVisible(False)
            
            self.labely0.setVisible(True)
            self.labely1.setVisible(True)
            self.labely2.setVisible(False)
            self.labely3.setVisible(False)
            self.labely4.setVisible(False)
            self.labely5.setVisible(False)
            self.labely6.setVisible(False)
            self.labely7.setVisible(False)
            self.labely8.setVisible(False)
            self.labely9.setVisible(False)
        elif (n==3):
            self.x0.setVisible(True)
            self.x1.setVisible(True)
            self.x2.setVisible(True)
            self.x3.setVisible(False)
            self.x4.setVisible(False)
            self.x5.setVisible(False)
            self.x6.setVisible(False)
            self.x7.setVisible(False)
            self.x8.setVisible(False)
            self.x9.setVisible(False)
            
            
            
            self.y0.setVisible(True)
            self.y1.setVisible(True)
            self.y2.setVisible(True)
            self.y3.setVisible(False)
            self.y4.setVisible(False)
            self.y5.setVisible(False)
            
            self.y6.setVisible(False)
            self.y7.setVisible(False)
            self.y8.setVisible(False)
            self.y9.setVisible(False)
            
            self.labelx0.setVisible(True)
            self.labelx1.setVisible(True)
            self.labelx2.setVisible(True)
            self.labelx3.setVisible(False)
            self.labelx4.setVisible(False)
            self.labelx5.setVisible(False)
            self.labelx6.setVisible(False)
            self.labelx7.setVisible(False)
            self.labelx8.setVisible(False)
            self.labelx9.setVisible(False)
            self.labely0.setVisible(True)
            self.labely1.setVisible(True)
            self.labely2.setVisible(True)
            self.labely3.setVisible(False)
            self.labely4.setVisible(False)
            self.labely5.setVisible(False)
            self.labely6.setVisible(False)
            self.labely7.setVisible(False)
            self.labely8.setVisible(False)
            self.labely9.setVisible(False)
        elif(n==4):
            self.x0.setVisible(True)
            self.x1.setVisible(True)
            self.x2.setVisible(True)
            self.x3.setVisible(True)
            self.x4.setVisible(False)
            self.x6.setVisible(False)
            self.x7.setVisible(False)
            self.x8.setVisible(False)
            self.x9.setVisible(False)
            
            self.y0.setVisible(True)
            self.y1.setVisible(True)
            self.y2.setVisible(True)
            self.y3.setVisible(True)
            self.y4.setVisible(False)
            self.y5.setVisible(False)
            self.y6.setVisible(False)
            self.y7.setVisible(False)
            self.y8.setVisible(False)
            self.y9.setVisible(False)
            
            self.labelx0.setVisible(True)
            self.labelx1.setVisible(True)
            self.labelx2.setVisible(True)
            self.labelx3.setVisible(True)
            self.labelx4.setVisible(False)
            self.labelx5.setVisible(False)
            self.labelx6.setVisible(False)
            self.labelx7.setVisible(False)
            self.labelx8.setVisible(False)
            self.labelx9.setVisible(False)
            
            self.labely0.setVisible(True)
            self.labely1.setVisible(True)
            self.labely2.setVisible(True)
            self.labely3.setVisible(True)
            self.labely4.setVisible(False)
            self.labely5.setVisible(False)
            self.labely6.setVisible(False)
            self.labely7.setVisible(False)
            self.labely8.setVisible(False)
            self.labely9.setVisible(False)
        elif (n==5):
            self.x0.setVisible(True)
            self.x1.setVisible(True)
            self.x2.setVisible(True)
            self.x3.setVisible(True)
            self.x4.setVisible(True)
            self.x6.setVisible(False)
            self.x7.setVisible(False)
            self.x8.setVisible(False)
            self.x9.setVisible(False)
            
            self.y0.setVisible(True)
            self.y1.setVisible(True)
            self.y2.setVisible(True)
            self.y3.setVisible(True)
            self.y4.setVisible(True)
            self.y5.setVisible(False)
            self.y6.setVisible(False)
            self.y7.setVisible(False)
            self.y8.setVisible(False)
            self.y9.setVisible(False)
            
            self.labelx0.setVisible(True)
            self.labelx1.setVisible(True)
            self.labelx2.setVisible(True)
            self.labelx3.setVisible(True)
            self.labelx4.setVisible(True)
            self.labelx5.setVisible(False)
            self.labelx6.setVisible(False)
            self.labelx7.setVisible(False)
            self.labelx8.setVisible(False)
            self.labelx9.setVisible(False)
            
            self.labely0.setVisible(True)
            self.labely1.setVisible(True)
            self.labely2.setVisible(True)
            self.labely3.setVisible(True)
            self.labely4.setVisible(True)
            self.labely6.setVisible(False)
            self.labely7.setVisible(False)
            self.labely8.setVisible(False)
            self.labely9.setVisible(False)
        elif (n==6):
            self.x0.setVisible(True)
            self.x1.setVisible(True)
            self.x2.setVisible(True)
            self.x3.setVisible(True)
            self.x4.setVisible(True)
            self.x6.setVisible(True)
            self.x7.setVisible(False)
            self.x8.setVisible(False)
            self.x9.setVisible(False)
            
            self.y0.setVisible(True)
            self.y1.setVisible(True)
            self.y2.setVisible(True)
            self.y3.setVisible(True)
            self.y4.setVisible(True)
            self.y5.setVisible(True)
            self.y6.setVisible(False)
            self.y7.setVisible(False)
            self.y8.setVisible(False)
            self.y9.setVisible(False)
            
            self.labelx0.setVisible(True)
            self.labelx1.setVisible(True)
            self.labelx2.setVisible(True)
            self.labelx3.setVisible(True)
            self.labelx4.setVisible(True)
            self.labelx5.setVisible(True)
            self.labelx6.setVisible(False)
            self.labelx7.setVisible(False)
            self.labelx8.setVisible(False)
            self.labelx9.setVisible(False)
            
            
            self.labely0.setVisible(True)
            self.labely1.setVisible(True)
            self.labely2.setVisible(True)
            self.labely3.setVisible(True)
            self.labely4.setVisible(True)
            self.labely5.setVisible(True)
            self.labely6.setVisible(False)
            self.labely7.setVisible(False)
            self.labely8.setVisible(False)
            self.labely9.setVisible(False)
        elif (n==7):
            self.x0.setVisible(True)
            self.x1.setVisible(True)
            self.x2.setVisible(True)
            self.x3.setVisible(True)
            self.x4.setVisible(True)
            self.x5.setVisible(True)
            self.x6.setVisible(True)
            self.x7.setVisible(False)
            self.x8.setVisible(False)
            self.x9.setVisible(False)
            
            self.y0.setVisible(True)
            self.y1.setVisible(True)
            self.y2.setVisible(True)
            self.y3.setVisible(True)
            self.y4.setVisible(True)
            self.y5.setVisible(True)
            self.y6.setVisible(True)
            self.y7.setVisible(False)
            self.y8.setVisible(False)
            self.y9.setVisible(False)
            
            self.labelx0.setVisible(True)
            self.labelx1.setVisible(True)
            self.labelx2.setVisible(True)
            self.labelx3.setVisible(True)
            self.labelx4.setVisible(True)
            self.labelx5.setVisible(True)
            self.labelx6.setVisible(True)
            self.labelx7.setVisible(False)
            self.labelx8.setVisible(False)
            self.labelx9.setVisible(False)
            
            self.labely0.setVisible(True)
            self.labely1.setVisible(True)
            self.labely2.setVisible(True)
            self.labely3.setVisible(True)
            self.labely4.setVisible(True)
            self.labely6.setVisible(True)
            self.labely7.setVisible(False)
            self.labely8.setVisible(False)
            self.labely9.setVisible(False)
        elif (n==8):
            self.x0.setVisible(True)
            self.x1.setVisible(True)
            self.x2.setVisible(True)
            self.x3.setVisible(True)
            self.x4.setVisible(True)
            self.x5.setVisible(True)
            self.x6.setVisible(True)
            self.x7.setVisible(True)
            self.x8.setVisible(False)
            self.x9.setVisible(False)
            
            self.y0.setVisible(True)
            self.y1.setVisible(True)
            self.y2.setVisible(True)
            self.y3.setVisible(True)
            self.y4.setVisible(True)
            self.y5.setVisible(True)
            self.y6.setVisible(True)
            self.y7.setVisible(True)
            self.y8.setVisible(False)
            self.y9.setVisible(False)
            
            self.labelx0.setVisible(True)
            self.labelx1.setVisible(True)
            self.labelx2.setVisible(True)
            self.labelx3.setVisible(True)
            self.labelx4.setVisible(True)
            self.labelx5.setVisible(True)
            self.labelx6.setVisible(True)
            self.labelx7.setVisible(True)
            self.labelx8.setVisible(False)
            self.labelx9.setVisible(False)
            
            self.labely0.setVisible(True)
            self.labely1.setVisible(True)
            self.labely2.setVisible(True)
            self.labely3.setVisible(True)
            self.labely4.setVisible(True)
            self.labely6.setVisible(True)
            self.labely7.setVisible(True)
            self.labely8.setVisible(False)
            self.labely9.setVisible(False)
        elif (n==9):
            self.x0.setVisible(True)
            self.x1.setVisible(True)
            self.x2.setVisible(True)
            self.x3.setVisible(True)
            self.x4.setVisible(True)
            self.x5.setVisible(True)
            self.x6.setVisible(True)
            self.x7.setVisible(True)
            self.x8.setVisible(True)
            self.x9.setVisible(False)
            
            
            self.y0.setVisible(True)
            self.y1.setVisible(True)
            self.y2.setVisible(True)
            self.y3.setVisible(True)
            self.y4.setVisible(True)
            self.y5.setVisible(True)
            self.y6.setVisible(True)
            self.y7.setVisible(True)
            self.y8.setVisible(True)
            self.y9.setVisible(False)
            
            
            self.labelx0.setVisible(True)
            self.labelx1.setVisible(True)
            self.labelx2.setVisible(True)
            self.labelx3.setVisible(True)
            self.labelx4.setVisible(True)
            self.labelx5.setVisible(True)
            self.labelx6.setVisible(True)
            self.labelx7.setVisible(True)
            self.labelx8.setVisible(True)
            self.labelx9.setVisible(False)
            
            self.labely0.setVisible(True)
            self.labely1.setVisible(True)
            self.labely2.setVisible(True)
            self.labely3.setVisible(True)
            self.labely4.setVisible(True)
            self.labely5.setVisible(True)
            self.labely6.setVisible(True)
            self.labely7.setVisible(True)
            self.labely8.setVisible(True)
            self.labely9.setVisible(False)
        elif (n==10):
            self.x0.setVisible(True)
            self.x1.setVisible(True)
            self.x2.setVisible(True)
            self.x3.setVisible(True)
            self.x4.setVisible(True)
            self.x5.setVisible(True)
            self.x6.setVisible(True)
            self.x7.setVisible(True)
            self.x8.setVisible(True)
            self.x9.setVisible(True)
            
            
            self.y0.setVisible(True)
            self.y1.setVisible(True)
            self.y2.setVisible(True)
            self.y3.setVisible(True)
            self.y4.setVisible(True)
            self.y5.setVisible(True)
            self.y6.setVisible(True)
            self.y7.setVisible(True)
            self.y8.setVisible(True)
            self.y9.setVisible(True)
            
            
            self.labelx0.setVisible(True)
            self.labelx1.setVisible(True)
            self.labelx2.setVisible(True)
            self.labelx3.setVisible(True)
            self.labelx4.setVisible(True)
            self.labelx5.setVisible(True)
            self.labelx6.setVisible(True)
            self.labelx7.setVisible(True)
            self.labelx8.setVisible(True)
            self.labelx9.setVisible(True)
            
            self.labely0.setVisible(True)
            self.labely1.setVisible(True)
            self.labely2.setVisible(True)
            self.labely3.setVisible(True)
            self.labely4.setVisible(True)
            self.labely5.setVisible(True)
            self.labely6.setVisible(True)
            self.labely7.setVisible(True)
            self.labely8.setVisible(True)
            self.labely9.setVisible(True)
        
            
            
            
            
            
    def calcular(self):
        n = (self.nBox.value())
       
            
        listax = [] 
        listay = []
        if (self.x0.text()!=""):
            listax.append(float(self.x0.text()))
        if (self.x1.text()!=""):
            listax.append(float(self.x1.text()))
        if (self.x2.text()!=""):
            listax.append(float(self.x2.text()))
        if (self.x3.text()!=""):
            listax.append(float(self.x3.text()))
        if (self.x4.text()!=""):
            listax.append(float(self.x4.text()))
        if (self.x5.text()!=""):
            listax.append(float(self.x5.text()))
        if (self.x6.text()!=""):
            listax.append(float(self.x6.text()))
        if (self.x7.text()!=""):
            listax.append(float(self.x7.text()))
        if (self.x8.text()!=""):
            listax.append(float(self.x8.text()))
        if (self.x9.text()!=""):
            listax.append(float(self.x9.text()))

        if (self.y0.text()!=""):
            listay.append(float(self.y0.text()))
        if (self.y1.text()!=""):
            listay.append(float(self.y1.text()))
        if (self.y2.text()!=""):
            listay.append(float(self.y2.text()))
        if (self.y3.text()!=""):
            listay.append(float(self.y3.text()))
        if (self.y4.text()!=""):
            listay.append(float(self.y4.text()))
        if (self.y5.text()!=""):
            listay.append(float(self.y5.text()))
        if (self.y6.text()!=""):
            listay.append(float(self.y6.text()))
        if (self.y7.text()!=""):
            listay.append(float(self.y7.text()))
        if (self.y8.text()!=""):
            listay.append(float(self.y8.text()))
        if (self.y9.text()!=""):
            listay.append(float(self.y9.text()))
        
        
        ##calcular h
        h = (listax[n-1] - listax[0])/(n-1)
        ##dividir h por 3
        k = h/3
        ##sumar los valores que no son multiplicados
        integral = listay[0]+listay[n-1]
        
        ##sumar a eso los valores multiplicados por 2 y 4
        for i in range (1,n-1):
            if (i%2==0):
                integral += 2*listay[i]
                
            else:
                integral += 4*listay[i]
                
        integral *= k
        
        resultado = "El valor de la ijtegral es" +str(integral)   
        self.resultTxt.setText(resultado)

class SimpsonFun(QDialog):
    
    def __init__(self, parent=None):
        super(SimpsonFun, self).__init__(parent)
        loadUi('simpsonFun.ui', self)
        
        self.calcBtn.clicked.connect(self.calculos)
        self.inicioBtn.clicked.connect(self.abrirVentanaPrincipal)
        
    #aqui van las dunciones
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()
    def calculos(self):
        def function(x):
        #el valor de x es con el    que se evaluara
            return (eval(fun))#en esta funcion
        #funcion dada por el usuario
        fun = (self.funcionTxt.toPlainText())
        interv = (self.nBox.value())
        limInf = float((self.limInfEdit.text()))
        limSup = float((self.limSupEdit.text()))
        
        h = (limSup-limInf)/interv 
        ##dividir h por 3
        k = h/3
        ##sumar los valores que no son multiplicados
        integral = function(limInf)+function(limSup)
        #print(integral)
        ##sumar a eso los valores multiplicados por 2 y 4
        if interv ==2:
            integral *=k
            integral_st = str(integral)
            self.resultadoTxt.setText(integral_st)
        else:
            for i in range (1,interv):#okaaay est amdre tiene sentido por que se tiene que multiplicar por los 3 valores claro que si
                if (i%2==0):
                    integral += 2*(function(limInf + h*i))
                    #print("multiplicado por 2",function(limInf + h*i))
                else:
                    integral += 4*(function(limInf + h*i))
                    #print("multiplicado por 4",integral)
            integral *= k ##aqui hice algo raro con el signo pero no me acuerdo por qué
            #print("La integral buscada es igual a: ", integral)## debe ir en a interfaz
            integral_st = str(integral)
            self.resultadoTxt.setText(integral_st)
        
class Trapecio(QDialog):
    
    def __init__(self, parent=None):
        super(Trapecio, self).__init__(parent)
        loadUi('trapecio.ui', self)
        
        self.calcBtn.clicked.connect(self.calculos)
        self.inicioBtn.clicked.connect(self.abrirVentanaPrincipal)
        
    #aqui van las dunciones
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()
    def calculos(self):
        
        
        def function(x):
        #el valor de x es con el    que se evaluara
            return (eval(fun))#en esta funcion
        #funcion dada por el usuario
        fun = (self.funcionTxt.toPlainText())
        n = (self.nBox.value())
        limInf = float((self.limInfEdit.text()))
        limSup = float((self.limSupEdit.text()))
        
        if n == 2:
            h = (limSup - limInf) / 2
            integral = (function(limInf) + function(limSup))
            integral *= h
        #de dos puntos nda mas, aun hay error en la de más puntos
            #solucionado
        ##esta es la forma ampliada del la regla del trapecio
        else :
            h = (limSup - limInf) / n
            integral = (function(limInf) + function(limSup))
            
            for i in range(1,n):
                integral += 2*(function(limInf + h * i))
            integral *= h/2
        integral_st = str(integral) 
        
        self.resultadoTxt.setText(integral_st)
class Newton(QDialog):
    def __init__(self, parent=None):
        super(Newton, self).__init__(parent)
        loadUi('newton.ui', self)
        
        self.crearBtn.clicked.connect(self.visibilidad)
        self.calcBtn.clicked.connect(self.calcular)
        self.inicioBtn.clicked.connect(self.abrirVentanaPrincipal)
        self.x0.setVisible(False)
        self.x1.setVisible(False)
        self.x2.setVisible(False)
        self.x3.setVisible(False)
        self.x4.setVisible(False)
        self.x5.setVisible(False)
        self.x6.setVisible(False)
        self.x7.setVisible(False)
        self.x8.setVisible(False)
        self.x9.setVisible(False)
        self.y0.setVisible(False)
        self.y1.setVisible(False)
        self.y2.setVisible(False)
        self.y3.setVisible(False)
        self.y4.setVisible(False)
        self.y5.setVisible(False)
        self.y6.setVisible(False)
        self.y7.setVisible(False)
        self.y8.setVisible(False)
        self.y9.setVisible(False)
        self.labelx0.setVisible(False)
        self.labelx1.setVisible(False)
        self.labelx2.setVisible(False)
        self.labelx3.setVisible(False)
        self.labelx4.setVisible(False)
        self.labelx5.setVisible(False)
        self.labelx6.setVisible(False)
        self.labelx7.setVisible(False)
        self.labelx8.setVisible(False)
        self.labelx9.setVisible(False)
        
        
        self.labely0.setVisible(False)
        self.labely1.setVisible(False)
        self.labely2.setVisible(False)
        self.labely3.setVisible(False)
        self.labely4.setVisible(False)
        self.labely5.setVisible(False)
        self.labely6.setVisible(False)
        self.labely7.setVisible(False)
        self.labely8.setVisible(False)
        self.labely9.setVisible(False)
        


        
    #aqui van las dunciones
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()
    def visibilidad(self):
        n = (self.nBox.value())
       
        if (n==2):
            
            self.x0.setVisible(True)
            self.x1.setVisible(True)
            self.x2.setVisible(False)
            self.x3.setVisible(False)
            self.x4.setVisible(False)
            self.x5.setVisible(False)
            self.x6.setVisible(False)
            self.x7.setVisible(False)
            self.x8.setVisible(False)
            self.x9.setVisible(False)
            
            
            self.y0.setVisible(True)
            self.y1.setVisible(True)
            self.y2.setVisible(False)
            self.y3.setVisible(False)
            self.y4.setVisible(False)
            self.y5.setVisible(False)
            self.y6.setVisible(False)
            self.y7.setVisible(False)
            self.y8.setVisible(False)
            self.y9.setVisible(False)
            
            self.labelx0.setVisible(True)
            self.labelx1.setVisible(True)
            self.labelx2.setVisible(False)
            self.labelx3.setVisible(False)
            self.labelx4.setVisible(False)
            self.labelx5.setVisible(False)
            self.labelx6.setVisible(False)
            self.labelx7.setVisible(False)
            self.labelx8.setVisible(False)
            self.labelx9.setVisible(False)
            
            self.labely0.setVisible(True)
            self.labely1.setVisible(True)
            self.labely2.setVisible(False)
            self.labely3.setVisible(False)
            self.labely4.setVisible(False)
            self.labely5.setVisible(False)
            self.labely6.setVisible(False)
            self.labely7.setVisible(False)
            self.labely8.setVisible(False)
            self.labely9.setVisible(False)
        elif (n==3):
            self.x0.setVisible(True)
            self.x1.setVisible(True)
            self.x2.setVisible(True)
            self.x3.setVisible(False)
            self.x4.setVisible(False)
            self.x5.setVisible(False)
            self.x6.setVisible(False)
            self.x7.setVisible(False)
            self.x8.setVisible(False)
            self.x9.setVisible(False)
            
            
            
            self.y0.setVisible(True)
            self.y1.setVisible(True)
            self.y2.setVisible(True)
            self.y3.setVisible(False)
            self.y4.setVisible(False)
            self.y5.setVisible(False)
            
            self.y6.setVisible(False)
            self.y7.setVisible(False)
            self.y8.setVisible(False)
            self.y9.setVisible(False)
            
            self.labelx0.setVisible(True)
            self.labelx1.setVisible(True)
            self.labelx2.setVisible(True)
            self.labelx3.setVisible(False)
            self.labelx4.setVisible(False)
            self.labelx5.setVisible(False)
            self.labelx6.setVisible(False)
            self.labelx7.setVisible(False)
            self.labelx8.setVisible(False)
            self.labelx9.setVisible(False)
            self.labely0.setVisible(True)
            self.labely1.setVisible(True)
            self.labely2.setVisible(True)
            self.labely3.setVisible(False)
            self.labely4.setVisible(False)
            self.labely5.setVisible(False)
            self.labely6.setVisible(False)
            self.labely7.setVisible(False)
            self.labely8.setVisible(False)
            self.labely9.setVisible(False)
        elif(n==4):
            self.x0.setVisible(True)
            self.x1.setVisible(True)
            self.x2.setVisible(True)
            self.x3.setVisible(True)
            self.x4.setVisible(False)
            self.x6.setVisible(False)
            self.x7.setVisible(False)
            self.x8.setVisible(False)
            self.x9.setVisible(False)
            
            self.y0.setVisible(True)
            self.y1.setVisible(True)
            self.y2.setVisible(True)
            self.y3.setVisible(True)
            self.y4.setVisible(False)
            self.y5.setVisible(False)
            self.y6.setVisible(False)
            self.y7.setVisible(False)
            self.y8.setVisible(False)
            self.y9.setVisible(False)
            
            self.labelx0.setVisible(True)
            self.labelx1.setVisible(True)
            self.labelx2.setVisible(True)
            self.labelx3.setVisible(True)
            self.labelx4.setVisible(False)
            self.labelx5.setVisible(False)
            self.labelx6.setVisible(False)
            self.labelx7.setVisible(False)
            self.labelx8.setVisible(False)
            self.labelx9.setVisible(False)
            
            self.labely0.setVisible(True)
            self.labely1.setVisible(True)
            self.labely2.setVisible(True)
            self.labely3.setVisible(True)
            self.labely4.setVisible(False)
            self.labely5.setVisible(False)
            self.labely6.setVisible(False)
            self.labely7.setVisible(False)
            self.labely8.setVisible(False)
            self.labely9.setVisible(False)
        elif (n==5):
            self.x0.setVisible(True)
            self.x1.setVisible(True)
            self.x2.setVisible(True)
            self.x3.setVisible(True)
            self.x4.setVisible(True)
            self.x6.setVisible(False)
            self.x7.setVisible(False)
            self.x8.setVisible(False)
            self.x9.setVisible(False)
            
            self.y0.setVisible(True)
            self.y1.setVisible(True)
            self.y2.setVisible(True)
            self.y3.setVisible(True)
            self.y4.setVisible(True)
            self.y5.setVisible(False)
            self.y6.setVisible(False)
            self.y7.setVisible(False)
            self.y8.setVisible(False)
            self.y9.setVisible(False)
            
            self.labelx0.setVisible(True)
            self.labelx1.setVisible(True)
            self.labelx2.setVisible(True)
            self.labelx3.setVisible(True)
            self.labelx4.setVisible(True)
            self.labelx5.setVisible(False)
            self.labelx6.setVisible(False)
            self.labelx7.setVisible(False)
            self.labelx8.setVisible(False)
            self.labelx9.setVisible(False)
            
            self.labely0.setVisible(True)
            self.labely1.setVisible(True)
            self.labely2.setVisible(True)
            self.labely3.setVisible(True)
            self.labely4.setVisible(True)
            self.labely6.setVisible(False)
            self.labely7.setVisible(False)
            self.labely8.setVisible(False)
            self.labely9.setVisible(False)
        elif (n==6):
            self.x0.setVisible(True)
            self.x1.setVisible(True)
            self.x2.setVisible(True)
            self.x3.setVisible(True)
            self.x4.setVisible(True)
            self.x6.setVisible(True)
            self.x7.setVisible(False)
            self.x8.setVisible(False)
            self.x9.setVisible(False)
            
            self.y0.setVisible(True)
            self.y1.setVisible(True)
            self.y2.setVisible(True)
            self.y3.setVisible(True)
            self.y4.setVisible(True)
            self.y5.setVisible(True)
            self.y6.setVisible(False)
            self.y7.setVisible(False)
            self.y8.setVisible(False)
            self.y9.setVisible(False)
            
            self.labelx0.setVisible(True)
            self.labelx1.setVisible(True)
            self.labelx2.setVisible(True)
            self.labelx3.setVisible(True)
            self.labelx4.setVisible(True)
            self.labelx5.setVisible(True)
            self.labelx6.setVisible(False)
            self.labelx7.setVisible(False)
            self.labelx8.setVisible(False)
            self.labelx9.setVisible(False)
            
            
            self.labely0.setVisible(True)
            self.labely1.setVisible(True)
            self.labely2.setVisible(True)
            self.labely3.setVisible(True)
            self.labely4.setVisible(True)
            self.labely5.setVisible(True)
            self.labely6.setVisible(False)
            self.labely7.setVisible(False)
            self.labely8.setVisible(False)
            self.labely9.setVisible(False)
        elif (n==7):
            self.x0.setVisible(True)
            self.x1.setVisible(True)
            self.x2.setVisible(True)
            self.x3.setVisible(True)
            self.x4.setVisible(True)
            self.x5.setVisible(True)
            self.x6.setVisible(True)
            self.x7.setVisible(False)
            self.x8.setVisible(False)
            self.x9.setVisible(False)
            
            self.y0.setVisible(True)
            self.y1.setVisible(True)
            self.y2.setVisible(True)
            self.y3.setVisible(True)
            self.y4.setVisible(True)
            self.y5.setVisible(True)
            self.y6.setVisible(True)
            self.y7.setVisible(False)
            self.y8.setVisible(False)
            self.y9.setVisible(False)
            
            self.labelx0.setVisible(True)
            self.labelx1.setVisible(True)
            self.labelx2.setVisible(True)
            self.labelx3.setVisible(True)
            self.labelx4.setVisible(True)
            self.labelx5.setVisible(True)
            self.labelx6.setVisible(True)
            self.labelx7.setVisible(False)
            self.labelx8.setVisible(False)
            self.labelx9.setVisible(False)
            
            self.labely0.setVisible(True)
            self.labely1.setVisible(True)
            self.labely2.setVisible(True)
            self.labely3.setVisible(True)
            self.labely4.setVisible(True)
            self.labely6.setVisible(True)
            self.labely7.setVisible(False)
            self.labely8.setVisible(False)
            self.labely9.setVisible(False)
        elif (n==8):
            self.x0.setVisible(True)
            self.x1.setVisible(True)
            self.x2.setVisible(True)
            self.x3.setVisible(True)
            self.x4.setVisible(True)
            self.x5.setVisible(True)
            self.x6.setVisible(True)
            self.x7.setVisible(True)
            self.x8.setVisible(False)
            self.x9.setVisible(False)
            
            self.y0.setVisible(True)
            self.y1.setVisible(True)
            self.y2.setVisible(True)
            self.y3.setVisible(True)
            self.y4.setVisible(True)
            self.y5.setVisible(True)
            self.y6.setVisible(True)
            self.y7.setVisible(True)
            self.y8.setVisible(False)
            self.y9.setVisible(False)
            
            self.labelx0.setVisible(True)
            self.labelx1.setVisible(True)
            self.labelx2.setVisible(True)
            self.labelx3.setVisible(True)
            self.labelx4.setVisible(True)
            self.labelx5.setVisible(True)
            self.labelx6.setVisible(True)
            self.labelx7.setVisible(True)
            self.labelx8.setVisible(False)
            self.labelx9.setVisible(False)
            
            self.labely0.setVisible(True)
            self.labely1.setVisible(True)
            self.labely2.setVisible(True)
            self.labely3.setVisible(True)
            self.labely4.setVisible(True)
            self.labely6.setVisible(True)
            self.labely7.setVisible(True)
            self.labely8.setVisible(False)
            self.labely9.setVisible(False)
        elif (n==9):
            self.x0.setVisible(True)
            self.x1.setVisible(True)
            self.x2.setVisible(True)
            self.x3.setVisible(True)
            self.x4.setVisible(True)
            self.x5.setVisible(True)
            self.x6.setVisible(True)
            self.x7.setVisible(True)
            self.x8.setVisible(True)
            self.x9.setVisible(False)
            
            
            self.y0.setVisible(True)
            self.y1.setVisible(True)
            self.y2.setVisible(True)
            self.y3.setVisible(True)
            self.y4.setVisible(True)
            self.y5.setVisible(True)
            self.y6.setVisible(True)
            self.y7.setVisible(True)
            self.y8.setVisible(True)
            self.y9.setVisible(False)
            
            
            self.labelx0.setVisible(True)
            self.labelx1.setVisible(True)
            self.labelx2.setVisible(True)
            self.labelx3.setVisible(True)
            self.labelx4.setVisible(True)
            self.labelx5.setVisible(True)
            self.labelx6.setVisible(True)
            self.labelx7.setVisible(True)
            self.labelx8.setVisible(True)
            self.labelx9.setVisible(False)
            
            self.labely0.setVisible(True)
            self.labely1.setVisible(True)
            self.labely2.setVisible(True)
            self.labely3.setVisible(True)
            self.labely4.setVisible(True)
            self.labely5.setVisible(True)
            self.labely6.setVisible(True)
            self.labely7.setVisible(True)
            self.labely8.setVisible(True)
            self.labely9.setVisible(False)
        elif (n==10):
            self.x0.setVisible(True)
            self.x1.setVisible(True)
            self.x2.setVisible(True)
            self.x3.setVisible(True)
            self.x4.setVisible(True)
            self.x5.setVisible(True)
            self.x6.setVisible(True)
            self.x7.setVisible(True)
            self.x8.setVisible(True)
            self.x9.setVisible(True)
            
            
            self.y0.setVisible(True)
            self.y1.setVisible(True)
            self.y2.setVisible(True)
            self.y3.setVisible(True)
            self.y4.setVisible(True)
            self.y5.setVisible(True)
            self.y6.setVisible(True)
            self.y7.setVisible(True)
            self.y8.setVisible(True)
            self.y9.setVisible(True)
            
            
            self.labelx0.setVisible(True)
            self.labelx1.setVisible(True)
            self.labelx2.setVisible(True)
            self.labelx3.setVisible(True)
            self.labelx4.setVisible(True)
            self.labelx5.setVisible(True)
            self.labelx6.setVisible(True)
            self.labelx7.setVisible(True)
            self.labelx8.setVisible(True)
            self.labelx9.setVisible(True)
            
            self.labely0.setVisible(True)
            self.labely1.setVisible(True)
            self.labely2.setVisible(True)
            self.labely3.setVisible(True)
            self.labely4.setVisible(True)
            self.labely5.setVisible(True)
            self.labely6.setVisible(True)
            self.labely7.setVisible(True)
            self.labely8.setVisible(True)
            self.labely9.setVisible(True)
        
            
            
            
            
            
    def calcular(self):
        n = (self.nBox.value())
       
            
        listax = [] 
        listay = []
        if (self.x0.text()!=""):
            listax.append(float(self.x0.text()))
        if (self.x1.text()!=""):
            listax.append(float(self.x1.text()))
        if (self.x2.text()!=""):
            listax.append(float(self.x2.text()))
        if (self.x3.text()!=""):
            listax.append(float(self.x3.text()))
        if (self.x4.text()!=""):
            listax.append(float(self.x4.text()))
        if (self.x5.text()!=""):
            listax.append(float(self.x5.text()))
        if (self.x6.text()!=""):
            listax.append(float(self.x6.text()))
        if (self.x4.text()!=""):
            listax.append(float(self.x7.text()))
        if (self.x4.text()!=""):
            listax.append(float(self.x8.text()))
        if (self.x4.text()!=""):
            listax.append(float(self.x9.text()))

        if (self.y0.text()!=""):
            listay.append(float(self.y0.text()))
        if (self.y1.text()!=""):
            listay.append(float(self.y1.text()))
        if (self.y2.text()!=""):
            listay.append(float(self.y2.text()))
        if (self.y3.text()!=""):
            listay.append(float(self.y3.text()))
        if (self.y4.text()!=""):
            listay.append(float(self.y4.text()))
        if (self.y5.text()!=""):
            listay.append(float(self.y5.text()))
        if (self.y6.text()!=""):
            listay.append(float(self.y6.text()))
        if (self.y7.text()!=""):
            listay.append(float(self.y7.text()))
        if (self.y8.text()!=""):
            listay.append(float(self.y8.text()))
        if (self.y9.text()!=""):
            listay.append(float(self.y9.text()))
        
        x = np.array(listax) # x coordinates in space
        y = np.array(listay)
        
        
        def getNDDCoeffs(x, y):
            """ Creates NDD pyramid and extracts coeffs """
            n = np.shape(y)[0]
            pyramid = np.zeros([n, n]) # Create a square matrix to hold pyramid
            pyramid[::,0] = y # first column is y
            for j in range(1,n):
                for i in range(n-j):
                    # create pyramid by updating other columns
                    pyramid[i][j] = (pyramid[i+1][j-1] - pyramid[i][j-1]) / (x[i+j] - x[i])
            return pyramid[0] # return first row
        
        coeff_vector = getNDDCoeffs(x, y)
        
        final_pol = np.polynomial.Polynomial([0.]) # our target polynomial
        n = coeff_vector.shape[0] # get number of coeffs
        for i in range(n):
            p = np.polynomial.Polynomial([1.]) # create a dummy polynomial
            for j in range(i):
                # each vector has degree of i
                # their terms are dependant on 'x' values
                p_temp = np.polynomial.Polynomial([-x[j], 1.]) # (x - x_j)
                p = np.polymul(p, p_temp) # multiply dummy with expression
            p *= coeff_vector[i] # apply coefficient
            final_pol = np.polyadd(final_pol, p) # add to target polynomial
        
        p = np.flip(final_pol[0].coef, axis=0)
        p_st = str(p)
        self.resultTxt.setText(p_st)
        
class PuntoFijo(QDialog):
    
    def __init__(self, parent=None):
        super(PuntoFijo, self).__init__(parent)
        loadUi('puntoFijo.ui', self)
        
        self.calcBtn.clicked.connect(self.calculos)
        self.inicioBtn.clicked.connect(self.abrirVentanaPrincipal)
        
    #aqui van las dunciones
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()
    def calculos(self):
        
        
        def function(x):
        #el valor de x es con el    que se evaluara
            return (eval(fun))#en esta funcion
        #funcion dada por el usuario
        fun = (self.funcionTxt.toPlainText())
        N = (self.nBox.value())
        x = float((self.limInfEdit.text()))
        tolerancia = float((self.limSupEdit.text()))
        er=100;
        i=0;
        print('#iteracion\tg(f(x))\t\terror')
        while(i<=N and er>=tolerancia):
            temp=x;
            x=eval(fun);
            er=abs((x-temp));
            print("%d\t\t%.4f\t\t%.4f"%(i,x,er));
            i+=1;
    
        x_st=str(x)
        er_st=str(er)
        sol_st = str("La solucion mas aproximada es:"+ x_st + "con un error de"+er_st)  
        
        self.resultadoTxt.setText(sol_st)
app = QApplication(sys.argv)
main = VentanaPrincipal()
main.show()
sys.exit(app.exec_())
