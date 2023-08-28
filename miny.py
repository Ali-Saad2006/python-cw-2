my_name = input("enter your name")
my_age = input("ernter your age")
print("me is {my name } and I am {my age} years old")


first_number = float(input("nymber one: "))
second_numer = float(input("number tow: "))
operation = input("enter an operation")
if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second number )
elif operation == '*':
    print(first number * second number)
elif operation == "/"
    print(first_number / second_numer)
#part there 
bus_capcity = 27
in_bus = int(input("how many people in the bus "))

join_bus = int(input('how many will join the bus '))

empty_seats = bus_capcity - in_bus
print(empty_seats)

if empty_seats > bus_capcity :
    print(f"there are empty seats. the empty seats are {empty_seats}")

else:
    print("sorry there are no empty seats")