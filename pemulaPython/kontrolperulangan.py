for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, ' adalah bilangan prima')

        """
        Digunakan jika Anda menginginkan sebuah pernyataan atau blok pernyataan (statement), namun tidak melakukan apapun - melanjutkan eksekusi sesuai dengan urutannya. Kontrol ini banyak digunakan saat Anda belum melakukan implementasi (atau menyiapkan tempat untuk implementasi), serta membiarkan program tetap berjalan saat misalnya Anda mengalami kegagalan atau exception.

"""
def sebuahfungsi():
    pass
##Ada kalanya Anda perlu untuk membuat sebuah list baru dari dengan sebuah operasi dari list sebelumny
#Cara 1
angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
  pangkat.append(n**2)
print(pangkat)

#Cara 2 List Comprehension
angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)

# Contoh3 menemukan item yang ada di kedua list
list1 = ['d', 'i', 'c', 'o']
list2 = ['d', 'i', 'n', 'g']
duplikat = []
for a in list1:
    for b in list2:
        if a == b:
            duplikat.append(a)

print(duplikat)  # Output ['d','i']

#Contoh4 Implementasi dengan list comprehension
list1 = ['d', 'i', 'c', 'o']
list2 = ['d', 'i', 'n', 'g']
duplikat = [a for a in list1 for b in list2 if a == b]
print(duplikat) # Output: ['d','i']

#kecilkan semua huruf
list_a=["Hello","World","In","python"]
small_list_a =[_.lower() for _ in list_a]
print(small_list_a)

list_a = range(1, 10, 2)
x = [[a**2, a**3] for a in list_a]
print(x)