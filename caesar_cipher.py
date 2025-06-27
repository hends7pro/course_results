# простой скрипт для использования (де)шифрования по алгоритму Цезаря
encryption_or_decryption = input("шифрование или дешифрование?: ")   # выбор режима работы скрипта "шифрование" или "дешифрование"
language = input("алфавит? (русский или английский поддерживаются): ")     # выбор алфавита "русский" или "английский"
k = int(input('Шаг сдвига (со сдвигом вправо)?'))   # запрашиваем сдвиг для работы алгоритма
s = input("строка для операции: ")    # кладем строку для операции (де)шифрования

def get_msg(code_type, lang, shift):
    # объявляем переменные
    global encryption_or_decryption
    alphabet_RU = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    alphabet_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    alphabet_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_en = 'abcdefghijklmnopqrstuvwxyz'
    k = shift
    s1 = ''

    # тело функции
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

# вызов функции и вывод конечного результата
print(get_msg(encryption_or_decryption, language, k))
