#  Age Calculator
# This program calculates how long you've been surviving on Earth…
# counting all your birthdays, bad decisions, and random midnight thoughts.
# It basically tells you how many years, months, and days you've existed
# without getting deleted by life yet 


from datetime import date

def calculate_age(birth_date, current_date):
    years = current_date.year - birth_date.year
    months = current_date.month - birth_date.month
    days = current_date.day - birth_date.day

    if days < 0:
        months -= 1
        prev_month = current_date.month - 1 if current_date.month > 1 else 12
        prev_year = current_date.year if current_date.month > 1 else current_date.year - 1
        
        days_in_prev_month = (date(prev_year, prev_month % 12 + 1, 1) - date(prev_year, prev_month, 1)).days
        days += days_in_prev_month

    if months < 0:
        years -= 1
        months += 12

    return years, months, days


# input
def get_valid_date(label):
    while True:
        try:
            print(f"\nEnter {label} date:")
            year = int(input("Year: "))
            month = int(input("Month: "))
            day = int(input("Day: "))

            return date(year, month, day)  

        except ValueError:
            print("Invalid input! Please enter a valid date.\n")



birth_date = get_valid_date("birth")
current_date = get_valid_date("current")


if current_date < birth_date:
    print("Error: Current date cannot be before birth date!")
else:
    years, months, days = calculate_age(birth_date, current_date)
    print(f"\n Age: {years} years, {months} months, {days} days")