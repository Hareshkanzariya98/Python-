m1=int(input("enter marks 1:"))
m2=int(input("enter marks 2:"))
m3=int(input("enter marks 3:"))
if m1>=28 and m2>=28 and m3>=28:
    total=m1+m2+m3
    per=total/3
    result="PASS"
    if per>=80:
        grade="A"
    elif per>=70:
        grade="B"
    elif per>=60:
        grade="c"
    else:
        grade="D"
else:
    total=m1+m2+m3
    per="***"
    result="FAIL"
    grade="F"
print("Total:",total)
print("Percentage:",per)
print("Result:",result)
print("Grade:",grade)