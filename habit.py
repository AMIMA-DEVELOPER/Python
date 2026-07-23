habit_info = ("Exercise", "Read", "Drink Water", "Meditate", "Sleep Early")
weekly_record = ("Done", "Done", "Missed", "Done", "Done", "Missed", "Done")

print("Habit Information:", habit_info)
print("Weekly Record:", weekly_record)

print("Number of Habits:", len(habit_info))
print("Number of Records:", len(weekly_record))

print("First Habit:", habit_info[0])
print("Last Habit:", habit_info[-1])

print("First Three Habits:", habit_info[:3])
print("Last Three Records:", weekly_record[-3:])

try:
    habit_info[0] = "Yoga"
except TypeError as e:
    print(e)