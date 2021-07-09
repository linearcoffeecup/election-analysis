
# POSSIBLE MODIFCATIONS FOR ELECTIONS

# 1) User inputs counties and candidates then code enters into a dictionary

Supplemental_Dict = {"The_Candidate" : "" , "The_County" : ""}

FirstName = input("Input candidate's FirstName: \n")
MiddleName = input("Input candidate's MiddleName: \n")
LastName = input("Input candidate's LastName: \n\n")
FullName = "FirstName" + " " + "MiddleName" + " " + "LastName"

TheCounty =  input("Input name of candidate's county: ")

Supplemental_Dict["The_Candidate"] = FullName
Supplemental_Dict["The_County"] = TheCounty

print(Supplemental_Dict)

# 2) Create the ability to track election-analysis.txt as election-analysis-reports.txt
#    which appends each previous report to the current report

# Add a report_counter then append each output text file to election_analysis.txt
report_counter = 0
report_counter += 1
# Append to election_analysis.txt
with open("file_to_save", "a") as txt_file
txt_file.write("report number =" + str(report_counter), end ="")
report_to_append = (    f'{election_results}
                        f'{county_results}
                        f'{largest_county_summary}
                        f'{candidate_results}'
                        f'{winning_candidate_summary}' )
