# LAMBDA
# lambda argument: expression
#############################
add = lambda x, y : x + y
print(f"add: {add(2, 3)} ") # Output: 5

# MAP
# map() expects a function object and an iterable and returns an iterator or map object.
# map(function_object, iterable1, iterable2,...)
# iterator which gets lazily evaluated using list()
# cannot access the elements of the map object with index, nor can we use len() to find the length
###################################################################################################
def multiply2(x):
  return x * 2
list0 = [1, 2, 3, 4]
print(f"multiply {list0} by 2: {list(map(multiply2, list0 ))}")  # Output [2, 4, 6, 8])

iteratable = range(0, 10)
function = lambda x: x**2

ans_gen = map(function, iteratable)
print(f"Output of map() is : {type(ans_gen)}")

# Use list() to convert generator to list.
print(f"squaring all numbers from 0-9: {list(ans_gen)}")

# Doing multiplication in one line
print(list(map(lambda x : x*2, [1, 2, 3, 4]))) # Output [2, 4, 6, 8]

# Iterating Over a Dictionary Using Map and Lambda
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
print(list(map(lambda x : x['name'], dict_a) ))             # Output: ['python', 'java']
print(list(map(lambda x : x['points']*10,  dict_a)))        # Output: [100, 80]
print(list(map(lambda x : x['name'] == "python", dict_a)))  # Output: [True, False]

# Multiple Iterables to the Map Function
# each i^th element of list_a and list_b will be passed as an argument to the lambda function.
list_a = [1, 2, 3]
list_b = [10, 20, 30]
print(list(map(lambda x, y: x + y, list_a, list_b)))    # Output: [11, 22, 33]

# FILTER
# filter(function_object, iterable)
# function_object returns a boolean value and is called for each element of the iterable.
# iterator which gets lazily evaluated using list()
# filter returns only those elements for which the function_object returns True.
# Unlike map, the filter function can only have one iterable as input.
##############################################################################################
a = [1, 2, 3, 4, 5, 6]
ans = filter(lambda x : x % 2 == 0, a) # Output: [2, 4, 6]
print(f'filter returns an object of type: {type(ans)}')

dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
ans2 = filter(lambda x : x['name'] == 'python', dict_a) # Output: [{'name': 'python', 'points': 10}]
print(f"Dictionary: {dict_a}")
print(f"Filtering the list of dictionary to find a dictionary with x['name'] == 'python' => {list(ans2)}")

list_a = [1, 2, 3, 4, 5]
filter_obj = filter(lambda x: x % 2 == 0, list_a) # filter object <filter at 0x4e45890>
even_num = list(filter_obj) # Converts the filer obj to a list
print(f"Even number of {list_a} are: {even_num}") # Output: [2, 4]