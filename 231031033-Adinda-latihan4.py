pendapatan = int (input('Pendapatan: '))

if pendapatan >= 5001:
    persentase = 50
if pendapatan >= 4000:
    persentase = 40
if pendapatan >= 3000:
    persentase = 30
if pendapatan >= 2000:
    persentase = 20
if pendapatan >= 1000:
    persentase = 10

else:
    persentase = 0
bonus = pendapatan*(persentase/100)
total_pendapatan = pendapatan + bonus

print('Pendapatan', pendapatan)
print('Persentase', persentase)
print('Bonus', bonus)
print('Total Pendapatan', total_pendapatan)

