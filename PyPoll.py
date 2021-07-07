import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Print the file object.
     #print(election_data)
    file_reader = csv.reader(election_data)
    #for row in file_reader:
        #print(row)
    headers = next(election_data)
    print(headers)

    

#create a filename 
#outfile = open(file_to_save, "w")
#outfile.write("hello World")
#outfile.close
#with open(file_to_save, "w") as text_file:
    #text_file.write("Hello World\n")
    #text_file.write("Counties In The Election\n--------------------------\n")
    #text_file.write("Araphoe ,")
    #text_file.write("Denver ,")
    #text_file.write("Jefferson ,")


