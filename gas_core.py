import gas_shell

def do_prepay(prepay, gas_type):
    ''' (float, string) -> None
    Calculates how much gas you would get when you
    input a number

    >>> do_prepay(1.00, 'premium')
    Your total gallons would be: 
    '''
    
    if gas_type =='premium':
         return 'Your total gallons would be: {:.2f} gal '.format(float(prepay) / 2.49, 2) 
    elif gas_type == 'regular':
        return 'Your total gallons would be: {:.2f} gal '.format(float(prepay)/ 2.07, 2)
    elif gas_type =='mid grade':
        return 'Your total gallons would be: {:.2f} gal'.format(float(prepay)/ 2.10, 2)

    else:
        return 'Ummmmmm Me no Compute'
     
def do_gas_after_pumping(gallons,gas_type):
    """(float, str) -> price of gas
    Calculates after pumping how much money you would
    have to pay after pumping your gas

    >>> do_gas_after_pumping(1.00, 'premium')
    Your total is: $2.49
    >>> do_gas_after_pumping(1.00, 'regular')
    Your total is: $2.07
    >>> do_gas_after_pumping(1.00, 'mid grade')
    Your total is: $2.10
    """
    if gas_type == 'premium':
        return 'Your total is: ${:.2f}'.format(float(gallons)  * 2.49, 2)
    elif gas_type == 'regular' :
        return 'Your total is: ${:.2f}'.format(float(gallons)  * 2.07, 2)
    elif gas_type == 'mid grade' :
        return 'Your total is: ${:.2f}'.format(float(gallons)  * 2.10, 2)
    else:
        return 'Ummmmm Me no Compute'