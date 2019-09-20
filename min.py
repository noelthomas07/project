#!/usr/bin/env python3
# -*- coding: utf-8 -*-


min = float("inf")

print("entrer un entier par ligne, et finir par FIN")
while True:
  c = input()
  if  c=="FIN":
    break
  else:
    i = int(c)
    if i<min: min=i

print(f"le plus petit est {min}")