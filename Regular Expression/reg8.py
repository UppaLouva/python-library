import re
liste=["özcan","özhan","ali","ayşe","özkan","kibariye"]
for i in liste:
    s=re.search("öz[chk]an",i)
    if s:
        print(s.group())
