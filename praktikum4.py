inputNama = input("Masukan Nama Kalian : ")
inputNim = input("Masukan Nim : ")
input_Tugas1 = int(input("Nilai Tugas 1 : "))
input_Tugas2 = int(input("Nilai Tugas 2 : "))
input_Tugas3 = int(input("Nilai Tugas 3 : "))
input_Tugas4 = int(input("Nilai Tugas 4 : "))

def latihan(nama, nim, tugas1, tugas2, tugas3, tugas4):
    print("Nama Depan : ", nama)
    print("Nim : ", nim)
    avg = (tugas1 + tugas2 + tugas3 + tugas4) / 4
    print(f"Nilai Rata - Rata {nama} : {avg}")

latihan(inputNama, inputNim, input_Tugas1, input_Tugas2, input_Tugas3, input_Tugas4)
#latihan("Ivan Sukhito", 32210108, 90, 80, 80, 100)