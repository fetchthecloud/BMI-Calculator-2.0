# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

total_bmi = round(weight / height ** 2)

if total_bmi <= 18.5:
  print(f"Your BMI is {total_bmi}, you are underweight")
elif total_bmi <= 25:
  print(f"Your BMI is {total_bmi}, you have a normal weight")
elif total_bmi <= 30:
  print(f"Your BMI is {total_bmi}, you are slightly overweight")
elif total_bmi <= 35:
  print(f"Your BMI is {total_bmi}, you are obese")
elif total_bmi > 35:
  print(f"Your BMI is {total_bmi}, you are clinically obese")
else:
  print("You are healthy")