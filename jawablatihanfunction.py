import latihanfunction

harga_awal = int(input("Harga Barang : "))
diskon = int(input("Diskon dalam (%): "))


potongan = latihanfunction.potongan(harga_awal, diskon)
'''1'''
print("potongan : ", potongan)

'''2'''
hasilKomisi = latihanfunction.komisi(potongan)
print("hasil komisi :", hasilKomisi)

'''3'''

upahHarian = latihanfunction.upahharian(hasilKomisi)


print("Upah Harian : ", upahHarian)
print("Upah 20 Hari : ", latihanfunction.upahBulanan(upahHarian))
