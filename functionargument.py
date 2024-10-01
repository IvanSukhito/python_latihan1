'''Fungsi dengan argument (input)'''

#bisa dimasukin suatu input / parameter / argument

def hello_world(inputNama):
    '''fungsi hello_world menerima input dengan membawa variable inputNama'''
    print("Selamat Datang Dunia Wahai", inputNama)

# hello_world("Ucup")
# hello_world("Mamat")

def tambah(angka1, angka2):
    ''' Fungsi Tambah '''
    hasil = angka1 + angka2
    print("Hasil : ", hasil)


# tambah(100,55)
# tambah(1000000, 1)

def sayHi(anggota_boyband):
    #logicnya
    nama1 = anggota_boyband[0]
    nama2 = anggota_boyband[1]
    nama3 = anggota_boyband[2]

    print("Welcome our personinl :", nama1)
    print("Welcome our personinl :", nama2)
    print("Welcome our personinl :", nama3)

anggota_boyband = ["Coki", "Dudung", "Saep"]

sayHi(anggota_boyband)