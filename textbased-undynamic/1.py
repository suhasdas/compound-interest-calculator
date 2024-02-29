print("SIMPLE INTEREST \n -------------------------------------------------------")

money = 48_000
print(f"current money deposited in bank account with 50% interest: {money}")

percent = 0.5

for years in (1,10):
    money += money*percent*years
    print(f"money now after {years}/10 years: {money}")

print(f"final money: {money}")

print("COMPOUND INTEREST \n -------------------------------------------------------")

starting_money = 70_000
print(f"current money deposited in bank account with 99% interest: {money}")
percent = 0.99
ending_money = 0

for years in range(1,10):
    ending_money += starting_money*(1+percent)
    print(f"money now after {years}/10 years: {ending_money}")

print(f"final money: {ending_money}")
