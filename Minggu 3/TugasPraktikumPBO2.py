import random

class Father:
    def __init__(self, blood_type):
        self.blood_type = blood_type
        self.alleles = self.get_alleles()

    def get_alleles(self):
        return self.blood_type_to_alleles(self.blood_type)

    @staticmethod
    def blood_type_to_alleles(blood_type):
        return {
            'A': ['A', 'O'],
            'B': ['B', 'O'],
            'AB': ['A', 'B'],
            'O': ['O', 'O']
        }[blood_type]

class Mother:
    def __init__(self, blood_type):
        self.blood_type = blood_type
        self.alleles = self.get_alleles()

    def get_alleles(self):
        return self.blood_type_to_alleles(self.blood_type)

    @staticmethod
    def blood_type_to_alleles(blood_type):
        return {
            'A': ['A', 'O'],
            'B': ['B', 'O'],
            'AB': ['A', 'B'],
            'O': ['O', 'O']
        }[blood_type]

class Child:
    def __init__(self, father, mother):
        self.father_allele = random.choice(father.alleles)
        self.mother_allele = random.choice(mother.alleles)
        self.blood_type = self.determine_blood_type()
    
    def determine_blood_type(self):
        alleles = {self.father_allele, self.mother_allele}
        if alleles == {'A', 'B'}:
            return 'AB'
        elif 'A' in alleles and 'O' in alleles:
            return 'A'
        elif 'B' in alleles and 'O' in alleles:
            return 'B'
        elif alleles == {'A', 'A'}:
            return 'A'
        elif alleles == {'B', 'B'}:
            return 'B'
        elif alleles == {'O'}:
            return 'O'
        else:
            return 'Unknown'
    
    def display_info(self):
        print(f"Golongan darah anak: {self.blood_type} (Alel: {self.father_allele}, {self.mother_allele})")

# Input dari pengguna
father_blood_type = input("Masukkan golongan darah Ayah (A, B, AB, O): ").strip().upper()
mother_blood_type = input("Masukkan golongan darah Ibu (A, B, AB, O): ").strip().upper()

# Membuat objek orang tua
dad = Father(father_blood_type)
mom = Mother(mother_blood_type)

# Membuat objek anak
child = Child(dad, mom)
child.display_info()
