#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote

# Assign a variable for file to load and path
file_to_load = 'Resources\election_results.csv'

#open the election results and read the files
#election_data = open(file_to_load,'r')
with open(file_to_load) as election_data:



    #To perform analysis

    print(election_data)

import os
dir(os)
dir(os.path)

# close the file
election_data.close()