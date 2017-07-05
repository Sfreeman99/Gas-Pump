import gas_shell

def do_prepay(prepay, gas_type):
    ''' (float, string) -> None
    Calculates how much gas you would get when you
    input a number

    '''
    
    if gas_type =='premium':
         print('Your total gallons would be:  ',round(float(prepay) / 2.49, 2),'gal', sep= ' ')
    elif gas_type == 'regular':
        print('Your total gallons would be: $ ', round(float(prepay)/ 2.07, 2),'gal', sep=' ')
    elif gas_type =='mid grade':
        print('Your total gallons would be: ', round(float(prepay)/ 2.10, 2),'gal', sep=' ')

    else:
        print('Ummmmmm Me no Compute')
     
def do_gas_after_pumping(gas_price,gas_type):
    """(str) -> price of gas
    Calculates after pumping how much money you would
    have to pay after pumping your gas
    """
    if gas_type == 'premium':
        print('Your total is: $',round(float(gas_price)  * 2.49, 2), sep='')
    elif gas_type == 'regular' :
        print('Your total is: $',round(float(gas_price)  * 2.07, 2), sep='')
    elif gas_type == 'mid grade' :
        print('Your total is: $', round(float(gas_price)  * 2.10, 2), sep='')

    else:
        print('Ummmmm Me no Compute')