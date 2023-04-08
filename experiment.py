from math import inf

def single_tax_calc(agi, deductions, payments, credits):
    tax = 0
    taxable_income = agi - deductions
    remainder = taxable_income
    brackets = [(10275, .10), (31500, .12), (47300, .22), (80975, .24), (45445, .32), (323950, .35), (inf, .37)]
    while remainder > 0:
        for bracket, rate in brackets:
            if remainder == 0:
                break
            elif remainder < bracket:
                tax = tax + (remainder * rate)
                remainder = 0
            elif remainder > bracket:
                tax = tax + (remainder * rate)
                remainder = remainder - bracket

    print(f"Your taxable income is {taxable_income}")
    tax_return = tax - credits - payments
    return tax_return

tax_return = single_tax_calc(50000, 12950, 2200, 1000)

print(tax_return)
