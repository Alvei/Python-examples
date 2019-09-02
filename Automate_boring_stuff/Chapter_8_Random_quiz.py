""" Chapter_8_Random_quiz.py
    Generalized quiz creation function.
    Saves the answer to quiz.txt and the answers to quiz_answers.txt
    Inspired from Automate the Boring Stuff with Python - Al Sweigart. Chapter 8. Page 186.
"""

import random
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)

NUM_CHOICE = 4   # Cannot exceed 5 because of the ABCDE string index


def read_questions(quiz_questions):
    """ Reads the list of key,value pairs that will be the questions. The 1st line is different.
        It contains the name of the key, value pairs.
        Signature: (str) -> (list, dict)."""

    with open(quiz_questions, 'r') as answer_object:
            my_dict = {}
            count = 0
            for line in answer_object:              # Loop of each line
                (key, value) = line.split(',')      # Extract the key,value pair
                if count == 0:                      # 1st line is the name of the key,value pairs
                    title = [key, value.strip()]
                    count += 1
                else:
                    my_dict[key] = value.strip()

            return (title, my_dict)


def main():
    """ Core code """
    quiz_file = 'quiz.txt'
    quiz_questions = 'quiz_questions.txt'
    answer_file = "quiz_answers.txt"

    key_value, multiple_choice =  read_questions(quiz_questions)
    print("Reading the questions in quiz_questions.txt")
    print(key_value)

    no_question = len(multiple_choice)

    quiz_object = open(quiz_file, 'w')
    answer_object = open(answer_file, 'w')

    # Shuffle the keys
    keys = list(multiple_choice.keys())
    random.shuffle(keys)

    for question in range(no_question):
        key = keys[question]
        correct_answer = multiple_choice[key]

        # Get all the values and remove the value associated with the correct value, then shuffle
        wrong_answers = list(multiple_choice.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        random.shuffle(wrong_answers)

        # Create the list of all potential answers for that question and shuffle them
        # Only keep NUM_CHOICE-1 wrong answers
        answer_options = wrong_answers[:NUM_CHOICE-1] + [correct_answer]
        random.shuffle(answer_options)

        logging.debug(correct_answer)
        logging.debug(wrong_answers)
        logging.debug(answer_options)

        # Write the Quiz
        #print("\n%s. What is the corresponding %s to %s" % (question+1, key_value[1], key))
        quiz_object.write("\n%s. What is the corresponding %s to %s\n" % (question+1, key_value[1], key))

        for index in range(NUM_CHOICE):
            #print("\t %s) %s" % ("ABCDE"[index], answer_options[index]))
            quiz_object.write("\t %s) %s\n" % ("ABCDE"[index], answer_options[index]))

        # Write the answer
        this_answer = answer_options.index(correct_answer)
        logging.debug(this_answer)
        answer_object.write("%s. %s\n" % (question+1, "ABCDE"[this_answer]))
        #print("%s. %s \n" % (question+1, "ABCDE"[this_answer]))

    answer_object.close()
    quiz_object.close()
    print("Finished writing the quiz in quiz.txt and the answer in quiz_answers.txt")

if __name__ == "__main__":
    main()