from Animal import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembangBiak, corak, berbisa):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.corak = corak 
        self.berbisa = berbisa
        
    def cetak_ular(self):
        super().cetak()
        print("Corak \t\t\t:", self.corak,
              "\nBerbisa \t\t:", self.berbisa)

Anaconda = Ular("Viper", "Daging", "Darat", "Bertelur", "Pelangi", "Iya")
Anaconda.cetak_ular()