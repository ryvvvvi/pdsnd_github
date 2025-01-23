import time
import pandas as pd
import numpy as np

CITY_FILES = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_user_input():
    city = ""
    available_cities = list(CITY_FILES.keys())
    while city not in available_cities:
        city = input(f"Choose a city from {available_cities}: ").lower()

    month = ""
    valid_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june',
                    'july', 'august', 'september', 'october', 'november', 'december']
    while month not in valid_months:
        month = input("Enter month (e.g., 'all', 'january', ... 'december'): ").lower()

    day = ""
    valid_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while day not in valid_days:
        day = input("Enter day (e.g., 'all', 'monday', ... 'sunday'): ").lower()

    return city, month, day

def load_city_data(city, month, day):
    file_path = CITY_FILES[city]
    df = pd.read_csv(file_path)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.strftime('%B').str.lower()
    df['Day'] = df['Start Time'].dt.day_name().str.lower()

    if month != 'all':
        df = df[df['Month'] == month]
    if day != 'all':
        df = df[df['Day'] == day]

    return df

def time_statistics(df):
    print("Calculating time statistics...")
    print(f"Most common month: {df['Month'].mode()[0]}")
    print(f"Most common day: {df['Day'].mode()[0]}")
    df['Hour'] = df['Start Time'].dt.hour
    print(f"Most common hour: {df['Hour'].mode()[0]}")

def station_statistics(df):
    print("Calculating station statistics...")
    print(f"Most common start station: {df['Start Station'].mode()[0]}")
    print(f"Most common end station: {df['End Station'].mode()[0]}")
    print(f"Most common trip: {(df['Start Station'] + ' -> ' + df['End Station']).mode()[0]}")

def trip_duration_statistics(df):
    print("Calculating trip duration statistics...")
    print(f"Total travel time: {df['Trip Duration'].sum()} seconds")
    print(f"Average travel time: {df['Trip Duration'].mean()} seconds")

def user_statistics(df):
    print("Calculating user statistics...")
    print(f"사용자 유형형:\n{df['사용자 유형형'].value_counts()}")
    if '성' in df.columns:
        print(f"성 counts:\n{df['성'].value_counts()}")
    if 'Birth Year' in df.columns:
        print(f"가장빠른 birth year: {int(df['Birth Year'].min())}")
        print(f"Most recent birth year: {int(df['Birth Year'].max())}")
        print(f"Most common birth year: {int(df['Birth Year'].mode()[0])}")

def display_raw_data(df):
    start_row = 0
    while True:
        show_data = input("Show raw data? Enter 'yes' or 'no': ").lower()
        if show_data == 'yes':
            print(df.iloc[start_row:start_row + 5])
            start_row += 5
        elif show_data == 'no':
            break

def main():
    while True:
        city, month, day = get_user_input()
        df = load_city_data(city, month, day)
        if df.empty:
            print("No data available for the selected filters.")
        else:
            display_raw_data(df)
            time_statistics(df)
            station_statistics(df)
            trip_duration_statistics(df)
            user_statistics(df)
        if input("Restart? Enter 'yes' or 'no': ").lower() != 'yes':
            break

if __name__ == "__main__":
    main()
