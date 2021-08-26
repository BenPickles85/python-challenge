# Modules
import os
import csv

#Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

#Create dicitonary for results
election_results = {}

#Set vote count variable as zero
vote_count = 0

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #Set header
    csv_header = next(csvreader)  
        
    for row in csvreader:           
    
    #Calculate total votes
        vote_count += 1

    #Set dictionary key as candidate names
        candidate = row[2]
        election_results.setdefault(candidate, 0)

    #Count votes for each candidate and store as value
        election_results[candidate] += 1

#Create lists from dictionary for candidates and their vote count
candidate_list = []
candidate_votes = []

#Create list of candidates and similar list for their respective vote counts
for candidate, votes in election_results.items():
    candidate_list.append(candidate)
    candidate_votes.append(votes)

#Calculate percentage of vote for each candidate and create a list for this
vote_percentage = []

for votes in candidate_votes:
    vote_percentage.append(round(votes/vote_count * 100, 2))
    
#Create tuple of candidate name, vote percentage and votes won
final_data = list(zip(candidate_list, vote_percentage, candidate_votes))

#determine winning candidate
winning_candidate = []

for candidate in final_data:
    if max(candidate_votes) == candidate[2]:
        winning_candidate.append(candidate[0])

#print list of candidates and results
print('Election Results \n------------------------')
print(f'Total Votes: {vote_count}\n------------------------')

for i in range(len(final_data)):
    print(f'{candidate_list[i]}: {vote_percentage[i]}% ({candidate_votes[i]})')

print(f'------------------------\nWinner: {winning_candidate[0]}\n------------------------')

#Create and write results to text file
textpath = os.path.join("Analysis", "Polling_Summary.txt")
with open(textpath, 'w') as text_file:
    text_file.writelines('Election Results \n------------------------\n')
    text_file.writelines(f'Total Votes: {vote_count}\n------------------------\n')
    for i in range(len(final_data)):
        text_file.writelines(f'{candidate_list[i]}: {vote_percentage[i]}% ({candidate_votes[i]})\n')
    text_file.writelines(f'------------------------\nWinner: {winning_candidate[0]}\n------------------------')