while True:
print("Welcome to Google")
print("1. CEO")
print("2. CFO")
print("3. Manager")
print("4. Employee")
print("5. Exit")
choice = int(input("Enter your choice: "))
if choice == 5:
break
if choice == 1:
bsalary = int(input("Enter your monthly basic salary: "))
hra = bsalary * 0.1
da = bsalary * 0.05
ma = bsalary * 0.06
pf = bsalary * 0.12
gross = bsalary + hra + da + ma - pf
elif choice == 2:
bsalary = int(input("Enter your basic salary: "))
hra = bsalary * 0.09
da = bsalary * 0.04
ma = bsalary * 0.06
pf = bsalary * 0.12
gross = bsalary + hra + da + ma - pf
elif choice == 3:
bsalary = int(input("Enter your basic salary: "))
hra = bsalary * 0.08
da = bsalary * 0.03
ma = bsalary * 0.06
pf = bsalary * 0.12
gross = bsalary + hra + da + ma - pf
elif choice == 4:
bsalary = int(input("Enter your basic salary: "))
hra = bsalary * 0.07
da = bsalary * 0.02
ma = bsalary * 0.06
pf = bsalary * 0.12
gross = bsalary + hra + da + ma - pf
else:
print("Enter right choice")
print("Your monthly gross salary: ", gross)
annual = 12 * gross
if annual >= 1500000.00:
tax = annual * 0.3

elif annual <= 1500000 and annual >= 1250000:
tax = annual * 0.25
elif annual <= 1250000 and annual >= 1000000:
tax = annual * 0.2
elif annual <= 1000000 and annual >= 750000:
tax = annual * 0.15
elif annual <= 750000 and annual >= 500000:
tax = annual * 0.10
elif annual <= 500000 and annual >= 250000:
tax = annual * 0.05
else:
tax = 0
print("Your HRA: ", hra)
print("Your DA: ", da)
print("Your MA: ", ma)
print("Your PF: ", pf)
print("Your tax: ", tax)
net = annual - tax
print("Your NET: ", net)
# Add a new feature to the program that allows the user to calculate their annual bonus.
bonus = 0.02 * annual
print("Your annual bonus: ", bonus)
# Add a new feature to the program that allows the user to calculate their total
compensation.
total_compensation = net + bonus
print("Your total compensation: ", total_compensation)
# Function to calculate tax based on income slab

def calculate_tax(annual_income):

    if annual_income <= 250000:

        tax = 0

    elif annual_income <= 500000:

        tax = (annual_income - 250000) * 0.05

    elif annual_income <= 750000:

        tax = 250000 * 0.05 + (annual_income - 500000) * 0.1

    elif annual_income <= 1000000:

        tax = 250000 * 0.05 + 250000 * 0.1 + (annual_income - 750000) * 0.15

    elif annual_income <= 1250000:

        tax = 250000 * 0.05 + 250000 * 0.1 + 250000 * 0.15 + (annual_income - 1000000) * 0.2

    elif annual_income <= 1500000:

        tax = 250000 * 0.05 + 250000 * 0.1 + 250000 * 0.15 + 250000 * 0.2 + (annual_income - 1250000) * 0.25

    else:

        tax = 250000 * 0.05 + 250000 * 0.1 + 250000 * 0.15 + 250000 * 0.2 + 250000 * 0.25 + (annual_income - 1500000) * 0.3

    return tax

while True:

    print("Welcome to Google")

    print("1. CEO")

    print("2. CFO")

    print("3. Manager")

    print("4. Employee")

    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:

        break

    if choice == 1:

        bsalary = int(input("Enter your monthly basic salary: "))

        hra = bsalary * 0.1

        da = bsalary * 0.05

        ma = bsalary * 0.06

        pf = bsalary * 0.12

    elif choice == 2:

        bsalary = int(input("Enter your basic salary: "))

        hra = bsalary * 0.09

        da = bsalary * 0.04

        ma = bsalary * 0.06

        pf = bsalary * 0.12

    elif choice == 3:

        bsalary = int(input("Enter your basic salary: "))

        hra = bsalary * 0.08

        da = bsalary * 0.03

        ma = bsalary * 0.06

        pf = bsalary * 0.12

    elif choice == 4:

        bsalary = int(input("Enter your basic salary: "))

        hra = bsalary * 0.07

        da = bsalary * 0.02

        ma = bsalary * 0.06

        pf = bsalary * 0.12

    else:

        print("Enter the right choice")

        continue

    gross = bsalary + hra + da + ma - pf

    print("Your monthly gross salary: ", gross)

    annual = 12 * gross

    tax = calculate_tax(annual)

    print("Your HRA: ", hra)

    print("Your DA: ", da)

    print("Your MA: ", ma)

    print("Your PF: ", pf)

    print("Your tax: ", tax)

    net = annual - tax

    print("Your NET: ", net)

    # Add a new feature to the program that allows the user to calculate their annual bonus.

    bonus = 0.02 * annual

    print("Your annual bonus: ", bonus)

    # Add a new feature to the program that allows the user to calculate their total compensation.

    total_compensation = net + bonus

    print("Your total compensation: ", total_compensation)
