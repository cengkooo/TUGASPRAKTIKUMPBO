class Mobil:
    def __init__(self, jenis, kecepatan_maksimum):
        self.jenis = jenis
        self.kecepatan_maksimum = kecepatan_maksimum

    def info_kendaraan(self):
        return f"Jenis Kendaraan: {self.jenis}\nTop Speed: {self.kecepatan_maksimum} km/h\n"
    
    def bergerak(self):
        return "Mobil Bergerak Maju"

class Toyota(Mobil):
    def __init__(self, merk, jumlah_pintu, jenis, kecepatan_maksimum):
        super().__init__(jenis, kecepatan_maksimum)
        self.merk = merk
        self.jumlah_pintu = jumlah_pintu
    
    def info_mobil(self):
        return f"Merk Kendaraan: {self.merk}\nJumlah Pintu: {self.jumlah_pintu}\n"

    def bunyikan_klakson(self):
        return "FUFUFAFA!!!"

class MobilSport(Toyota):  # Warisi dari Toyota
    def __init__(self, merk, jumlah_pintu, jenis, kecepatan_maksimum, tenaga_kuda, harga):
        super().__init__(merk, jumlah_pintu, jenis, kecepatan_maksimum)
        self.__tenaga_kuda = tenaga_kuda
        self.__harga = harga

    def get_tenaga_kuda(self):
        return self.__tenaga_kuda
    
    def set_tenaga_kuda(self, value):
        self.__tenaga_kuda = value
    
    def get_harga(self):
        return self.__harga
    
    def set_harga(self, value):
        self.__harga = value
    
    def info_mobil_sport(self):
        return f"Tenaga Kuda: {self.__tenaga_kuda} HP\nHarga: ${self.__harga:,}\n"

    def mode_balap(self):
        return "BROOOMMMMMMMMMM!!!"

# Membuat objek MobilSport
MobilSport1 = MobilSport(
    merk="Supra",
    jumlah_pintu=2,
    jenis="Sport",
    kecepatan_maksimum=300,
    tenaga_kuda=500,
    harga=1000000
)

# Menampilkan informasi
print("="*40)
print(MobilSport1.info_kendaraan())
print(MobilSport1.info_mobil())
print(MobilSport1.info_mobil_sport())
print(MobilSport1.bergerak())
print(MobilSport1.mode_balap())
print(MobilSport1.bunyikan_klakson())
print("Tenaga Kuda:", MobilSport1.get_tenaga_kuda(), "HP")
print("Harga:", f"${MobilSport1.get_harga():,}")
print("="*40)