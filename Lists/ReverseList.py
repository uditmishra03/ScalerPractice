'''Given a list of all runs by Virat Kohli, create a new list of with opposite Order i.e. Last Match Runs as first Match and So On.

input_runs = [62, 85, 74, 10, 12, 101, 122, 99, 81, 55]

Expected_Output = [55, 81, 99, 122, 101, 12, 10, 74, 85, 62]'''

input_runs = [62, 85, 74, 10, 12, 101, 122, 99, 81, 55]
reversed_list = []
print("input_runs: ")
for each in input_runs:
    print(each, end = ' ')
print("\n")
for i in range(len(input_runs)-1, -1, -1):
    # print(i, input_runs[i])
    reversed_list.append(input_runs[i])
print("reversed_list: ")
for each in reversed_list:
    print(each, end = ' ')