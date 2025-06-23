height =eval(input("enter your height:"))
weight =eval(input("enter your weight:"))

bmi = weight / (height**2)
print(bmi)
if bmi < 18:
    print("your underweight")
elif bmi <=24:
    print("you are healthy")
elif bmi >=29:
    print("you ae overweight")
else:
    print("you are obese")
