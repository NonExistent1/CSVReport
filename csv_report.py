'''
----Why 2020 Has a Lower Average----
2020 has a lower average because only the first 4 months and 13 days of the year are accounted for.
'''
'''
-----DESIGN-----
I will solve the problem by going through the csv file and pulling the info I need to print the average,
minimum and maximum.
To solve the problem I will break each line down into 4 values and take the last two to find the
average, minimum, and maximum for each year.
I tested to see why it was always out of index for the last few lines, which was because the last two 
were empty and had to skip them. I also had to test why it wasn't printing the last year. The last thing I 
had to test was that the numbers were right.
My code breaks each line down into 4 values and takes the last two to find the
average, minimum, and maximum for each year.
'''
'''
-----USER DOCUMENTATION-----
To use this program, run the program. The program will figure out the average, minimum, and maximum temperature
for each year between 1957 and 2020. It will then print them out accordingly for your viewing.
'''
'''
Name: Jordyn Kuhn
Date: 11/3/22
CRN: 10230
CIS 216: Python Programming
Time Estimate: 3 hours
'''

#prints out the header
def header():
    print('{:>6} | {:>7} | {:>7} | {:>7}'.format("Year","Minimum", "Maximum", "Average"))
    print("-------------------------------------")


#reads the file and prints out the info from it
def read_file():
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


if __name__ == '__main__':
    header()
    read_file()