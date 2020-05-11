""" Password Locker.
    An insecured password locker program. Works from the command line.
    Inspired from Automate the Boring Stuff with Python - Al Sweigart. Chapter 6. Page 137.
    Signature: (string, string) -> None
"""
import sys, pprint, random

passwd = {'Bob': 'yikes!'}


if len(sys.argv) < 2:
    print("Usage: Python pw.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]       # First command line arg is the account name.

# Very insecure. Only doing to use setdefault. It uses a random integer generator.
print("For account ", account), "the pwd is ", passwd.setdefault(account, random.randint(1000,10000))

print(passwd)