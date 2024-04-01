def display_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

display_info(name="xyz",arg=50,city="A,B,C")