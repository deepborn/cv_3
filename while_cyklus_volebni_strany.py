# mame 4 volebni strany A, B, C, D nebo X
# A, B, C, D pripocte hlas dane strane
# X vypise pocet hlasu jednotlivych stran a skonci

# kdyz napisu nejaky to pismenko, budu chtit, aby se pricetlo 1 k nejakymu pocitadlu ty strany
dbA = 0
dbB = 0
dbC = 0
dbD = 0

a = input("Zadej hlas strany: ")
while True:
    if a == "A":
        dbA = dbA + 1
        #tohle pricita ke strane A

    if a == "B":
        dbB = dbB + 1
       #tohle pricita ke strane B

    if a == "C":
        dbC = dbC + 1

    if a == "D":
        dbD = dbD + 1

    if a == "X":
        break

    a = input("Zadej hlas strany: ")
print("pocet hlasu strany A =", dbA, "pocet hlasu strany B =", dbB, "pocet hlasu strany C =", dbC, "pocet hlasu strany D =", dbD)