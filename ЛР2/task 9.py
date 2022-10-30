salary = 5000
spend = 6000
months = 10
increase = 0.03

need_money = 0

for month in range(months):
    if month >= 1:
        spend *= increase + 1
    need_money += spend - salary

print(round(need_money))
