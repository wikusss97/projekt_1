# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 12:30:13 2019

@author: lenovo
"""

import matplotlib.pyplot as plt
def wczytaj (wsp):
#wsp to ciąg znaków np 'xA'
    komunikat = 'Podaj ' + wsp 
    x = input(komunikat)
    
    while x.lstrip('-').replace('.', '', 1).isdigit() == 0:
        x = input(komunikat)   

    
    return float(x)
#
#xA = wczytaj ('xA')
#yA = wczytaj ('yA') 
#xB = wczytaj ('xB')
#yB = wczytaj ('yB')
#xC = wczytaj ('xC')
#yC = wczytaj ('yC')
#xD = wczytaj ('xD')
#yD = wczytaj ('yD')
#
#
#
def WyznaczeniePrzeciecia(xA,yA,xB,yB,xC,yC,xD,yD):
    
    
    dxAB = xB - xA
    dyAB = yB - yA
    
    dxCD = xD - xC
    dyCD = yD - yC
    
    dxAC = xC - xA
    dyAC = yC - yA
    
    if dxAB*dyCD - dyAB*dxCD == 0:
        odp='Proste są równoległe - brak punktów przecięcia'
        xP=None
        yP=None
        t1=None
        t2=None
    
    else:
        t1 = (dxAC*dyCD - dyAC*dxCD)/(dxAB*dyCD - dyAB*dxCD)
        t2 = (dxAC*dyAB - dyAC*dxAB)/(dxAB*dyCD - dyAB*dxCD)
        
        xP = round(xA + t1*dxAB,3)
        yP = round(yA + t1*dyAB,3)
       
        if (0<=t1 and t1<=1) and (0<=t2 and t2<=1):
           odp='Punkt leży na przecięciu obu prostych'
        elif (0<=t1 and t1<=1) and (t2<0 or t2>1):
           odp='Punkt leży na jednej prostej, oraz przedłużeniu drugiej'
           plt.plot([xC,xP],[yC,yP],':')
        elif (0<=t2 and t2<=1) and (t1<0 or t1>1): 
           odp='Punkt leży na jednej prostej, oraz przedłużeniu drugiej'
           plt.plot([xA, xP],[yA,yP],':')
        else:
           plt.plot([xA,xP],[yA,yP],':')
           plt.plot([xC,xP],[yC,yP],':')
           odp='Punkt leży na przedłużeniach obu prostych'
        
        zapisz_wynik = open("wynik.txt", "w")
        zapisz_wynik.write('xP='+str(xP)+'\n'+'yP='+str(yP))
        zapisz_wynik.close()  
        
    #    fig = plt.figure()    
        plt.plot([xA,xB],[yA,yB])
        plt.plot([xC,xD],[yC,yD])
        plt.scatter(xP,yP)
        plt.show
        
    return xP,yP, odp, t1, t2



#xA= 1186.00
#yA= 17962.69
#xB= 1144.74 
#yB= 18006.22
#xC= 1184.31
#yC= 18004.14
#xD= 1151.14
#yD= 17957.41
#print('P wzorcowe=> x=1168.210 \t y=17981.459')    

#W  yznaczeniePrzeciecia(xA,yA,xB,yB,xC,yC,xD,yD)

#WyznaczeniePrzeciecia(1,2,1,3,2,3,2,4)
#WyznaczeniePrzeciecia(1,1,5,4,3,8,7,2)    

    




























    