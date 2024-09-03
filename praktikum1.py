#jika ingin memasukan input

#ada 2 cara

#string
input_nama = input("Masukan Nama Anda : ")
print("Nama Saya = ", input_nama, "type data : ", type(input_nama))

#integer atau float
input_nim = input("Nim Kamu Berapa : ")
print("Nim Saya :", input_nim, "type datanya apa : ", type(input_nim))

input_tahunlahir = int(input("Masukan Tahun lahir kamu :")) 
print("Tahun lahir ku, ", input_tahunlahir, "Type Datanya apa :", type(input_tahunlahir))

#program umur
tahun_sekarang = 2024
umur = tahun_sekarang - input_tahunlahir
print("Umur Ku :", umur)

#looping nama 5 kali
#tugas_iNama = input("Masukan Nama Anda :")
for i in range(5):
    tugas_iNama = input("Masukan Nama Anda :")
    print("Nama Saya : ", tugas_iNama)

#looping dan input nama sbyk n kali

nilaiLooping = int(input("Mau Looping Berapa Banyak : "))
for i in range(nilaiLooping):
    tugas_iNama = input(f"Input Nama Ke{i+1}: ")
    print("Nama Ke ",i+1," : ", tugas_iNama)