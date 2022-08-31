# bmicalc
## BMI Calculator for adults above the age of 20 years.
This is a package that contains 4 functions to define height, weight, BMI and weight class.

### *bmi.bmi_cal(weight, height)*
To calculate your BMI from your height and weight.

Parameters:	
weight (float) – weight returned by weight_cal()
height (float) – height returned by height_cal()

Returns: BMI in kg/m^2

### *bmi.bmi_category(bmi)*
To identify weight range based on BMI.

Parameters:	bmi (float) – bmi returned by bmi_cal()

Returns: Your weight class

### *bmi.height_cal()*
To define your height in SI Units to calculate BMI.

Input(s): By User through prompt

Returns: Height in metre

### *bmi.weight_cal()*
To define your weight in SI Units to calculate BMI.

Input(s): By User through prompt

Returns: Weight in kilogram
