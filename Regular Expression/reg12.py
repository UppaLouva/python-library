import re
liste=["23bh56","TY76z","4Y7UZ","TYUDZ","34534","lagAY54"]
for i in liste:
    if re.match(".[0-9a-z]",i):
        print (i) 
