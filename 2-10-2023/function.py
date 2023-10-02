def calculate_text(bill,tax_rate):
    return(bill*tax_rate)/100.00

print('total tax',calculate_text(175.00,15))