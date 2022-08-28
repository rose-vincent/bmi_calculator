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