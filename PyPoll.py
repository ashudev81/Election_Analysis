#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote



# add dpendencies 
import csv
import os


# Assign a variable for file to load and path
#file_to_load = 'Resources\election_results.csv'
file_to_load = os.path.join("Resources","election_results.csv")

# Create the file name variable to a direct path to a file
file_to_save = os.path.join("analysis","election_analysis.txt")

# 1. initialized the votes counter
total_votes = 0

# candidate options
candidate_options = []

# create empty dictionary
candidate_vote= {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


#open the election results and read the files
#election_data = open(file_to_load,'r')
with open(file_to_load) as election_data:

    # read the file object with reader function
    file_reader = csv.reader(election_data)

    
    #print the header

    headers = next(file_reader)
       
    # print the row in file reader.
    for row in file_reader:
        
        # 2. Add to total vote count. 
        total_votes = total_votes + 1

        # print candidate name from each row
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:

            # add candidate name to candidate options
            candidate_options.append(candidate_name) 

            # begin candidate vote count
            candidate_vote[candidate_name] = 0

        # adding the vote
        candidate_vote[candidate_name] +=1

    # Determine the percentage of the votes received by candidate
    # iterate through candidate list
    for candidate_name in candidate_vote:

        # retrive the vote
        vote= candidate_vote[candidate_name]

        # calculate vote percentage
        vote_percentage = float(vote)/float(total_votes)*100

        # print candidate percentage
        print(f'{candidate_name}: {vote_percentage:.1f}% ({vote:,})\n')

        # Determine candidate votes and winning
        # Determine if votes is grater than winning vote
        if (vote>winning_count) and (vote_percentage>winning_percentage):
            #if true then chnage winning count to vote count.
            #winning percentage = vote percentage
            winning_count= vote
            winning_percentage= vote_percentage
            winning_candidate= candidate_name
    
    winning_candidate_summary = (
        f"----------------------------------------\n"
        f"winner: {winning_candidate}\n"
        f"winning vote count: {winning_count:}\n"
        f"winning percentage: {winning_percentage:.1f}%\n"
        f"-----------------------------------------\n")
    print(winning_candidate_summary)

    

# 3. print total votes

print(candidate_vote)

    #To perform analysis

    #print(election_data)

dir(os)
dir(os.path)



# using open function with w write permision we will open and the write to the file
#outfile = open(file_to_save,"w")

with open(file_to_save,"w") as txt_file:


    # write some data to the file
    txt_file.write("Counties in the Election\n__________________________\nArapahoe\nDenver\nJefferson")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson ")

#outfile.write("Hello World")


#clsoe the file

#outfile.close()





# close the file
election_data.close()