import re
liste = ["özcan demir","esra","mehmet","esra baykal","esma","esma vanda"]
for i in liste:
    s=re.search("es[mr]a",i)
    if s:
        print(s.group())
