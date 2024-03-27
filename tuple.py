thislist=("PASS","FAIL","ATKT","PASS")
thislist1=list(thislist)
thislist1[0]="COVID"
thislist=tuple(thislist1)
print(thislist)
for i in thislist:
    print(i)
i=0
while i<len(thislist):
    print(thislist[i])
    i=i+1
c=thislist.count("PASS") 
print(c)
i=thislist.index("PASS")
print(i)
