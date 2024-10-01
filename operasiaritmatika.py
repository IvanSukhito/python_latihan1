a = 10
b = 3


#operasi tambah
hasil = a + b
print(f"{a} + {b}={hasil}")
#operasi kurang
hasil = a - b
print(f"{a} - {b}={hasil}")
#operasi kali
hasil = a*b
print(f"{a} * {b}={hasil}")
#operasi bagi
hasil = a/b
print(f"{a} : {b}={round(hasil,2)}")

#operasi eksponen / pangkat
hasil = a**b    
print(f"{a} ^ {b} = {hasil}")

#Operasi modulus
hasil = a%b
print(f"{a} modulus {b} = {hasil}")

#Operasi floor division
hasil = a // b
print(f"{a} // {b} = {hasil}")

#operasi
w = 2
x = 10
y = 15
z = 5

#operasi yang didahulukan
#1.()
#2.eksponen **
#3.perkalian dan teman temannya * / ** % //
#4.pertambahan

total = (x + y) / z
print(f"{x} + {y} / {z} = {round(total)}")

total = z ** w + y / x
print(f"{z} ** {w} + {y} / {x} = {total}")

total = (z ** w + y) / x
print(f"({z} ** {w} + {y}) / {x} = {total}")