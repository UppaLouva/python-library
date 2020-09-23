import re
liste=["st","sat","saat","saaat","filanca"]
for i in liste:
    if re.match("sa+t",i):
        print(i)
