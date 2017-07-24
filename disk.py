

def read_text():
    with open('log.txt', 'r') as revenue:
        revenue.readline()
        revenue = revenue.readlines()
    return revenue