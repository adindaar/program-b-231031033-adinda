import pipes
import pkg_resources


nama = 'ADINDA AULIA RAHMI'
nim  = '231031033'
meet = 'Praktikum 4'
prodi = 'Sistem Informasi B'
email = 'adindaauliar11@gmail.com'
date = '11 Oktober 2023'
sp = 50
print(len(nama)) 

print('-'*sp)
print(nama.center(sp))
print(nim.center(sp))
print('\n'*2)
print(prodi.rjust(sp)+f'\r{meet}')
print(email.rjust(sp)+f'\r{date}')
print('-'*sp)

paragraf = '''Halo, selamat datang perkenalkan nama saya {} dengan NIM {} dari prodi {}. Ini adalah file {}.'''
p = paragraf.format(nama,nim,prodi,meet)
print(p)
 
print('--------8++++++++')
x = 9 #input
hasil = x>8
print(x,'hasilnya adalah',hasil)
print('--------8++++++++')
x = 9 #input
hasil = x<8
print(x,'hasilnya adalah',hasil)

print('--------4++++++++8---------')
x = 9
# cek1 = x>4 true
cek1 = x>4
# cek2 = x<8
cek2 = x<8
# hasil = cek1 and cek2 --> true
hasil = cek1 and cek2
# cetak hasil
print(x,'hasilnya adalah',hasil)

print('++++++++4---------8++++++++')
x = 2
# cek1 = x<4 true
cek1 = x>4
# cek2 = x>8
cek2 = x<8
# hasil = cek1 or cek2 --> true
hasil = cek1 or cek2
# cetak hasil
print(x,'hasilnya adalah',hasil)