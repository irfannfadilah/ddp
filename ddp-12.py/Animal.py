class Animal:
    def __init__(self, nama, makanan, hidup, berkembangBiak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangBiak = berkembangBiak
        
    def cetak(self):
        print("Nama \t\t\t:", self.nama,
              "\nMakanan \t\t:", self.makanan,    
              "\nHidup \t\t\t:", self.hidup,   
              "\nBerkembang Biak\t\t:", self.berkembangBiak
              ) 

# objek = Animal("Buaya","Daging", "Amfibi", "Bertelur")
# print(objek.cetak())