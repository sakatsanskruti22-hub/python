print("start")
try:
    print(10/0)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
print("end")


print("start")
try:
    print(10/0)
except ZeroDivisionError as e:
    print(e)
print("end")


ip=int(input("Enter a num: "))
print(ip)
except ValueError
print("enter numbers only !")
