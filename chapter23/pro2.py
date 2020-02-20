row, col = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] != '*':
            matrix[i][j] = int(0)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 0:
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if x < 0 or y < 0 or x >= row or y >= col:
                        continue
                    else:
                        if matrix[x][y] == '*':
                            matrix[i][j] += 1
        print(matrix[i][j], end=' ')
    print()