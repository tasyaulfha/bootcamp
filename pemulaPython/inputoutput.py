nama="Dicoding"
umur=5
print("Umur %s adlaah %d tahun." % (nama, umur))

#Contoh menambahkan objek selain string (otomatis dikonversi):
angka = [7,9,11,13]
print("Angka saya : %s " %angka)
"""
%s - String
%d - Integers
%f - Bilangan Desimal
%.<digit>f - Bilangan desimal dengan sejumlah digit angka dibelakang koma.
%x/%X - Bilangan bulat dalam representasi Hexa (huruf kecil/huruf besar)
"""

a,b = 10,11
a,b
print('a: %x and b: %X' %(a,b))

nilai = input('Masukkan angka : ')
print(nilai)

"""
Jika input merupakan string berisi ekspresi matematika, maka konversi dengan int() atau float() akan menghasilkan error. Anda dapat menggunakan fungsi eval() yang sekaligus juga berfungsi menyelesaikan ekspresi matematika. Anda akan mempelajari lebih jauh mengenai fungsi pada modul Fungsi.
"""

print(eval('90+10'))