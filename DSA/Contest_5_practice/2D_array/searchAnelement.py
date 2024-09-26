'''1. start from the top right corner, i=0, j = m-1
2. if arr[i][j] > k --> then move left/ j--
3. if arr[i][j] < k --> then move down / i++
4. If found, try to minimize the value of j (or as asked in question).
	4a. set min_i and min_j as n-1, m-1
	4b. once the element is found, set the value of min_i, min_j = min(min_i, i), min(min_j, j)
	4c. Run a loop in range of j till 0  and keep checking if the value matches the search element.
		4ca. If yes then set the min_j value as min(min_j, k)

5. Return the min_i and min_j values as final coordinates of search element.'''

# A = [[1, 2],
#      [3, 3]]
# B = 3

A = [[2,8,8,8],[2,8,8,8],[2,8,8,8]]
B = 8
# A = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# B = 5

n = len(A)
m = len(A[0])

i, j = 0, m-1
min_i, min_j = n-1, m-1
while i < n and j >= 0:
    if A[i][j] == B:
        print('Found it')
        min_i, min_j = min(min_i, i), min(min_j, j)
        for k in range(j, -1, -1):
            if A[i][k] == B:
                print('minimizing j', k)
                min_j = min(min_j, k)
        print('Final coords: ', min_i, min_j)
        
        break
    if A[i][j] > B:
        print('Move left')
        j-=1
    if A[i][j] < B:
        print('Move down')
        i+=1
    