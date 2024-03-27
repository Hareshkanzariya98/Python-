thislist=["PASS","FAIL","ATKT"]
thislist.append("COVID PASS")
thislist.remove("FAIL")
print(len(thislist))
print(type(thislist))
print(thislist[0])
thislist[0]="FAIL"
print(thislist[0])
i=0
while i<len(thislist):
    print(thislist[i])
    i=i+1