'''
-----DESIGN-----
I will solve the problem by going through the csv file and pulling the info I need to print the average,
minimum and maximum and only from the month specified when requested by the user.
To solve the problem I will break each line down into 4 values, use the first to make sure it is the 
right month and take the last two to find the average, minimum, and maximum for each year.
I tested to see that my new functions worked and that my old functions worked. I had to test to make sure
that they got the correct values as well.
My code asks for user input and lets them choose whether to break the temperatures down by the year,
or choose a specific month or to quit. If they choose yearly breakdown it breaks each line down into 4 
values and takes the last two to find the average, minimum, and maximum for each year. If they choose a
specific month it does the same thing but skips the months that are not the right month, and the 
program quits if they quit.
'''
'''
-----USER DOCUMENTATION-----
To use this program, run the program. It will ask you whether you would like a breakdown of temperature by
year, for a month, or to quit. Enter 1, 2, or 3, according to which you would like to do. It will then 
show you the yearly breakdown, ask you for a month, or quit. When asked for a month type a number 
1-12 according to month. It will then print out the breakdown for a month for you.
'''
'''
Name: Jordyn Kuhn
Date: 11/5/22
CRN: 10230
CIS 216: Python Programming
Time Estimate: 3 hours
'''

#Switches month from number to String
def get_month(month):
    if month == 1:
        return "January"
    elif month == 2:
        return "February"
    elif month == 3:
        return "March"
    elif month == 4:
        return "April"
    elif month == 5:
        return "May"
    elif month == 6:
        return "June"
    elif month == 7:
        return "July"
    elif month == 8:
        return "August"
    elif month == 9:
        return "September"
    elif month == 10:
        return "October"
    elif month == 11:
        return "Novemeber"
    elif month == 12:
        return "December"
    return

#prints out the header
def header(choice,month=0):
    if choice == 2:
        print('{:^37}'.format(month))
    print('{:>6} | {:>7} | {:>7} | {:>7}'.format("Year","Minimum", "Maximum", "Average"))
    print("-------------------------------------")

#reads the file and prints out the breakdown of each years total
def breakdown_year():
    #start all variables
    year = 0
    total = 0
    count = 0
    average = 0
    header = True

    #open report and read
    report = open('D:\Programs\CSV Report\MIGRNDRA.csv')
    with open('D:\Programs\CSV Report\MIGRNDRA.csv') as report:
        #go through each line
        for line in report.readlines():
            #skip the header
            if header:
                header = False
                continue

            #divide each line into the 4 values
            values = line.split(',')
            
            #skip empty lines
            if len(values) == 1:
                continue

            #set the current year
            current_year = values[2].strip()

            #if no year is set, set it to current and set the min and max to the first val
            if year == 0:
                year = current_year
                min = float(values[3].strip())
                max = float(values[3].strip())
                total = 0
                count = 0

            #if the info is for the right year continue
            if year == current_year:
                #add temps to the total
                total += float(values[3].strip())

                #count how many temps have been added
                count += 1

                #see if its the min
                if float(values[3].strip()) < min:
                    min = float(values[3].strip())

                #see if its the max
                if float(values[3].strip()) > max:
                    max = float(values[3].strip())
            else:
                #find the average
                average = total/count

                #print the info
                print('{:>6} | {:>7} | {:>7} | {:>7}'.format(year, min, max, round(average, 1)))

                #reset the year
                year = 0

        #print the info for the last year
        print('{:>6} | {:>7} | {:>7} | {:>7}'.format(year, min, max, round(average, 1)))

#reads the file and prints out the breakdown of a specified month for each year
def breakdown_month(month):
    #start all variables
    year = 0
    total = 0
    count = 0
    average = 0
    header = True

    #open report and read
    report = open('D:\Programs\CSV Report\MIGRNDRA.csv')
    with open('D:\Programs\CSV Report\MIGRNDRA.csv') as report:
        #go through each line
        for line in report.readlines():
            #divide each line into the 4 values
            values = line.split(',')

            #see if anything is getting skipped
            if header:
                header = False
                continue
            elif len(values) == 1:
                continue
            elif int(values[0]) != month:
                continue

            #set the current year
            current_year = values[2].strip()

            #if no year is set, set it to current and set the min and max to the first val
            if year == 0:
                year = current_year
                min = float(values[3].strip())
                max = float(values[3].strip())
                total = 0
                count = 0

            #if the info is for the right year continue
            if year == current_year:
                #add temps to the total
                total += float(values[3].strip())

                #count how many temps have been added
                count += 1

                #see if its the min
                if float(values[3].strip()) < min:
                    min = float(values[3].strip())

                #see if its the max
                if float(values[3].strip()) > max:
                    max = float(values[3].strip())
            else:
                #find the average
                average = total/count

                #print the info
                print('{:>6} | {:>7} | {:>7} | {:>7}'.format(year, min, max, round(average, 1)))

                #reset the year
                year = 0

        #print the info for the last year
        print('{:>6} | {:>7} | {:>7} | {:>7}'.format(year, min, max, round(average, 1)))


if __name__ == '__main__':
    #get the input
    choice = int(input('''1) See temperature breakdown by year 
    \n2) See temperature breakdown for a month 
    \n3) Quit 
    \n'''))

    #do what was inputted and then print out the header and get the month if necessary
    if choice == 1:
        header(choice)
        breakdown_year()
    elif choice == 2:
        month = int(input("Choose a month (1-12)"))
        month_name = get_month(month)
        header(choice, month_name)
        breakdown_month(month)
    elif choice == 3:
        quit()
    
    
    