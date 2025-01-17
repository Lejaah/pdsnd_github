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
    city = input("\nWould you like to see data for Chicago, New York city, or Washington?\n").lower()
    while city not in CITY_DATA:
        city = input("\ninvalid city, please try again!\n").lower()
        
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', "all"]
    month = input("\nWhich month? January, February, March, April, May or June\nOr 'all' to apply no month filter?\n").lower()
    while month not in months:
        month = input("\ninvalid month, please try again!\n").lower()
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "all"]
    day = input("\nWhich day? Monday, ... Sunday\nOr 'all' to apply no day filter?\n").title()
    while day not in days:
        day = input("\ninvalid day, please try again!\n").title()
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df["month"] = df ["Start Time"].dt.month
    df["day_of_week"] = df ["Start Time"].dt.weekday_name
   
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
              
    # filter by day of week if applicable
    if day != "all":
       days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
       df = df[df["day_of_week"] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most common month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most common day of week:', popular_day)

    # TO DO: display the most common start hour
    df["hour"]= df ["Start Time"].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most common Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most common used start station:', popular_start_station)

    # TO DO: display most commonly used end stations
    popular_end_station = df['End Station'].mode()[0]
    print('Most common used end station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    # extract trips to create new column
    df['popular_trip'] = df['Start Station'] + " , " + df['End Station']
    
    print("Most popular trip: {} ".format( df['popular_trip'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time:', total_travel_time)
              
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The total travel time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The counts of user types:', user_types)

    # TO DO: Display counts of gender
    if "Gender" in df.columns:
       gender = df['Gender'].value_counts()
       print('The counts of gender:', gender)
    else: print("Sorry! the gender data are not available for this city")
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        print("The earliest year of birth: ", df["Birth Year"].min())
        print("The most recent year of birth: ", df["Birth Year"].max())
        print("The most common year of birth: ", df["Birth Year"].mode()[0])
    else: print("Sorry! the Birth Year data are not available for this city")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    #prompt the user whether they want to see 5 lines of raw data
    answers = ["yes" , "no"]
    answer = input("Would you like to see more data? type 'Yes' or 'No'\n").lower()
    
    while answer not in answers:
          answer = input("Please type Yes or No\n").lower()
              
    #Display data if the answer is 'yes'
    n = 0
    while True:
        for i in range(len(df)):
            if answer.lower() == 'yes':
               print(df.iloc[n:n+5])
               n += 5     
              
    #Stop the program when the user says 'no' or there is no more raw data to display
               answer = input("Would you like to see more data? type 'Yes' or 'No'\n").lower()
               while answer not in answers:
                     answer = input("Please type Yes or No\n").lower()
                     if answer.lower() == 'yes':
                        continue
                     else:
                        break
        break
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
    
""" Sources: 
1. datacamp.com for loops in python tutorial
2. stackoverflow.com
"""