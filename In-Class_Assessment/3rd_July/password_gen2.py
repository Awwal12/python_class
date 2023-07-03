import random as r


def generatePassword(length):
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = lower_case.upper()
    special_characters = '!"@#$%^&*()_+?><~`'

    password = []
    for _ in range(length):
        our_choice = [r.choice(special_characters), str(
            r.randrange(0, 9)), r.choice(lower_case), r.choice(upper_case)]
        password.append(r.choice(our_choice))
    return ''.join(password)


pss = generatePassword(2)
print(pss)
with open(f'secretKey.txt', "w") as file:
    file.write(generatePassword(10))
