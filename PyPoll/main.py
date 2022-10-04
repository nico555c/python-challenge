#In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

#You will be given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following:

#* The total number of votes cast

#* A complete list of candidates who received votes

#* The percentage of votes each candidate won

#* The total number of votes each candidate won

#* The winner of the election based on popular vote.

#Your analysis should look similar to the following:

#  Election Results
#-------------------------
#  Total Votes: 369711
#-------------------------
#  Charles Casper Stockham: 23.049% (85213)
#  Diana DeGette: 73.812% (272892)
#  Raymon Anthony Doane: 3.139% (11606)
# -------------------------
#  Winner: Diana DeGette
#  -------------------------
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import csv
import os




csv_path = os.path.join("Resources", "election_data.csv")

#define variables
i= 0
total_votes = 0
#list of all candidates
candidate_list =[]
#dictionary to store unique names and number of occurences
unique_dic ={}
#unique lists
u_c_list = []
per_list =[]
vote_list =[]
name_list =[]
per_format_list=[]
#variables for calculations
vote = 0
u_vote = 0
u_vote_per = 0
max_vote = 0

newfile_path = os.path.join('Analysis','analysis.txt')

with open(newfile_path,'w') as newfile:



    with open(csv_path, encoding = "utf8") as csvfile:

        csvreader = csv.reader(csvfile, delimiter = ",")
        heder = next(csvreader)

#calculate total votes and create unique list
        for each_row in csvreader:

            total_votes = total_votes + 1
            candidate_list.append(each_row[2])

        print("Election Results")        
        print("-------------------------")  
        print(f"Total Votes: {str(total_votes)}")        
        print("-------------------------")  
    newfile.write("Election Results \n")
    newfile.write("-------------------------- \n")
    newfile.write("Total votes: %s \n" % (total_votes))

    for i in candidate_list:
        unique_dic[i] = unique_dic.get(i,0) +1 

    u_c_list = list(unique_dic.items())

    for each_row in u_c_list:
        name = str(each_row[0])
        vote = int(each_row[1])
        u_vote_per = vote/total_votes
        per_list.append(u_vote_per)
        vote_list.append(vote)
        name_list.append(name)

      

    for i in range(len(name_list)):
        per_format = "{:.3%}".format(per_list[i])
        per_format_list.append(per_format)
        print(f'{name_list[i]}: {per_format} ({vote_list[i]}) ')
        newfile.write(f'{name_list[i]}: {per_format} ({vote_list[i]}) \n')

    print("-------------------------") 
    newfile.write("-------------------------- \n")
    
    for i in range(len(vote_list)):
        if max_vote < vote_list[i]:
            max_vote = vote_list[i]
            winner = name_list[i]
        else: 
            max_vote = max_vote
            

    
    print(f'Winner: {str(winner)}')
    print("-------------------------") 
    newfile.write("Winner: %s \n" % (winner))
    newfile.write("-------------------------- \n")








