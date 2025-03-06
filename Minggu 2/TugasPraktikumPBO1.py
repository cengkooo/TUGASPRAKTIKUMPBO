import random
import time

class Character:
    def __init__(self, name, hp, chakra, attack, defense, speed, jutsu):
        self.name = name
        self.hp = hp
        self.chakra = chakra
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.jutsu = jutsu

    def is_alive(self):
        return self.hp > 0

    def physical_attack(self, target):
        damage = self.attack - target.defense
        if damage < 0:
            damage = 0
        target.hp -= damage
        print(f"\n{self.name} menyerang {target.name} dan menyebabkan {damage} damage!")

    def use_jutsu(self, target, jutsu_name):
        if jutsu_name in self.jutsu and self.chakra >= self.jutsu[jutsu_name]['cost']:
            damage = self.jutsu[jutsu_name]['damage']
            target.hp -= damage
            self.chakra -= self.jutsu[jutsu_name]['cost']
            print(f"\n{self.name} menggunakan {jutsu_name} pada {target.name} dan menyebabkan {damage} damage!")
        else:
            print(f"\n{self.name} tidak memiliki cukup chakra untuk menggunakan {jutsu_name}!")

    def recharge_chakra(self):
        self.chakra += 10
        print(f"\n{self.name} mengisi chakra! Chakra sekarang: {self.chakra}")

    def display_status(self):
        print(f"{self.name} - HP: {self.hp}, Chakra: {self.chakra}")
        print("--------------------------------------")

def battle(player, enemy):
    print("\n======================================")
    print("          PERTEMPURAN DIMULAI          ")
    print("======================================\n")
    time.sleep(1)
    
    while player.is_alive() and enemy.is_alive():
        if player.speed >= enemy.speed:
            # Giliran pemain
            print("\n========== GILIRAN PEMAIN ==========")
            action = input("Pilih aksi (1: Serangan Fisik, 2: Jutsu, 3: Isi Chakra): ")
            
            if action == '1':
                player.physical_attack(enemy)
            elif action == '2':
                jutsu_list = ", ".join(player.jutsu.keys())
                jutsu_name = input(f"\nPilih jutsu ({jutsu_list}): ").strip()
                player.use_jutsu(enemy, jutsu_name)
            elif action == '3':
                player.recharge_chakra()
            else:
                print("\nAksi tidak valid!")

            # Giliran musuh jika masih hidup
            if enemy.is_alive():
                print("\n========== GILIRAN MUSUH ==========")
                enemy.physical_attack(player)
            else:
                break

        else:
            # Giliran musuh lebih dulu
            print("\n========== GILIRAN MUSUH ==========")
            enemy.physical_attack(player)
            
            # Giliran pemain jika masih hidup
            if player.is_alive():
                print("\n========== GILIRAN PEMAIN ==========")
                action = input("Pilih aksi (1: Serangan Fisik, 2: Jutsu, 3: Isi Chakra): ")
                
                if action == '1':
                    player.physical_attack(enemy)
                elif action == '2':
                    jutsu_list = ", ".join(player.jutsu.keys())
                    jutsu_name = input(f"\nPilih jutsu ({jutsu_list}): ").strip()
                    player.use_jutsu(enemy, jutsu_name)
                elif action == '3':
                    player.recharge_chakra()
                else:
                    print("\nAksi tidak valid!")
            else:
                break

        # Menampilkan status setelah satu ronde
        print("\n========== STATUS ==========")
        player.display_status()
        enemy.display_status()
        print("============================")
        time.sleep(1)

    # Hasil akhir pertempuran
    print("\n======================================")
    if player.is_alive():
        print(f"          {player.name} MENANG!          ")
    else:
        print(f"          {enemy.name} MENANG!           ")
    print("======================================\n")

def main():
    # Definisikan karakter
    naruto = Character("Naruto", 100, 50, 20, 5, 10, {
        "Rasengan": {"damage": 30, "cost": 20},
        "Healing": {"damage": -20, "cost": 15}
    })
    
    sasuke = Character("Sasuke", 90, 60, 25, 5, 12, {
        "Chidori": {"damage": 35, "cost": 25},
        "Gokakyu": {"damage": 25, "cost": 15}
    })
    
    sakura = Character("Sakura", 80, 70, 15, 5, 8, {
        "Okasho": {"damage": 25, "cost": 20},
        "Healing": {"damage": -30, "cost": 20}
    })
    
    kakashi = Character("Kakashi", 85, 65, 22, 6, 11, {
        "Chidori": {"damage": 30, "cost": 20},
        "Gokakyu": {"damage": 25, "cost": 15}
    })

    # Pilih karakter pemain
    print("\n======================================")
    print("             PILIH KARAKTER           ")
    print("======================================")
    print("1: Naruto (Jutsu: Rasengan dan Healing)")
    print("2: Sasuke (Jutsu: Chidori dan Gokakyu)")
    print("3: Sakura (Jutsu: Okasho dan Healing)")
    print("4: Kakashi (Jutsu: Chidori dan Gokakyu)")
    choice = input("\nMasukkan pilihan (1-4): ")

    if choice == '1':
        player = naruto
    elif choice == '2':
        player = sasuke
    elif choice == '3':
        player = sakura
    elif choice == '4':
        player = kakashi
    else:
        print("\nPilihan tidak valid! Menggunakan Naruto sebagai default.")
        player = naruto

    # Definisikan musuh
    enemy = Character("Orochimaru", 95, 55, 18, 7, 9, {
        "Snake Bite": {"damage": 28, "cost": 15},
        "Healing": {"damage": -25, "cost": 20}
    })

    print(f"\n\n======================================")
    print(f"         {player.name} vs {enemy.name}         ")
    print("======================================\n")
    time.sleep(1)

    # Mulai pertarungan
    battle(player, enemy)

if __name__ == "__main__":
    main()