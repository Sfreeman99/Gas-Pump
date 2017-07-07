import time
import gas_core

input("Welcome to Shedlia's gas Station!! How are you doing? \n")
inventory = gas_core.open_inventory()
paying_type = input('would you like to prepay?\n\tYes\n\tNo\n').upper()
if paying_type== 'Yes'.upper():
    money=input("How much money would you like to put in?\n$: ")
    gas_type = input("Which gas would you like to choose?: \n\tpremium = 2.49\n\tregular = 2.07\n\tmid grade = 2.10\n")
    print('pumping...')
    time.sleep(2)
    gallons = gas_core.gas_pump(gas_type, money)
    with open('log.txt','a') as history:

        history.write('\n{0}, ${1} , {2}'.format(gas_type,money,gas_core.gas_pump(gas_type,money)))
    print('With $',money,' you get ',gas_core.gas_pump(gas_type,money),' gal.')
elif paying_type == 'No'.upper():
    print('pumping...')
    time.sleep(2)   
    gallons=input("How many gallons did you put in?\n")
    gas_type=input('Which gas did you choose?\n\tpremium \n\tregular \n\tmid grade\n')
    with open('log.txt','a') as history:
        
        history.write('\n{0}, {1} gal. , {2}'.format(gas_type,gallons,gas_core.do_gas_after_pumping(gallons,gas_type)))
    
    print(gas_core.do_gas_after_pumping(gallons,gas_type))
else :
    print(".......")
    time.sleep(2)
    print("Well you can hit the door!!!") 

gas_core.update_inventory(inventory, gas_type, gallons)

            
    
    

