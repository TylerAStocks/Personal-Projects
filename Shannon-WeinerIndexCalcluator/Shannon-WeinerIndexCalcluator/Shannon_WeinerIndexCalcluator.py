
import math

#make a loop that takes inputs of animal names and pops, also logs how many there are

endInput = False
species = []
population = []
sum = 0
proportion = []
propProp = []
natLog = []
logSum = 0
swIndex = 0


while endInput == False:
    name = ""
    pop = 0
    name = input('Species Name (Enter "End" to stop listing): ')
    if name.lower() == 'end':
        endInput = True
        break
    else:
        species.append(name)

    try:
        pop = int(input('Population size: '))
    except:
        print ("Invalid input. It's 0 now")
    if pop < 0:
        pop = 0
    population.append(pop)
    


    #get total pop
for p in population:
    sum += p

for p in population:
    proportion.append(round((p/sum), 3))

for r in proportion:
    propProp.append(round((r**r), 3))

for q in propProp:
    natLog.append(round(math.log(q), 3))

for l in natLog:
    logSum += l

swIndex = logSum*(-1)



print()
for s, p, r, q, l in zip(species, population, proportion, propProp, natLog):
    print(s, p, r, q, l)

print()
print("SW Index: " + str(swIndex))


