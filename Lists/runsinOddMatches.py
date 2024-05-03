'''Question-2:
Given a list of all runs by Virat Kohli, create a new list of runs made in odd matches (even indices).

input_runs = [62, 85, 74, 10, 12, 101, 122, 99, 81, 55]

Expected_Output:
[62, 74, 12, 122, 81]'''

input_runs = [62, 85, 74, 10, 12, 101, 122, 99, 81, 55]

# i = 0
oddMatchList=[]
for i in range(0, len(input_runs), 2):
    # print(i, input_runs[i])
    oddMatchList.append(input_runs[i])

for each in oddMatchList:
    print(each, end = ' ')
