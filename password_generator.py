from random import choice


def get_pass_specs():
    digits = "0123456789"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    punctuation = "!#$%&*+-=?@^_."
    chars = digits + lowercase_letters + uppercase_letters + punctuation

    password_amount = int(input("Passwords amount: "))
    password_length = int(input("Password length: "))

    if not input("Include 0123456789? y/n: ") == 'y':
        chars = chars.replace(digits, "")
    if not input("Include ABCDEFGHIJKLMNOPQRSTUVWXYZ? y/n: ") == 'y':
        chars = chars.replace(uppercase_letters, "")
    if not input("Include abcdefghijklmnopqrstuvwxyz? y/n: ") == 'y':
        chars = chars.replace(lowercase_letters, "")
    if not input("Include !#$%&*+-=?@^_? y/n: ") == 'y':
        chars = chars.replace(punctuation, "")

    return password_length, chars, password_amount


def generate_password(length, character_set, amount):
    if amount == 1:
        print("Your new password is:")
    else:
        print("Your new passwords are:")
    for _ in range(amount):
        password = ''
        for _ in range(length):
            password += choice(character_set)
        print(password)


password_length, char_set, quantity = get_pass_specs()
generate_password(password_length, char_set, quantity)
