import re
yeniliste=["st","sat","saat","saaat","falanca"]
for i in yeniliste:
    if re.match("sa?t",i):
        print(i)
