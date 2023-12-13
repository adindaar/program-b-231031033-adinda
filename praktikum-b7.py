import os
os.system('cls')

a = True

while a:
    jawab = input('Apakah ingin melanjutkan? (y/n)')
    if jawab == 'y':
        print('Selamat Datang Lagi!')
        a = True

    elif jawab == 'n':
        print('Sampai Ketemu Lagi:D')
        a = False

    else:
        os.system('cls')
        print('Jangan aneh-aneh deh :.)')
        a = True
