# Inspired by analytics-vidhya medium article
# Bitor Freitas blog

from decouple import config

userID = config("userID", default="")
password = config("password", default="")

print(f"user: {userID} with PWD: {password}")
