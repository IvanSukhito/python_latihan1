#dictionary auto input

#nama
#nim
#kelas
nama = input("Masukan Nama Kalian : ")
nim = (int(input("Masukan Nim Kalian : ")))
kelas = input("Masukan Kelas Kalian : ")

#deklariskan

biodata_mahasiswa = {}

biodata_mahasiswa['nama'] = nama
biodata_mahasiswa['nim'] = nim
biodata_mahasiswa['kelas'] = kelas

print(biodata_mahasiswa)
#output  #berdasarkan hasil input nanti
# {
#     "nama" : "Ivan ",
#     "nim" : 32210108,
#     "kelas" : "1PSI"

# }