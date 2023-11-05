salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
all_spend = 0
for i in range(months):
    all_spend += spend * (1 + increase) ** i
capital = all_spend - salary * 10

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(capital, 2))
