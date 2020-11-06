# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 19:08:17 2020
Условие задачи:
    Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
@author: 1
"""

letter1 = input("Введите первую букву ").lower()
letter2 = input("Введите вторую букву ").lower()

place1 = ord(letter1) - ord('a') + 1
place2 = ord(letter2) - ord('a') + 1
ltr = abs(place1 - place2)

print(f"\nБуква '{letter1}' находится на месте {place1}")
print(f"Буква '{letter2}' находится на месте {place2}")
print(f"Между буквами '{letter1}' и '{letter2}' ещё {ltr-1} букв(а)")


