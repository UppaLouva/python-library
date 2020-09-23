import re
yeniliste=["saaat","saat","st"]
for i in yeniliste:
    if re.match("sa{3}t",i):
        print(i)
