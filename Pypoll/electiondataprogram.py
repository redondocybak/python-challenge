import csv

def load_data(csv_path):
    total_votes = 0
    candidate_votes = {}

    with open(csv_path) as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader) 

        for x in csvreader:
            total_votes += 1 
            candidate = x[2]

            if candidate not in candidate_votes:
                candidate_votes[candidate] = 0  

            candidate_votes[candidate] += 1

    return total_votes, candidate_votes

def calculate_results(total_votes, candidate_votes):
    output = (
        "Election Results\n"
        "-------------------------\n"
        f"Total Votes: {total_votes}\n"
        "-------------------------\n"
    )
    for candidate, votes in candidate_votes.items():
        vote_percentage = (votes / total_votes) * 100
        output += f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

    winner = max(candidate_votes, key=candidate_votes.get)
    output += (
        "-------------------------\n"
        f"Winner: {winner}\n"
        "-------------------------\n"
    )
    return output

def output_results(output):
    print(output)

    with open("election_results.txt", "w") as file:
        file.write(output)

    print("Election Results have been saved to 'election_results.txt'.")

def main():
    csv_path = 'election_data.csv'
    total_votes, candidate_votes = load_data(csv_path)
    output = calculate_results(total_votes, candidate_votes)
    output_results(output)

main()