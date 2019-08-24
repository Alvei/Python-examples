""" Convert a list of multiple integers into a single integer
for Python 3.6
"""

# creating a list of integer
lst = [12, 15, 17] 
  
def convert1(lst): 
    """ Iterate over each element and accumulate them in a string
        Signature: (list(int)) -> int. """

    # iterating each element. print statement changed end from EOL to "" to avoid line return
    res = ''
    for index in lst: 
        # print(index, end="") 
        res = res + str(index)
    return int(res)

def convert2(lst): 
    """ First convert the list of integer into a list of strings 
        (join() works with strings only). Then, join them using join(). 
        It takes a time complexity of O(n).
        Signature: (list(int)) -> int. """

    # Converting integer list to string list 
    string = [str(i) for i in lst] 
      
    # Join list items using join() 
    res = int("".join(string)) 
      
    return(res) 


def convert3(lst): 
    """ Converting integer list to string list and joining the list using join().
        Signature: (list(int) -> int). """
         
    res = int("".join(map(str, lst))) 
      
    return res 
  

print(convert1(lst))
print(convert2(lst))
print(convert3(lst))
