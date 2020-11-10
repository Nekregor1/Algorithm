# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 19:26:27 2020

Условие задачи:
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
    
@author: 1
"""

N = int(input("Введите число "))

N1 = N
count_odd = 0
count_even = 0

while N1 > 0:
    temp = N1 % 10
    if temp % 2 == 0:
        count_even = count_even + 1
    else:
        count_odd = count_odd + 1
    N1 = N1 // 10


print(f"Количество четных цифр равно {count_even}, а нечетных - {count_odd}")