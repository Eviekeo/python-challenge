#import the csv and os modules
import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join("Resources", "election_data.csv")

# Lists and dictionaries to store data
voterID = []
candidate = []
votes = {}

# Open and read csv 
with open(election_data_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # Read the header row first 
    csv_header = next(csv_file)

    # Append column 1 of the csv file to the empty voterID list
    for row in csv_reader:
        voterID.append(row[0])
        
        # fill the list with unique candidates using 'if', and reset the vote count to zero for each unique candidate
        if row[2] not in candidate:
            candidate.append(row[2])  
            votes[row[2]]=0
        # where the candidate is the same, add it to the vote count    
        votes[row[2]] += 1

    # calculate the vote count percentages
    percentages = {key: round((val / len(voterID)*100),3) for key, val in votes.items()}

    # use max to get identify the winning candidate
    winning_candidate = max(votes, key=votes.get)
    # Count the number of rows in the voterID column
    total_votes = len(voterID)

#save the output file path
output_file = os.path.join("Analysis","output.txt")  
with open(output_file, "w") as datafile:
    # Print the results:
    output_1= (f"Election Results\n"
    f"---------------------------------------------------\n"
    f"Total Votes: {str(total_votes)}\n"
    f"---------------------------------------------------\n")
    print(output_1)
    datafile.write(output_1)
    datafile.write("\n")
    for key, val in votes.items():
        output_2=(f"{key}: {percentages[key]}% ({val})\n")
        print(output_2)
        datafile.write(output_2)
        datafile.write("\n")
    output_3= (f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"-------------------------")
    print(output_3)
    datafile.write(output_3)

