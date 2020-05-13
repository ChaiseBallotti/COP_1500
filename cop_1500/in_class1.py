def get_age():
    age = int(input("please enter your age: "))
    while (age < 0) or (age > 110):
        print("that is not a valid age")
        age = int(input("please enter your age: "))

    return age

def get_height():
    height = -1
    while (height <= 0):

        height = int(input("please enter your height: "))
        if (height <=0):
            print("that is not a valid height.")
    return height

def get_weight():
    valid_input = False
    while not valid_input:
        weight = int(input("please enter your weight: "))
        if (weight <= 0):
            print("that is not a valid weight.")
        else:
            valid_input = True
    return weight

def get_salary():
    while True:
        salary = int(input("please enter your salary: "))
        if salary >= 0:
            break
        else:
            print("that is not a valid salary.")

    return salary

#print(get_age())
#print(get_height())
#print(get_weight())
print(get_salary())


