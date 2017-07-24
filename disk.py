

def read_text():
    with open('log.txt', 'r') as revenue:
        revenue.readline()
        revenue = revenue.readlines()
    return revenue

def admin_read_tank():
    with open('tank.txt') as tank:
        return tank.read()

def admin_purchase_history():
    with open('log.txt') as file:
        file = file.read()
    return file

def purchase_history(gas_type, money, gallons):
    with open('log.txt','a') as history:
        history.write('\n{0}, {1}, {2}'.format(gas_type, money, gallons))

def initiate_tank():
    t = [
        'name, price, quantity',
        'regular, 2.07, 5000.00',
        'mid grade, 2.10, 5000.00',
        'premium, 2.49, 5000.00'
    ]
    with open('tank.txt', 'w') as file:
        return file.write('\n'.join(t))

def open_inventory():
    with open('tank.txt', 'r') as tank:
        tank.readline()
        str_inventory = tank.readlines()
    inventory = []
    for item in str_inventory:
        sublist = item.split(', ')
        inventory.append([sublist[0], float(sublist[1].strip()), float(sublist[2].strip())])

    return inventory


