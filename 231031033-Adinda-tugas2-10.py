print(f'Tugas 2 : buat program')
print()

print(f'1. program penjumlaham waktu')
print()

jam1 = int(input('masukan jam awal : '))
menit1 = int(input('masukan menit awal : '))
jam2 = int(input('masukan tambahan jam : '))
menit2 = int(input('masukan tambahan menit : '))

print(f'\nwaktu awal = {jam1}:{menit1}')
print(f"jumlah waktu yang mau di tambahkan = {jam2}:{menit2}")

hasil_jam = (jam1 + jam2)
hasil_menit = (menit1 + menit2)

if hasil_menit >= 60:
    hasil_jam += hasil_menit // 60
    hasil_menit = hasil_menit % 60

print(f'\nhasilnya adalah = {hasil_jam}:{hasil_menit}')
print('\n')


print(f'2. program selisih waktu')
print()

jam1 = int(input('masukan jam awal : '))
menit1 = int(input('masukan menit awal : '))
jam2 = int(input('masukan selisih jam : '))
menit2 = int(input('masukan selisih menit : '))

print(f'\nwaktu awal = {jam1}:{menit1}')
print(f"jumlah waktu yang mau diselisihkan = {jam2}:{menit2}")

hasil_jam = (jam1 - jam2)
hasil_menit = (menit1 - menit2)

if hasil_menit <= 0:
    hasil_jam -= 1
    hasil_menit += 60

print(f'\nhasilnya adalah = {hasil_jam}:{hasil_menit}')
print('\n')
