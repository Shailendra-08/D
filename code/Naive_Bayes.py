import csv

def printing_output(message, file):
    print(message)
    file.write(message + "\n")

data = []
with open('Naive_bayes_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if row:
            data.append(row)

with open('Navie_output.txt', 'w') as output_file:

    total = len(data)
    yes_count = sum(1 for row in data if row[-1] == "yes")
    no_count = total - yes_count
    prob_yes = f"{yes_count}/{total} = {yes_count / total:.3f}"
    prob_no = f"{no_count}/{total} = {no_count / total:.3f}"

    printing_output(f"Total count of 'yes': {yes_count}, Probability of 'yes': {prob_yes}", output_file)
    printing_output(f"Total count of 'no': {no_count}, Probability of 'no': {prob_no}\n", output_file)

    def calculate_prob(index, value, target):
        count = yes_count if target == "yes" else no_count
        match_count = sum(1 for row in data if row[index] == value and row[-1] == target)
        result = match_count / count if count else 0
        printing_output(f"Probability of attribute[{index}]={value} | Target={target}: {match_count}/{count} = {result:.3f}", output_file)
        return result

    test_instance = ["sunny", "cool", "high", "strong"]

    printing_output(f"\nTest instance to be classified: {test_instance}\n", output_file)

    def calculate_posterior(target):
        posterior = yes_count / total if target == "yes" else no_count / total
        for i, value in enumerate(test_instance):
            posterior *= calculate_prob(i, value, target)
        return posterior

    posterior_yes = calculate_posterior("yes")
    posterior_no = calculate_posterior("no")

    printing_output(f"\nProbability of instance for 'yes': {posterior_yes:.6f}", output_file)
    printing_output(f"Probability of instance for 'no': {posterior_no:.6f}\n", output_file)

    printing_output(f"Comparing posterior probabilities:\nP('yes' | X) = {posterior_yes:.6f} vs P('no' | X) = {posterior_no:.6f}", output_file)
    predicted_class = "yes" if posterior_yes > posterior_no else "no"

    printing_output(f"\nPredicted Class: {predicted_class}", output_file)
