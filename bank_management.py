#Bank management project
print('='*35)
customers=['Sathish','sai','Ramesh','Naveen','Naresh']
customers_pin_no=['1234','7677','9989','7657','9876']
customers_balance=[10000,2000,43500,76520,88760]
deposition = 0
balance = 0
withdraw = 0
counter_1 = 1
counter_2 = 5
i=0
def create_pin():  #function to get only 4 digits pin number
    pin=input('enter 4 digits pin no : ')
    if len(pin)==4:
        return pin
    else:
        print('*** Please enter valid 4 digits pin ***')
        create_pin()

# here main programme starts
while True:   # to run continously 

    print('--- Welcome to My Village Bank ---')
    print('*'*35)
    options='''
    =>> 1.Open new account    <<=
    =>> 2.Withdraw amount     <<=
    =>> 3.Deposit amount      <<=
    =>> 4.Check bank balance  <<=
    =>> 5.Exit                <<=
    '''
    print(options)
    print('*'*35)
    choice=input('Enter any option from above : ')
    if choice=='1':
        no_of_cust=eval(input('enter no.of customers : '))
        i=i+no_of_cust
        if i > 5:  #this restricts the customers if customer number is greater than 5
            print('Customers registration exceed ')
            i=i-no_of_cust
        else:
            while counter_1 <=i:
                name=input('Please your enter name :')
                customers.append(name)
                pin_no=create_pin() # it calls function 
                customers_pin_no.append(pin_no)
                balance=0  # 0 balance in u r account
                deposition=eval(input('enter a value to start your account : '))
                balance=balance+deposition
                customers_balance.append(balance)
                print('Name : ',end=' ')
                print(customers[counter_2])
                print('Pin : ',end=' ')
                print(customers_pin_no[counter_2])
                print('Balance : ',end=' ')
                print(customers_balance[counter_2],end=' ')
                print("-/Rs")
                counter_1=counter_1+1
                counter_2=counter_2+1
                print('\n')
                print('*'*35)
                print('Your name is added to Customer System')
                print('Your pin no. is added to Customer system')
                print('Your balance is added to Customer system')
                print('*'*35)
                print('---New account created successfully--')
                print('\n')
                print('Your name is available in customers list : ')
                print(customers)
                print('\n')
                print('NOte! please remember name and pin no.')
                print('='*35)
        #this statement helps to move to main menu
        main_menu=input('please enter any key to go to main function \ to exit')
    elif choice=='2':
        j=0 # by this we can exit if user enter incorrect password
        print('option 2 selected by customer')
        while j < 1:
            k=-1 #it acts as index for acessing custsomers
            name=input('enter your name : ')
            pin=input('enter your pin : ')
            while k < len(customers) -1: # insex starts at 0 so get length -1
                k=k+1 # here index increases until customer name matches i.e k=0,1,2,3
                if name == customers[k]:
                    if pin == customers_pin_no[k]:
                        j=j+1 # if pin no matches j gets increment
                        print('Your account Balance : ',customers_balance[k])
                        print('/Rs \n')
                        balance=customers_balance[k]
                        withdrawl=eval(input("enter amount to withdraw : "))
                        if withdrawl > balance:
                            print("Your balance is low than your withdraw amount so please deposit money")
                            print('\n')
                            depo=input('if u want deposit press 1 : ')
                            if depo== '1':
                                deposit=eval(input("enter amount to deposit : "))
                                balance=balance+deposit
                                print("Your current balance is : ",balance)
                                balance=balance-withdrawl
                                print('**** Withdraw successfull ***')
                                customers_balance[k]=balance
                                print("After withdrwaing money")
                                print('new balance : ',customers_balance[k])
                            else:
                                break
                        elif withdrawl < balance:
                            balance=balance-withdrawl
                            print('**** Withdraw successfull ***')
                            customers_balance[k]=balance
                            print("After withdrwaing money")
                            print('new balance : ',customers_balance[k])
            if j < 1:
                print('Incorrect pin n Name')
                break
         #this statement helps to move to main menu
        main_menu=input('please enter any key to go to main function \ to exit')
    elif choice=='3':
        print('Choice no. 3 is selected by customer')
        n=0 # it takes pin as correct r not
        while n < 1:
            k=-1
            name=input('Please enter your name : ')
            pin=input("Please enter your pin : ")
            while k < len(customers) -1:
                k=k+1
                if name==customers[k]:
                    if pin==customers_pin_no[k]:
                        n=n+1 #after pin and name gets verified n gets increment
                        #   this prints deposition and current balance
                        print('Your current balance : ', end=' ') 
                        print(customers_balance[k],end=' ')
                        print('/Rs \n')
                        balance=customers_balance[k]
                        deposit=eval(input("Please enter amount to deposit : "))
                        balance=balance+deposit
                        customers_balance[k]=balance
                        print("New balance : ",end=' ')
                        print(customers_balance[k])
                        print('\n')
            if n < 1: # if pin and name incorrect then n won't get increased i.e, n=0 only
                print('incorrect pin and name')
        #this statement helps to move to main menu
        main_menu=input('please enter any key to go to main function \ to exit')
    elif choice=='4':
        print("Choice number 4 is selected by the customer")
        k = 0
        print("Customer name list and balances mentioned below : ")
        print("\n")
        # The while loop below will keeping running until all the customers and balances are shown.
        while k <= len(customers) - 1:
            print("->.Customer =", customers[k])
            print("->.Balance =", customers_balance[k], end=" ")
            print("-/Rs")
            print("\n")
            k = k + 1
        #this statement helps to move to main menu
        main_menu=input('please enter any key to go to main function \ to exit')
    elif choice == "5":
        # These statements would be just showed to the customer.
        print("Choice  5 is selected by the customer")
        print("Thank you for using our banking system!")
        print("\n")
        print("Come again")
        print("Bye bye")
        break
    else:
        # This else function above would work when a wrong function is chosen.
        print("Invalid option selected by the customer")
        print("Please Try again!")
        # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")





        

