"""
music_recommendation.py
A simple music recommender system. Inspired from CS for scientist and engineer
"""
import sys
from typing import Any, Optional

PREF_FILE = "music.txt"


def load_users(filename: str) -> dict:
    """Reads a file of stored users's preferences
    Returns a dictionary containing a mapping of users names to a
    list preferred artists."""
    try:
        file = open(filename, "r")
    except IOError:
        print(f"\n*** Could not open {filename} ***\n")
        sys.exit()

    user_dict = {}
    # parse a single line => username: band1, band2, etc
    for line in file:
        try:
            [user_name, bands] = line.strip().split(":")
            band_list = bands.split(",")
            band_list.sort()
            user_dict[user_name] = band_list
        except ValueError:
            print(f"\n*** Error while reading lines in {filename} ***\n")
            sys.exit()
    file.close()
    return user_dict


def get_preferences(user_name: str, user_map: dict) -> list:
    """ Returns a list of the users' preferred artists. """
    new_pref = ""
    if user_name in user_map:
        prefs = user_map[user_name]
        print("\nI see that you have used the system before.")
        print("Your music preferences include:")
        for artist in prefs:
            print(artist)
        print("Please enter another artist or band that you like,")
        print("or just press Enter to see your recommendations: ")
        new_pref = input()
    else:
        prefs = []
        print("I see that you are a new user.")
        print("please enter the name of an artist or band that you like: ")
        new_pref = input("")

    while new_pref != "":
        prefs.append(new_pref.strip().title())
        print("\nPlease enter another artist or band that you like,")
        print("or just press Enter to see your recommendations: ")
        new_pref = input("")

    # Always keep the list in sorted order for ease of comparison
    prefs.sort()
    return prefs


def get_recommendations(curr_user: str, prefs: list, user_map: dict) -> list:
    """Gets recommendations for a user based on the users in
    user_map and the user's preferences in prefs."""
    best_user = find_best_user(curr_user, prefs, user_map)
    recommendations = drop(prefs, user_map[best_user])
    return recommendations


def find_best_user(curr_user: str, prefs, user_map: dict) -> Optional[Any]:
    """Find the user whose tastes are closests to the current user.
    Returns the best user's name or -1 if nothing is found."""
    users = user_map.keys()  # Creates a list of all the users
    best_user = None
    best_score = -1
    for user in users:
        score = num_matches(prefs, user_map[user])
        if score > best_score and curr_user != user:
            best_score = score
            best_user = user
    return best_user


def drop(list1: list, list2: list) -> list:
    """Returns a new list that contains only the elements in list2
    that were NOT in list1."""
    list3 = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            list3.append(list2[j])
            j += 1

    return list3


def num_matches(list1: list, list2: list) -> int:
    """ Returns the number of elements that are a match between 2 sorted lists. """
    matches, i, j = 0, 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1

    return matches


def save_user_preferences(
    user_name: str, prefs: list, user_map: dict, filename: str
) -> None:
    """ Writes all of the user preferences to the file."""
    user_map[user_name] = prefs  # Add the latest users to the dictionary
    try:
        file = open(filename, "w")
    except IOError:
        print(f"\n*** Could not open {filename} ***\n")
        sys.exit()

    for user in user_map:
        # Uses the join() to convert list to a string separated by ','
        to_save = str(user) + ":" + ",".join(user_map[user]) + "\n"
        file.write(to_save)

    file.close()


def main():
    """ Test Harness. """
    user_map = load_users(PREF_FILE)
    print("\nWelcome to the music recommendation ENGINE!")

    user_name = input("Please enter your name: ").lower()
    print("Welcome, ", user_name)

    prefs = get_preferences(user_name, user_map)
    recs = get_recommendations(user_name, prefs, user_map)

    # Print the user's recommendations
    print("\n")
    if len(recs) == 0:
        print("\nI'm sorry but I have no recommendations")
    else:
        print(user_name, "\nBased on the users I currently know about")
        print("I believe you might like: ")
        for artist in recs:
            print(artist)

    save_user_preferences(user_name, prefs, user_map, PREF_FILE)


if __name__ == "__main__":
    main()
