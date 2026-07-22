students = {
    "Ali": "Math",
    "Sara": "Science",
    "Ahmed": "English",
    "Ayesha": "Computer"
}

print(students.get("Ali"))
print(students.get("Zain", "Not Found"))

students["Ali"] = "Physics"
students["Zain"] = "Biology"

students.pop("Ahmed")

print("Total Records:", len(students))

for name, subject in students.items():
    print(name, ":", subject)