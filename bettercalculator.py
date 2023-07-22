num1= float(input("enter the first number"))
operator=input("enter the first operator")
num2= float(input("enter the second number"))

#now applying if statement
if operator == "+":
    print(num1+num2)

elif operator == "-":
    print(num1-num2)

elif operator == "*":
    print(num1*num2)

#elif operator == "/":
 #   print(num1/num2)

else:
    print("invalid operator")


