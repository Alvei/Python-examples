# https://towardsdatascience.com/10-algorithms-to-solve-before-your-python-coding-interview-feb74fb9bc27
import collections


def solution(num: int) -> int:
    """ Reverse integers:
        Given an integer, return the integer with reversed digits.
        Note: The integer could be either positive or negative.
    """
    string = str(num)

    if string[0] == "-":
        return int("-" + string[:0:-1])
    else:
        return int(string[::-1])


def solution2(sentence: str) -> float:
    """ For a given sentence, return the average word length.
        Note: Remember to remove punctuation first.
    """
    # Loop over all special characters to replace them with nothing
    for p in "!?',;.":
        sentence = sentence.replace(p, "")
    words = sentence.split()

    # sum the length of all the words and divide by no. of words
    return round(sum(len(word) for word in words) / len(words), 2)


def solution_3a(num1: int, num2: int) -> int:
    """ Add Strings - Approach 1:
        Given two non-negative integers num1 and num2 represented as string,
        return the sum of num1 and num2. You must not
        use any built-in BigInteger library or convert the inputs to integer directly.
        Both num1 and num2 contains only digits 0-9 and do not contain any leading zero.
    """
    return str(eval(num1) + eval(num2))


def solution_3b(num1: int, num2: int) -> str:
    """ Add Strings - Approach 2:
        Given a string of length one, the ord() function returns an integer
        representing the Unicode code point of the character when the argument is a
        unicode object, or the value of the byte when the argument is an 8-bit string.
    """
    n1, n2 = 0, 0
    m1, m2 = 10 ** (len(num1) - 1), 10 ** (len(num2) - 1)

    for i in num1:
        n1 += (ord(i) - ord("0")) * m1
        m1 = m1 // 10

    for i in num2:
        n2 += (ord(i) - ord("0")) * m2
        m2 = m2 // 10

    return str(n1 + n2)


def solution_4a(s: str) -> int:
    """ First Unique Character - Approach 1:
        Given a string, find the first non-repeating character in it and return its index.
        If it doesn't exist, return -1. # Note: all the input strings are already lowercase.
    """
    frequency = {}
    # Create the dictionary of characters
    for i in s:
        if i not in frequency:
            frequency[i] = 1
        else:
            frequency[i] += 1

    # Go through the word looking for the 1st character that was only present once
    for i in range(len(s)):
        if frequency[s[i]] == 1:
            return i
    return -1


def solution_4b(word: str) -> int:
    """ First Unique Character - Approach 2:
    """

    # build hash map : character and how often it appears
    # <-- gives back a dictionary with words occurrence count
    # Counter({'l': 1, 'e': 3, 't': 1, 'c': 1, 'o': 1, 'd': 1})
    count = collections.Counter(word)

    # find the index
    for idx, ch in enumerate(word):
        if count[ch] == 1:
            return idx
    return -1


def solution5(word: str) -> bool:
    """ Valid palindrome:
        Given a non-empty string s, judge whether you can make it a palindrome.
        The string will only contain lowercase characters a-z.
    """
    for i in range(len(word)):
        t = word[:i] + word[i + 1 :]
        if t == t[::-1]:
            return True

    return word == word[::-1]


#### Run each questions ####
# 1. Reverse integers
print(f"Inverse of {-231} is {solution(-231)}")
print(f"Inverse of {345} is {solution(345)}")

# 2. Average word length F
sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"
print(f"Average: {solution2(sentence1)}")
print(f"Average: {solution2(sentence2)}")

# 3. Add Strings
num1 = "364"
num2 = "1836"
print(f"{num1} + {num2} = {solution_3a(num1, num2)}")
print(f"{num1} + {num2} = {solution_3b(num1, num2)}")

# 4. First Unique Character
words = ["alphabet", "barbados", "crunch"]
for word in words:
    print(f"{word}: {solution_4a(word)}")

for word in words:
    print(f"{word}: {solution_4b(word)}")

# 5. Valid palindrome
s = "radkar"
print(f"Is {s} a palindrome? {solution5(s)}")
