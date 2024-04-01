def call_by_value(x):
    x=x*2
    print("Function value Updated To:",x)

def call_reference(list):
    list.append("D")
    print("Function list Updated To:",list)

my_list=['E']
num=2
print("Number Before:",num)
call_by_value(num)
print("list Before:",my_list)
call_reference(my_list)