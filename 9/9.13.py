fajl = open("test01.in","r")
matrix = []
for row in fajl :
    matrix.append(row.strip().split())
m = len(matrix)

oldMatrix = [row[:] for row in matrix]
for i in range(m):
    for j in range(m):
        if oldMatrix[i][j] == "0":
            matrix[i][j] = "-"
            if matrix[i-1][j] == "8":
                matrix[i-1][j] == "0"
            elif matrix[i][j+1] == "8":
                matrix[i][j+1] = "0"
            elif matrix[i+1][j] == "8":
                matrix[i+1][j] == "0"
            elif matrix[i][j-1] == "8":
                matrix[i][j-1] = "0"
for l in matrix:
    for e in l:
        print(e,end = " ")
    print()
