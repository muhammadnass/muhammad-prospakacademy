# This program calculates Zakat in Nigerian Naira
zakat_rate = 0.025 # Zakat rate is 2.5%

cash_savings = float(input("Enter your total cash savings in Naira: "))

gold_value = float(input("Enter the total value of your gold in Naira: "))

inventory_value = float(input("Enter the value of your business inventory in Naira: "))

#Calculating total wealth
total_wealth = cash_savings + gold_value + inventory_value

#Calculating the due zakat amount
zakat_due = total_wealth * zakat_rate

#Output formatted to 2 decimal places
print(f"\nTotal Zakatable Wealth: N{total_wealth:,.2f}")
print(f"Zakat Due (2.5%): N{zakat_due:,.2f}")