row = 2947
column = 3029

size = row + column
elements = sum(range(1,row+column))  - (size - column)

code = 20151125
for n in range(elements):
    code = (code * 252533) % 33554393

print(code)