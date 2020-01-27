# Dependencies
import os
import csv

# Path to csv
employee_data_csv = os.path.join('Resources', 'employee_data.csv')
employee_data_output = os.path.join('Resources', 'employee_data_output.csv')

empID = []
empFirstName = []
empLastName = []
empDOB = []
empSSN = []
empState = []

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Openning csv
with open(employee_data_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvfile)
    for row in csvreader:
        empID = empID + [row[0]]
        # The Name column should be split into separate First Name and Last Name columns
        nameSplit = row[1].split(' ')
        empFirstName = empFirstName + [nameSplit[0]]
        empLastName = empLastName + [nameSplit[1]]
        # The DOB data should be re-written into MM/DD/YYYY format
        changeDOB = row[2].split('-')
        month = changeDOB[2]
        day = changeDOB[1]
        year = changeDOB[0]
        changedDOB = f"{month}/{day}/{year}"
        empDOB.append(changedDOB)
        # The SSN data should be re-written such that the first five numbers are hidden from view
        SSN_split = list(row[3])
        SSN_split[0:3] = ('*', '*', '*')
        SSN_split[4:6] = ('*', '*')
        SSN_join = ''.join(SSN_split)
        empSSN.append(SSN_join)
        # The State data should be re-written as simple two-letter abbreviations
        state_abbrev = us_state_abbrev[row[4]]
        empState.append(state_abbrev)
        
emp_zip = zip(empID, empFirstName, empLastName, empDOB, empSSN, empState)

with open(employee_data_output, 'w', newline='') as datafile:
    csv_writer = csv.writer(datafile)
    csv_writer.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
    csv_writer.writerows(emp_zip)
