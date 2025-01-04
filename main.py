# Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз - dz.csv
# В поле сдачи домашнего задания приложите ссылку на репозиторий с кодом.

import pandas as pd

df = pd.read_csv("dz.csv")

group = df.groupby("City")["Salary"].mean()
print(group)
print(group.describe())