##
## EPITECH PROJECT, 2022
## exo2.py
## File description:
## exo2
##

import re

txt = open("exo2/exo2.txt", "r")

m = re.findall(".* : {\n(?:.* = .*\n)*}", txt.read());
print(m);
