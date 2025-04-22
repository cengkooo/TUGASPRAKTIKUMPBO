import math

def main():
    while True:
        try:
            angka = input("Masukkan angka: ")

            # coba konversi input menjadi float
            angka = float(angka)

            if angka < 0:
                print ("Input tidak valid. Harap masukkan angka positif.")
            elif angka == 0:
                print("Error: Akar kuadrat dari nol tidak diperbolehkan")
            else:
                hasil = math.sqrt(angka)
                print(f"Akar kuadrat dari {angka} adalah {hasil:.2f}")
                break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka yang valid.")

if __name__ == "__main__":
    main()