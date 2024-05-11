import random

comp_win, user_win = 0, 0
choices = ['камень', 'ножницы', 'бумага']
outcome = {
    ('камень', 'ножницы'): True,
    ('ножницы', 'бумага'): True,
    ('бумага', 'камень'): True
}
while comp_win < 3 and user_win < 3:
  comp_choice = random.choice(choices)
  user_choice = input("Выберите: камень, ножницы или бумага: ").lower()
  if user_choice not in choices:
    print("Неправильный выбор. Пожалуйста, введите одно из трех слов.")
    continue
  print(f"Компьютер выбрал: {comp_choice}")

  if user_choice == comp_choice:
    print("Ничья!\n")
  elif outcome.get((comp_choice, user_choice), False):
    comp_win += 1
    print(f"Вы проиграли! Счет: {comp_win}:{user_win}\n")
  else:
    user_win += 1
    print(f"Вы выиграли! Счет: {comp_win}:{user_win}\n")

if comp_win == 3:
    print("Компьютер - победитель!")
else:
    print("Вы - победитель!")
