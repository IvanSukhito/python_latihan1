#operasi logic atau boolean
#OR, aND, NOT, XNOr


#OR, kesimpulannya jika salah satu TRUE maka akan bernilai TRUE
print("====== OR ======")
a = False
b = False
c = a or b
print(f"{a} or {b} = {c}")
a = True
b = False
c = a or b
print(f"{a} or {b} = {c}")
a = False
b = True
c = a or b
print(f"{a} or {b} = {c}")
a = True
b = True
c = a or b
print(f"{a} or {b} = {c}")


#kesimpulan and, jika benar 2 2nya baru bernilai true
print("\n====== AND ======")
a = False
b = False
c = a and b
print(f"{a} and {b} = {c}")
a = True
b = False
c = a and b
print(f"{a} and {b} = {c}")
a = False
b = True
c = a and b
print(f"{a} and {b} = {c}")
a = True
b = True
c = a and b
print(f"{a} and {b} = {c}")

#XOR, Kesimpulannya dia akan true jika salah satu aja yang true
print("\n====== XOR ======")
a = False
b = False
c = a ^ b
print(f"{a} ^ {b} = {c}")
a = True
b = False
c = a ^ b
print(f"{a} ^ {b} = {c}")
a = False
b = True
c = a ^ b
print(f"{a} ^ {b} = {c}")
a = True
b = True
c = a ^ b
print(f"{a} ^ {b} = {c}")

print("\n ===== NOT =====")
a = True
print(f"Data A adalah : {a}")
print("=======================NOT")
a = not a
print(f"Data A setelah di not : {a} ")