class Person:
    def __init__(self, nama, umur, gender):
        self.nama = nama
        self.umur = umur
        self.gender = gender
        
    def jalan(self):
        print(f'{self.nama} bisa berjalan')
        
    def ngomong(self):
        print(f'Dia berbicara karena  ')
        
class supir (Person):
    def __init__(self, nama, umur, gender, sim):
        super().__init__(nama, umur, gender) 
        self.sim = sim
        
    def nyupir(self):
        print(f'{self.nama} bisa nyupir karena memiliki SIM {self.sim}')       
        
class Mahasiswa(Person):
    def __init__(self, nama, umur, gender, nim):
        super().__init__(nama, umur, gender)
        self.nim = nim
        
    def belajar(self):
        print(f'{self.nama} sedang belajar dengan nim {self.nim}')      
        
bayu = Person("bayu", 28, "laki-laki")
bayu.jalan
bayu.ngomong

andi = supir("andi", 23, "laki-laki", "A")
andi.jalan 
andi.ngomong
andi.nyupir

bunga = Mahasiswa("Bunga", 21, "Perempuan", 1234)
bunga.belajar