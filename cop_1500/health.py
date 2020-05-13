def get_age() -> float:
    """prompt for user to enter age, validates imput, returns a valid age in years"""

    print("Welcome to the health calculator, enter your age to get started")
    age = float(input())

    if age > 0 and age <= 125:
        # valid age
        return age
    else:
        # invalid age
        print("""
that is not a valid age, please try again.
try entering a whole number less than 126.
    """)
        return get_age()

def get_height() -> float:
    """prompt for user to enter hight, validates imput, returns a valid hight in inches"""

    height = float(input("""next we need your hight. this code is bad, so convert your hight into inches
    """))

    if height > 0:
        # valid hight
        return height
    else:
        #invalid hight
        print(""""
        invalid hight, please try that again.
        """)
        return get_height()

def get_weight() -> float:
    """prompt for user to enter weight, validates imput, returns a valid weight in pounds"""

    weight = float(input("""please input your weight in pounds
    """))

    if weight > 0:
        # valid hight
        return weight
    else:
        #invalid weight
        print("try again, that is not a valid weight")
        return get_weight


def bmi(weight : float, height : float) -> float:
    """calculates and returns BMI"""

    return 703 * weight / (height ** 2)

def bmi_level(bmi : float) -> str:
    """returns level defined by bmi value. levels are under weight, normal, overweight, and obese."""

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25.0:
        return "Normal weight"

    elif bmi < 30.0:
        return "Overweight"

    else:
        return "Obese"


#print(bmi_level(1))
#print(bmi_level(18.5))
#print(bmi_level(22))
#print(bmi_level(25))
#print(bmi_level(27))
#print(bmi_level(30))
#print(bmi_level(30.1))

height = get_height()
weight = get_weight()

bmi=bmi(weight,height)
print("Your BMI score is", bmi)
print("This suggests you are", bmi_level(bmi))