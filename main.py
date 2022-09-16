# Definició de classes
class UnitatFormativa:
    nom = None
    nota = None

    def __init__(self, nom, nota):
        self.nom = nom
        self.nota = nota


# Inici del programa
uf1 = UnitatFormativa("UF1. Desenvolupament del programari", 10)
uf2 = UnitatFormativa("UF2. Optimització del programari", 9)
uf3 = UnitatFormativa("UF3. Introducció al Disseny Orientat a Objectes", 9.5)

print(uf1.nom)
print(uf1.nota)
print(uf2.nom)
print(uf2.nota)
print(uf3.nom)
print(uf3.nota)
