

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