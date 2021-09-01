import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input ('Which city you want to see data for Chicago, NewYork City or Washington :')
    city = city.casefold()
    if city not in CITY_DATA:
        city = input('Invalid, Try Again!')
        city = city.casefold()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = input('Which month from January to June or type "all" : ')
    month = month.casefold()
    if month not in months:
        month = input('Invalid, Try Again!')
        month = month.casefold()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    day = input('Which day from Monday to Sunday or type "all" : ')
    day = day.casefold()
    if day not in days:
        day = input('Invalid, Try Again!')
        day = day.casefold()
        
        
    print('-'*40)
    return city, month, day


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
    # data file
    df = pd.read_csv(CITY_DATA[city])
    
    # convert start time column
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # month column 
    df['month'] = df['Start Time'].dt.month 
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # day column
    df['day'] = df['Start Time'].dt.day_name()
    
    # filter by month
    if month != 'all':
      months = ['january', 'february', 'march', 'april', 'may', 'june']
      month = months.index(month) + 1
        
     # filter by month to create the new dataframe
      df = df[df['month'] == month]

     # filter by day 
      if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
  
    
    # TO DO: display the most common month
    print('\nThe Most Common Month of Travel:')
    print(df['month'].mode()[0])
    

    # TO DO: display the most common day of week
    print('\nThe Most Common Day of Travel:')
    print(df['day_of_week'].mode()[0])


    # TO DO: display the most common start hour
    print('\n The Most Common Start Hour of Travel:')
    print(df['Start Time'].dt.hour.mode()[0])
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode().to_string(index=False)
    print("The most commonly used start station: ", most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode().to_string(index=False)
    print("The most commonly used end station: ", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_combination = df['combination'].mode()[0]
    print(common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Trip Duration:', df['Trip Duration'].sum())
 
    

    # TO DO: display mean travel time
    print('Mean Trip Duration:', df['Trip Duration'].mean())
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print("no gender data in this city.")
     
    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.columns:
        print('Earliest year of Birth:', df['Birth Year'].min())
        print('Most Recent year of Birth:', df['Birth Year'].max())
        print('Most Common year of Birth:', df['Birth Year'].mode()[0])
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # Display 5 raw data
        def data(df):
           start_loc = 0
           while yes:
                 answer = input("Would you like to view 5 rows of individual trip data? type yes or no").lower()
           if answer not in ['yes', 'no']:
              answer = input("wrong word. Please type yes or no.").lower()
           elif answer == 'yes':
                raw_data += 5
           print(df.iloc[raw_data : raw_data + 5])
           start_loc += 5
           view_data = input("Do you wish to continue?: ").lower()
     
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        
        

if __name__ == "__main__":
         main()
       