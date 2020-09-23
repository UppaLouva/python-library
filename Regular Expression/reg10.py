import re
liste=["234GHY","FGB23","HHYT1","234X"]
for i in liste:
    s=re.match("[0-9]",i)
    if s:
        print(i)
