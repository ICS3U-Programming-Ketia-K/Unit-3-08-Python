#!/usr/bin/env python3

# Created by: Ketia Gaelle Kaze
# Created on: Jan. 3, 2021
# This program determines if the entered
# year is a leap year

import math

# user input
user_year_string = input("Enter a year (ex. YYYY): ")
print("")


# checks if it is a leap year
def main():
    try:
        # casts user input to integer
        user_year_int = int(user_year_string)
        if user_year_int % 4 == 0:
            if user_year_int % 100 == 0:
                if user_year_int % 400 == 0:
                    # displays that it is a leap year
                    print("This is a leap year!")
                    print("It has 366 days.")
                else:
                    print("This is not a leap year.")
            else:
                print("This is not a leap year.")
        else:
            print("This is not a leap year.")
    # checks for errors
    except Exception:
        print("{} is not a valid year.". format(user_year_string))


if __name__ == "__main__":
    main()
