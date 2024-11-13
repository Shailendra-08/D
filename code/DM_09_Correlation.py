import csv
import math

def find_mean(values):
    mean_value = sum(values) / len(values)
    return mean_value


def find_covariance(a, b, mean_a, mean_b):
    covariance = sum((a[i] - mean_a) * (b[i] - mean_b) for i in range(len(a))) / len(a)
    return covariance

def find_standard_deviation(values, mean):
    variance = sum((x - mean) ** 2 for x in values) / (len(values) - 1)
    standard_deviation = math.sqrt(variance)
    return standard_deviation

def find_correlation(a, b):
    mean_a = find_mean(a)
    mean_b = find_mean(b)
    covariance = find_covariance(a, b, mean_a, mean_b)
    sd_a = find_standard_deviation(a, mean_a)
    sd_b = find_standard_deviation(b, mean_b)
    
    if sd_a == 0 or sd_b == 0:
        return None, mean_a, mean_b, covariance, sd_a, sd_b
    
    correlation = covariance / (sd_a * sd_b)
    return correlation, mean_a, mean_b, covariance, sd_a, sd_b

def read_csv(filename):
    x_data, y_data = [], []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            x_data.append(float(row[0]))
            y_data.append(float(row[1]))
    return x_data, y_data

# File paths
input_filename = 'DM_09_correlation.csv'
output_filename = 'correlation_output.txt'

# Read data from the CSV
x_data, y_data = read_csv(input_filename)

# Calculate correlation and intermediate values
correlation, mean_x, mean_y, covariance, sd_x, sd_y = find_correlation(x_data, y_data)

# Write the results to the output file
with open(output_filename, 'w') as file:
    # Mean of X and Y
    file.write(f"Mean of X: {mean_x}\n")
    file.write(f"Mean of Y: {mean_y}\n\n")
    
    # Covariance
    file.write(f"Covariance: {covariance}\n\n")
    
    # Standard Deviation of X and Y
    file.write(f"Standard Deviation of X: {sd_x}\n")
    file.write(f"Standard Deviation of Y: {sd_y}\n\n")
    
    # Pearson Correlation Coefficient
    if correlation is not None:
        file.write(f"Pearson Correlation Coefficient (r): {correlation}\n")
        if correlation > 0:
            file.write("Interpretation: Positive correlation\n")
        elif correlation < 0:
            file.write("Interpretation: Negative correlation\n")
        else:
            file.write("Interpretation: No correlation\n")
    else:
        file.write("Correlation cannot be calculated due to zero variance in one of the datasets.\n")

# Confirmation message
print(f"Correlation result has been written to '{output_filename}'.")
