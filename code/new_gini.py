import csv

def read_data(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            data.append(row)
    return data

def count_classes(subset):
    class_counts = {}
    for entry in subset:
        class_label = entry[1]
        if class_label in class_counts:
            class_counts[class_label] += 1
        else:
            class_counts[class_label] = 1
    return class_counts

def calculate_gini_index(subset):
    total_instances = len(subset)
    if total_instances == 0:
        return 0
    class_counts = count_classes(subset)
    gini = 1
    for count in class_counts.values():
        probability = count / total_instances
        gini -= probability ** 2
    return gini

def weighted_gini(data, attribute_index=0):
    total_instances = len(data)
    subsets = {}

    # Divide data into subsets based on unique values in the specified attribute
    for entry in data:
        attribute_value = entry[attribute_index]
        if attribute_value not in subsets:
            subsets[attribute_value] = []
        subsets[attribute_value].append(entry)

    weighted_gini_value = 0
    for subset in subsets.values():
        subset_size = len(subset)
        subset_gini = calculate_gini_index(subset)
        weighted_gini_value += (subset_size / total_instances) * subset_gini

    return weighted_gini_value, subsets

# Main program
filename = "gini1.csv"
data = read_data(filename)

weighted_gini_value, subsets = weighted_gini(data)
print(f"Weighted Gini Index for splitting on 'Colour': {weighted_gini_value:.4f}")

# Gini index for each subclass of Colour
for colour, subset in subsets.items():
    print(f"Gini Index for {colour}: {calculate_gini_index(subset):.4f}")
