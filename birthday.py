# import modules and functions
import datetime
from time import sleep
from dateutil.relativedelta import relativedelta 

# type in your date of birth in dd.mm.yy format
birthdayString = input()

# define main function
def birthdayTimer():

# set current time in local timezone
    now = datetime.datetime.now()
    now = now + datetime.timedelta(hours=1)

# convert birthday to date
    try: 
        birthday = datetime.datetime.strptime(birthdayString, "%d.%m.%Y")
            
    except:
        print("date of birth must be in dd.mm.yy format")
        
# calculate difference in years
    dif_years = relativedelta(now, birthday).years

# increment difference in years to birthday

    birthday = birthday + relativedelta(years=dif_years + 1)

# calculate time left until birthday
    delta = birthday - now
    print(delta)

# countdown 
# while True: # infinite loop won't run in Sololearn

# example timer with 5 lines' output
i=0
while i<5: 
    birthdayTimer()
    i=i+1
    sleep(1)