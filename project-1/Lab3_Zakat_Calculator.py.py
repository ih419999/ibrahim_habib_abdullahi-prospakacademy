# Lab 3: Zakat Calculator

zakat_rate = 0.025

cash = float(input("Enter your total cash savings: "))
gold = float(input("Enter the total value of your gold (in your local currency): "))
business = float(input("Enter the value of your business inventory: "))

total_wealth = cash + gold + business

zakat_due = total_wealth * zakat_rate

print(f"\nTotal Zakatable Wealth: ${total_wealth:,.2f}")
print(f"Zakat Due (2.5%): ${zakat_due:,.2f}")