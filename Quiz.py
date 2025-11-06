# Del 1
namn = input("Ange ditt namn: ")
print("Hej " + namn + " välkommen till spelet!")

# Del 2
import random as rand
tal = rand.randint(1, 10)
gissning = int(input("Gissa ett tal mellan 1 och 10: "))
if gissning == tal:
    print("Rätt gissat!")
else:
    print("Tyvärr, det var " + str(tal))
