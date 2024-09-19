inputNama = input("Masukan Nama Mobil : ")

mobil = {
    "name" : inputNama,
    "merek" : "Mitsubishi",
    "harga" : 500000000,
    "tahun" : 2018
}

mobil["umur"] = f"{2024 - mobil['tahun']} tahun"
#print(mobil)
print(f"Nama Mobil : {mobil['name']}")
print(f"Merek Mobil : {mobil['merek']} ")
print(f"harga Mobil : {mobil['harga']}")
print(f"Tahun Mobil : {mobil['tahun']}")
print(f"Umur Mobil : {mobil['umur']}")
# print(f"mobil Name : {mobil['name']}")
# print(f"mobil Name : {mobil['name']}")

# string1 = 'Hello'
# string2 = "Hello"

# print(string1 == string2)