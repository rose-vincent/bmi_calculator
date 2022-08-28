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