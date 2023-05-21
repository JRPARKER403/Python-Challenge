import os
import csv

#election_data.csv ='"C:\Users\JMARS\OneDrive\Desktop\Bootcamp\HOMEWORK\python-challenge\PyPoll\Resources\election_data.csv"'
election_data = os.path.join("/election_data.csv")

# Open and read csv
with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")

    #variables
    candidates = []
    num_votes = 0
    vote_counts = []
    percent_votes = []
    total_votes = []
    max_votes = vote_counts[0]
    max_index = 0
    candidate = []


    #total number of votes
    num_votes = num_votes + 1

    #voted for candidate
    candiate = row[2]

    #if other votes are present for a candidate
    if candidate in candidates:
        candidate_index = candidates.index(candidate)
        vote_counts[candidate_index] = vote_counts[candidate_index] + 1
    else:
        candidates.append(candidates)
        vote_counts.append(1)
   
   #find the percentages for each candidate
for count in range(len(candidate)):
    vote_percentage = vote_counts[count]/num_votes*100
    percent_votes.append(vote_percentage)
    if vote_counts[count]> max_votes:
        max_votes = vote_counts[count]
        print(max_votes)
        max_index = count

    #the winner is
winner = candidates [max_index]   

#print results

print("Election Results")
print("---------------------")
print(f"Total Votes: {num_votes}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percent_votes[count]}% ({vote_counts[count]})")
print("---------------------")   
print(f"Winner: {winner}")
print("---------------------")   
    
    
   
   
   
   
   
   
   
   
   

    
    

