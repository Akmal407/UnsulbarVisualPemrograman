class kendaraan:
  def __init__(self, merk, harga, tahun):
    self.merk = merk
    self.harga = harga
    self.tahun = tahun
 
  def printname(self):
    print(self.merk, 'Harga: Rp,',self.harga, 'Keluaran Tahun :',self.tahun)

class motor(kendaraan):
  pass

mot1 = motor("Supra", "13.000.000", "2013")
mot1.printname()
mot1 = motor("NMAX", "30.000.000", "2020")
mot1.printname()
