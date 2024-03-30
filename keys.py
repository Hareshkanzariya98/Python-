thisdict={
    "name":"a",
    "course":"2",
}
myKeys=list(thisdict.keys())
myKeys.sort()
sortedDict={i:thisdict[i] for i in myKeys}
print(sortedDict)