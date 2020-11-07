# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 19:14:08 2020

Условие задачи:
Определить, является ли год, который ввел пользователь, високосным или не високосным.

@author: 1
"""

type_year = 0

# 0 - не високосный год, 1 - високосный

year = int(input("Введите год "))

if (year >= -45) and (year < -8):
    if (year % 3) == 0:
        type_year = 1
elif (year >= 8) and (year < 1582):
    if (year % 4) ==0:
        type_year = 1
elif year > 1582:
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                type_year = 1
        else:
            type_year = 1

if type_year == 0:
    print(f"Год {year} - не високосный!")
else:
    print(f"Год {year} - високосный!")
    
