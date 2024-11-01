print()
kendaraan = ['Beat Karbu', 'Motor', 200, 'pink', 2]

kendaraan.append('13jt')
kendaraan.append('matic')
print(kendaraan)

kendaraan.insert(2, 'Honda')
print(kendaraan)

print(type(kendaraan))
print(type(kendaraan[0]))
print(type(kendaraan[1]))
print(type(kendaraan[2]))
print(type(kendaraan[3]))
print(type(kendaraan[4]))
print(type(kendaraan[5]))
print(type(kendaraan[6]))
print(type(kendaraan[7]))


print()

hitung_luas = int(input("pilih salah satu: 1. Hitung luas persegi, 2. Hitung luas lingkaran, 3. Hitung luas segitiga: "))

match hitung_luas:
    case 1:
        print('menghitung luas persegi')
        sisi = int(input("Masukkan Sisi: "))
        luas_persegi = sisi * sisi
        print(f'Luas persegi dari sisi {sisi} cm adalah: {luas_persegi} cm')
    case 2:
        print('menghitung luas lingkaran')
        jari_jari = int(input("Masukkan Jari-jari: "))
        luas_lingkaran = (jari_jari ** 2)
        print(f'Luas lingkaran dari jari-jari {jari_jari} cm adalah: {luas_lingkaran} cm')
    case 3:
        print('menghitung luas segitiga')
        alas = int(input("Masukkan Alas: "))
        tinggi = int(input("Masukkan Tinggi: "))
        luas_segitiga = 0.5 * alas * tinggi
        print(f'Luas segitiga dari alas {alas} cm dan tinggi {tinggi} cm adalah: {luas_segitiga} cm')