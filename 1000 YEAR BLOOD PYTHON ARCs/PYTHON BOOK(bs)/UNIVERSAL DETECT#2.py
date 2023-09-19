import random, datetime

#binp = int(input("How many Birthdays shall I generate? (Max 100)"))
#Need to generate the dates from the diff moths tht exist  
evdays = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
#oddays = list(evdays.append(31))
#leapdays = list(evdays.remove(30))
gen_months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

gen_birthdays = []

#random_BDAY = random(evdays)

#print(random_BDAY)

"""for i in range(23):
    entry = random.randint(1,32)
    #print(entry)"""

"""ir = random.sample(gen_months,k = 1)

ent = random.choice(gen_months) + " " + str(random.choice(evdays))

print(ent)
#print(random.randint(1,31))"""
#_____________________________________________________________________________________________________


"""count = 0
while count < binp:
    entry = random.choice(gen_months) + " " + str(random.choice(evdays))
    gen_birthdays.append(entry)
    count +=  1

test_mons = ["Jan","Feb","Jan","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

cou = 0
#def get_Match(test_mons):
    #COMPARES EACH MONTH TO EVERY OTHER MONTH
for a, test_monsA in enumerate(gen_birthdays):
    for b, test_monsB in enumerate(gen_birthdays[a + 1 :]):
        if test_monsA == test_monsB:
            cou += 1
            print(gen_birthdays.count(test_monsA))
            print(test_monsA)
                
                #return test_monsA #return the matching month

print(gen_birthdays)
print("There are ", cou , "pairs of matching birthdays" )
print("That means ", 2*cou , " people have matching birthdays")"""

"""test = get_Match(gen_birthdays)
print(test)"""

"""liste = ["T","Y","L","O","N","s"]

iterate = iter(liste)

try: 
    while True:
        elemen = next(iterate)
        print(elemen)
except StopIteration:
    pass
"""

#____________________________________________________________________________________________________________
name = "Tylons"
print(name.upper())

MONTHS = ("Jan","Feb","Mar","Apr","May","Jun","Jul","Äug","Sep","Dec","Nov","Dec")

numBDays = 25
def getBirthdays(numberOfBirthdays):
    """Resturns a list of number randon date objects for birthdays."""
    birthdays = []

    for i in range(numberOfBirthdays):
        #The year is unimportant for our simulation, as long as birthdays have the same year
        startOfYear = datetime.date(2001,1,1)

        #Get a random day into the year:
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays 
        birthdays.append(birthday)
    return birthdays
container = []

birthdays = getBirthdays(numBDays)
"""for i, birthday in enumerate(birthdays):
    container.append(birthday)
    if i != 0:
        #Display a coma for each birthday after the first birthday.
        print(",", end=" ")
        monthName = MONTHS[birthday.month - 1]
        dateText = "{} {}".format(monthName, birthday.day)
        print(dateText, end=" ")


print()
print(container)"""

"""for i in enumerate(MONTHS):
    print(i)
    if i != 0:
        print(",", end=" ")"""


#____________________________________________________________________________________________________________

