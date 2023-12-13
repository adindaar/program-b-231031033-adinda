import os
os.system('cls')

print('BIODATA'.center(50))
print('\n')
biodata = {'namal' : 'Adinda Aulia Rahmi',
           'namap' : 'Dinda',
           'nim' : 231031033,
           'kelas' : 'SI23-B',
           'prodi' : 'Sistem Informasi',
           'ttl' : 'Parepare, 17 November 2004',
           'agama' : 'Islam',
           'alamat' : 'Jl. A. Mappangara',
           'asalsklh' : 'UPT SMK Negeri 3 Parepare',
          }
print('Nama Lengkap         : ',biodata['namal'])
print('Nama Panggilan       : ',biodata['namap'])
print('NIM                  : ',biodata['nim'])
print('Kelas                : ',biodata['kelas'])
print('Program Studi        : ',biodata['prodi'])
print('Tempat Tanggal Lahir : ',biodata['ttl'])
print('Agama                : ',biodata['agama'])
print('Alamat               : ',biodata['alamat'])
print('Asal Sekolah         : ',biodata['asalsklh'])
print('\n')
print('Tipe data dari biodata adalah',type(biodata))
print('\n')