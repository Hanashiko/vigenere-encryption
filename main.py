ukrainian_alphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"

def encrypt(plaintext, key):
  key_length = len(key)
  key_as_int = [ukrainian_alphabet.index(i) for i in key]
  plaintext_int = [ukrainian_alphabet.index(i) for i in plaintext]
  ciphertext = ''
  for i in range(len(plaintext_int)):
    value = (plaintext_int[i] + key_as_int[i % key_length]) % len(ukrainian_alphabet)
    ciphertext += ukrainian_alphabet[value]
  return ciphertext

def decrypt(ciphertext, key):
  key_length = len(key)
  key_as_int = [ukrainian_alphabet.index(i) for i in key]
  ciphertext_int = [ukrainian_alphabet.index(i) for i in ciphertext]
  plaintext = ''
  for i in range(len(ciphertext_int)):
    value = (ciphertext_int[i] - key_as_int[i % key_length]) % len(ukrainian_alphabet)
    plaintext += ukrainian_alphabet[value]
  return plaintext

continues = True
while continues:
  print("1 - шифрувати\n2 - дешифрувати\n3 - вийти")
  choise = int(input("Що ви хочете зробити? "))
  if choise == 1:
    original_text = input('Введіть оригінальний текст: ').upper()
    key = input("Введіть ключ: ").upper()
    print(f"Зашифрований текст: {encrypt(original_text, key)}")
  elif choise == 2:
    cipher_text = input("Введіть зашифрований текст: ").upper()
    key = input("Введіть ключ: ").upper()
    print(f"Розшифрований текст: {decrypt(cipher_text, key)}")
  elif choise == 3:
    continues = False
