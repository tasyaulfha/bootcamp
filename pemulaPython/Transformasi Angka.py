kata = 'dicoding'
kata = kata.upper()
print(kata)

kata ='DICODING'
kata = kata.lower()
print(kata)

##Metode ini akan menghapus whitespace pada sebelah kanan string atau akhir string.
print('Dicoding    '.rstrip())
## lstrip() yang bertugas untuk menghapus whitespace pada sebelah kiri atau awal string
print('    Dicoding'.lstrip())
print('    Dicoding    '.strip())
kata = 'CodeCodeDicodingCodeCode'
print(kata.strip('Code'))

##Metode startswith() akan mengembalikan nilai True jika string diawali dengan kata awalan tertentu yang kita inginkan, jika tidak maka akan mengembalikan nilai False.
print('Dicoding Indonesia'.startswith('Dicoding'))
##Metode endswith() ini kebalikannya dari metode startswith(), metode ini akan mengembalikan nilai True jika string diakhiri dengan kata akhiran tertentu yang kita inginkan, jika tidak maka akan mengembalikan nilai False.
print('Dicoding Indonesia'.endswith('Indonesia'))
print(' '.join(['Dicoding', 'Indonesia', '!']))

##metode split() adalah metode yang memisahkan substring berdasarkan delimiter tertentu
print('Dicoding Indonesia !'.split())

##Metode replace() dapat mengembalikan string baru dalam kondisi substring telah tergantikan dengan parameter yang dimasukkan.
string ="Ayo belajar Coding di Dicoding"
print(string.replace("Coding","Pemrograman"))

string = "Ayo belajar Coding di Dicoding karena Coding adalah bahasa masa depan"
print(string.replace("Coding", "Pemrograman", 1))

kata ='DICODING'
kata.isupper()

kata ='Dicoding'
kata.isupper()