# your code goes here
weight = int(input())
height = int(input())
BMI = weight / (height * height)
if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI < 25:
    print("Normal")
elif 25 <= BMI < 30:
    print("Normal")
elif BMI >= 30:
    print("Normal")
