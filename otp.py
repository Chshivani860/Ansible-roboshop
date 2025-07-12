import random

otp = random.randint(100000, 999999)
print("your OTP is:",otp)

entered_otp = int(input("enter the otp:"))

if entered_otp == otp:
    print("OTP verified succesfully!")

else:
    print("invalid OTP. Please try Again.")
