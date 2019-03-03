import os
import csv

election_data_csv = os.path.join("Resources", "election_data.csv")
electionList = list()

with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    totalVotes = 0
    totalKhan = 0
    totalCorrey = 0
    totalLi = 0
    totalOTooley = 0
    winnerTotal = 0
    winnerName = ''

    for row in csvreader:
        voterID = int(row[0])
        county = row[1]
        candidate = row[2]

        #The total number of votes cast
        totalVotes = totalVotes + 1

        #A complete list of candidates who received votes
        if candidate == 'Khan':
            totalKhan += 1
            if winnerTotal < totalKhan:
                winnerTotal = totalKhan
                winnerName = 'Khan'
        elif candidate == 'Correy':
            totalCorrey += 1
            if winnerTotal < totalCorrey:
                winnerTotal = totalCorrey
                winnerName = 'Correy'
        elif candidate == 'Li':
            totalLi += 1
            if winnerTotal < totalLi:
                winnerTotal = totalLi
                winnerName = 'Li'
        elif candidate == "O'Tooley":
            totalOTooley +=1
            if winnerTotal < totalOTooley:
                winnerTotal = totalOTooley
                winnerName = "O'Tooley"

    print('Election Results')
    print('----------------------')
    print(f'Total Votes: {totalVotes}')
    print('----------------------')
    print(f'Khan: {round((totalKhan/totalVotes)*100,3)}% ({totalKhan})')
    print(f'Correy: {round((totalCorrey/totalVotes)*100,3)}% ({totalCorrey})')
    print(f'Li: {round((totalLi/totalVotes)*100,3)}% ({totalLi})')
    print(f"O'Tooley: {round((totalOTooley/totalVotes)*100,3)}% ({totalOTooley})")
    print('----------------------')
    print(f'Winner: {winnerName}')
    print('----------------------')
