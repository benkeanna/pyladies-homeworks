current_birth_number = input('Enter your birth number. ')


def correct_format(birth_number):
    if len(birth_number) == 11:
        if '/' in birth_number:
            pre, after = birth_number.split('/')
            if (len(pre) == 6 and len(after) == 4 and
                    pre.isnumeric() and after.isnumeric()):
                return True
            else:
                return False
        else:
            return False


def divisibility_by_11(birth_number):
    return int(birth_number[:6] + birth_number[7:]) % 11 == 0


def sex(birth_number):
    # ternary operator
    return 'woman' if birth_number[2] in ('5', '6') else 'man'


def date_of_birth(birth_number):
    day = int(birth_number[4:6])
    month = int(birth_number[2:4])
    year = int(birth_number[0:2])

    if month > 12:
        month = (month - 50)

    if year < 18:
        year = "20" + birth_number[0:2]
    else:
        year = "19" + birth_number[0:2]

    birth_date = [day, month, year]

    return birth_date


if correct_format(current_birth_number):
    print(('You entered correct birth number. '
           'Your date of birth is {}.{}. {} and you sex is {}.').format(
            *date_of_birth(current_birth_number), sex(current_birth_number)))

else:
    print('Birth number in wrong format.')
