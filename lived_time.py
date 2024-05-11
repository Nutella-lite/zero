# Для установки модулей `datetime`и `dateutil.relativedelta`- `pip install python-dateutil`
from datetime import datetime
from dateutil.relativedelta import relativedelta

name = input("Добрый день! Как к Вам обращаться?  ")
print("Приятно познакомиться, ", name, "!")
date_str = input("Введите дату вашего рождения в формате ДД.ММ.ГГГГ: ")

try:
  # Пытаемся преобразовать введенные данные в объект datetime
  birthday = datetime.strptime(date_str, "%d.%m.%Y")
except ValueError:
  print("Неверный формат даты.")
  exit()

# Текущая дата
now = datetime.now()

# Рассчитываем разницу между текущей датой и датой рождения
difference = relativedelta(now, birthday)

# Выводим информацию о прожитых годах, месяцах, днях и часах
print(
    f"Вам примерно {difference.years} лет, {difference.months} месяцев, {difference.days} дней и {difference.hours} часов."
)
