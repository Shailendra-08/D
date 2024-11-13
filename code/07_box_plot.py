import csv

def median(arr):
    arr_sorted = sorted(arr)
    n = len(arr_sorted)
    if n % 2 == 0:
        return (arr_sorted[n//2 - 1] + arr_sorted[n//2]) / 2
    else:
        return arr_sorted[n//2]

def getQ1(arr):
    arr_sorted = sorted(arr)
    n = len(arr_sorted)
    # Q1 is the median of the lower half
    return median(arr_sorted[:n//2])

def getQ2(arr):
    return median(arr)

def getQ3(arr):
    arr_sorted = sorted(arr)
    n = len(arr_sorted)
    # Q3 is the median of the upper half
    return median(arr_sorted[(n+1)//2:])

def five_number_summary(arr):
    arr_sorted = sorted(arr)
    Q1 = getQ1(arr)
    Q2 = getQ2(arr)
    Q3 = getQ3(arr)
    IQR = Q3 - Q1
    mini = min(arr_sorted)
    maxi = max(arr_sorted)
    outliers = [x for x in arr_sorted if x < Q1 - 1.5 * IQR or x > Q3 + 1.5 * IQR]
    return Q1, Q2, Q3, IQR, mini, maxi, outliers

def min_max_normalization(data, min_val, max_val):
    data_min = min(data)
    data_max = max(data)
    return [(x - data_min) / (data_max - data_min) * (max_val - min_val) + min_val for x in data]

# Read data from CSV
path = 'cropcultivation.csv'  # Replace with your CSV file path
data = []
with open(path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header if any
    for row in reader:
        data.append(float(row[0]))  # Assuming data is in the first column

# Apply box-plot before normalization
Q1, Q2, Q3, IQR, low, high, outliers = five_number_summary(data)

# Get min and max values for normalization from user input
min_val = float(input("Enter the minimum value for normalization: "))
max_val = float(input("Enter the maximum value for normalization: "))

# Open the output file to write the results
with open('box_output.txt', 'w') as file:
    file.write("Five Number Summary before normalization:\n")
    file.write("Data (sorted): " + str(sorted(data)) + "\n")
    file.write(f"Q1: {Q1}\n")
    file.write(f"Q2 (Median): {Q2}\n")
    file.write(f"Q3: {Q3}\n")
    file.write(f"IQR: {IQR}\n")
    file.write(f"Low: {low}, High: {high}\n")
    file.write(f"Outliers: {outliers}\n")
    file.write("-" * 50 + "\n")

    # Normalize data using Min-Max normalization
    normalized_data = min_max_normalization(data, min_val, max_val)

    # Apply box-plot after normalization
    Q1_norm, Q2_norm, Q3_norm, IQR_norm, low_norm, high_norm, outliers_norm = five_number_summary(normalized_data)

    file.write("\nFive Number Summary after normalization:\n")
    file.write("Normalized Data (sorted): " + str(sorted(normalized_data)) + "\n")
    file.write(f"Q1: {Q1_norm}\n")
    file.write(f"Q2 (Median): {Q2_norm}\n")
    file.write(f"Q3: {Q3_norm}\n")
    file.write(f"IQR: {IQR_norm}\n")
    file.write(f"Low: {low_norm}, High: {high_norm}\n")
    file.write(f"Outliers: {outliers_norm}\n")
    file.write("-" * 50 + "\n")

print("Results written to box_output.txt")