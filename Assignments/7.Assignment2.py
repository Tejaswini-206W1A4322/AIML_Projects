#2 question
n = int(input("Enter number of values: "))

data = []
print("Enter values (type 'None' for missing value):")

for i in range(n):
    value = input()
    if value == "None":
        data.append(None)
    else:
        data.append(int(value))

missing_count = 0

for item in data:
    if item is None:
        missing_count = missing_count + 1


total_values = len(data)
percentage = (missing_count / total_values) * 100

print("Missing Value Percentage:", round(percentage, 2))

#1 QUESTION

n1 = int(input("Enter number of transactions: "))

transactions = []
print("Enter transaction amounts:")
for i in range(n1):
    value = int(input())
    transactions.append(value)


freq = {}

for amount in transactions:
    if amount in freq:
        freq[amount] = freq[amount] + 1
    else:
        freq[amount] = 1


freq_list = []
for key in freq:
    freq_list.append((key, freq[key]))


for i in range(len(freq_list)):
    for j in range(i + 1, len(freq_list)):
        if freq_list[i][1] < freq_list[j][1] or\
           (freq_list[i][1] == freq_list[j][1] and freq_list[i][0] > freq_list[j][0]):
            freq_list[i], freq_list[j] = freq_list[j], freq_list[i]


result = []
for i in range(2):
    result.append(freq_list[i][0])

print("Top 2 most frequent transaction amounts:", result)
