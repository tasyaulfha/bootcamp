class Kalkulator:
    def __init__(self,nilai=0):
        self.nilai=nilai
    def tambah_angka(self,angka1,angka2):
        self.nilai=angka1+angka2
        if self.nilai > 9 :
            print('kalkulator sederhana melebihi batas angka: {}' .format(self.nilai))
        return self.nilai
class KalkulatorKali(Kalkulator):
    def kali_angka(self, angka1, angka2):
        self.nilai= angka1*angka2
        return self.nilai

    def tambah_angka(self, angka1, angka2):
        if angka1 + angka2 <= 9:  # fitur ini sudah oke di kelas dasar, gunakan yang ada saja
            super().tambah_angka(angka1, angka2)  # panggil fungsi dari Kalkulator lalu isi nilai
        else:  # ini adalah fitur baru yang ingin diperbaiki dari keterbatasan kelas dasar
            self.nilai = angka1 + angka2
        return self.nilai
kk=KalkulatorKali()
a = kk.kali_angka(2,3)
print(a)

b= kk.tambah_angka(5,6)
print(b)

"""
Dalam proses pewarisan, kita bisa menimpa (override) definisi metode yang dimiliki oleh kelas dasar (kelas orang tua, yang diwarisi) dengan nama metode yang sama"""
