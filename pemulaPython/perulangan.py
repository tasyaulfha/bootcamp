for huruf in 'Dicoding':
    print('Huruf : {}'.format(huruf))
flowers=['mawar','melati','anggrek']
for flower in flowers:
    print('Flower: {}'.format(flower))

    """
    Bedanya di Python, For tidak hanya untuk perulangan dengan jumlah finite (terbatas), 
    melainkan lebih ke fungsi yang dapat melakukan perulangan pada setiap jenis variabel berupa kumpulan atau urutan. Variabel yang dimaksud bisa berupa list, string, ataupun range. Jika sebuah list atau urutan berisi expression, maka Ia akan dievaluasi terlebih dahulu. Kemudian item pertama pada urutan/list akan diassign sebagai variabel iterating_var. Setelahnya
    , blok statement akan dieksekusi, berlanjut 
    ke item berikutnya, berulang, hingga seluruh urutan hab
    """

flowers=['mawar','melati','anggrek']
for index in range (len(flowers)):
    print('Flowers: {}'.format(flowers[index]))

count = 0
while (count < 7):
    print('Hitungannya adalah: {}'.format(count))
    count = count + 1

var = 1
while var == 1:  # This constructs an infinite loop
    num = input('Masukkan angka: ')
    print('Anda memasukkan angka: {}'.format(num))

while True:  # This constructs an infinite loop
    num = input('Masukkan angka: ')
    print('Anda memasukkan angka: {}'.format(num))

for i in range(0, 6):
    for j in range(0, 6 - i):
        print('*', end='')
    print()