import os
os.system('cls')


import random

angka = [1,2,3,4,5]
angka_benar = random.choice(angka)
a = True
limit = 3
i = 0

print('Selamat datang di permainan tebak angkaa!')
print('Anda memiliki 3 kesempatan untuk menebak')


while a:
    i += 1
    tebakan= int(input('Masukkan angka acak (1-5): '))

    if tebakan == angka_benar:
        print('Tebakan Anda Benar!')
        print('Angka Benar = ', angka_benar)
        a = False
    elif tebakan > len(angka):
        print('Angka harus 1-5 tidak boleh kurang dan lebih!')
    else:
        if i == limit:
            print('Tebakan salah, belum berhasil')
            print('Angka yang dicari adalah', angka_benar)
            a = False
        else:
            print(f'Tebakan salah, anda memiliki {limit-i} kesempatan lagi')
