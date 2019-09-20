#!/usr/bin/env python3
import sys

max = -float("inf")

for arg in sys.argv[1:]:
    i = int(arg)
    if i>max:
        max = i

print(f"le plus grand entier est {max}")