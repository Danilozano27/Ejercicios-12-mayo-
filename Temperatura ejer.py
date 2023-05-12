# -*- coding: utf-8 -*-
"""
Created on Fri May 12 14:39:23 2023

@author: Dany
"""

import random

def generar_arreglo_tempereaturas():
    temperaturas = []
    for i in range(31):
        temperaturas.append(round(random.uniform(-40,40),2))
     
    print("TEMPERATURAS")
    print(temperaturas)
    return temperaturas 

def mostrar_datos(lista):
    suma = 0 
    calor = 0
    frio = lista[0]
    for i in lista:
        suma += i
        if i > calor:
            calor = i
        
        if i < frio:
            frio = i
     
    promedio = suma/len(lista)
    print("EL promedio de temperatura es: " + str(promedio)+"\n"+
          "El dia mas calido hubo una temperatura de: " +str(calor)+ "\n"+
          "El dia mas frio hubo una temperatura de: " +str(frio))

temp = generar_arreglo_tempereaturas()
mostrar_datos(temp)

