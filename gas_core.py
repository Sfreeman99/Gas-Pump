# def do_prepay(prepay, gas_type):
#     ''' (float, string) -> None
#     Calculates how much gas you would get when you
#     input a number

#     >>> do_prepay(2.49, 'premium')
#     '1.00 gal'
#     '''
    
#     for item in tank:
#         if gas_type == item[0]:
#             return '{:.2f} gal'.format(float(prepay) / item[1])
     
# def do_gas_after_pumping(gallons,gas_type):
#     """(float, str) -> price of gas
#     Calculates after pumping how much money you would
#     have to pay after pumping your gas

#     >>> do_gas_after_pumping(1.00, 'premium')
#     '$2.49'
#     >>> do_gas_after_pumping(1.00, 'regular')
#     '$2.07'
#     >>> do_gas_after_pumping(1.00, 'mid grade')
#     '$2.10'
#     """
    
#     for item in tank:
#         if gas_type == item[0]:
#             return '${:.2f}'.format(float(gallons) * item[1])

def gas_pump(gas_type, money):
    ''' '''
    open_inventory()
    for item in open_inventory():
        if gas_type.lower().strip() == item[0].lower().strip():
            gallons = float(money) * float(item[1])
            return gallons
            



def open_inventory():
    with open('tank.txt', 'r') as tank:
        tank.readline()
        str_inventory = tank.readlines()

    inventory = []
    for item in str_inventory:
        sublist = item.split(', ')
        inventory.append([sublist[0], float(sublist[1].strip()), float(sublist[2].strip())])

    return inventory

  
def update_inventory(inventory, gas_type, gallons):
    message = 'name, price, quantity\n'
    for item in inventory:
        if item[0] == gas_type:
            item[2] = float(item[2]) - float(gallons)
        message += ('{0}, {1:.2f}, {2:.2f}\n'.format(item[0],item[1],item[2]))
    with open('tank.txt','w') as tank:
        tank.write(message)
    



tank = open_inventory()
