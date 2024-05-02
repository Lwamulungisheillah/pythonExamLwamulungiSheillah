#NO.4
#(a)
#program to ask an employee for their salary and year of service, and display the net bonus and net salary
 # Run the loop indefinitely until the user decides to quit
def bonus_structure():
    while True: 
        salary = int(input("Please enter your salary: "))
        years_of_service = int(input("Please enter your years of service: "))
        
        if years_of_service > 4:
            bonus = salary * 0.08
        elif years_of_service == 3:
            bonus = salary * 0.05
        else:
            bonus = 0
        #sum of net salary and net bonus
        net_salary = salary + bonus 
        
        print("Net bonus :", bonus)
        print("Net salary :", net_salary)
        
        #when the user decides to exit, finish with a thankyou statement
        run = input("Enter 1 to continue or any other input to exit: ")
        if run != '1':
            print("Thank you for your cooperation")
            break
#testing the program
bonus_structure()



#(b)

def saccoTransactions():
     # making sure the initial account balance is 0
    accountBalance = 0  
    run = 1
    while run == 1: 
        print("\nWelcome to WITU Sacco.")
        print('1. Deposit Money')
        print('2. Withdraw Money')
        print('3. Check Balance')
        
        studentChoice = int(input("Enter your selection (1, 2, or 3): "))
        
        #deposite conditions
        if studentChoice == 1:
            print('\n...Processing a deposit transaction...')
            depositAmount = int(input("Enter amount to be deposited: "))
            if depositAmount < 1000:   
                print('\nMinimum deposit is 1000')
            else:
                accountBalance += depositAmount
                print(f'Dear student, you have deposited {depositAmount:,} and your new account balance is {accountBalance:,}')
        
        #withdraw conditions
        elif studentChoice == 2:
            print('\n...Processing a withdraw transaction...')
            withdrawAmount = int(input("Enter amount to be withdrawn: "))
            if accountBalance == 0:
                print("Your balance is 0")
            elif withdrawAmount < 500:
                print("Minimum withdraw amount is 500")
            elif withdrawAmount > accountBalance:
                print("Withdraw failed, insufficient funds")  
            else:
                accountBalance -= withdrawAmount
                print(f'Dear student, you have withdrawn {withdrawAmount:,} and your new account balance is {accountBalance:,}')
        
        elif studentChoice == 3:
            print(f"Your account balance is {accountBalance:,}")
        
        else:
            print("You entered a wrong choice!! Please select 1, 2, or 3\n")
        
        run = int(input("Enter 1 to continue or any other number to exit: "))
        if run != 1:
            print("Thanks for using our sacco")
            break

saccoTransactions()
def saccoTransactions():
    accountBalance = 0
    run = 1
    while run == 1:
        print("\nWelcome to UTAMUGuild Sacco.")
        print('1. Deposit Money')
        print('2. Withdraw Money')
        print('3. Check Balance')
        
        studentChoice = int(input("Enter your selection (1, 2, or 3): "))
        
        if studentChoice == 1:
            print('\n...Processing a deposit transaction...')
            depositAmount = int(input("Enter amount to be deposited: "))
            if depositAmount < 1000:   
                print('\nMinimum deposit is 1000')
            else:
                accountBalance += depositAmount
                print(f'Dear student, you have deposited {depositAmount:,} and your new account balance is {accountBalance:,}')
        
        elif studentChoice == 2:
            print('\n...Processing a withdraw transaction...')
            withdrawAmount = int(input("Enter amount to be withdrawn: "))
            if accountBalance == 0:
                print("Your balance is 0")
            elif withdrawAmount < 500:
                print("Minimum withdraw amount is 500")
            elif withdrawAmount > accountBalance:
                print("Withdraw failed, insufficient funds")  
            else:
                accountBalance -= withdrawAmount
                print(f'Dear student, you have withdrawn {withdrawAmount:,} and your new account balance is {accountBalance:,}')
        
        elif studentChoice == 3:
            print(f"Your account balance is {accountBalance:,}")
        
        else:
            print("You entered a wrong choice!! Please select 1, 2, or 3\n")
        
        run = int(input("Enter 1 to continue or any other number to exit: "))
        if run != 1:
            print("Thanks for using our sacco")
            break
saccoTransactions()

#(c)
#a surveyor needs to prepare maps and adjust the coordinates of a new location
