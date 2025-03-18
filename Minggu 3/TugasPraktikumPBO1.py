from tkinter import *
import tkinter.font as font
import math

class Calculator:
    def __init__(self, value):
        self.value = float(value)
        try:
            # Konversi koma ke titik untuk decimal
            self.value = float(str(value).replace(',', '.'))
        except:
            self.value = 0.0
    
    def __add__(self, other):
        return Calculator(self.value + other.value)
    
    def __sub__(self, other):
        return Calculator(self.value - other.value)
    
    def __mul__(self, other):
        return Calculator(self.value * other.value)
    
    def __truediv__(self, other):
        if other.value == 0:
            return "Error"
        return Calculator(self.value / other.value)
    
    def __pow__(self, other):
        return Calculator(self.value ** other.value)
    
    def log(self, base):
        try:
            base = float(base)
            if base <= 0 or base == 1:
                return "Error: Basis invalid"
            if self.value <= 0:
                return "Error: Bilangan <= 0"
            return Calculator(math.log(self.value, base))
        except:
            return "Error: Input invalid"

    
    def mod(self, other):
        return Calculator(self.value % other.value)
    


root = Tk()
root.title("Kalkulator by Python GUI")
root["background"] = "#FEFAE0"
root.geometry("310x450")

myfont = font.Font(size=15)

e = Entry(root, width=25, borderwidth=0)
e["font"] = myfont
e["background"] = "#FEFAE0"
e.grid(row=0, columnspan=4, pady=20, padx=20)

def cetak(nilai):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(nilai))

def operasi(op):
    global n_awal, mtk
    n_awal = Calculator(e.get())
    mtk = op
    e.delete(0, END)

def pangkat():
    global n_awal
    n_awal = Calculator(e.get())
    e.delete(0, END)
    e.insert(0, n_awal.__pow__(Calculator(2)).value)

def logaritma():
    global n_awal
    try:
        # Ambil dan parse input
        input_text = e.get()
        if ',' not in input_text:
            raise ValueError("Format: [basis],[bilangan]\nContoh: 2,8")
            
        basis, bilangan = map(float, input_text.split(','))
        
        # Validasi input
        if basis <= 0 or basis == 1:
            raise ValueError("Basis harus >0 dan ≠1")
        if bilangan <= 0:
            raise ValueError("Bilangan harus >0")
            
        # Hitung logaritma
        n_awal = Calculator(bilangan)
        hasil = n_awal.log(basis)
        
        # Tampilkan hasil
        e.delete(0, END)
        e.insert(0, hasil.value if isinstance(hasil, Calculator) else hasil)
        
    except Exception as err:
        e.delete(0, END)
        e.insert(0, str(err))

def hapus():
    e.delete(0, END)

def samadengan():
    global n_awal, mtk
    n_akhir = Calculator(e.get())
    e.delete(0, END)
    if mtk == "Penjumlahan":
        e.insert(0, (n_awal + n_akhir).value)
    elif mtk == "Pengurangan":
        e.insert(0, (n_awal - n_akhir).value)
    elif mtk == "Perkalian":
        e.insert(0, (n_awal * n_akhir).value)
    elif mtk == "Pembagian":
        hasil = n_awal / n_akhir
        e.insert(0, hasil.value if isinstance(hasil, Calculator) else hasil)
    elif mtk == "SisaBagi":
        e.insert(0, (n_awal.mod(n_akhir)).value)

# Tombol angka
tombol = []
for i in range(10):
    tombol.append(Button(root, text=str(i), padx=30, bg="#798645", fg="white", pady=20, command=lambda x=i: cetak(x)))

tombol[1].grid(row=3, column=0, pady=2)
tombol[2].grid(row=3, column=1, pady=2)
tombol[3].grid(row=3, column=2, pady=2)
tombol[4].grid(row=2, column=0, pady=2)
tombol[5].grid(row=2, column=1, pady=2)
tombol[6].grid(row=2, column=2, pady=2)
tombol[7].grid(row=1, column=0, pady=2)
tombol[8].grid(row=1, column=1, pady=2)
tombol[9].grid(row=1, column=2, pady=2)
tombol[0].grid(row=4, column=1, pady=2)

koma = Button(root, text=",", padx=30, bg="#798645", fg="white", pady=20, command=lambda: cetak(","))
koma.grid(row=4, column=2, pady=2)

# Tombol operasi
tam = Button(root, text="+", padx=30, bg="#626F47", fg="white", pady=20, command=lambda: operasi("Penjumlahan"))
kur = Button(root, text="-", padx=30, bg="#626F47", fg="white", pady=20, command=lambda: operasi("Pengurangan"))
bag = Button(root, text="/", padx=30, bg="#626F47", fg="white", pady=20, command=lambda: operasi("Pembagian"))
kal = Button(root, text="x", padx=30, bg="#626F47", fg="white", pady=20, command=lambda: operasi("Perkalian"))
pang = Button(root, text="x²", padx=30, bg="#626F47", fg="white", pady=20, command=pangkat)
log = Button(root, text="a log b", padx=25, bg="#626F47", fg="white", pady=20, command=logaritma)
sisbag = Button(root, text="%", padx=30, bg="#626F47", fg="white", pady=20, command=lambda: operasi("SisaBagi"))
hap = Button(root, text="C", padx=30, bg="#626F47", fg="white", pady=20, command=hapus)
equal = Button(root, text="=", padx=60, bg="#31511E", fg="white", pady=20, command=samadengan)

# Menempatkan tombol
tam.grid(row=1, column=3, pady=2)
kur.grid(row=2, column=3, pady=2)
bag.grid(row=3, column=3, pady=2)
kal.grid(row=4, column=3, pady=2)
hap.grid(row=6, column=0, pady=2)
equal.grid(row=5, column=1, columnspan=2)
pang.grid(row=4, column=0, pady=2)
log.grid(row=5, column=3, pady=2)
sisbag.grid(row=5, column=0, pady=2)

root.mainloop()