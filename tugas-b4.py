print()
print('Tugas Praktikum 4'.center(35))
nama = 'Adinda Aulia Rahmi'
nim  = '231031033'
prodi= 'Sistem Informasi B'
print(f'''
Nama\t: {nama}
NIM\t: {nim}
prodi\t: {prodi}''')


'''Dari beberapa string berikut, buatkan manipulasi kode
agar hasil outpunya sesuai'''
print()
str1 = 'duFort Frankel Von Neumann'
#output: NEUMANN DUFORT FRANKEL VON
up = str1.upper()
up = up.split()
print(up[-1],up[0],up[1],up[2])

str2 = 'duFort Frankel Von Neumann'
#output: dfv neumann
up   = str2.lower()
up = up.split()
print(up[0][0]+up[1][0]+up[2][0],(up[-1]))

str3 = 'duFort Frankel Von Neumann'
#output: DUFORT F V N
up = str3.upper()
up = up.split()
print(up[0],up[1][0],up[2][0],up[3][0])

str4 = 'duFOrt Frankel Von Neumann'
#output: N duFort f v
up = str4.split()
print(up[3][0],up[0][0:3]+up[0][3:].lower(),up[1][0].lower(),up[2][0].lower())

str5 = 'DuFort Frankel Von Neumann'
#output: NEUMANN d f v
up = str5.lower()
up = up.split()
print(up[-1].upper(),up[0][0],up[1][0],up[2][0])

str6 = 'duFort Frankel Von Neumann'
#output: NEUMANN DFV
up = str6.upper()
up = up.split()
print(up[-1],up[0][0]+up[1][0]+up[2][0])

str7 = '@duFort Frankel Von Neumann$'
#output: duFort Frankel Von NEUMANN
up = str7.split()
print(up[0].strip('@'),up[1],up[2],up[3].strip('$').upper())

str8 = '#duFort@Frankel@Von@Neumann$'
#output: duFort Frankel Von Neumann
up = str8.replace('@',' ')
up = up.strip('#$')
print(up)

str9 = '@duFort@#^Frankel*#(Von(#(Neumann$'
#output: duFort Frankel Von Neumann
up = str9.replace('@#^',' ').replace('*#(',' ').replace('(#(',' ')
up = up.strip('@$')
print(up)

str10 = '@DUFort@!^FraNkel!1(VoN(!(NeuMann^'
#output: duFort Frankel Von Neumann
up = str10.replace('@!^',' ').replace('!1(',' ').replace('(!(',' ')
up = up.strip('@^')
up = up.split()
print(up[0][0:2].lower()+up[0][2:6],up[1].capitalize(),up[2].capitalize(),up[3].capitalize())



print()