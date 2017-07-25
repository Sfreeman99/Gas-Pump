from gas_core import *
from disk import read_text


def test_gas_pump_regular():
    assert gas_pump('regular', 26) == 12.56

def test_premium():
    assert gas_pump('premium', 5) == 2.01

def test_mid_grade():
    assert gas_pump('mid grade', 5) == 2.38

def test_refill_tank():
    assert refill_tank([['regular', 2.07, 4567.3],
    ['mid grade', 2.10, 5000.0],['premium', 2.49, 5000.0]]) == 'name, price, quantity\nregular, 2.07, 5000.00\nmid grade, 2.10, 5000.00\npremium, 2.49, 5000.00\n'


def test_update_inventory():
    assert update_inventory([['regular', 2.07, 5000.00],['mid grade', 2.10, 5000.00],['premium', 2.49, 5000.00]], 'premium', '10.0') == 'name, price, quantity\nregular, 2.07, 5000.00\nmid grade, 2.10, 5000.00\npremium, 2.49, 4990.00\n'


def test_admin_revenue():
    revenue = read_text()
    assert admin_revenue(revenue) == '$806.0'