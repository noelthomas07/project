#!/usr/bin/env python3
#!/bin/env python3

from fonctions import readconf
import fonctions

conf_file = "minmax.conf"

config = readconf(conf_file)

if config["read"]=="keyboard":
    l = fonctions.read_from_keyboard
elif config["read"]=="arg":
    l = fonctions.read_from_cmdline
elif config["read"]=="file":
    if "datafile" in config:
        fonctions.read_from_file    
    else:
        print("Veuillez rentrer le nom du fichier")
        filename = input()
    l = fonctions.read_from_file(filename)

if (config["search"]=="min"):
    print(f"le min est {min(l)}")
elif (config["search"]=="max"):
    print(f"le max est {max(l)}")
else:
    print("valeur inconnue pour search")