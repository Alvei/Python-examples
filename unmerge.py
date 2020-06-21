def unmerge(*args):
    """ Split a list into two smaller lists with even-indexed elements
        in one and odd-indexed elements in the others"""
    left = []
    right = []
    for i in range(0, len(args), 2):
        left.append(args[i])        # even
        if i+1 < len(args):
            right.append(args[i+1]) # uneven
    return (left, right)


print(unmerge([12, 17, 5, 63, 101]))

def agg( fun, lst):
    return fun(lst)

def powsum(lst, p):
    sum = 0
    for e in lst:
        sum += e**p
    return sum

ans = agg(lambda x: powsum(x, 2) , [1, 3, 5, 7, 9])
print(ans)

li = ["hi", "welcome"]
def addToList():
    li.append("hello")

addToList()
print(li)

print(20/2.)

Dict = {'tophat': 2, "bowtie": 4, "monocle": 5}

value = "tophat1"
if value in Dict:
    print(Dict[value])
else:
    print("nothing")

msg = "I am super excited for this course!"
print((msg+" ")*5)