from datetime import datetime, date

from Garden.Plant import Plant
from library.Author import Author
from university.Student import Student

#sukurti 3 objektus su reikšmėmis naudojantis tuščiu konstruktoriu, ir tris naudojantis pilnu konstuktoriu.
# sudėti juos į autorių masyvą.
# prasukti ciklą per masyvą ir atspausdinti knygas

autorius1 = Author()
autorius1.name = "Janina"
autorius1.surname = "Degutytė"
autorius1.birth_year = 1928
print(autorius1._str_())

autorius2 = Author()
autorius2.name = "Tomas"
autorius2.surname = "Dirgėla"
autorius2.birth_year = 1989
print(autorius2._str_())

autorius3 = Author()
autorius3.name = "William"
autorius3.surname = "Shakespeare"
autorius3.birth_year = 1564
print(autorius3._str_())

autorius4 = Author("Jonas", "Mačiulis", 1862)
print(autorius4._str_())
autorius5 = Author("Vincas", "Krėvė-Mickevičius",1882)
print(autorius5._str_())
autorius6 = Author("Balys", "Sruoga", 1896)
print(autorius6._str_())

autoriai = [autorius1, autorius2, autorius3, autorius4, autorius5, autorius6]

print()

for autorius in autoriai:
    print(autorius._str_())

print("---------------------------------------------------------------------------")

#Susikuriam masyvą saugoti augalams. sukuriame 4 augalus (2x2 pagal konstruktorius)
#prasukti ciklą ir atspausdinti augalus

plant1 = Plant()
plant1.pavadinimas = "Morka"
plant1.lotyniskas_pavadinimas = "Daucus carota"
plant1.vienmetis = True
plant1.zemynas = "Europa"
plant1.aukstis = 0.3
plant1.valgomas = True

plant2 = Plant()
plant2.pavadinimas = "Rožė"
plant2.lotyniskas_pavadinimas = "Rosa"
plant2.vienmetis = False
plant2.zemynas = "Azija"
plant2.aukstis = 1.5
plant2.valgomas = False


plant3 = Plant("Pomidoras", "Solanum lycopersicum", True, "Pietų Amerika", 0.8, True)
plant4 = Plant("Kaktusas", "Cactaceae", False, "Šiaurės Amerika", 2.0, False)

plants = [plant1, plant2, plant3, plant4]

for plant in plants:
    print(plant)

print("---------------------------------------------------------------------------")

#sukurti metodą get_age() kuris gražintų tikslų, gražiai suformatuotą amžių su metais, mėnesiais ir dienomis
# sukurti metodą, kuris padavus disciplinos pavadinimą gražintų jos pažymių vidurkį
# sukurti metodą, kuris paskaičiuotų visų disciplinų(int) vidurkių vidurkį(double). galima kurtis pagalbines funkcijas.
# parašyti __str__ kuris gražiai atspausdintų visą išsamią, gražiai suformatuotą studento informaciją
#
# Vėliau studentą išskaidysime į kelias klases.


student1 = Student("Jonas", "Jonaitis", date(1983,8,28), "matematika")
print(student1)
