print('praktikum-3\n\n')
print('Nama Lengkap : ADINDA AULIA RAHMI')
print('NIM          : 231031033')
print('Prodi        : Sistem Informasi B')

#############################################

a = True
b = False

print('\n==========NAND==========')
hasil = not (a and a)
print(a,'nand',a,'adalah =',hasil)
hasil = not (a and b)
print(a,'nand',b,'adalah =',hasil)
hasil = not (b and a)
print(b,'nand',a,'adalah =',hasil)
hasil = not (b and b)
print(b,'nand',b,'adalah =',hasil)

print('\n==========NOR==========')
hasil = not (a or a)
print(a,'nor',a,'adalah =',hasil)
hasil = not (a or b)
print(a,'nor',b,'adalah =',hasil)
hasil = not (b or a)
print(b,'nor',a,'adalah =',hasil)
hasil = not (b or b)
print(b,'nor',b,'adalah =',hasil)

print('\n==========NXOR==========')
hasil = not (a ^ a)
print(a,'nxor',a,'adalah =',hasil)
hasil = not (a ^ b)
print(a,'nxor',b,'adalah =',hasil)
hasil = not (b ^ a)
print(b,'nxor',a,'adalah =',hasil)
hasil = not (b ^ b)
print(b,'nxor',b,'adalah =',hasil) 

# INI OPERATOR MEMBERSHIP

print('\n==========IN==========')
nama = 'adinda aulia rahmi'

test = 'di' 
cek = test in nama
print(test,'ada di', nama,'adalah=',cek)

test = 'id' 
cek = test in nama
print(test,'ada di', nama,'adalah=',cek)
 
test1 = 'a'
test2 = 'i'
test3 = 'u'
test4 = 'e'
test5 = 'o'

cek = test1 in nama
print(test1,'ada di', nama,'adalah=',cek)

cek = test2 in nama
print(test2,'ada di', nama,'adalah=',cek)

cek = test3 in nama
print(test3,'ada di', nama,'adalah=',cek)

cek = test4 in nama
print(test4,'ada di', nama,'adalah=',cek)

cek = test5 in nama
print(test5,'ada di', nama,'adalah=',cek)

##################################################### tugas

print('\n==========NOT IN==========')
nama = 'adinda aulia rahmi'

test = 'di' 
cek = test not in nama
print(test,'tidak ada di', nama,'adalah=',cek)

test = 'id' 
cek = test not in nama
print(test,'tidak ada di', nama,'adalah=',cek)
 
test1 = 'a'
test2 = 'i'
test3 = 'u'
test4 = 'e'
test5 = 'o'

cek = test1 not in nama
print(test1,'tidak ada di', nama,'adalah=',cek)

cek = test2 not in nama
print(test2,'tidak ada di', nama,'adalah=',cek)

cek = test3 not in nama
print(test3,'tidak ada di', nama,'adalah=',cek)

cek = test4 not in nama
print(test4,'tidak ada di', nama,'adalah=',cek)

cek = test5 not in nama
print(test5,'tidak ada di', nama,'adalah=',cek)

###########################################################

# INI OPERATOR BITWISE

print('\n')
a = 17 
b = 11
a += 60
b += 80
print('==========AND==========')
print('Nilai',a,'biner adalah     =',format(a,'09b'))
print('Nilai',b,'biner adalah     =',format(b,'09b'))
print('----------------------------------------AND')
c = a & b
print('Nilai',a,'&',b,'biner adalah=',format(c,'09b'))

############################################################ tugas

print('\n==========OR==========')
print('Nilai',a,'biner adalah     =',format(a,'09b'))
print('Nilai',b,'biner adalah     =',format(b,'09b'))
print('----------------------------------------OR')
c = a | b
print('Nilai',a,'|',b,'biner adalah=',format(c,'09b'))

print('\n==========XOR==========')
print('Nilai',a,'biner adalah       =',format(a,'09b'))
print('Nilai',b,'biner adalah       =',format(b,'09b'))
print('------------------------------------------XOR')
c = a ^ b
print('Nilai',a,'Xor',b,'biner adalah=',format(c,'09b'))

##############################################################

print('\n==========NOT==========')
c = ~a
print('Nilai',a,'biner adalah     =',format(a,'09b'))
print('Nilai not',a,'biner adalah =',format(c,'09b'))

############################################################## tugas

c = ~b
print('Nilai',b,'biner adalah     =',format(b,'09b'))
print('Nilai not',b,'biner adalah =',format(c,'09b'))

##############################################################

print('\n==========Left Shift==========')
c = a << 2
print('Nilai',a,'biner adalah      =',format(a,'09b'))
print('Nilai',a,'<< 2 biner adalah =',format(c,'09b'))
c = b << 2
print('Nilai',b,'biner adalah      =',format(b,'09b'))
print('Nilai',b,'<< 2 biner adalah =',format(c,'09b'))

print('\n==========Right Shift==========')
c = a >> 2
print('Nilai',a,'biner adalah      =',format(a,'09b'))
print('Nilai',a,'>> 2 biner adalah =',format(c,'09b'))
c = b >> 2
print('Nilai',b,'biner adalah      =',format(b,'09b'))
print('Nilai',b,'>> 2 biner adalah =',format(c,'09b'))

############################################################## Tugas

print('\n==========Not And==========')
print('Nilai',a,'biner adalah           =',format(a,'09b'))
print('Nilai',b,'biner adalah           =',format(b,'09b'))
print('----------------------------------------NOT AND')
c = ~(a & b)
print('Nilai',a,'not And',b,'biner adalah=',format(c,'09b'))

print('\n==========Not Or==========')
print('Nilai',a,'biner adalah          =',format(a,'09b'))
print('Nilai',b,'biner adalah          =',format(b,'09b'))
print('----------------------------------------NOT OR')
c = ~(a | b)
print('Nilai',a,'not or',b,'biner adalah=',format(c,'09b'))

print('\n==========Not Xor==========')
print('Nilai',a,'biner adalah           =',format(a,'09b'))
print('Nilai',b,'biner adalah           =',format(b,'09b'))
print('----------------------------------------NOT XOR')
c = ~(a ^ b)
print('Nilai',a,'not Xor',b,'biner adalah=',format(c,'09b'))

print('\n==========Not << 2==========')
c = ~(a << 2)
print('Nilai',a,'biner adalah          =',format(a,'09b'))
print('Nilai',a,'not << 2 biner adalah =',format(c,'09b'))
c = ~(b << 2)
print('Nilai',b,'biner adalah          =',format(b,'09b'))
print('Nilai',b,'not << 2 biner adalah =',format(c,'09b'))

print('\n==========Not >> 2==========')
c = ~(a >> 2)
print('Nilai',a,'biner adalah          =',format(a,'09b'))
print('Nilai',a,'not >> 2 biner adalah =',format(c,'09b'))
c = ~(b >> 2)
print('Nilai',b,'biner adalah          =',format(b,'09b'))
print('Nilai',b,'not >> 2 biner adalah =',format(c,'09b'))
