day_in_week= input("Enter a day:").lower()
print(day_in_week)

if day_in_week in ("monday", "tuesday"):
    print("I WILL DEFINITELY WORK")
else:
    print("I WILL NOT WORK AT ALL")
 
num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))

choice= input("Enter a operator(options +,-,*,/)")

if choice== "+":
 sum_of_number = num1+num2
 print("addition",sum_of_number)

elif choice == "-":
 diff_of_number= num1-num2
 print("substraction",diff_of_number)

elif choice=="*":
 prod_of_number=num1*num2
 print("multiplication",prod_of_number)

elif choice=="/":
 division_of_number=num1/num2
 print("division", division_of_number)

else:
 print('INVALID')


