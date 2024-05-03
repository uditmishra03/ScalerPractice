'''Given a list of all runs by Virat Kohli, create a new list of runs made in last 5 matches in opposite order with last match being first element in output .

input_runs = [62, 85, 74, 10, 12, 101, 122, 99, 81, 55]

Expected_Output =[55, 81, 99, 122, 101]'''

input_runs = [62, 85, 74, 10, 12, 101, 122, 99, 81, 55]
# size = len(input_runs)
# # print(size)
LastMatches = int(input("Enter the last no of matches you want to process: "))
backCount = 0-LastMatches-1
# # print(backCount)
# lastMatches_list = []
# for i in range(-1, backCount, -1):
#     # print(i, input_runs[i])
#     lastMatches_list.append(input_runs[i])
#
# print("lastMatches_list: ")
# for each in lastMatches_list:
#     print(each, end = ' ')
print(input_runs[:backCount:-1])