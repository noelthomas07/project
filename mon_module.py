#!/usr/bin/env python3

import mon_module        # charge mon_module.py

print(ma_variable) # erreur !
print(mon_module.ma_variable)

ma_variable = 1
print(ma_variable)
print(mon_module.ma_variable)

print(mon_module.ma_fonction())

mon_module.ma_variable = 5
print(mon_module.ma_fonction())

from mon_module import ma_fonction

print(ma_fonction())

#from le_module import *