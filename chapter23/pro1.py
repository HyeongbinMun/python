row, col = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))
for i in range(len(matrix)):  # 세로 크기
    for j in range(len(matrix[i])):  # 가로 크기
        if matrix[i][j] == '*':
            continue
        else:
            matrix[i][j] = int(0)
i = j = 0
for i in range(len(matrix)):  # 세로 크기
    for j in range(len(matrix[i])):  # 가로 크기
        if matrix[i][j] == '*':
            if i == 0 and j == 0:
                if type(matrix[i][j + 1]) == int:
                    matrix[i][j + 1] += 1
                if type(matrix[i + 1][j]) == int:
                    matrix[i + 1][j] += 1
                if type(matrix[i + 1][j + 1]) == int:
                    matrix[i + 1][j + 1] += 1
            elif i == 0 and j == len(matrix[i])-1:
                if type(matrix[i][j - 1]) == int:
                    matrix[i][j - 1] += 1
                if type(matrix[i + 1][j - 1]) == int:
                    matrix[i + 1][j - 1] += 1
                if type(matrix[i + 1][j]) == int:
                    matrix[i + 1][j] += 1
            elif i == len(matrix)-1 and j == 0:
                if type(matrix[i - 1][j]) == int:
                    matrix[i - 1][j] += 1
                if type(matrix[i - 1][j + 1]) == int:
                    matrix[i - 1][j + 1] += 1
                if type(matrix[i][j + 1]) == int:
                    matrix[i][j + 1] += 1
            elif i == len(matrix)-1 and j == len(matrix[i])-1:
                if type(matrix[i - 1][j - 1]) == int:
                    matrix[i - 1][j - 1] += 1
                if type(matrix[i - 1][j]) == int:
                    matrix[i - 1][j] += 1
                if type(matrix[i][j - 1]) == int:
                    matrix[i][j - 1] += 1
            elif i == 0:
                if type(matrix[i][j - 1]) == int:
                    matrix[i][j - 1] += 1
                if type(matrix[i][j + 1]) == int:
                    matrix[i][j + 1] += 1
                if type(matrix[i + 1][j - 1]) == int:
                    matrix[i + 1][j - 1] += 1
                if type(matrix[i + 1][j]) == int:
                    matrix[i + 1][j] += 1
                if type(matrix[i + 1][j + 1]) == int:
                    matrix[i + 1][j + 1] += 1
            elif j == 0:
                if type(matrix[i - 1][j]) == int:
                    matrix[i - 1][j] += 1
                if type(matrix[i - 1][j + 1]) == int:
                    matrix[i - 1][j + 1] += 1
                if type(matrix[i][j + 1]) == int:
                    matrix[i][j + 1] += 1
                if type(matrix[i + 1][j]) == int:
                    matrix[i + 1][j] += 1
                if type(matrix[i + 1][j + 1]) == int:
                    matrix[i + 1][j + 1] += 1
            elif j == len(matrix[i])-1:
                if type(matrix[i - 1][j - 1]) == int:
                    matrix[i - 1][j - 1] += 1
                if type(matrix[i - 1][j]) == int:
                    matrix[i - 1][j] += 1
                if type(matrix[i][j - 1]) == int:
                    matrix[i][j - 1] += 1
                if type(matrix[i + 1][j - 1]) == int:
                    matrix[i + 1][j - 1] += 1
                if type(matrix[i + 1][j]) == int:
                    matrix[i + 1][j] += 1
            elif i == len(matrix)-1:
                if type(matrix[i - 1][j - 1]) == int:
                    matrix[i - 1][j - 1] += 1
                if type(matrix[i - 1][j]) == int:
                    matrix[i - 1][j] += 1
                if type(matrix[i - 1][j + 1]) == int:
                    matrix[i - 1][j + 1] += 1
                if type(matrix[i][j - 1]) == int:
                    matrix[i][j - 1] += 1
                if type(matrix[i][j + 1]) == int:
                    matrix[i][j + 1] += 1
            else:
                if type(matrix[i - 1][j - 1]) == int:
                    matrix[i - 1][j - 1] += 1
                if type(matrix[i - 1][j]) == int:
                    matrix[i - 1][j] += 1
                if type(matrix[i - 1][j + 1]) == int:
                    matrix[i - 1][j + 1] += 1
                if type(matrix[i][j - 1]) == int:
                    matrix[i][j - 1] += 1
                if type(matrix[i][j + 1]) == int:
                    matrix[i][j + 1] += 1
                if type(matrix[i + 1][j - 1]) == int:
                    matrix[i + 1][j - 1] += 1
                if type(matrix[i + 1][j]) == int:
                    matrix[i + 1][j] += 1
                if type(matrix[i + 1][j + 1]) == int:
                    matrix[i + 1][j + 1] += 1
i = j = 0
for i in range(len(matrix)):  # 세로 크기
    for j in range(len(matrix[i])):  # 가로 크기
        print(matrix[i][j], end=' ')
    print()