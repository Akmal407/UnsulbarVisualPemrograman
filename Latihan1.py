class Makanan:
    def __init__(self, inputNama, inputHarga, inputStok):
        self.nama = inputNama
        self.harga = inputHarga
        self.stok = inputStok

roti1 = Makanan("Sari Roti", 4500, 500)
nasi1 = Makanan("Nasi Kuning", 10000, 100)

print (roti1.nama)
