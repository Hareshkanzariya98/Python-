#ordered dict
from collections import OrderedDict
print("Normal Dict.\n")
d={}
d['b']=2
d['a']=1
d['c']=3
d['d']=4
for key,value in d.items():
    print(key,value)

print("ordered Dict.\n")
od=OrderedDict
od['b']=2
od['a']=1
od['c']=3
od['d']=4
for key,value in od.items():
    print(key,value)