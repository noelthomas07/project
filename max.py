#!/usr/bin/env python3
# -*- coding: utf-8 -*-


max = -float("inf")

print("entrer un entier par ligne, et finir par FIN")
while True:
  c = input()
  if  c=="FIN":
    break
  else:
    i = int(c)
    if i>max: max=i

print(f"le plus grand est {max}")