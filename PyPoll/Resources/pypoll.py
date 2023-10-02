import csv
import os

# this is the path to the soruces file
file_path = os.path.join("Resources", "election_data.csv")

# counting the vote beginning with 0
TotalVotes = 0
candidates_dict = {}  # Initialize a dictionary to store the vote counts for each candidate

# open the file with read mode
with open(file_path, mode='r') as file:
    
    csv_reader = csv.reader(file)
    
    # Skip the header row, don't read the necessary data
    next(csv_reader)
    
    # looping starts from here
    for row in csv_reader:
        TotalVotes += 1  # Increment the vote count for every row
        
        # Extract the candidate name from each row (assuming it's in the third column)
        candidate_name = row[2]
        
        # If the candidate is already in the dictionary, increment their vote count. If not, add them to the dictionary with a vote count of 1.
        if candidate_name in candidates_dict:
            candidates_dict[candidate_name] += 1
        else:
            candidates_dict[candidate_name] = 1

# to display correctly base on the requirements
print("Election Results")
print("-------------------------")
print("Total Votes: ", TotalVotes)
print("-------------------------")

#set up variables to determine the winner
winner_name = ""
winner_votes = 0

# Calculate and print the required data for each candidate
for candidate, votes in candidates_dict.items():
    percentage = (votes / TotalVotes) * 100  # Calculate the percentage of total votes for the candidate
    print(f"{candidate}: {percentage:.3f}% ({votes})")  # Print the candidate's name, their percentage of the total votes, and their total vote count
                                                        # format to 3 digits after the decimal
    # find out the winner
    if votes > winner_votes:
        winner_votes = votes
        winner_name = candidate

# display the result as required
print("-------------------------")
print("Winner: ", winner_name)
print("-------------------------")
