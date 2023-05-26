#SYITB96

print("--Hotel Booking--")

print("Deluxe Room\t\t\tRs.2000")

print("Executive Room\t\t\tRs.3000")

print("No. of Guests\t\t\tCost")

print("2 Guest\t\t\t\tRs.2000")

print("3 Guest\t\t\t\tRs.3000")

print("4 Guest\t\t\t\t|Rs.4000")

print("Additional/person\t\tRs.1000")

print("---------------------------------")

print("\nSpecial Discount")

print("15% discount for Affiliated Companies.")

print("20% discount for Senior Citizen.")

print("Note: Both discounts cannot be clubbed together.\n\n")

name = input("Enter your name: ")

age = int(input("Age: "))

mobile = input("Enter Mobile Number: ")

guests = int(input("No. of guests: "))

print("Select Room Type")

room = int(input("1. Deluxe\n2. Executive Room\nYour Choice: "))

if room == 1:

room_cost = 2000

elif room == 2:

room_cost = 3000

type = input("Business Trip (y/n): ")

# Calculation

guest_cost = 2000 + (1000 * (guests - 2))

total = room_cost + guest_cost

discount = 0

if type == 'y':

comp = int(input("1. Infosys\n2. Cognizant\n3. TCS\n4. Capgemini\n5. None of the

above\nYour Choice: "))

if comp >= 1 and comp <= 4:

discount = room_cost * 0.15

elif type != 'y' and age >= 60:

discount = room_cost * 0.20

print("\n\n--Payments--")

print("Name:\t\t\t", name)

print("Age:\t\t\t", age)
                 print("Mobile No:\t\t", mobile)

print("No. of guests:\t", guests)

if room == 1:

print("Room Type:\t\t Deluxe Room")

elif room == 2:

print("Room Type:\t\t Executive Room")

print("Basic Cost:\t\t", guest_cost)

print("Room Cost:\t\t", room_cost)

print("Discount:\t\t", discount)

print("-------------------------------------")

print("Total Cost:\t\t", total - discount)
