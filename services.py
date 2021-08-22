from datetime import datetime
from datetime import timedelta
import time
import random

def get_random_dates(start, end, number_of_dates, day_gap=0):
    ''' --------------------------------------------------------------
    Retrieve a set of random dates given some parameters. 
    -------------------------------------------------------------- '''
    
    start_date = datetime.strptime(start, "%m/%d/%Y")
    end_date = datetime.strptime(end, "%m/%d/%Y")
    
    # Get all the days in a given range. 
    date_array = (start_date + timedelta(days=x) for x in range(0, (end_date-start_date).days + 1))
    # if (start + timedelta(days=x)).weekday() == 0
    
    ''' --------------------------------------------------------------
    TODO filter for weekends and holidays
    -------------------------------------------------------------- '''

    date_list = list(date_array)
    
    random_dates_list = []

    while len(random_dates_list) < number_of_dates:
        random_date = random.choice(date_list)
        if random_date not in random_dates_list:
            add_date = True
            for existing_date in random_dates_list:
                if abs((existing_date-random_date).days) < day_gap:
                    add_date = False
                    break
            if add_date:
                random_dates_list.append(random_date)
                
                # Remove added date from list of available dates + remove dates that fall in interval
                for i in range(1, day_gap):
                    lower_date = random_date - timedelta(days=i)
                    upper_date = random_date + timedelta(days=i)

                    if lower_date in date_list:
                        date_list.remove(lower_date)
                    if upper_date in date_list:
                        date_list.remove(upper_date)
                
                date_list.remove(random_date)

        print('random_dates_list:', len(random_dates_list), 'date_list:', len(date_list))
    
    random_dates_list.sort()
    
    test_pass = True
    
    for index, date_object in enumerate(random_dates_list):
        if index < len(random_dates_list) - 1:
            next_date = random_dates_list[index + 1]
            if (next_date-date_object).days < day_gap:
                test_pass = False
        print(date_object.strftime("%Y-%m-%d"), date_object.weekday())
    
    if test_pass:
        print('Pass')
    

    ''' --------------------------------------------------------------
    TODO Understand how many possible dates given the number of days
    and the desired gap between days. 
    -------------------------------------------------------------- '''
    
 