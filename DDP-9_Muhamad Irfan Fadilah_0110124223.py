# Buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius. 
# Fungsi ini harus mengembalikan suhu yang dikonversi ke Fahrenheit.
("---- Mengkonversi suhu fahrenheit ke suhu celcius ----")
def celcius_ke_fahrenheit(celcius):
    return (celcius * 9/5 ) + 32
print (celcius_ke_fahrenheit(23))
print (celcius_ke_fahrenheit(64))

# Buatlah sebuah fungsi bernama is_genap yang menerima satu argumen: bilangan bulat. 
# Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan False jika bilangan tersebut ganjil
("---- Menampilkan true or false dari bilangan bulat ----")
def is_genap(bilangan):
    return bilangan % 2 == 0
print (is_genap(8))
print (is_genap(3))

# Buatlah fungsi untuk melihat ketrangan lulus atau tidak lulus : 
# Jika nilai dibawah 75 tidak lulus, jika nilai diatas 75 lulus 
("---- Keterangan lulus atau tidak lulus ----")
def nilai_ujian(nilai):
    if nilai >= 75:
        return "lulus"
    else:
        return "tidak lulus"
print (nilai_ujian(98))
print (nilai_ujian(74))

# Buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumens
print("\n---- Nampilin bilangan ganjil ----")
def bilangan(angka):
    for i in range(1, angka, 2):
        print (i, end=" ")
bilangan(20)    
