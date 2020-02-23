"""Check_balanced_parentheses.py """

from data_classes import Stack

def balanced_parentheses(parentheses: str) -> bool:
    """ Use a stack to check if a string of parentheses is balanced. """
    stack = Stack()

    for parenthesis in parentheses:
        # Add or .push() when ( is found
        if parenthesis == "(":
            stack.push(parenthesis)

        # Remove or .pop() when ) is found
        elif parenthesis == ")":
            if stack.empty:
                return False
            stack.pop()
    return stack.empty


if __name__ == "__main__":
    examples = ["((()))", "((())", "(()))", "(2)", "((a)", "(1(a)%)", "1(2(abc)2)1"]
    print(f"\nTesting Balanced parentheses with Stack:\n", 40*"=")

    for example in examples:
        print(example + ": " + str(balanced_parentheses(example)))