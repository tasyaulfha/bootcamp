class Kalkulator:
    """contoh kelas kalkulator sederhana"""

    def __init__(self, i =12345):
        self.i = i

    def f(self):
        return 'hello world'

    @classmethod
    def tambah_angka(cls, angka1, angka2):
        return '{} + {} = {}'.format(angka1, angka2, angka1 + angka2)

    @staticmethod
    def kali_angka(angka1, angka2):
        return '{} x {} = {}'.format(angka1, angka2, angka1 * angka2)
Kalkulator.tambah_angka(1, 2)
k = Kalkulator()
print(k.tambah_angka(1, 2))

k = Kalkulator()
a = k.kali_angka(2, 3)
print(a)