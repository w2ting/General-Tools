import datetime
 
#Step 1: calculate the total number of days
today = datetime.date.today() #today's date
someday = datetime.date(2023, 1, 27) #target date
diff = someday - today
print("The total number of days till " + str(someday) + " is " + str(diff.days))

#Step 2: calculate the number of no work days
weekends = 1
publicholidays = 2
leave = 1
noworkdays = weekends + publicholidays + leave
print("The total number of no work days is " + str(noworkdays))

#Step 3: calculate the number of work days - step 1 minus step 2
workdays = (diff.days) - int(noworkdays)
print("The total number of work days is " + str(workdays))

if diff.days < 1:
    print("Today is the day!")
elif diff.days == 1:
    print("Tomorrow is the day!")
elif diff.days > 90:
    print("Wait long long sia...")