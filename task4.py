# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 17:19:21 2020

Условие задачи:
Написать программу, которая генерирует в указанных пользователем границах: 
    ● случайное целое число, 
    ● случайное вещественное число, 
    ● случайный символ. 
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. 
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

@author: 1
"""

import random

bottom_edge_1 = float(input("Генерация случайного целого числа\nВведите первую границу диапазона "))
top_edge_1 = float(input("Введите вторую границу диапазона "))

bottom_edge_2 = float(input("Генерация случайного вещественного числа\nВведите первую границу диапазона "))
top_edge_2 = float(input("Введите вторую границу диапазона "))

bottom_edge_3 = input("Генерация случайного символа\nВведите первую границу диапазона ").lower()
top_edge_3 = input("Введите вторую границу диапазона ").lower()

if top_edge_1 > bottom_edge_1:
    random_1 = random.randint(bottom_edge_1,top_edge_1)
else:
    random_1 = random.randint(top_edge_1,bottom_edge_1)

if top_edge_2 > bottom_edge_2:
    random_2 = random.uniform(bottom_edge_2,top_edge_2)
else:
    random_2 = random.uniform(top_edge_2,bottom_edge_2)

if ord(top_edge_3) > ord(bottom_edge_3):
    random_3 = chr(random.randint(ord(bottom_edge_3),ord(top_edge_3)))
else:
    random_3 = chr(random.randint(ord(top_edge_3),ord(bottom_edge_3)))

print(f"Случайное целое число в диапазоне от {bottom_edge_1} до {top_edge_1} это {random_1}")

print(f"Случайное вещественное число в диапазоне от {bottom_edge_2} до {top_edge_2} это {round(random_2,2)}")

print(f"Случайный символ от '{bottom_edge_3}' до '{top_edge_3}' это '{random_3}'")