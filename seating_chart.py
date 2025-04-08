import numpy as np
from numpy import random

# Get classroom size from user
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of chairs per row: "))
total_seats = rows * cols

# Pre-defined list of student names (must be >= total_seats)
student_names = [
    "Alice", "Bob", "Charlie", "David", "Eve", "Fay", "Grace", "Heidi",
    "Ivan", "Judy", "Karl", "Laura", "Mallory", "Niaj", "Olivia", "Peggy",
    "Quinn", "Rupert", "Sybil", "Trent", "Uma", "Victor", "Walter", "Xena",
    "Yvonne", "Zach"
]

# Check if there are enough names
if len(student_names) < total_seats:
    print("Error: Not enough student names for this classroom size.")
    exit()

# Convert to 1D NumPy array and shuffle
names_array = np.array(student_names[:total_seats])
random.shuffle(names_array)

# Reshape into 2D array
seating_chart = names_array.reshape(rows, cols)

# Print seating chart with positions
print("\nSeating Chart (row, col):")
for r in range(rows):
    for c in range(cols):
        name = seating_chart[r, c]
        print(f"{name:<10} at ({r}, {c})")

