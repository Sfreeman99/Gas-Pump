import time 

def do_prepay():
    ''' (float, string) -> None
    Calculates how much gas you would get when you
    input a number

    '''

    if gas =='premium':
         print('Your total gallons would be:  ',round(float(prepay) / 2.49),'gal', sep= ' ')
    elif gas == 'regular':
        print('Your total gallons would be: $ ', round(float(prepay)/ 2.07),'gal', sep=' ')
    elif gas =='mid grade':
        print('Your total gallons would be: ', round(float(prepay)/ 2.10),'gal', sep=' ')

    else:
        print('Ummmmmm Me no Compute')
     
def do_gas_after_pumping():
    """(gal) -> price
    Calculates after pumping how much money you would
    have to pay after pumping your gas
    """
    if gas_type == 'premium':
        print('Your total is: $',round(float(gas_price)  * 2.49), sep='')
    elif gas_type == 'regular' :
        print('Your total is: $',round(float(gas_price)  * 2.07), sep='')
    elif gas_type == 'mid grade' :
        print('Your total is: $', round(float(gas_price)  * 2.10), sep='')

    else:
        print('Ummmmm Me no Compute')



input("Welcome to Shedlia's gas Station!! How are you doing? \n")
paying_type = input('would you like to prepay?\n\tYes\n\tNo\n').upper()
if paying_type== 'Yes'.upper():
    prepay=input("How much money would you like to put in?\n$: ")
    gas = input("Which gas would you like to choose?: \n\tpremium = 2.49\n\tregular = 2.07\n\tmid grade = 2.10\n")
    print('pumping...')
    time.sleep(5.5)
    do_prepay()

elif paying_type == 'No'.upper():
    print('pumping...')
    time.sleep(5)   
    gas_price=input("How many gallons did you put in?\n")
    gas_type=input('Which gas did you choose?\n\tpremium \n\tregular \n\tmid grade\n')
    
    do_gas_after_pumping()

else :
    print(".......")
    time.sleep(2) 
    print ("Well you can leave!!! Hit the door!!!")



