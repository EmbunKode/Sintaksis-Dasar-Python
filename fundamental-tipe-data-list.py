# tipe data skalar => tipe data sederhana
anak1 = "Sigit"
anak2 = "wasis"
anak3 = "Subekti"
anak4 = "Hamid"

print(anak1)
print(anak2)
print(anak3)
print(anak4)

# tipe data list/daftar/array

anak = ['Sigit', 'wasis', 'subekti', 'hamid']
print(anak)
# append => menambahkan list
anak.append('Dwi')
print(anak)

# Panggil anak ke 2
# \n merupakan new line atau jarak
print(f'\nHai {anak[1]}')

# Panggil semua anak
for a in anak:
    print(f'Hello {a}!')

# Panggil semua anak dengan cara yang ribet
for a in range(0, len(anak)):
    print(f'Hai anak {a}!')
