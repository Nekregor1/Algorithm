# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 19:37:10 2020

Условие задачи:
Вывести на экран коды и символы таблицы ASCII,
начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

@author: 1
"""

start = 32
ending = 127

for count in range(ending - start):
    if count % 10 == 0:
        print("\n")
        print(f"{start+count} - {chr(start+count)} ",end="")
    else:
        print(f"{start+count} - {chr(start+count)} ",end="")
    
