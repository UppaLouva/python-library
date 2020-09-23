import re
from urllib.request import urlopen 
kelime = input("Aranmak istenen kelime:")
f = urlopen("https://www.yazbel.com/")
data =str(f.read())
nesne = re.search(kelime, data)
if nesne:
    print("kelime bulundu:",nesne.group())
else:
    print("Not matched:",kelime)
