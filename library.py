books = ["Python", "Math", "Science", "English", "History"]
copies = [3, 0, 5, 2, 1]

library = list(zip(books, copies))

print("Books:")
for book, copy in library:
    print(book, "-", copy)

available = list(filter(lambda x: x[1] > 0, library))

print("\nAvailable Books:")
for book in available:
    print(book)

late_fees = [10, 20, 15, 25, 30]
new_fees = list(map(lambda x: x + 5, late_fees))

print("\nUpdated Late Fees:")
print(new_fees)

choice = input("\nEnter a book name: ")

for book, copy in library:
    if book.lower() == choice.lower():
        if copy == 0:
            print("Book is unavailable")
            break
        else:
            print("Book is available")
            break
else:
    print("Book not found")