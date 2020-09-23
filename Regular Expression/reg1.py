import re


def Main():
    line = "I think I understand regular expressions"

    matchResult = re.match('think', line, re.M|re.I)
    if matchResult:
        print("Match Found:"+matchResult.group())
    else:
        print("No match was Found")

    searchResult=re.search('think', line, re.M|re.I)
    if searchResult:

        print("Found: "+searchResult.group())

    else:
        print("Nothing Found")

Main()
