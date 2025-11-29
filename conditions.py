day_in_week= input("day_in_week:").lower()
print(day_in_week)

if day_in_week=="saturday" or day_in_week=="sunday":
    print("i will work")

else: 
    print("i will not work")

num1= int(input("Enter first number:"))
num2= int(input("Enter second number:"))

choice=input("Enter a operation:(options +,-,*,/)")

if choice=="+":
    sum_of_number= num1+num2
    print("addition",sum_of_number)

elif choice=="-":
    diff_of_number= num1-num2
    print("subtraction",diff_of_number)

elif choice=="*":
    prod_of_number= num1*num2
    print("multiplication",prod_of_number)

elif choice=="/":
    division_of_number= num1/num2
    print("divide",division_of_number)     

else:
    print("INVALID")       
