import time
import gas_core
import disk
from os.path import isfile
def prepay():
    inventory = disk.open_inventory()
    money = input("How much money would you like to put in?\n$: ")
    gas_type = input("Which gas would you like to choose?: \n\tpremium = 2.49\n\tregular = 2.07\n\tmid grade = 2.10\n")
    print('pumping...')
    time.sleep(2)
    gallons = gas_core.gas_pump(gas_type, money)
    disk.purchase_history(gas_type,money,gallons)
    print('With $',money,'you get',gas_core.gas_pump(gas_type,money),'gal.')
    gas_core.update_inventory(inventory, gas_type, gallons)

def pay_after():
    inventory = disk.open_inventory()
    print('Head to the cashier to continue')
    time.sleep(2)
    money = input("How much money did you give the cashier?\n$: ")
    gas_type = input('Which gas did you choose?\n\tpremium \n\tregular \n\tmid grade\n')
    gallons = gas_core.gas_pump(gas_type, money)
    disk.purchase_history(gas_type,money,gallons)
    print('With $',money,'you get',gas_core.gas_pump(gas_type,money),'gal.')
    gas_core.update_inventory(inventory, gas_type, gallons)

def decision():
    input("Welcome to Shedlia's gas Station!! How are you doing? \n")
    paying_type = input('would you like to prepay with a card?\n\tYes\n\tNo\n').upper().strip()
    if paying_type == 'YES':       
        prepay()
        

    elif paying_type == 'NO':
        pay_after()
        
    else :
        print(".......")
        time.sleep(2)
        print("Well you can hit the door!!!") 

def main():
    if isfile('tank.txt'):
        decision()
    if not isfile('tank.txt'):
        disk.initiate_tank()
        decision()

if __name__ == '__main__':
    main()