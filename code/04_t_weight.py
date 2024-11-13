import csv
from typing import List, Tuple

def calculate_total_weight(a_value: float, b_value: float) -> float:
    if a_value + b_value == 0:
        return 0
    return (a_value / (a_value + b_value)) * 100

def calculate_direct_weight(current_value: float, total: float) -> float:
    if total == 0:
        return 0 
    return (current_value / total) * 100

def write_to_csv(filename: str, regions: List[str], t_wt_a: List[float], 
                 t_wt_b: List[float], d_wt_a: List[float], d_wt_b: List[float]) -> bool:
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Region", "t_wt_A %", "t_wt_B %", "d_wt_A %", "d_wt_B %"])
            for i in range(len(regions)):
                writer.writerow([regions[i], f"\t\t{t_wt_a[i]:.2f}", f"\t{t_wt_b[i]:.2f}", 
                                 f"\t{d_wt_a[i]:.2f}", f"\t{d_wt_b[i]:.2f}"])
        return True
    except IOError as e:
        print(f"error writing to file {filename}. {e}")
        return False

def read_from_csv(filename: str) -> Tuple[List[str], List[float], List[float]]:
    regions, values_a, values_b = [], [], []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader) 
            for row in reader:
                regions.append(row[0])
                values_a.append(float(row[1]))
                values_b.append(float(row[2]))
        return regions, values_a, values_b
    except IOError as e:
        print(f"error oprning the file {filename}. {e}")
        return [], [], []

def main():
    input_filename = "04_t-weight.csv"
    regions, values_a, values_b = read_from_csv(input_filename)
    if not regions:
        return
    t_wt_a = [calculate_total_weight(a, b) for a, b in zip(values_a, values_b)]
    t_wt_b = [calculate_total_weight(b, a) for a, b in zip(values_a, values_b)]
    total_a = sum(values_a)  
    total_b = sum(values_b)  
    d_wt_a = [calculate_direct_weight(a, total_a) for a in values_a]
    d_wt_b = [calculate_direct_weight(b, total_b) for b in values_b]

    output_filename = "Output.csv"
    write_to_csv(output_filename, regions, t_wt_a, t_wt_b, d_wt_a, d_wt_b)

if __name__ == "__main__":
    main()