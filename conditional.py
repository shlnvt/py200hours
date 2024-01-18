"""Conditional Python
Conditional Python adalah sebuah konsep penting dalam pemrograman untuk membuat sebuah keputusan berdasarkan kondisi tertentu. Dalam Python, pernytaan kondisional menggunakan If, Else dan Elif
"""

x = 10

if x > 5:
    print("Nilai x lebih besar dari 5")
else:
    print("Nilai x tidak lebih dari 5")

""" Operator Perbandingan
Operator perbandingan digunakan untuk membandingkan dua nilai dan menghasilkan sebuah kebenaran (True atau False)
"""
a = 7
b = 5

if a > b:
    print("a lebih besar dari b")
else:
    print("a tidak lebih besar dari b")

""" Kondisional Bersarang
Pengkondisian bersarang memungkina kita menyusun beberapa pernyataan kondisional di dalam satu blok
"""
nilai_tuton = 80

if nilai_tuton >= 70:
    print("Lulus")
    if nilai_tuton == 100:
        print("Nilai sempurna!")
else:
    print("Belum Lulus")

"""
Kondisional menggunakan Elif
Pernyataan Elif digunakan untuk memnentukan kondisi alternatif jika kondisi sebelumya tak terpenuhi.
"""
umur = 18

if umur < 12:
    print("Umur Anda masih Anak-anak")
elif 12 <= umur < 18:
    print("Umur Anda sudah Remaja")
else:
    print("Umur Anda sudah Dewasa")

"""Perbedaan dari kondisional bersarang (if nested) dan elif
Kondisional bersarang digunakan untuk menguji sebuah kondisi secara bertahap atau membuat keputusan yang kompleks dengan menguji beberapa kondisi secara berurutan.

Kondisional Elif digunakan untuk menyederhanakan pengujian kondisi alternatif. Elif sangat berguna bila ada beberapa opsi yang harus diuji dan kita ingin menjalankan salah satu blok kode yang sesuai dengan kondisi pertama yang terpenuhi.
"""

""" Operator Logika pada Kondisional Python
Operator logika yang dipakai adalah and, or dan not. Operator ini berfungsi untuk menggabungkan beberapa kondisi
"""
usia = 26
pengalaman = 2

if usia <= 25 and pengalaman >= 1:
    print("Anda memenuhi syarat")
else:
    print("Anda belum memenuhi syarat")

if usia <= 25 or pengalaman == 2:
    print("Anda memenuhi syarat")
else:
    print("Anda belum memenuhi syarat")

""" Mencari angka genap dan ganjil
Rumus untuk mencari angka genap adalah habis dibagi dengan atau kelipatannya.
Contoh angka genap yang habis dibagi dengan 2
"""
def cek_angka(angka):
    if angka % 2 == 0:
        return "Angka {} adalah genap.".format(angka)
    else:
        return "Angka {} adalah ganjil.".format(angka)

"""Input dari pengguna"""
angka_input = int(input("Masukkan angka: "))

"""Memanggil fungsi cek_angka"""
print(cek_angka(angka_input))

"""Mencari tahun Kabisat
Tahun kabisat adalah tahun yang habis dibagi 4 namum tidak habis dibagi 100, atau tahun yang habis dibagi 400.
"""
def cek_tahun_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return "Tahun {} adalah tahun kabisat.".format(tahun)
    else:
        return "Tahun {} bukan tahun kabisat".format(tahun)

"""input tahun"""
tahun_input = int(input("Masukkan tahun: "))

"""Memanggil fungsi dan cetak hasil"""
print(cek_tahun_kabisat(tahun_input))

"""Mencari BMI
Rumus BMI = berat badan / (tinggi ** 2)
"""
def kalkulator_bmi(berat_badan, tinggi_badan):
    bmi = berat_badan / (tinggi_badan ** 2)

    if bmi < 18.5:
        return "BMI Anda adalah {:.2f}, kategori: Kurang berat badan.".format(bmi)
    elif 18.5 <= bmi < 24:
        return "BMI Anda adalah {:.2f}, kategori: Normal (sehat).".format(bmi)
    elif 25 <= bmi < 29.9:
        return "BMI Anda adalah {:.2f}, kategori: Kelabihan berat badan.".format(bmi)
    else:
        return "BMI Anda adalah {:.2f}, kategori: Obesitas".format(bmi)

"""Input berat badan dan tinggi badan"""
bb_input = float(input("Masukkan berat badan (kg): "))
tb_input = float(input("Masukkan tinggi (m): "))

"""Memanggil fungsi kalkulator_bmi"""
print(kalkulator_bmi(bb_input, tb_input))