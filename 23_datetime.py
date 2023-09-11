import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()
print("Current Date and Time:", current_datetime)

# Get the current date
current_date = datetime.date.today()
print("Current Date:", current_date)

# Create a custom date
custom_date = datetime.date(2023, 9, 11)
print("Custom Date:", custom_date)

# Format a date as a string
formatted_date = custom_date.strftime("%Y-%m-%d")
print("Formatted Date:", formatted_date)

# Parse a date string into a datetime object
date_str = "2023-09-11"
parsed_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
print("Parsed Date:", parsed_date)

# Perform arithmetic operations with dates
one_week_ago = current_date - datetime.timedelta(days=7)
print("One Week Ago:", one_week_ago)

# Calculate the difference between two dates
date1 = datetime.date(2023, 9, 11)
date2 = datetime.date(2023, 9, 18)
date_difference = date2 - date1
print("Date Difference:", date_difference.days, "days")
