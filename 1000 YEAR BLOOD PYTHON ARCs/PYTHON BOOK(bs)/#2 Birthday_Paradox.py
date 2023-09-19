"""The Birthday Paradox, also called the Birthday Problem, 
is the suprisingly high probability that two people will have the same birthday even in a small group of people.
In a group of 70 people, there's a 99.9 chance of two people having the same birthday.
But even in a group as small as 23 people, 
there's 50 percent chance of matching birthday. 
THIS PROGRAM PERFOMS SEVERAL PROBABILITY EXPERIMENTS TO DETERMINE THE PECENTSGES FOR GROUPS OF DIFFERENT SIZES.
We call these type of experiments, in which we conduct multiple random trials to understand the likely outcomes,
Monte Carlo experiments
"""
import random,datetime

print("Birthday Paradox, by TYLONs17")
def snip():
    print("--snip--")
snip()



#_______________________________________________________________________________________________________
#_______________________________________________________________________________________________________
"""
#_______________________________________________________________________________________________________

while True:
    cont = input("Do you wish to continue? : Type (YES or NO)")



    #___________________________________________________________________________________________________

    binp = int(input("How many Birthdays shall I generate? (Max 100)"))
    #Need to generate the dates from the diff months tht exist  
    evdays = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    #oddays = list(evdays.append(31))
    #leapdays = list(evdays.remove(30))
    gen_months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

    gen_birthdays = []
    matching_birthdays = []
    num_times = 0 

    mode = "No matching dates"
    mode_count = 0
    mode_percent = 0


    #def run(num_times):
    
    count = 0
    while count < binp:
        entry = random.choice(gen_months) + " " + str(random.choice(evdays))
        gen_birthdays.append(entry)
        count +=  1

        #def get_match():
    for index_a, gen_birthdays1 in enumerate(gen_birthdays):
        for index_b, gen_birthdays2 in enumerate(gen_birthdays[index_a + 1 :]):
            if gen_birthdays1 == gen_birthdays2:
                matching_birthdays.append(gen_birthdays1)
                #what if 3 or more gen birthdays match? 
                #
                print(gen_birthdays1, " appears ", gen_birthdays.count(gen_birthdays1), " times!")
                mode_count += 1
                mode = gen_birthdays1
    mode_percent = (mode_count / binp) * 100   
    

    

    if mode_count == 0 :
        print("There are no matching birthdays this time.")
    else:
        print("Here are ", binp , " Birthdays: ")
        print(gen_birthdays)
        print("In this simulation ", mode_count , " PAIRS of people have matching birthdays on ", matching_birthdays)
        print("In this simulation ", 2* mode_count , " people have matching birthdays")



        #
        #
        #
        #
        #
        #Automate to run multiple times
        #
        #
        #
        #

        print("Generating ", binp ," random Birthdays 100,000 times...")
        print("Press Enter to begin...")
        print("Let's run another 100,000 simulations.")
        print("0 simulations run...")
        print("10,000 simulations run...")
        snip()
        print("90,000 simulations run...")
        print("100,000 simulations run...")
        print("Out of 100,000 simulations of ", binp , " people, there was a matching Birthday in that group ", mode_count ," times. This means that ", binp ," people have a " , mode_percent , " chance of having a matching Birthday in their group.Thats probably more than you would think!")

    #___________________________________________________________________________________________________
    if not cont[0].upper() == "Y":
        break

#_______________________________________________________________________________________________________ 
""" 
#_______________________________________________________________________________________________________
#_______________________________________________________________________________________________________

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

def getMatch(birthdays):
    """Returns the date object that occurs more than once in the birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        return None #All birthdays are uniquez, so return None.

    #Compare each birthday to every other birthday:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA #Return the matching birthday.


#Display the intro:
print("""The birthday Paradox shows us that in a group of N people, the odds
        that two of them have matching birthdays is surprisingly large.
        This program does a Monte Carlo simulation (that is, repeated random simulations)
        to explore this concept.
        
        (It's not actually a paradox, its's just a surprising result.)
        """)

#Set up a tuple of month names in oder:
MONTHS = ("Jan","Feb","Mar","Apr","May","Jun","Jul","Äug","Sep","Dec","Nov","Dec")

while True: #Keep asking until the user enters a valid amount.
    print("How many birthdays shall i generate? (Max 100)")
    response = input("> ")
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break #User has entered a valid amount.
print()

#Generate and display the birthdays:
print("Here are ", numBDays, " birthdays:")
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        #Display a coma for each birthday after the first birthday.
        print(",", end=" ")
        monthName = MONTHS[birthday.month - 1]
        dateText = "{} {}".format(monthName, birthday.day)
        print(dateText, end=" ")
print()
print()

#Dermine if there are two birthdays that match.
match = getMatch(birthdays)

#Display the results:
print("In this simulation, ", end=" ")
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = "{} {}".format(monthName, match.day)
    print("multiple people have a birthday on ", dateText)
else:
    print("there are no matching birthdays.")
print()

#Run through 100,000 simulations:
print("Generating", numBDays, "random birthdays 100,000 times...")
input("Press Enter to begin...")

print("Let's rub another 100,000 simulations.")
simMatch = 0 #How many simulations had matching birthdays in them.
for i in range(100_000):
    #Report on the progress every 10,000 simulations:
    if i % 10_000 == 0:
        print(i, "simulations run...")
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print("100,000 simulations run.")

#Display simulation results:
probability = round(simMatch/100_000 * 100, 2)
print("Out of 100,000 simulations of", numBDays, "peole, there was a")
print("matching birthday in that group", simMatch, "times. This means that")
print(numBDays, "people have a", probability, "% chace of having a matching birthday in their group.")
print("That's probably more than you would think!")

