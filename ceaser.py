shift = 4
word = "baka"

char_list = list(word)

ascii_list = [ord(ch) for ch in char_list]
print("Буквы в цифры:", ascii_list)

encrypted_ascii = [x + shift for x in ascii_list]
print("Зашифровано:", encrypted_ascii)

encrypted_word_list = [chr(code) for code in encrypted_ascii]
encrypted_word = ''.join(encrypted_word_list)
print("Зашифрованное слово:", encrypted_word)

decrypted_ascii = [x - shift for x in encrypted_ascii]
print("Убираем шаг:", decrypted_ascii)

decrypted_word_list = [chr(code) for code in decrypted_ascii]
decrypted_word = ''.join(decrypted_word_list)
print("Расшифрованное слово:", decrypted_word)
