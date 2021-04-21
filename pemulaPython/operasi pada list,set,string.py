contoh_list=[1,3,3,5,5,5,7,7,9]
print(contoh_list)
print(len(contoh_list))

contoh_set=set([1,3,3,3,5,5,5,7,7,7,9])
print(contoh_set)
print(len(contoh_set))


contoh_string="Belajar python"
print(contoh_string)
print(len(contoh_string))

genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(genap.count(6))
string = "Belajar Python di Dicoding sangat menyenangkan"
substring = "a"
print(string.count(substring))

angka = [2, 4, 6, 8]
huruf = ['P', 'Y', 'T', 'H', 'O', 'N']
gabung = angka + huruf
print(gabung)

learn = ['P', 'Y', 'T', 'H', 'O', 'N']
replikasi = learn * 2
print(replikasi)

tujuh = [7]*7
print(len(tujuh))
print(tujuh)

##Fungsi range() memberikan deret bilangan dengan pola tertentu.
# Untuk melakukan perulangan (misalnya for) dalam mengakses elemen list,

#1.     Range dengan 1 parameter n: membuat deret bilangan yang dimulai dari 0, sebanyak n bilangan.
for i in range (5):
    print(i)
#2.Range dengan 2 parameter n,p: membuat deret bilangan yang dimulai dari n,
# hingga sebelum p (bilangan p tidak ikut).
for i in range (1,11):
    print(i)
#3Range dengan 3 parameter n,p,q: membuat deret bilangan yang dimulai dari n, hingga sebelum p (bilangan p tidak ikut),
# dengan setiap elemennya memiliki selisih q.
print([_ for _ in range(0,20,5)])

#in dan not in
#Untuk mengetahui sebuah nilai atau objek ada dalam list,
# Anda dapat menggunakan operator in dan not in.

kalimat= "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('tidak' not in kalimat)

#Memberikan nilai untuk multiple variable
data = ['shirt', 'white', 'L']
apparel = data[0]
color = data[1]
size = data[2]
#Anda dapat melakukannya dengan cara:
data = ['shirt', 'white', 'L'] # From List
apparel, color, size = data
data = ('shirt', 'white', 'L')  # From Tuple
apparel, color, size = data