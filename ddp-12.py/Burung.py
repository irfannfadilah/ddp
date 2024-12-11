from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembangBiak, jenisParuh, bunyi):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.jenisParuh = jenisParuh
        self.bunyi = bunyi
        
    def cetak_burung(self):
        super().cetak()
        print("Jenis Paruh\t\t:", self.jenisParuh,
              "\nBunyi \t\t\t:", self.bunyi)
        
Elang = Burung("Elang", "Daging", "Darat", "Bertelur", "Paruh Melengkung", "NgakNgakNgak")
Elang.cetak_burung()