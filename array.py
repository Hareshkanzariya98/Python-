cars=["Nano","nanoxl"]
cars[0]="xyz"
print(cars[0])
print(len(cars))
cars.append("Honda")
cars.append("Honda1")
cars.pop(0)
cars.remove("Honda1")
for x in cars:
    print(x)