# BUBBLE SORT

# Some Random Numbers
l = [1, 2, 3, 4, 23, 23, 323, 23, 24, 3, 45, 658, 74, 34, 5, 4, 3, 65547, 5, 5, 3, 25, 47, 4, 523, 54365, 74, 5, 246,
     54, 75, 326, 45, 756]

for i in range(len(l)-1):
    for j in range(len(l)-1):
        if l[j + 1] < l[j]:
            temp = l[j]
            l[j] = l[j + 1]
            l[j + 1] = temp
print(l)
