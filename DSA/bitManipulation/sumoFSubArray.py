def sum_of_bitwise_or(arr):
    n = len(arr)
    total_sum = 0
    max_bits= len(bin(max(arr))[2:])
    total_subarray = n * (n + 1) // 2

    for i in range(max_bits):  # Assuming 32-bit integers
        suffix_sum = 0
        cnt = 0  # Count of subarrays with ith bit not set

        for num in arr[::-1]:
            # print(num)
            bit = (num >> i) & 1

            if bit == 0:
                cnt += 1
            else:
                cnt = 0

            suffix_sum += cnt
        print(suffix_sum, total_subarray, total_sum )

        total_sum += (1 << i) * (total_subarray - suffix_sum)

    return total_sum

# Example usage
arr = [1, 2, 3, 4, 5]
print(sum_of_bitwise_or(arr))