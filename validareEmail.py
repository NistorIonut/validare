#validare adreasa de email

import string


inc = 0
yahoo = input('Introduceti adresa de e-mail: ')
special_char = string.punctuation
if yahoo[-10:]== '@yahoo.com':
    name = yahoo[:-10]
    print(name)
    for c in special_char:
        if c in name and c != '.' and c !='-' and c !='_':
            print('Adresa de e-mail nu este valida')
            break
        else:
            inc += 1
        if inc == len(special_char):
            print('Adresa de e-mail este valida')
else:
    print('Adresa nu este valida')