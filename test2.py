import matplotlib.pyplot as plt
import statistics

list = []

#math#
nbn = int(input("nombres de notes en math : "))


def liste(nbn):
    for i in range(nbn):
        note = int(input("note : "))
        list.append(note)
    return(list)

math = liste(nbn)
moymath = statistics.mean(math)

#Francais#
nbn = int(input("nombres de notes en francais : "))
list.clear()

francais = liste(nbn)
moyfrancais = statistics.mean(francais)

#Anglais#
nbn = int(input("nombres de notes en anglais : "))
list.clear()

anglais = liste(nbn)
moyanglais = statistics.mean(anglais)

#PHYSIQUE CHIMIE#
nbn = int(input("nombres de notes en physique chimie : "))
list.clear()

pc = liste(nbn)
moypc = statistics.mean(pc)

print("moyènne de mathématique : ", moymath)
print("moyènne de francais : ", moyfrancais)
print("moyènne de anglais : ", moyanglais)
print("moyènne de physique chimie : ", moypc)

