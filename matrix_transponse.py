# -matrix_transponse-1/9/25-------------------------------------------
matrix = [[1,2,3],               # matrix find diags
          [4,5,6],
          [7,8,9]]    
col1 = [row[0] for row in matrix]
col2 = [row[1] for row in matrix]
col3 = [row[2] for row in matrix]
diag = [matrix[i][i] for i in range(len(matrix))]
subdiag = [matrix[i][len(matrix)-1-i] for i in range(len(matrix))]
print(col1)                      # matrix transpose
print(col2)
print(col3)
print(diag)
print(subdiag)
