import time
import gas_core

input("Welcome to Shedlia's gas Station!! How are you doing? \n")
paying_type = input('would you like to prepay?\n\tYes\n\tNo\n').upper()
if paying_type== 'Yes'.upper():
    prepay=input("How much money would you like to put in?\n$: ")
    gas_type = input("Which gas would you like to choose?: \n\tpremium = 2.49\n\tregular = 2.07\n\tmid grade = 2.10\n")
    print('pumping...')
    time.sleep(3)
    with open('log.txt','a') as history:
        history.write(gas_core.do_prepay(prepay, gas_type))

elif paying_type == 'No'.upper():
    print('pumping...')
    time.sleep(3)   
    gallons=input("How many gallons did you put in?\n")
    gas_type=input('Which gas did you choose?\n\tpremium \n\tregular \n\tmid grade\n')
    with open('log.txt','a') as history:
        
        history.write('\n{0}, {1} gal. , {2}'.format(gas_type,gallons,gas_core.do_gas_after_pumping(gallons,gas_type)))
    
    print(gas_core.do_gas_after_pumping(gallons,gas_type))
else :
    print(".......")
    time.sleep(2) 