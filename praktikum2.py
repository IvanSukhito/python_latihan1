mobil = {
    "brand" : "Ferrari",
    "model" : "Sport",
    "Harga" : 1000000,
    "Tahun" : 1998
}

a = mobil.get("brand")
print(f"Merek Mobil : {a}")

b = mobil["Tahun"]
print(f"Mobil ini keluaran tahun : {b}")

#pajak

#umur
TahunSekarang = 2024
Umur_mobil = TahunSekarang - mobil['Tahun']
print(f"Usia mobil ialah :", Umur_mobil)

#pajak
pajak = mobil['Harga']*(Umur_mobil/100)
print(f"Pajak Mobil Ialah : ", pajak)