# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 20:09:11 2020

Условие задачи:
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

@author: 1
"""
a = float(input("Введите первое число "))
b = float(input("Введите второе число "))
c = float(input("Введите третье число "))

if a > b:
    if b > c:
        res = b
    else:
        if a > c:
            res = c
        else:
            res = a
else:
    if c > a:
        if b > c:
            res = c
        else:
            res = b
    else:
        res = a

print(f"Из чисел {a}, {b}, {c} средним является число {res}")