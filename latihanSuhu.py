#latihan konversi satuan temperature

#program konversi celcius ke satuan lain

print(f"\n PROGRAM KONVERSI TEMPERATUR")

iSuhu = float(input("Masukan Suhu Dalam Celcius : "))

print(f"Suhu adalah : {iSuhu} Celcius")

celcius = iSuhu
#reamur = 4/5 C
reamur = (4/5) * celcius
print(f"Suhu Reamur adalah : {reamur} Reamur")

#fahrenhit= 9/5C + 32
fahrenheit = ((9/5) * celcius) + 32
print(f"Suhu Fahrenheit adalah : {fahrenheit} Fahrenheit")

#kelvin = C + 273
kelvin = celcius + 273
print(f"SUhu Kelvin adalah : {kelvin} Kelvins")

#fahrenheit ke kelvin
#hitung dulu nilai celcius = fahrenheit ke celcius
#selanjutnya kelvin = celcius + 273