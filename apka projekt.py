# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:32:23 2019

@author: lenovo
"""
import sys

from PyQt5.QtWidgets import QLineEdit, QPushButton, QLabel, QWidget, QApplication, QGridLayout, QColorDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from zadanie5 import WyznaczeniePrzeciecia
from matplotlib.ticker import FormatStrFormatter
import webbrowser


class AppWindow(QWidget):
    
    def __init__(self):
        super().__init__()      #klasa nadrzędna (odniesienie do wyżej w hierrchii)
        self.title = "Wyznaczenie punktu przecięcia dwóch odcinków"
        self.initInterface()
        self.initWidgets()
        
    def initInterface(self):
        self.setWindowTitle(self.title)
        self.setGeometry(200,200,900,650) #geometria okienka
        self.show()    #wywietlanie okienka
        
    def initWidgets(self):
    
        #definiujemy guziki
        color = QPushButton("Wybierz kolor P",self)
        czysc = QPushButton('Czysć okna',self)
        oblicz = QPushButton('Oblicz',self)
        niespodzianka = QPushButton('Niespodzianka',self)
        
        s = QLabel('Podaj współrzędne ziom')
        zp = QLabel('Zapisuje wsp. P do pliku "wynik.txt"' )
        pg = QLabel('Przedstawienie graficzne')
        
        x = QLabel('X')             #tytuły kolumn
        y = QLabel('Y')
        zet = QLabel('Pkt')
        A = QLabel('A',self)        #miejsca na współrzędne
        B = QLabel('B',self)
        C = QLabel('C',self)
        D = QLabel('D',self)
        xP = QLabel('xP =',self)
        yP = QLabel('yP =',self)
        self.xEdit = QLineEdit()
        self.yEdit = QLineEdit()
        self.aEdit = QLineEdit()
        self.bEdit = QLineEdit()
        self.cEdit = QLineEdit()
        self.dEdit = QLineEdit()
        self.eEdit = QLineEdit()
        self.fEdit = QLineEdit()
        
        self.pEdit = QLineEdit()
        self.rEdit = QLineEdit()
        self.zEdit = QLineEdit()
        
        self.figure = plt.figure()          # miejsce do rysowania
        self.canvas = FigureCanvas(self.figure)
        
        #wywietlanie
        grid = QGridLayout()
        grid.addWidget(s,0,1)
        grid.addWidget(zet,1,0)
        grid.addWidget(x,1,1)
        grid.addWidget(y,1,2)
        grid.addWidget(A,2,0)  
        grid.addWidget(pg,15,1)
        grid.addWidget(zp,4,4)
         
        grid.addWidget(self.xEdit,2,1)
        grid.addWidget(self.yEdit,2,2) 
        grid.addWidget(B,3,0)     
        grid.addWidget(self.aEdit,3,1)
        grid.addWidget(self.bEdit,3,2)
        grid.addWidget(C,4,0)     
        grid.addWidget(self.cEdit,4,1)
        grid.addWidget(self.dEdit,4,2)
        grid.addWidget(D,5,0)     
        grid.addWidget(self.eEdit,5,1)
        grid.addWidget(self.fEdit,5,2)
        grid.addWidget(czysc,6,1,1,2)
        grid.addWidget(xP,2,3)     
        grid.addWidget(self.pEdit,2,4)
        grid.addWidget(yP,2,5)     
        grid.addWidget(self.rEdit,2,6)
        grid.addWidget(self.zEdit,3,4,1,4)
        
        grid.addWidget(oblicz,1,4,1,3)       
        grid.addWidget(color,15,4,1,1)
        grid.addWidget(niespodzianka,15,6,1,1)
        
        
        grid.addWidget(self.canvas,17,0,17,-1)  #rozciągłoć, -1 dociąga do końca od prawej strony 
        # 1 miejsce w którym wierszu, 2m w której kolumnie, 3 m(-1) rozciągnie nam wiersz do samego końca(do prawej aż)
        #4m rozciągnie nam po kolumnach. WSZYSTKO SIĘ DZIEJE NA NASZEJ ZAŁOŻONEJ SIATCE  
        
        self.setLayout(grid)
        
        oblicz.clicked.connect(self.oblicz)
        color.clicked.connect(self.zmienKolor)
        czysc.clicked.connect(self.mop)
        niespodzianka.clicked.connect(self.link)
        

    def link(self):
        webbrowser.open('https://youtu.be/MmtbHRsySZg?t=461')
    
    def zmienKolor(self):
            kolor = QColorDialog.getColor()
            print(kolor.name())
            if kolor.isValid():
                print(kolor.name)
                self.rysuj(kol=kolor.name())
                
    def sprawdzLiczbe(self, element):
            if element.text().lstrip('-').replace('.','',1).isdigit():
                return float(element.text())
            else:
                element.setFocus()
                return None
    
    def mop(self):
        self.xEdit.clear()
        self.yEdit.clear()
        self.aEdit.clear()
        self.bEdit.clear()
        self.cEdit.clear()
        self.dEdit.clear()
        self.eEdit.clear()
        self.fEdit.clear()
        self.pEdit.clear()
        self.rEdit.clear()
        self.zEdit.clear()
    
    

    def oblicz(self):
        self.rysuj()

    
    def rysuj(self, kol= 'red'):
        xA = self.sprawdzLiczbe(self.xEdit)
        yA = self.sprawdzLiczbe(self.yEdit)
        xB = self.sprawdzLiczbe(self.aEdit)
        yB = self.sprawdzLiczbe(self.bEdit)
        xC = self.sprawdzLiczbe(self.cEdit)
        yC = self.sprawdzLiczbe(self.dEdit)
        xD = self.sprawdzLiczbe(self.eEdit)
        yD = self.sprawdzLiczbe(self.fEdit)
        
        if None not in [xA,yA,xB,yB,xC,yC,xD,yD]:
#            self.xEdit.text().lstrip('-').replace('.','',1).idigit() and self.yEdit.text().lstrip('-').replac('.','',1).isdigit():
            xA = float(self.xEdit.text())
            yA = float(self.yEdit.text())
            xB = float(self.aEdit.text())
            yB = float(self.bEdit.text())
            xC = float(self.cEdit.text())
            yC = float(self.dEdit.text())
            xD = float(self.eEdit.text())
            yD = float(self.fEdit.text())
            
            xP, yP, odp, t1, t2 = WyznaczeniePrzeciecia(xA,yA,xB,yB,xC,yC,xD,yD)
            self.pEdit.setText(str(xP))
            self.rEdit.setText(str(yP))
            self.zEdit.setText(str(odp))
        
            self.figure.clear()    #czyscimy wykres przed wykonaniem nowego działania 
            ax = self.figure.add_subplot(111) #z przecinkami to samo wyjdzie
            ax.plot([yA, yB], [xA, xB], marker = 'o',label = 'linia AB')
            ax.plot([yC, yD], [xC, xD], marker = 'o',label = 'linia AC')
            
            if t1 is not None:
                ax.scatter(yP, xP, color = kol, label = 'Pkt P')
                if (0<=t1 and t1<=1) and (0<=t2 and t2<=1):
                   pass
                elif (0<=t1 and t1<=1) and (t2<0 or t2>1):
                   ax.plot([yC,yP],[xC,xP],':')
                elif (0<=t2 and t1<=1) and (t1<0 or t1>1):
                   ax.plot([yA, yP],[xA,xP],':')
                else:
                   ax.plot([yA,yP],[xA,xP],':')
                   ax.plot([yC,yP],[xC,xP],':')
            ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
            ax.xaxis.set_major_formatter(FormatStrFormatter('%.0f'))
            plt.legend()
            self.canvas.draw()   #Rysuje 'wyniki' na wykresie
            
    
def main():
        app = QApplication(sys.argv)
        window = AppWindow()
        app.exec_()

if __name__ == '__main__':
    main()
    




























