import gas_core
import disk
    


#needs multiple ways to make the
name = input('What\'s your name?: ').title().strip()
answer = input('Hello Administrator {0}. What would you like to do today?\n1. Look at purchase history\n2. Look at Tank Levels\n3. Total Revenue\n4. Refill Tanks\n\n'.format(name)).upper()


if answer == '1'.strip():
    print(disk.admin_purchase_history())

elif answer == '2'.strip():
    print(disk.admin_read_tank())

elif answer == '3'.strip():
    print(gas_core.admin_revenue())

elif answer == '4'.strip():
    inventory = gas_core.open_inventory()
    print(gas_core.refill_tank(inventory))

