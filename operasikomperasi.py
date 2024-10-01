#operasi komparasi

#setiap hasil dari operasi komperasi adalah boolean true/false

# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 3

#lebih besar dari > 
print("\n=== LEBIH BESAR DARI (>) ===")
hasil = a > 3
print(f"{a} > 3  = {hasil}")

hasil = b > 3
print(f"{b} > 3 = {hasil}")

hasil = b > 2 
print(f"{b} > 2 = {hasil}")

#lebih kurang dari
print("\n=== KURANG DARI (<) ===")
hasil = a < 3
print(f"{a} < 3  = {hasil}")

hasil = b < 3
print(f"{b} < 3 = {hasil}")

hasil = b < 2 
print(f"{b} < 2 = {hasil}")

print("\n=== BESAR DARI SAMA DENGAN (>=) ===")
hasil = a >= 3
print(f"{a} >= 3  = {hasil}")

hasil = b >= 3
print(f"{b} >= 3 = {hasil}")

hasil = b >= 2 
print(f"{b} >= 2 = {hasil}")


print("\n=== KURANG DARI SAMA DENGAN (<=) ===")
hasil = a <= 3
print(f"{a} <= 3  = {hasil}")

hasil = b <= 3
print(f"{b} <= 3 = {hasil}")

hasil = b <= 2 
print(f"{b} <= 2 = {hasil}")

print("\n=== SAMA DENGAN (==) ===")
hasil = a == 3
print(f"{a} == 3  = {hasil}")

hasil = b == 3
print(f"{b} == 3 = {hasil}")

hasil = b == 2 
print(f"{b} == 2 = {hasil}")

print("\n=== BUKAN SAMA DENGAN (!=) ===")
hasil = a != 3
print(f"\n{a} != 3  = {hasil}")

hasil = b != 3
print(f"{b} != 3 = {hasil}")

hasil = b != 2 
print(f"{b} != 2 = {hasil}")

#is sebagai komperasi object identiti
# x = 10
# y = 10
# print("\n=== is dan is not ===")
# hasil = x is y
# print(f"\n x is y  = {hasil}")

# hasil = x is not y
# print(f" x is not y = {hasil}")

# x = 10
# y = 20
# print("\n=== is dan is not ===")
# hasil = x is y
# print(f"\n x is y  = {hasil}")

# hasil = x is not y
# print(f" x is y = {hasil}")
