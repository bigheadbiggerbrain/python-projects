weight = float(input("Introduce your weight"))
height = float(input("Introduce your height"))
bmi = weight/height**2

if bmi < 18.5:
    print(bmi)
    print("Your BMI is underweight")
elif bmi >= 18.5 and bmi <= 25:
    print(bmi)
    print("Your BMI is normal")
elif bmi >= 25 and bmi <= 30:
    print(bmi)
    print("Your BMI is overweight")
elif bmi > 30:
    print(bmi)
    print("Your BMI is obesity")