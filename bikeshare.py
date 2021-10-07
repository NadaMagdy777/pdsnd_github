import calendar
import time
import pandas as pd
import numpy as np
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
          'august', 'september', 'october', 'november', 'december','all']
weekDays = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday","all"]
hours_pm={13:1,14:2,15:3,16:4,17:5,18:6,19:7,20:8,21:9,22:10,23:11,24:12}

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
city=None
def get_filters():
    day=None
    month=None
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input('whould you like to see data for chicago, new york city or washington\n').lower().strip()
    while (city not in ('chicago','new york city' , 'washington')):
        city=input('please enter correct city \n').strip().lower()
        
   
   
    month_or_day=input('whould you like to filter data by month , day, both or not at all? type none for no time filter   \n').strip().lower()    
   
    # TO DO: get user input for month (all, january, february, ... , june)
    day=None
    month=None
    while(month_or_day not in ('month','day','both','none')):
        month_or_day=input('please enter correct chooces from month, day, both or none')
    else:
        if(month_or_day == 'month'):
            month=input('which month? {0} \n'.format(months)).strip().lower()
            while(month not in months):
                 month=input('please enter correct month name ( {0} )\n'.format(months)).strip().lower()
              
       
        elif(month_or_day == 'day'):
            
                day=input('which day ? {0}\n'.format(weekDays))
                while (day not in weekDays):
                         day=input('please enter correct day name ( {0} )\n'.format(weekDays))
                    
         
        elif(month_or_day == 'both'):
            month=input('which month? {0} \n'.format(months)).strip().lower()
            while(month not in months):
              month=input('please enter correct month name ( {0} )\n'.format(months)).strip().lower()
            day=input('which day ? {0}\n'.format(weekDays))
            while (day not in weekDays):
              day=input('please enter correct day name ( {0} )\n'.format(weekDays))
        else:
            day=None
            month=None
            
          

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city,month,day
   


def load_data(city, month, day):
    
    """
    Loads data for the specified city and filters by month and day if applicable.
    

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df= pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    
    df['day_of_week'] =df['Start Time'].dt.day_name()
    
    if month != 'all' and month != None :
       
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
          'august', 'september', 'october', 'november', 'december','all']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all' and day != None:
        
        df = df[df['day_of_week'] == day.title()]
    return df

def filter_summary(city, month, day, df):
    """
    Displays selected city, filters chosen, and simple stats on dataset.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        (int) init_total_rides - total number of rides in selected city before filter
        (dataframe) df - filtered dataset
    """
    start_time = time.time()

    filtered_rides = len(df)
    num_stations_start = len(df['Start Station'].unique())
    num_stations_end = len(df['End Station'].unique())
    print('Gathering statistics for:    ', city)
    print('Filters (month, day):        ', month, ', ', day)
    print('Rides in filtered set:       ', filtered_rides)
    print('Number of start stations:    ', num_stations_start)
    print('Number of end stations:      ', num_stations_end)
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=df["month"].value_counts()
    print('the common month is        ( {0} ) '.format(calendar.month_name[common_month.index[0]]))
        

    # TO DO: display the most common day of week
    common_day=df["day_of_week"].value_counts()
    print('the common day of week is  ( {0} ) '.format(common_day.index[0]))


    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    common_start_hour=df["start_hour"].value_counts()
    
    if((common_start_hour.index[0]<12 and common_start_hour.index[0]>=1) or common_start_hour.index[0]==24   ):
       
        if(common_start_hour.index[0]==24):
            print('the common start hour is   ({0} AM)'.format(hours_pm[common_start_hour.index[0]]))
        else:
            print('the common start hour is   ({0} AM)'.format(common_start_hour.index[0]))
    else:
        
        if(common_start_hour.index[0]==12):
             print('the common start hour is  ({0} PM)'.format(common_start_hour.index[0]))
        else:
              print('the common start hour is ({0} PM)'.format(hours_pm[common_start_hour.index[0]])) 
                
            


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    common_start_station=df["Start Station"].value_counts()
    print('the common start station is     ( {0} )'.format(common_start_station.index[0]))
           


    # TO DO: display most commonly used end station
    common_end_station=df["End Station"].value_counts()
    print('the common end station is     ( {0} )'.format(common_end_station.index[0]))
           


    # TO DO: display most frequent combination of start station and end station trip
    df["start & end station"]=df["Start Station"]+df["End Station"]
    common_start_end_station=df["start & end station"].value_counts()
    print('the common start & end station is  ( {0} )'.format(common_start_end_station.index[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration=df['Trip Duration'].sum()
    second=total_trip_duration%60
    minute=total_trip_duration/60
    hour=minute/60 
    minute=minute%60
    print('The total trip duration is {} hours, {} minutes and {}'
          ' seconds.'.format(round(hour), round(minute), round(second)))

    # TO DO: display mean travel time
    trip_duration_mean=round(df['Trip Duration'].mean())
    print ("Mean travel time is {0} seconds".format( trip_duration_mean))
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def show_raw(df):
    """display 5 raw"""
    request=input("Would you like to see some raw data from the current dataset?(y or n):  ").lower().strip()
    row_length=0
    while(request!='n' and row_length<=len(df)):
        if(request=='y'):
            print(" Displaying rows {0} to {1}:".format(row_length,row_length+5))
            print(df[row_length:row_length+5])
            row_length+=5
            request=input("Would you like to see the next 5 rows?(y or n):  "  )
        else:
           request=input("please enter (y or n)")
        
        
        
        
        
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("counts of user types :\n {}\n".format(df["User Type"].value_counts()))


    # TO DO: Display counts of gender
    if(city=='chicago' or city=='new york city'):
      print("counts of Gender:\n{}\n ".format(df["Gender"].value_counts()))


    # TO DO: Display earliest, most recent, and most common year of birth
    if(city=='chicago' or city=='new york city'):
       Earliest=round(min(df["Birth Year"]))
       most_recent=round(max(df["Birth Year"]))
       most_common=df["Birth Year"].value_counts()
       print("Year of birth:\n Earliest:  {0}\nmost_recent:  {1}\nmost_common:  {2} ".format(Earliest,most_recent,round(most_common.index[0])))
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        filter_summary(city, month, day, df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)

        user_stats(df)
        show_raw(df)
       
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


