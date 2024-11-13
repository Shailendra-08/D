import csv
import math

def entropy(data, target_attribute_index, file):
    freq = {}
    for row in data:
        target_value = row[target_attribute_index]
        if target_value in freq:
            freq[target_value] += 1
        else:
            freq[target_value] = 1
    
    total = len(data)
    ent = 0
    for count in freq.values():
        prob = count / total
        ent -= prob * math.log2(prob) if prob > 0 else 0  # Avoid log(0) error
    
    file.write(f"Entropy of the current set: {ent:.4f}\n")
    return ent

def info_gain(data, attribute_index, target_attribute_index, file):
    original_entropy = entropy(data, target_attribute_index, file)
    
    subsets = {}
    for row in data:
        attribute_value = row[attribute_index]
        if attribute_value in subsets:
            subsets[attribute_value].append(row)
        else:
            subsets[attribute_value] = [row]
    
    total_rows = len(data)
    subset_entropy = 0
    for attribute_value, subset in subsets.items():
        prob_subset = len(subset) / total_rows
        entropy_subset = entropy(subset, target_attribute_index, file)
        subset_entropy += prob_subset * entropy_subset
    
    return original_entropy - subset_entropy

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Read headers
        for row in reader:
            data.append(row)
    return data, headers

def best_split(data, headers, target_attribute_index, file):
    best_attribute_index = None
    best_info_gain = -1
    
    # Loop through all attributes (excluding the target attribute)
    for i in range(len(headers)):
        if i != target_attribute_index:
            ig = info_gain(data, i, target_attribute_index, file)
            file.write(f"Information Gain for {headers[i]}: {ig:.4f}\n")
            
            # Find the attribute with the highest information gain
            if ig > best_info_gain:
                best_info_gain = ig
                best_attribute_index = i
    
    return best_attribute_index, best_info_gain

def main():
    input_filename = "03_entropy.csv"  
    data, headers = read_csv(input_filename)

    target_attribute_index = len(data[0]) - 1  
    
    with open("info_output.txt", "w") as file:
        file.write(f"Target attribute: {headers[target_attribute_index]}\n\n")
        
        best_attribute_index, best_info_gain = best_split(data, headers, target_attribute_index, file)
        
        if best_attribute_index is not None:
            file.write(f"\nBest attribute to split on: {headers[best_attribute_index]}\n")
            file.write(f"Information Gain: {best_info_gain:.4f}\n")
        else:
            file.write("No best attribute found for splitting.\n")
    
    print("Output written to info_output.txt")

if __name__ == "__main__":
    main()
