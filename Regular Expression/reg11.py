import re
liste=["23BH56","TY76Z","4Y7UZ","TYUDZ","34534"]
for i in liste:
    s=re.search("TY[0-9][0-9]Z",i)
    if s:
        print(i)
    
