tax_rate = 0.2
std_ded = 10000
dependents = int(input("Enter number of dependents:"))
dep_ded = 3000
gross_income = float(input("Enter gross income:"))
tax_income = gross_income - std_ded - (dep_ded * dependents)
tax = tax_income * tax_rate
print ("The income tax is:", tax)
