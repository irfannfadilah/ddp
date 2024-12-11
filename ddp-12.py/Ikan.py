from Animal import *

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembangBiak, alatPernapasan, harga):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.alatPernapasan = alatPernapasan
        self.harga = harga
        
    def cetak_ikan(self):
        super().cetak()
        print("Alat pernapasan \t:", self.alatPernapasan,
              "\nHarga \t\t\t:", self.harga)
        
Terimedan = Ikan("Teri medan", "Cacing laut", "Air laut", "Bertelur", "insang", 25000)
Gurame = Ikan("Gurame", "plankton", "Laut", "Beranak", "Insang", 35000)
Terimedan.cetak_ikan()
Gurame.cetak_ikan()