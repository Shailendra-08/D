import csv
import math

def getMean(arr):
    return sum(arr) / len(arr)

def getSD(arr):
    mean = getMean(arr)
    variance = sum((x - mean) ** 2 for x in arr) / (len(arr) - 1)
    return math.sqrt(variance)

def zscore(arr):
    mean = getMean(arr)
    sd = getSD(arr)
    return [(x - mean) / sd for x in arr]

def minmax(arr, rmin, rmax):
    min_val = min(arr)
    max_val = max(arr)
    return [(x - min_val) / (max_val - min_val) * (rmax - rmin) + rmin for x in arr]

print("Please select the normalization method:")
print("1 --> Min-Max")
print("2 --> Z-score")

choice = int(input("Enter your choice (1 or 2): "))

path = '01_input.csv'

with open(path, 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)
    data = list(reader)

print("\nAvailable columns:", headers)
col_index = int(input("Enter the column index to normalize (e.g., 3 for 'Weight'): "))

selected_column_data = [float(row[col_index]) for row in data]
print(f"\nSelected column data for normalization: {selected_column_data}")

output_text = ""

if choice == 1:
    rmin, rmax = map(int, input("Enter min and max values for Min-Max normalization (e.g., 0 1): ").split())
    normalized_data = minmax(selected_column_data, rmin, rmax)
    output_text = f"Min-Max Normalized Values: {normalized_data}"
    print(output_text)

elif choice == 2:
    normalized_data = zscore(selected_column_data)
    output_text = f"Z-score Normalized Values: {normalized_data}"
    print(output_text)

else:
    print("Invalid choice. Please enter 1 or 2.")
    output_text = "Invalid choice."

with open("normalization_output.txt", "w") as output_file:
    output_file.write(output_text)
