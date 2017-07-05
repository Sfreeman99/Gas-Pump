input("Welcome to Shedlia's gas Station!! How are you doing? \n")
paying_type = input('would you like to prepay?\n\tYes\n\tNo\n').upper()
if paying_type== 'Yes'.upper():
    prepay=input("How much money would you like to put in?\n$: ")
    gas = input("Which gas would you like to choose?: \n\tpremium = 2.49\n\tregular = 2.07\n\tmid grade = 2.10\n")
    print('pumping...')
    time.sleep(5.5)
    do_prepay()

elif paying_type == 'No'.upper():
    print('pumping...')
    time.sleep(5)   
    gas_price=input("How many gallons did you put in?\n")
    gas_type=input('Which gas did you choose?\n\tpremium \n\tregular \n\tmid grade\n')
    
    do_gas_after_pumping()

else :
    print(".......")
    time.sleep(2) 