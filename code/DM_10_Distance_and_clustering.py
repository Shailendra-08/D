import csv
import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def read_data(file_name):
    data = []
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            unit_cost = float(row[1])
            discount_rate = float(row[2])
            data.append((unit_cost, discount_rate))
    return data

def calculate_mean_centroid(data):
    total_cost = sum(point[0] for point in data)
    total_discount = sum(point[1] for point in data)
    n = len(data)
    print("The Centroid Calculated based on the Mean is:")
    return (total_cost / n, total_discount / n)


def find_medoid(data, centroid):
    min_distance = float('inf')
    medoid = None
    for point in data:
        distance = euclidean_distance(point, centroid)
        if distance < min_distance:
            min_distance = distance
            medoid = point
    return medoid


def calculate_medoid_centroid(data):
   
    mean_centroid = calculate_mean_centroid(data)
    print(f"Calculated Mean Centroid: (Unit Cost: {mean_centroid[0]:.2f}, Discount Rate: {mean_centroid[1]:.2f})")

   
    medoid = find_medoid(data, mean_centroid)
    print(f"Nearest Point (Medoid) to Centroid: (Unit Cost: {medoid[0]}, Discount Rate: {medoid[1]})")

    return medoid

def print_upper_triangular_matrix(distances, labels, file):
    n = len(distances)
    file.write("Distance Matrix:\n")  
    file.write("       " + "".join([f"{label:<8}" for label in labels]) + "\n")  

    for i in range(n):
        file.write(f"{labels[i]:<5} | ")
        for j in range(n):
            if j > i:  
                file.write(f"{distances[i][j]:.2f}\t")
            else:
                file.write("0\t")  
        file.write("\n")  

def main():
    file_name = 'DM_10_Distance_clustering_data.csv' 
    data = read_data(file_name)


    with open('clustering_output.txt', 'w') as file:

    # Using Mean-based Centroid
    # centroid = calculate_mean_centroid(data)



        # Using Medoid-based Centroid
        centroid = calculate_medoid_centroid(data)  

        file.write(f"Centroid: (Unit Cost: {centroid[0]:.2f}, Discount Rate: {centroid[1]:.2f})\n\n")

        file.write("Distances from Centroid:\n")
        for i, point in enumerate(data):
            distance = euclidean_distance(point, centroid)  
            file.write(f"Product {i + 1}: {distance:.2f}\n")  
        file.write("\n")

        distances = []
        labels = [f"Product {i + 1}" for i in range(len(data))]  
        
        for i in range(len(data)):
            distance_row = []
            for j in range(len(data)):
                if i == j:
                    distance_row.append(0)  
                elif j > i:  
                    distance_row.append(euclidean_distance(data[i], data[j]))
                else:
                    distance_row.append(0)  
            distances.append(distance_row)

        print_upper_triangular_matrix(distances, labels, file)

    print("Clustering result has been written to 'clustering_output.txt'.")

if __name__ == "__main__":
    main()




  