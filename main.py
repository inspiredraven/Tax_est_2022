from math import inf

#tax brackets
"""
37%, for incomes over $539,900 ($647,850 for married couples filling jointly);
35%, for incomes over $215,950 ($431,900 for married couples filing jointly);
32% for incomes over $170,050 ($340,100 for married couples filing jointly);
24% for incomes over $89,075 ($178,150 for married couples filing jointly);
22% for incomes over $41,775 ($83,550 for married couples filing jointly);
12% for incomes over $10,275 ($20,550 for married couples filing jointly).
"""

def main():
    agi = int(input("What is your last year's Adjusted Gross Income? "))
    credits = int(input("How much was your last year's credits? "))
    deductions = int(input("How much was your last year's deductions? "))
    payments = int(input("How much was your widthholding/payments last year? "))
    print("single = S")
    print("Married filling joint = MFJ")
    status = input("What status are you filling? ").replace(" ", "").upper()
    if status == "S":
        tax_return = single_tax_calc(agi, deductions, payments, credits)
    else:
        tax_return = MFJ_tax_calc(agi, deductions, payments, credits)

    if tax_return >= 0:
        print(f"Your tax return is {tax_return}")
    else:
        tax_return = tax_return * (-1)
        print(f"You owe {tax_return}")

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

def MFJ_tax_calc(agi, deductions, payments, credits):
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

if __name__=="__main__":
    main()