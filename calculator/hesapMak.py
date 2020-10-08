class Calc():

    def __init__(self ,a ,b):
        self.value1 = a
        self.value2 = b

    def add(self):
        return self.value1 + self.value2

    def multiyply(self):
        return self.value1 * self.value2

    def divison(self):
        return self.value1 / self.value2

    def extraction(self):
        return self.value1 - self.value2

print("Choose add (1), multiply (2), divison (3), extraction (4)")
selection = input("select 1 or 2 or 3 or 4 : ")

v1 = int(input("first value : "))
v2 = int(input("second value: "))

c1 = Calc(v1 , v2)


if selection == "1":
    add_result = c1.add()
    print("Add : {}".format(add_result))
elif selection == "2":
    multiply_result = c1.multiyply()
    print("Multiply : {}".format(multiply_result))

elif selection == "3":
    try:
        divison_result = c1.divison()
        print("divison {}".format(divison_result))
        divison = v1 / v2
        divison == 0 
    except ZeroDivisionError:
        print("Divide by 0 error")        

elif selection == "4":
    extraction_result = c1.extraction()
    print("Extraction : {}".format(extraction_result))   
else:
    print("Error there is no proper selection")
