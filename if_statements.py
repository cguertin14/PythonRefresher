def who_do_you_know():
    return [person.strip() for person in input('Who do you know: ').split(',')]

def ask_user():
    person = input('Enter a nama of someone you know: ')
    if person in who_do_you_know():
        print('You know {}!'.format(person))

ask_user()