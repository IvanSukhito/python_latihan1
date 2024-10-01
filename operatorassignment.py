#operasi digabung dengan assignment

a = 5 
print("nilai a = ", a)

a += 1 
print("nilai a += 1, nilai a menjadi : ", a)
# sama aja a = a + 1
#artinya ialah a sebelumnya dipanggil kemudian ditambahkan dengan 1. Hasilnya dideklarasikan lagi dalam a

a -= 2 # artinya adalah a = a - 2
print("nilai a -= 2, nilai a menjadi : ", a)

a *= 5
print("nilai a *= 5, nilai a menjadi : ", a)

a /= 2
print("nilai a /= 2, nilai a menjadi : ", a)

b = 11
print("\n nilai b = ", b)

b = b // 2
print("nilai b %= 3, nilai b menjadi ", b)

c = 3
print("\n nilai c = ", c)

c **= 3
print("nilai c %= 3, nilai c menjadi ", c)

#operasi bitwise or
d = True
print("\n nilai d = ", d)
d |= False #sama kayak d = d(True) || False. salah 1 true maka hasilnya akan true
print("nilai d != true menjadi", d)
#sama aja kayak


#operasi bitwise and
e = True
print("\n nilai e = ", e)
e &= False #sama kayak e = e(True) && False. Salah 1 true hasilnya masih false
print("nilai e &= False menjadi ", e)

#operasi bitwise xor
f = True
print("\n nilai f = ", f)
f ^= False #sama kayak f = f(True) ^^ False. Salah 1 true hasilnya masih true
print("nilai f &= False menjadi ", f)