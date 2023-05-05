# -*- coding: utf-8 -*-
"""
Created on Fri May  5 12:36:06 2023

@author: Dany
"""
import random

def Generar_numero():
    aleatorio = random.randint(0, 999) 
    numero_formateado = "{:03d}".format(aleatorio)   
    return numero_formateado

def Capturar_numero():
    numero = input("Ingrese el numero que desea jugar: ") 
    return numero

def Capturar_valor():
    valor = int(input("Ingrese el valor que desea apostar: "))
    return valor

def Loteria (num_generado, num_apostado, valor):
    
    print("El numero ganador fue:", num_generado)
    
    
    if num_generado == num_apostado: 
        print("GANADOR!!!!!, Usted acerto las 3 cifras, su premio es de $", valor*1000)
        
    
    elif num_apostado[-1] == num_generado[-1]:
        print("LIBRÓ!!!!!, Usted acerto la ultima cifra, su premio es de $", valor*100)
        
    else:
        cont = 0
        for i in num_generado:
            if i in num_apostado:
                cont += 1
        
        if cont == 3:
            print("COMBINADO!!!!!, Usted acerto los numeros pero en otro orden, su premio es de $", valor*200)
            
        else:
            print("Lo siento, no ganaste nada. Mas suerte para la proxima")
    


Loteria(Generar_numero(), Capturar_numero(), Capturar_valor())
