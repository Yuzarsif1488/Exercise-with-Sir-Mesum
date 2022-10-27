Rate1 = .10
Rate2 = .25
Rate1_Single_limit = 32000
Rate1_Married_limit = 64000

income = float(input("Please enter your income: "))
maritalStatus = input("Please enter s for single, m for married: ")

tax1 = 0.0
tax2 = 0.0

if maritalStatus == "s" :
    if income <= Rate1_Single_limit:
        tax1 = Rate1 * income
    else :
        tax1 = Rate1 * Rate1_Single_limit
        tax2 = Rate2 * (income - Rate1_Single_limit)
else:
    if income <= Rate1_Married_limit:
        tax1 = Rate1 * income
    else:
        tax1 = Rate1 * Rate1_Married_limit
        tax2 = Rate2 *(income - Rate1_Married_limit)
    
TotalTax = tax1 +  tax2

print("The tax is $%.2f " %TotalTax)

