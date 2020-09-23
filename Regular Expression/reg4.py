import re 

text = 'abababbbbbabaaaab'
pattern='ab'

for match in re.findall(pattern,text):
    print ('Found {!r}'.format(match))


print(len(re.findall(pattern,text)))    
