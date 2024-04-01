def sum(*args):
    result=0
    for num in args:
        result=result+num
    return result
print(sum(1,2,3,4,5,6))