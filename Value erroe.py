try:
    num=int(input("Enter any number "))
    print("is this the number you entered ?  ",num)
except ValueError as ex:
    print("Exception",ex)