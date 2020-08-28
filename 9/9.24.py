import math
def distance (a, b, c, d):
    return math.sqrt((a-c)**2 + (b-d)**2)
file = open("test01.in")
matrix = []
for row in file:
    matrix.append(row.rstrip().upper().split())
m = len(matrix)
new_matrix = []
for i in range(m):
    new_matrix.append([])
    for j in range(m):
        if matrix[i][j] != "-":
            new_matrix[i].append(matrix[i][j])
        else:
            min_distance = distance(0, 0, len(matrix),len(matrix[i]))
            char = "Z"
            for k in range(m):
                for l in range(m):
                    if matrix[k][l] != "-":
                        curr_distance = distance(i,j,k,l)
                        if curr_distance < min_distance or curr_distance == min_distance and matrix[k][l] < char:
                            char = matrix[k][l]
                            min_distance = curr_distance

            new_matrix.append(char)

for line in new_matrix:
    for element in line:
        print(element,end =" " )
    print()
