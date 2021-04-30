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