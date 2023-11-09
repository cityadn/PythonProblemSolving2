day = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

day_of_week = str(input("Enter the day of the week:\n"))
lowercase = day_of_week.lower()
if lowercase in day:
    print(f"{day_of_week} has the index of", day.index(day_of_week)+1)

days = int(input("In how many days are we meeting:\n"))
num_of_days = ((day.index(day_of_week)) + days) % 7
meeting_day = day[num_of_days]
print(f"We'll meet on {meeting_day}")
