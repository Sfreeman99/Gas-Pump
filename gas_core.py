

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