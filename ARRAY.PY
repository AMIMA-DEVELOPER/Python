from array import *

snacks1 = {"Chips", "Cookies", "Juice"}
snacks2 = {"Juice", "Candy", "Cookies"}

snacks1.add("Popcorn")

print("Snack Box 1:", snacks1)
print("Snack Box 2:", snacks2)

shared = snacks1.intersection(snacks2)

print("Shared Snacks:", shared)

counts = array('i', [5, 8, 3, 10])

counts.append(6)
counts.append(8)

print("Snack Counts:", counts)

print("Count of 8:", counts.count(8))

counts.reverse()

print("Reversed Counts:", counts)