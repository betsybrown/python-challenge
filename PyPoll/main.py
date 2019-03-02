import os
import csv

#choose method of importing csv
csvpath=os.path.join('..','PyPoll','election_data.csv')

with open(csvpath, newline='') as csvfile:
    #define cvsreader
    csvreader = csv.reader(csvfile,delimiter=',')
    #print csv
    #print(csvreader)
    #read header row
    csv_header = next(csvreader)
    #print(f"CSV Header = {csv_header}")

    #print each row of data after header
    #for rows in csvreader:
        #print(rows)


    totalVotes = 0
    candidateVotes = {}
    voteWinner = ""

    for rows in csvreader:
        totalVotes = totalVotes + 1
        candidateVotes[rows[2]] = 0


    csvfile.seek(0)
    csv_header = next(csvreader)

    for rows in csvreader:
        candidateVotes[rows[2]] += 1

    summary = (
        "Election Results\n"
         "-----------------------------------\n" 
         f'Total Votes:  {totalVotes}\n'
         "-----------------------------------\n"
    )

    print()
    print("Election Results")
    print("-----------------------------------")
    print(f'Total Votes:  {totalVotes}')
    print("-----------------------------------")
    #print(f'Candidates:   {candidateVotes}')
    mostVoteCount = 0
    candidateList = []
    candidateVoteCount = []
    newTable = {}

    winnerCount = 0
    
    for c in candidateVotes:
        candidateVoteTotals = candidateVotes[c]
        candidateVoteCount.append(candidateVoteTotals)

        candidate = c
        candidateList.append(candidate)
        percentOfVote = candidateVoteTotals/totalVotes 
  
        if candidateVotes[c] > winnerCount:
                winnerCount = candidateVotes[c]
                voteWinner = c

      


        #print(f'{c}:  {candidateVotes[c]} {candidateVotes[c]/(totalVotes)}')
        print(f'{c}:   {(candidateVotes[c]*100/(totalVotes)):.2f}% ({candidateVotes[c]})')

        summary2 = (
             f'{c}:   {(candidateVotes[c]*100/(totalVotes)):.2f}% ({candidateVotes[c]})\n'

            )   
    
    #print('new')
    #print(winnerCount)
    #print(voteWinner)

    #newTable = candidateList + candidateVoteCount
    #print(newTable)
        
    """ if newTable > mostVoteCount:
            mostVoteCount = newTable[0]
            voteWinnner = newTable[0]"""
       

    print(f'Vote Winner:   {voteWinner}')

    summary3 = (
        f'Vote Winner:   {voteWinner}'
    
    )
    import os.path
    with open(os.path.join('..','PyPoll', "ElectionResults.txt"), "w") as f:
        f.write(summary+summary2+summary3)