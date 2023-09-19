MONTHS = ("JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER")
b = 1
a = "MAY"
if a in MONTHS or not b == 1:
    print("Good thinking")
elif not b in MONTHS:
 print("Still mid")
else :
    print("Try harder")


c = "june"

if c.upper() not in MONTHS:
        print("Please enter correct month value , like 4 for April or April")
else:
    print("It's in")

print("Enter the month for the calendar 1-12 : ")
response = input("> ")

if response.upper() not in MONTHS and not response.isdecimal() :
    print("Please enter correct month value , like 4 for April or April")
else:
    print("Pass")