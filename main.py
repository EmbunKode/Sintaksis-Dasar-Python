# KONSTRUKSI DASAR PYTHON
# SEQUENTIAL : Eksekusi Beruturan
print('Hello World!')
print('By Sigit Wasis Subekti')
print('Tanggal 24 Juli 2020')
print('---' * 3)

# PERCABANGAN: Dengan terpilih
ingin_cepat = True
if ingin_cepat:
    print('Jalan lurus saja!')
else:
    print('Cari jalan lain')

# PERULANGAN
jumlah_anak = 10

for index_anak in range(0, jumlah_anak + 1): # jumlah perulangan = 5 - 1 =4
    # menyisipkan variable ke dalam text maka gunakan f
    print(f'Halo anak {index_anak}')
