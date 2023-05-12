# -*- coding: utf-8 -*-
"""
Created on Fri May 12 15:07:53 2023

@author: Dany
"""

import random

ventas_diarias = [random.randint(1000, 100000) for _ in range(7)]

mejores_dias = sorted(ventas_diarias, reverse=True)[:2]

peor_dia = min(ventas_diarias)

indices_mejores_dias = [i for i, venta in enumerate(ventas_diarias) if venta in mejores_dias]

indice_peor_dia = ventas_diarias.index(peor_dia)

dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
mejores_dias_nombre = [dias_semana[i] for i in indices_mejores_dias]
peor_dia_nombre = dias_semana[indice_peor_dia]

print("Ventas diarias:", ventas_diarias)
print("Los dos mejores días de la semana son:", mejores_dias_nombre)
print("El peor día de la semana es:", peor_dia_nombre)
