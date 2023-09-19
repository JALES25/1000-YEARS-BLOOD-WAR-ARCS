"""This program generates printable text files of monthly calendars for the month and year you enter. 
   Dates and calendars are a tricky topic in programming because there are so many different rules for determining  the number of days in a month, 
   which years are leap years, and which day of the week a particular date falls on. 
   Fortunately, Python's datetime module handles these details for you. 
   This program focuses on generating the multiline string for the monthly calendar page.
   """
import re
import datetime

print("Calendar maker by TYLONs")

print("Creates monthly calendars, saved to a text file and fit for printing.")

#Defining the CONSTANTS: 
MONTHS = ("JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER")
DAYS = ("Sunday","Monday","Teusday","Wednesday","Thursday","Friday","Saturday")

CALENDAR = {MONTHS[0],(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31),
       MONTHS[1],(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28),
       MONTHS[2],(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31),
       MONTHS[3],(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30),
       MONTHS[4],(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31),
       MONTHS[5],(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30),
       MONTHS[6],(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31),
       MONTHS[7],(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30),
       MONTHS[8],(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31),
       MONTHS[9],(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30),
       MONTHS[10],(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31),
       MONTHS[11],(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30),
       }

while True: # Loop to get a year form the user.
    print("Enter the year for the caledar: ")
    response = input("> ") 

    if response.isdecimal() and int(response) > 0:
        cal_Year = int(response)
        break

    print("Please enter a numeric year, like 2023.")
    continue

while True: # Loop to get a month from the user.
    print("Enter the month for the calendar 1-12 : ")
    response = input("> ")

    if not response.isdecimal() and response.upper() not in MONTHS:
        print("Please enter correct month value , like 4 for April or April")
        continue

    if response.isdecimal():
        cal_Month = int(response)
    else:
        cal_Month = response
    
    if 1 <= cal_Month <= 12:
        break
    
    print("Please enter a number from 1 to 12.")


def get_Calendar_For(cal_Year, cal_Month):
    cal_Text =  '' # Container of the string of our text in calender

    # Putting the month and year at the top of the calendar
    cal_Text += ('' * 34) + MONTHS[cal_Month - 1] + '' + str(cal_Year) + '\n'

    # Adding the days of the week to the calender !(to be also abrivd)
    cal_Text += '...Sunday.....Monday....Teusday...Wednesday...Thursday....Friday....Saturday..\n'

    # The (10)Horizontal line string separating weeks
    week_Separator = ('+----------' * 7) + '+\n'

    # The blank rows have ten spaces in between the | day separators
    blank_Row = ('|          ' * 7) + '|\n'

    # Get the first date in the month. ( datetime module ) 
    current_Date = datetime.date(cal_Year, cal_Month, 1)

    # Roll the current_Date until its Sunday. (weekday() returns 6 for sunday not 0)
    while current_Date.weekday() != 6 :
        current_Date -= datetime.timedelta(days = 1)
    
    while True: # Loop over each week in the month
        cal_Text += week_Separator

        # day_Number_Row is the row with the day number labels
        day_Number_Row = ''
        for i in range(7): 
            day_Number_Label = str(current_Date.day).rjust(2)
            day_Number_Row += '|' + day_Number_Label + (' ' * 8)
            current_Date += datetime.timedelta(days = 1) # GO's to next day
        day_Number_Row += '|\n' # Adds the vertical line after Sarturday

        # Adding the day numbeer row and 3 blalnk rows to the calender text 
        cal_Text += day_Number_Row 
        for i in range (3): # 4 to 5 - 10?
            cal_Text += blank_Row
        
        # Checks if we're done with the month
        if current_Date.month != cal_Month:
            break

    # Adding the horizontal line at the very bottom of the calender
    cal_Text += week_Separator
    return cal_Text

cal_Text = get_Calendar_For(cal_Year, cal_Month)
print(cal_Text) # Displays calendar


#Save the calendar to a text file
calendar_File_Name = 'calendar_{}_{}.txt'.format(cal_Year, cal_Month)
with open(calendar_File_Name, 'w') as file_Obj:
    file_Obj.write(cal_Text)


print("Saved to " + calendar_File_Name)
        







    






#creating our default calalender
cal_proto = """

                                    cal_MonthP cal_YearP
...Sunday.....Monday....Teusday...Wednesday...Thursday....Friday....Saturday..
+----------+----------+----------+----------+----------+----------+----------+
|25        |26        |27        |29        |30        | 1        |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
| 2        | 3        | 4        | 5        | 6        | 7        | 8        |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
| 9        |10        |11        |12        |13        |14        |15        |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
|16        |17        |18        |19        |20        |21        |22        |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
|23        |24        |25        |26        |27        |28        |29
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
|30        |31        | 1        | 2        | 3        | 4        | 5        |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+

"""
#Making the logical statements to handle the output of cal_proto with user input values
#_________________________
"""#Loop over each line in the sample_card var:
    for line in f_hand.splitlines():
        #Loop over each character in the line:
        for i, sampleA  in  enumerate(line):
            if sampleA == ".":
                #Print top & bottom borders:
                print(".", end="")
            elif sampleA == " ":
                #Print an empty space since there's a space in the sample_card:
                print(" ", end="")
            elif sampleA == "_":
                #Print top & bottom borders:
                print("_", end="")
            elif sampleA == "|":
                #Print side borders:
                print("|", end="")
            elif sampleA == "A":
                #Print first Card_num:
                print(dgen1, end="")
            elif sampleA == "J":
                #Print second Card_num:
                print(dgen2, end="")
            elif sampleA == "#":
                print("#", end="")
            elif sampleA == "+":
                #Print card_group:
                print(random.choice(card_group), end="")"""
#_________________________
"""#Loop over each charecter in the line
    for cal, sampleA in enumerate(line):
    if sampleA == "+":
        print("+", end="")
    elif sampleA == "-":
        print("-", end="")
    elif sampleA == "|":
        print("|", end="")
    elif sampleA == " ":
        print(" ", end="")
"""  


#_________________________

"""
def re_get_cal():
    #Loop over each line in the sample cal_proto calendar
    for line in cal_proto.splitlines():
        #Find the Default values to be replaced
        #Replace the first occurrence of the Defaul values in the cal_proto calender
        word1 = "cal_YearP"
        word2 = "cal_MonthP"
        def_rep0 = re.sub(r'\b{}\b'.format(re.escape("cal_YearP")), cal_Year, cal_proto, count = 1 )
        def_rep = re.sub(r'\b{}\b'.format(re.escape("cal_MonthP")), cal_Month, def_rep0, count = 1 )
    return def_rep
print(re_get_cal())
"""
#____________________________






#print("Saved to calendar_",cal_Year,cal_Month,".txt")


#____________________________________________________________________
#____________________________________________________________________
#____________________________________________________________________
#____________________________________________________________________






#____________________________________________________________________
#____________________________________________________________________
#____________________________________________________________________
#____________________________________________________________________
