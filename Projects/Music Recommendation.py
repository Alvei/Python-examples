"""
A simple music recommender system
Inspired from CS for scientist and engineer

Python 3.5"""

PREF_FILE = "music.txt"


def load_users(fileName):
    """  Reads a file of stored users's preferences
         Returns a dictionary containing a mapping of users names to a
         list preferred artists.
         Signature: (str) -> """
    file = open(fileName, 'r')
    user_dict = {}
    for line in file:
        # read and parse a single line
        [user_name, bands] = line.strip().split(":")
        band_list = bands.split(",")
        band_list.sort()
        user_dict[user_name] = band_list
    file.close()
    return user_dict


def get_preferences(user_name, user_map):
    """Returns a list of the users' preferred artists.
    """
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

    while new_pref != '':
        prefs.append(new_pref.strip().title())
        print("\nPlease enter another artist or band that you like,")
        print("or just press Enter to see your recommendations: ")
        new_pref = input("")

    # Always kee the list in sorted order for ease of comparison
    prefs.sort()
    return prefs


def get_recommendations(curr_user, prefs, user_map):
    """Gets recommendations for a user (currUser) based on the users in
       user_map (a dictionary) and the user's preferences in prefs (a list)
       Returns a list of recommended artists."""
    best_user = find_best_user(curr_user, prefs, user_map)
    recommendations = drop(prefs, user_map[best_user])
    return recommendations


def find_best_user(curr_user, prefs, user_map):
    """Find the user whose tastes are closests to the current user.
       Returns the best user's name (a string) """
    users = user_map.keys()  # Creates a list of all the users
    best_user = None
    best_score = -1
    for user in users:
        score = num_matches(prefs, user_map[user])
        if score > best_score and curr_user != user:
            best_score = score
            best_user = user
    return best_user


def drop(list1, list2):
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


def num_matches(list1, list2):
    """Returns the number of elements that are a match between 2 sorted lists"""
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


def saveUserPreferences(user_name, prefs, user_map, fileName):
    """Writes all of the user preferences to the file."""
    user_map[user_name] = prefs  # Add the latest users to the dictionary

    file = open(fileName, "w")

    for user in user_map:
        # Uses the join() method to return a string that concatenate
        # the string in the iterable user_map[user]
        toSave = str(user) + ":" + ",".join(user_map[user]) + "\n"
        file.write(toSave)

    file.close()


def main():

    user_map = load_users(PREF_FILE)
    print("\nWelcome to the music recommendation ENGINGE!")

    user_name = input("Please enter your name: ")
    print("Welcome, ", user_name)

    prefs = get_preferences(user_name, user_map)
    recs = get_recommendations(user_name, prefs, user_map)

    # Print the user's recommendations
    print("\n")
    if len(recs) == 0:
        print("I'm sorry but I have no recommendations")
    else:
        print(user_name, "Based on the users I currently know about")
        print("I believe you might like: ")
        for artist in recs:
            print(artist)

    saveUserPreferences(user_name, prefs, user_map, PREF_FILE)


if __name__ == "__main__":
    main()
