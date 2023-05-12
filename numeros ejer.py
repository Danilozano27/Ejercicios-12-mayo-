# -*- coding: utf-8 -*-
"""
Created on Fri May 12 14:41:39 2023

@author: Dany
"""

import random

def generar_arreglo():
    arreglo = []
    for i in range(10):
        arreglo.append(random.randint(10,99))
     
    print("---------------- ARREGLO -----------------")
    print(arreglo)

    return arreglo 

def promedio(lista):
    suma = 0
    for i in lista:
        suma+=i
        
    return suma/len(lista)

def datos(lista):
    suma = 0
    pos_impares = []
    sum_80 = 0
    cant_80 = 0
    cant_menores_prom = 0
    sum_menores_prom = 0
    prom = promedio(lista)
    
    for i in range(len(lista)):
        if lista[i] < prom:
            sum_menores_prom += lista[i]
            cant_menores_prom += 1
            
        if lista[i] > 80:
            sum_80 += lista[i]
            cant_80 += 1
            
        if lista[i]%2 == 0:
            suma+=1
        else:
            pos_impares.append(i)
            
    print("El promedio de todo el arreglo es: "+ str(prom))
    print("La cantidad de numeros pares en el arreglo es: "+ str(suma))
    print("Las posiciones de los numeros impares son: "+ str(pos_impares))
    print("El promedio de numeros mayores a 80 es: "+ str(sum_80/cant_80))
    print("El promedio de numeros menores al promedio es: "+ str(sum_menores_prom/cant_menores_prom))
    

datos(generar_arreglo())