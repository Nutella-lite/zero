def caesar_cipher(message, shift):
  encrypted = ""
  for char in message:
      if char.isalpha():
        ordAa = ord('a') if char.islower() else ord('A')
        shifted_char = chr((ord(char) - ordAa + shift) % 26 + ordAa)
        encrypted += shifted_char
      else:
        encrypted += char
  return encrypted

def caesar_decipher(message, shift):
  decrypted = ""
  for char in message:
      if char.isalpha():
        ordAa = ord('a') if char.islower() else ord('A')
        shifted_char = chr((ord(char) - ordAa - shift) % 26 + ordAa)
        decrypted += shifted_char
      else:
        decrypted += char
  return decrypted

choice = int(input("Выберите действие:\n1 - Зашифровать\n2 - Расшифровать\nВаш выбор: "))
while choice != 3:
  message = input("Введите сообщение латиницей:  ")
  shift = int(input("Введите сдвиг (натуральное число):  "))
  if choice == 1:
    encrypted_message = caesar_cipher(message, shift)
    print("Зашифрованное сообщение:", encrypted_message)
  elif choice == 2:
    decrypted_message = caesar_decipher(message, shift)
    print("Расшифрованное сообщение:", decrypted_message)
  else:
    print("Неверный выбор действия, д.б. 1, 2 или 3")
  choice = int(input("Выберите действие:\n1 - Зашифровать\n2 - Расшифровать\n3 - Завершить работу\nВаш выбор: "))
