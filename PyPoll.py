# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Resources/election_results.csv
# /Users/crkaide/OneDrive - IL State University/Vanderbilt/Vanderbilt/Assignments/3_Python/Election_Analysis/Resources/election_results.csv





# # Assign a variable for the file to load and the path.
# file_to_load = '/Users/crkaide/OneDrive - IL State University/Vanderbilt/Vanderbilt/Assignments/Three_3_Python/Election_Analysis/Resources/election_results.csv'

# # Open the election results and read the file
# with open(file_to_load) as election_data:

#      # To do: perform analysis.
#      print(election_data)



# 1. Import the csv and os modules.
import csv
import os

# 2. Add the filename variable that references the path to election_results.csv.
file_to_load = '/Users/crkaide/OneDrive - IL State University/Vanderbilt/Vanderbilt/Assignments/Three_3_Python/Election_Analysis/Resources/election_results.csv'

# 3. Open the election_results.csv using the with statement as the filename object, election_data.
with open(file_to_load) as election_data:

    # 4. Print the filename object.
    print(election_data)


