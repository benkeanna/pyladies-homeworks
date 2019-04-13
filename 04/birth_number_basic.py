birth_number = input('Enter your birth number.' )


if len(birth_number) == 11:
    if '/' in birth_number:
        pre, after = birth_number.split('/')
        if (len(pre) == 6 and len(after) == 4 and
                pre.isnumeric() and after.isnumeric()):
            correct_format = True
        else:
            correct_format = False
    else:
        correct_format = False

    if correct_format:
        divisibility_by_11 = int(birth_number[:6] + birth_number[7:]) % 11 == 0

        # ternary operator
        sex = ('woman' if birth_number[2] in ('5', '6') else 'man')

        date_of_birth = [birth_number[:2], birth_number[2:4], birth_number[4:6]]

        if sex == 'woman':
            date_of_birth[2] = (int(date_of_birth[2]) - 50)

        print(('You entered correct birth number. '
               'Your date of birth is {}.{}. {} and you sex is {}.').format(
                birth_number[:2], birth_number[2:4], birth_number[4:6], sex))

    else:
        print('Birth number in wrong format.')

else:
    print('Birth number in wrong format.')
