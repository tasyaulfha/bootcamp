try:
    z=0
    x = 1/z
    print(x)
except ZeroDivisionError:
    print("Tidak bisa membagi angka dengan 0")

try:
    with open('contoh_tidak_ada.py') as file:
        print(file.read())
except(FileNotFoundError):
    print("File tidak ditemukan")