'''Question-1:
Given a list of all runs by Virat Kohli, create a new list of runs made in last 5 matches.

input_runs = [62, 85, 74, 10, 12, 101, 122, 99, 81, 55]

Expected_Output = [101, 122, 99, 81, 55]'''


input_runs = [62, 85, 74, 10, 12, 101, 122, 99, 81, 55]
# size = len(input_runs)
last5Matches = []
# for i in range(-1, -6, -1):
#     print(i, input_runs[i])
#     last5Matches.append(input_runs[i])
j = -5
while j <= -1:
    # print(input_runs[j])
    last5Matches.append(input_runs[j])
    j+=1

for each in last5Matches:
    print(each, end = ' ')

