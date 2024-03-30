#passing Dict. to function
def myFunct(arg):
    for key in arg:
        print("key:",key,"value:",arg[key])

Dict={'a':1,'b':2,'c':3}

myFunct(Dict)