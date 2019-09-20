#!/usr/bin/env python3
# -*- coding: utf-8 -*-


filename = input("nom du fichier contenant les données: ")

max = -float("inf")
with open(filename, "r") as f:
    for line in f:
        i = int(line)
        if i>max:
            max = i

print(f"le plus grand entier est {max}")

