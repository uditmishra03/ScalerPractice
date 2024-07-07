# A = [53, 39, 88]
A = [38, 44, 84, 12] 

result= 0

for bit in range(31, -1, -1):
    temp_result = result | (1 << bit)
    print(f"Temp result: {temp_result}")
    count =0
    for num in A:
        if num & temp_result == temp_result:
            count +=1
            print(f"count : {count}")
        if count >= 2:
            break
    if count >=2:
        result = temp_result

print(result)