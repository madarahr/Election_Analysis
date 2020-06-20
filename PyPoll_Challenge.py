# Add our dependencies.
import csv
import os


# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources\election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# County Options.
county_options = []
# Declare the empty dictionary.
county_votes = {}

# Largest county turnout
largest_county = ""
largestCounty_count = 0

# Candidate Options.
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Print the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count.
        total_votes += 1



        # Print the candidate name and county name from each row
        candidate_name = row[2]
        county_name = row[1]

        # If the county does not match any existing county...
        if county_name not in county_options:
            #Add it to the list of counties.
            county_options.append(county_name)

            # Begin tracking that county's vote count.
            county_votes[county_name] = 0
        
        # Add a vote to that county's count.
        county_votes[county_name] += 1


        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    #Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"----------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------------\n" "\n"
        f"County Votes:\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Irerate through each county.
    for county in county_votes:

        # retrieve vote turnout from each county 
        countyVotes = county_votes[county]

        # percentage of voter turnout from each county
        countyVote_percentage = float(countyVotes) / float(total_votes) * 100

        # Print each county's name, voter turnout, and percentage of turnout to terminal
        county_results = (
            f"{county}: {countyVote_percentage:.1f}% ({countyVotes:,})\n")
        
        # Print each county's name, voter turnout, and percentage to turnout the terminal.    
        print(county_results)

        #  Save the candidate results to our text file.
        txt_file.write(county_results)
        
        # Determine county with largest vote count.
        # Determine if the voter turnout is greater than the county votes.
        if (countyVotes > largestCounty_count):
            
            # If true then set largestCounty_count = countyVotes
            largestCounty_count = countyVotes
            largest_county = county

            # Set the county with largest turnout to summary
            largest_county_summary = ("\n"           
            f"------------------------\n"
            f"Largest County Turnover: {largest_county}\n"
            f"------------------------\n")

    # Print county with largest voter turnout to terminal    
    print(largest_county_summary)

    # write voter turnout to our output file.
    txt_file.write(largest_county_summary)


    # Iterate through the candidate list.
    for candidate in candidate_votes:
        
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # Print out each candidate's name, vote count, and percentage of votes to terminal

        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
    
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate

    #print(largest_county_summary)
    
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n") 
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)