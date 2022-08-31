def weight_cal():
    '''
    To define your weight in SI Units to calculate BMI
    Input(s): By User through prompt
    Output(s): Weight in kilogram
    '''
    unit_w = input("Is your weight in kilograms or pounds? Please enter k or p: ")
    if unit_w == "p" or unit_w == "k":
        weight = float(input("Please enter your weight: "))
        if unit_w == "p":
            weight *= 0.453592
        elif unit_w == "k":
            weight = weight
        print("Your weight is {:.2f} kg")
        return weight
    else:
        print("Please try again, thank you.")

def height_cal():
    '''
    To define your height in SI Units to calculate BMI
    Input(s): By User through prompt
    Output(s): Height in metre
    '''
    unit_h = input("Is your height in centimeters or feet? Please enter m or ft: ")
    if unit_h == "m" or unit_h == "ft":
        height = float(input("Please enter your height: "))
        if unit_h == "ft":
            height *= 0.3048
        elif unit_h == "m":
            height = height
        print("Your height is {:.2f} m")
        return height
    else:
        print("Please try again, thank you.")

def bmi_cal(weight,height):
    bmi = weight/(height**2)
    print("\nYour body mass index (BMI) is {:.2f}".format(bmi))
    
def bmi_category(bmi):
    print("Disclaimer: The BMI categories are prescribed here for an average adult. The program is under still constructrion to make it useful for all ages")
    if bmi<16:
        print("Severe Thinness")
    elif bmi<17:
        print("Moderate Thinness")
    elif bmi<18.5:
        print("Mild Thinness")
    elif bmi<25:
        print("Normal")
    elif bmi<30:
        print("Overweight")
    elif bmi<35:
        print("Obese Class I")
    elif bmi<40:
        print("Obese Class II")
    else:
        print("Obese Class III")
