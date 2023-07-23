#how to deal with an error


try:
    value=10
    #invalid input error
    number=int(input("enter a number"))
    print(number)
except ZeroDivisionError:
    print("invalid")

except ValueError:
    print("invalid input")
#using try and except whenever we try something wrong we dont have to look what is wrong over a code
