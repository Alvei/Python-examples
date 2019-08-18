"""
miniQuizlet
It is a short program that reads a file called entry.txt to create a dictionary
The program then asks users a question based on the key

Created on Sun Dec 21 12:35:53 2014. """

import random
# import os


def get_dict(filename):
    '''Function to read a dictionary from a file.
       Signature: (string)-> Dict.'''
    temp_dict = {}

    # This is the file that will contain the dictionary data separated by commas
    fobj = open(filename, 'r')

    '''fobj contains a list of strings. Loop over this list having the pointer
       line points to each new string.'''
    for line in fobj:
        line_list = line.split(",")
        key, value = line_list[0].rstrip(), line_list[1].lstrip().rstrip()

        # create the dictionary
        temp_dict[key] = value

    fobj.close()
    return temp_dict


def main():
    """ Main code """
    # filename = "C:\Users\Hugo Sarrazin\Documents\Python Scripts\entry.txt"
    filename = "entry.txt"
    mydict = get_dict(filename)

    # create a list of all the keys, my_dict.keys() returns the keys
    my_keys = list(mydict.keys())

    # determine how many time you want to ask questions or how manyr rounds
    rounds = int(input("How many rounds do you want to play: "))

    score = 0
    for index in range(rounds):

        # get the starting word by applying random on the list of keys
        question = random.choice(my_keys)
        # get the answer from the dictionary
        answer = mydict[question]

        mychoice = str(input("\n What is the matching word for : "
                             + question + "\n-> "))

        # print(mychoice, len(answer))
        if mychoice == answer:
            score += 1
            print("Congratulation! that is the correct answer. Your score is: " + str(score))
        else:
            print("Sorry!" + answer + " is the correct answer")

    print("The final score was: " + str(score))


if __name__ == '__main__':
    main()
