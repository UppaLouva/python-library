import re

liste = ["elma", "armut", "kiraz"]

for i in liste :

    nesne = re.search("kiraz", i)
    if nesne:
        print(nesne.group())

