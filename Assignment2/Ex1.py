# Calculate BMI

h = int(input("Enter your height (cm): "))
w = int(input("Enter your weight (kg): "))
bmi = w / (h/100*h/100)

if bmi < 16:
    print ("Severely underweight")
elif 16 <= bmi < 18.5:
    print ("Underweight")
elif 18.5 <= bmi < 25:
    print ("Normal")
elif 25 <= bmi < 30:
    print ("Overweight")
else:
    print ("Obese")
