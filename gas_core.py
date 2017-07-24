from disk import *

def gas_pump(gas_type, money):
    ''' '''
    for item in open_inventory():
        if gas_type.lower().strip() == item[0].lower().strip():
            gallons = float(money) / float(item[1])
            return round(gallons, 2)

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

def refill_tank(inventory):
    message = 'name, price, quantity\n'
    for item in inventory:
        item[2] = float(5000)    
        message += '{0}, {1:.2f}, {2:.2f}\n'.format(item[0],item[1],item[2])
    with open('tank.txt','w') as refill:
        refill.write(message)
    return message

def initiate_tank():
    t = [
        'name, price, quantity',
        'regular, 2.07, 5000.0',
        'mid grade, 2.10, 5000.0',
        'premium, 2.49, 5000.0'
    ]
    with open('tank.txt', 'w') as file:
        file.write('\n'.join(t))


def purchase_history(gas_type, money, gallons):
    with open('log.txt','a') as history:
        history.write('\n{0}, {1}, {2}'.format(gas_type, money, gallons))

def admin_revenue():
    revenue = read_text()
    history = []
    total = []
    for item in revenue:
        money = item.split(', ')
        history.append([money[0], float(money[1]), float(money[2])])

    for item in history:
        total.append(item[1])
    
    return '${}'.format(sum(total))


if __name__ == '__main__':
    tank = open_inventory()
    print(revenue())
    

