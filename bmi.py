def calculate_bmi(weight, height):
  # Расчет индекса массы тела
  bmi = weight / (height ** 2)
  return bmi

def interpret_bmi(b, w, h):
  # Интерпретация значения ИМТ
  if b < 18.5:
      return "Недостаточный вес"
  elif 18.5 <= b < 25:
      return "Нормальный вес"
  elif 25 <= b < 30:
      norm_w = 25 * h ** 2
      return f"Избыточный вес. \nДля Вашего роста нормальный вес д.б. менее {norm_w:.1f}. \nНужно сбросить минимум {w - norm_w:.1f} кг."
  else:
      return "Всё плохо! У Вас ожирение"

def main():
  # Запрос входных данных от пользователя
  weight = float(input("Введите вес в кг: "))
  height = float(input("Введите рост в см: ")) / 100
  # Расчет ИМТ
  bmi = calculate_bmi(weight, height)
  # Вывод результатов
  print(f"Ваш ИМТ: {bmi:.2f}")
  print(f"Оценка: {interpret_bmi(bmi, weight, height)}")

# Если этот скрипт запущен как основная программа, вызвать main
if __name__ == "__main__":
  main()
