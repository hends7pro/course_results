encryption_or_decryption = "дешифрование"   # choose "шифрование" or "дешифрование"
language = "английский"     # choose "русский" or "английский"
#k = int(input('Шаг сдвига (со сдвигом вправо)?'))

s = "is"     # enter the input string


def get_msg(code_type, lang, shift):
    global encryption_or_decryption
    alphabet_RU = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    alphabet_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    alphabet_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_en = 'abcdefghijklmnopqrstuvwxyz'
    k = shift
    s1 = ''
    if encryption_or_decryption.lower() == 'шифрование':
        if language.lower() == 'русский':
            for c in s:
                if c in alphabet_RU:
                    s1 += alphabet_RU[(alphabet_RU.find(c) + k) % 32]
                elif c in alphabet_ru:
                    s1 += alphabet_ru[(alphabet_ru.find(c) + k) % 32]
                else:
                    s1 += c
        elif language.lower() == 'английский':
            for c in s:
                if c in alphabet_EN:
                    s1 += alphabet_EN[(alphabet_EN.find(c) + k) % 26]
                elif c in alphabet_en:
                    s1 += alphabet_en[(alphabet_en.find(c) + k) % 26]
                else:
                    s1 += c
    if encryption_or_decryption.lower() == 'дешифрование':
        if language.lower() == 'русский':
            for c in s:
                if c in alphabet_RU:
                    s1 += alphabet_RU[(alphabet_RU.find(c) - k) % 32]
                elif c in alphabet_ru:
                    s1 += alphabet_ru[(alphabet_ru.find(c) - k) % 32]
                else:
                    s1 += c
        elif language.lower() == 'английский':
            for c in s:
                if c in alphabet_EN:
                    s1 += alphabet_EN[(alphabet_EN.find(c) - k) % 26]
                elif c in alphabet_en:
                    s1 += alphabet_en[(alphabet_en.find(c) - k) % 26]
                else:
                    s1 += c
    return s1


for i in range(26):
    print(get_msg(encryption_or_decryption, language, i))
