'''Question-1:
Given a list of all runs by Virat Kohli, create a new list of runs made in last 5 matches.

input_runs = [62, 85, 74, 10, 12, 101, 122, 99, 81, 55]

Expected_Output = [101, 122, 99, 81, 55]'''


input_runs = [62, 85, 74, 10, 12, 101, 122, 99, 81, 55]

LastMatches = int(input("Enter the last no of matches you want to process: "))
backCount = 0-LastMatches

lastMatchesList = []
j = backCount
while j <= -1:
    lastMatchesList.append(input_runs[j])
    j+=1

for each in lastMatchesList:
    print(each, end = ' ')

