"""
Tipe data dictionary sekedata menghubungkan antara KEY dan VALUE
KVP = Key Value Pair
"""

kamus_indo_eng = {'anak': 'son', 'istri': 'wave', 'ayah': 'father', 'ibu': 'mother'}

print(kamus_indo_eng)
print(kamus_indo_eng['ayah'])
print(kamus_indo_eng['ibu'])

print('Data ini dikirimkan oleh server Gojek, untuk memberikan info driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal': '2020-05-23',
    'driver_list': [
        {'nama': 'Sigit', 'jarak': 10},
        {'nama': 'Wasis', 'jarak': 2000},
        {'nama': 'Subekti', 'jarak': 200},
    ]
}

print(data_dari_server_gojek)
print(f"Driver disekitar sini {data_dari_server_gojek['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][2]}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][1]}")
# mengambil jarak dari driver
print(f"Jarak driver adalah {data_dari_server_gojek['driver_list'][0]['jarak']} meter")
