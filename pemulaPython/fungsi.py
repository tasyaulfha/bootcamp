def cetak(param1):
    print(param1)
    return


# panggil
cetak("Panggilan Pertama")
cetak("Panggilan Kedua")

def kali(angka1,angka2):
    hasil=angka1*angka2
    print('Dicetak dari dalam fungsi: {}' .format(hasil))
    return hasil
keluaran=kali(10,20)
print('Dicetak sebagai kembalian: {}'.format(keluaran))

"""
Nilai kembalian dari sebuah fungsi dapat disimpan dalam sebuah variabel. Ini yang akan membedakan sebuah fungsi yang mengembalikan nilai dengan 
sebuah fungsi yang tidak mengembalikan nilai (sering disebut sebagai prosedur)
"""
def kuadrat(x):
    return x*x
a=10
k=kuadrat(a)
print("nilai kuadraat dari {} adalah {}".format(a,k))

def ubah(list_saya):
    list_saya=([1, 2, 3, 4])
    print('Nilai di dalam fungsi: {}'.format(list_saya))

list_saya=[10,20,30]
ubah(list_saya)
print('Nilai di luar fungsi: {}'.format(list_saya))
