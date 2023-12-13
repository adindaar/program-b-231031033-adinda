import os
os.system('cls')

pwd_benar = 'si23b'
a = True
i = 0
limit = 3

while a:
    i += 1
    pwd = input('Masukkan Password: ')
    if pwd == pwd_benar:
        print('Selamat Anda Login!')
        a = False
    else:
        print('Password salah')
        if i == limit:
            a = False
            print('Anda Kehabisan Kesempatan')
        else:
            print(f'kesempatan anda tersisah {limit-i} kali')
        
#tugas buat program tebak angka 1-10 (3kali percobaan)pesan tebakan salah anda memiliki 2 kesempatan, anda tersisah 1 kesempatan, anda belu