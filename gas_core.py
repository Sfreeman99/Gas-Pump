from disk import *

def gas_pump(gas_type, money):
    ''' '''
    for item in open_inventory():
        if gas_type.lower().strip() == item[0].lower().strip():
            gallons = float(money) / float(item[1])
            return round(gallons, 2)
  
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
    

