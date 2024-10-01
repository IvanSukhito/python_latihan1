'''toko furniture ingin membuat sistem

dia bisa mengecek setiap harga dan diskon
cukup dengan memasukan input harga barangnya
dan cukup dengan memasukan total diskonnya

1. maka salesman dapat menghitung potongan dengan cepat
2. maka tahu komisi penjualan dari hasil potongan tersebut, mendapat bonus 5%
3. salesman tahu upah hariannya dari (upah harian=100rb + komisi no 2) dan upah bulananya dalam 20 hari masuk dari berhasil menjual 1 barang 1 aja 
'''

def potongan(harga_awal, diskon):
    harga = harga_awal - (harga_awal * diskon / 100)
    return harga


'''2'''
def komisi(potongan):
    komisi = potongan * 5/100
    return komisi


'''3'''
def upahharian(komisi):
    upahH = 100000 + komisi
    return upahH

#upah bulan jika dalam komisi yang sama setiap harinya
#20 hari x upah harian

def upahBulanan(upahharian):
    upah20hari = 20 * upahharian
    return upah20hari
