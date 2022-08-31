import time
import pandas as pd
import numpy as np
import calendar

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
    city = input('Please insert the city name: ')
    while city not in CITY_DATA.keys():
        city = input('Invalid!. Please insert the right name of the city: ')

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please insert the target month: ').capitalize()
    while not(month.title() in calendar.month_name[1:] or month == 'All'):
        month = input('Invalid!. Please insert the right name of the month: ').capitalize()
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please insert the target day: ').capitalize()
    while not(day.title() in calendar.day_name[1:] or day == 'All'):
        day = input('Invalid!. Please insert the right name of the week day: ').capitalize()

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
    # Importing Data
    df = pd.read_csv(CITY_DATA[city])
    
    # Converting to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # Creating two new columns with the month name and week day name
    df['Month'] = df['Start Time'].dt.month_name()
    df['Week_Day'] = df['Start Time'].dt.day_name()
    # Filtring by month and day
    if day =='All' and month =='All':
        return df
    elif day == 'All' or month =='All':
        if day == 'All':
               df = df[df['Month'] == month]
        elif month == 'All':
               df = df[df['Week_Day'] == day]
    else:
        df = df[(df['Week_Day'] == day) &(df['Month'] == month)]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is {} ".format(df['Month'].value_counts().index[0]))

    # TO DO: display the most common day of week
    print("The most common day is {} ".format(df['Week_Day'].value_counts().index[0]))

    # TO DO: display the most common start hour
    print("The most common hour is {} ".format(df['Start Time'].dt.hour.value_counts().index[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used start station is {} ".format(df['Start Station'].value_counts().index[0]))

    # display most commonly used end station
    print("The most commonly used end station is {} ".format(df['End Station'].value_counts().index[0]))

    # display most frequent combination of start station and end station trip
    df['Combination Stations'] = df['Start Station'] + "\t To \t   " + df['End Station']
    print("The most frequent combination of start station and end station trip is from {} ".format(df['Combination Stations'].value_counts().index[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time is {}'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('The mean travel time is {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("The counts of the user types are:\n {}".format(df['User Type'].value_counts()))
    if city != 'washington':
        # TO DO: Display counts of gender
        print('-'*40)
        print("The counts of genders are:\n {}".format(df['Gender'].value_counts()))

        # TO DO: Display earliest, most recent, and most common year of birth
        print('-'*40)
        print("The earliest year of birth is {} ".format(int(df['Birth Year'].min())))
        print("The most recent year of birth is {} ".format(int(df['Birth Year'].max())))
        print("The most common year of birth is {} ".format(int(df['Birth Year'].value_counts().index[0])))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    decision = input('\n\n Do you want to see 5 rows of this data? Enter yes or no: ').lower()
    print('\n')
    data_rows=0
    while decision == 'yes':
        data_rows+= 5
        print(df.head(data_rows))
        decision = input('\n\nDo you want to see the next 5 rows of this data? ? Enter yes or no: ').lower()
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
