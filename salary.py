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
   
    # Switch case statement
    if choice == 1:
       bsalary = int(input("Enter your montholy basic salary:"))
       hra = bsalary*0.1
       da = bsalary*0.05
       ma = bsalary*0.06
       pf = bsalary*0.12
       gross = bsalary + hra +da +ma -pf
    elif choice == 2:
       bsalary = int(input("Enter your basic salary:"))
       hra = bsalary*0.09
       da = bsalary*0.04
       ma = bsalary*0.06
       pf = bsalary*0.12
       gross = bsalary + hra +da +ma -pf
    elif choice == 3:
       bsalary = int(input("Enter your basic salary:"))
       hra = bsalary*0.08
       da = bsalary*0.03
       ma = bsalary*0.06
       pf = bsalary*0.12
       gross = bsalary + hra +da +ma -pf
    elif choice == 4:
       bsalary = int(input("Enter your basic salary:"))
       hra = bsalary*0.07
       da = bsalary*0.02
       ma = bsalary*0.06
       pf = bsalary*0.12
       gross = bsalary + hra +da +ma -pf
    else:
        print("Enter right choice")

    print("Your montholy Gross salary : ",gross)
    annual = 12*gross
    
    if annual>=1500000.00:
          tax=annual*0.3
    elif annual<=1500000 and annual>=1250000:
           tax = annual*0.25
    elif annual<=1250000 and annual>=1000000:
           tax = annual*0.2
    elif annual<=1000000 and annual>=750000:
           tax = annual*0.15
    elif annual<=750000 and annual>=500000:
           tax = annual*0.10
    elif annual<=500000 and annual>=250000:
           tax = annual*0.05
    else :
          tax = 0

    print("Your tax : ",tax)
    net = annual - tax
    print("Your CTC : ",net)
