# # Multiples of Three - Final Safe Version

# n = int(input())
# arr = input().replace(',', ' ').split()


# arr = list(map(int, arr[:n]))

# result = []

# for num in arr:
#     if num % 3 == 0:
#         result.append(num)

# if len(result) == 0:
#     print(-1)
# else:
#     print(*result)





# Longest Consecutive Multiples of 3

n = int(input())
arr = list(map(int, input().split()))

i = 0
j = 0
current = 0
maximum = 0

while j < n:
    if arr[j] % 3 == 0:
        current += 1
        maximum = max(maximum, current)
    else:
        current = 0
    j += 1

print(maximum)