import latihanfunction

#SPG Pekan Raya Jakarta
#upah harian karyawan 100.000 
#komisi harian = total penjualan * 2%  
#upah harian + komisi
#upah bulanan = harian * 20

#print("Upah Harian : ")
#print("Upah Bulanan : ")
iPenjualan = int(input("Masukan Penjualan SPG Hari ini : "))

komisiHarian = iPenjualan * 5/100

upahHarian = latihanfunction.upahharian(komisiHarian)

upahBulanan = latihanfunction.upahBulanan(upahHarian)

print("\nKomisi Hari ini : ", komisiHarian)
print("\n upah Hari ini  : ", upahHarian)
print("\n Prediksi Upah Bulanan Jika Konsisten: ", upahBulanan)