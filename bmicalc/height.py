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