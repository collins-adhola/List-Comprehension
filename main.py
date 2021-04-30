'''
List comprehension
'''

squares = []
for x in range(10):
  squares.append(x**2)
print(squares)

print( [x ** 2 for x in range (10)] )
#Above codes the same. Bottom one is list comprehension
#it is basically writting expressions within a list.abs

'''
Conditional List comprehension
'''
comb = []
for x in [1,2,3]:
  for y in [3,1,4]:
    if x != y:
      comb.append((x,y))
print(comb)      
#1 will go all the way in 'y' and so are the rest.
#the inner loop runs the whole time of the outer loo(3 times)
print ([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
#Same in comprehension- far left is what you return

'''
Nested List comprehension
'''
# matrix = [
#   [1,2,3,4],
#   [5,6,7,8],
#   [9,10,11,12]
# ]
# print(len(matrix))

# res = [ [row[i] for row in matrix] for i in range(4)]
# print(res)
#========================================================

# matrix = [
#   [1,2,3,4],
#   [5,6,7,8],
#   [9,10,11,12]
# ]

# res = []
# for i in range(4):
#   res.append([row[i] for row in matrix])

# print(res)  

matrix = [
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12]
]
res =[]
for i in range(4):
  res_row = []
  for row in matrix:
    res_row.append(row[i])
  res.append(res_row)
print(res)     