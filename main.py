from library.Author import Author

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


