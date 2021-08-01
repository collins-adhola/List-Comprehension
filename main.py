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




#Brad lists /Udemy
# A List is a collection which is ordered and changeable. Allows duplicate members.

#Create list
numbers = [1,2,3,4,5]
print(numbers)

# Using constructor
numbers = list((1,2,3,4,5))
fruits = ['Apples', 'Oragnges', 'Grapes', 'Pears']
print (numbers)
print (fruits[2])

#Get len
print(len(fruits))
#Append to list  / push in javascript
fruits.append('Mango')
print (fruits)

#Remove from list
fruits.remove('Grapes')
print (fruits)

# Insert into position
fruits.insert(2, 'Strawberies')

#Remove from specific position
fruits.pop(3)
print(fruits)

# Reverse
fruits.reverse()
print (fruits)

#Sort list
fruits.sort()
print (fruits)

#Reverse sort
fruits.sort(reverse=True)   #sorted alphabetically but the other way.


# add 2 lists

fruits01 = ['Apples', 'Oragnges', 'Grapes', 'Pears']
fruits02 = ['Maize', 'Cassava', 'Potato', 'Pears']

fruits01.extend(fruits02)
print(fruits01)