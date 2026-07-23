marks = [85, 92, 78, 64, 90, 88]

print("Marks:", marks)

print("Number of Marks:", len(marks))

print("First Mark:", marks[0])
print("Last Mark:", marks[-1])

print("First Three Marks:", marks[:3])
print("Last Three Marks:", marks[-3:])

print("All Marks:")
for mark in marks:
    print(mark)

total = sum(marks)
average = total / len(marks)
smallest = min(marks)
largest = max(marks)

print("Total:", total)
print("Average:", average)
print("Smallest:", smallest)
print("Largest:", largest)