money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0

money = money_capital + salary - spend

while money > 0:
    month += 1
    spend *= increase + 1
    money += salary - spend

print(month)
