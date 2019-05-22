heights = [[]]*11

# for i in range(5):
#     heights[i].append(1)
with open('dataset_3380_5.txt') as file:
    s = file.readlines()
    for i in range(len(s)):
        data = [j.strip() for j in s[i].split('\t')]
    heights[int(data[0])].append(int(data[2]))
print(data)
print(heights)