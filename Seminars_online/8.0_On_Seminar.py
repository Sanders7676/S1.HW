# По выводу в таблице в 6.2
header = " "*7
for col in range(1, num_columns+1):
  header +=f"{col:4d}"
print(header)
print(" "*7, "-"*num_columns*4)

