# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 18:46:32 2020

Условие задачи:
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

@author: 1
"""

N = int(input("Введите количество элементов ряда "))
def recursion(n):
    if n == 0:
        return 1
    else:
        return - 1/2*recursion(n-1)

my_sum = 0
for count in range(N):
    my_sum = my_sum + recursion(count)

print(f"Сумма элементов ряда {my_sum}")