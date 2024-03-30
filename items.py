thisdict={
    "name":"name1",
    "course":"course1",
    "course":"course2"
}
x=thisdict.items()
print(x)
thisdict["result"]="pass"
print(x)
if "name" in thisdict:
    print("ATKT")