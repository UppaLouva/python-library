import re

liste=["ahmet","mehmet","ismet","met","kamil","kamuran"]
for i in liste:
    if re.match(".*met",i):
        print(i)
