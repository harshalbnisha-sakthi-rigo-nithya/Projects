age = int(input("Enter your age: "))
student = input("Say Yes if your a student Say no for not a student: ")
if student == "yes".lower() or age >= 60:
    print("Yes, Discount!")
else:
    print("No, discount!")