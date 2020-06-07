""" tut_requests.py
    requests module tutorial
    Inspired from: https://realpython.com/python-requests/
"""

import requests
import requests
from requests.exceptions import HTTPError

#print("\n")
# for url in ['https://api.github.com', 'https://api.github.com/invalid']:
#     try:
#         response = requests.get(url)

#         # If the response was successful, no Exception will be raised
#         response.raise_for_status()
#     except HTTPError as http_err:
#         print(f'HTTP error occurred: {http_err}')   # Python 3.6
#     except Exception as err:
#         print(f'Other error occurred: {err}')       # Python 3.6
#     else:
#         print('Success!')

print("\n")
response = requests.get('https://api.github.com')

# .content gives you access to the raw bytes of the response payload. you see b before the ""
#print(f"Content: {response.content}")

# To convert raw byte into a string .text. The response is serialized JSON
#print(f"Content: {response.text}")

# To convert the JSON to a dictionary use .json() method
# dict = response.json()
# print(f"Content as a dictionary:")
# for items in dict.items():
#     print(f"Key: {items[0]} \t\t Value: {items[1]}")

# The response headers can give you useful information, such as
# the content type of the response payload and a time limit on how long to cache the response.
# dict = response.headers
# print(f"Header:")
# for items in dict.items():
#     print(f"Key: {items[0]} \t\t Value: {items[1]}")

# PASSING PARAMETERS IN URL
#####################################################
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(f"r.url when combining two  {payload['key1']} and {payload['key2']}: {r.url}\n")
# Search GitHub's repositories using the AP for requests AND Python.
# Here is the API guide https://developer.github.com/v3/search/. the combo is 'q': 'term to search'
# pass params to .get() in the form of a dictionary, as you have just done, or as a list of tuples

response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)

response = requests.get(
    'https://api.github.com/search/repositories',
    params=[('q', 'requests+language:python')],
)

# Inspect some attributes of the `requests` repository
json_response = response.json()
print(f"json keys: {json_response.keys()}")
print(f"Total_count: {json_response['total_count']}")  # 'total_count' is the 1st key, not clear what it is counting

# Look over all the key/value pairs of the 'item' key
items = json_response['items']                  # items is a list
print(f"items: {len(items)} repos x {len(items[0])} keys")

# Look at the 3rd item/repo the lists of item
""" repository = json_response['items'][2]#
print(f"repository is {type(repository)} with {len(repository.keys())} key")    # It is a dictionary with 74 keys
print(f'Repository name: {repository["name"]}')                 # Python 3.6+
print(f'Repository description: {repository["description"]}')   # Python 3.6+


print("Looking at the 3rd repo key/value pairs")
for k, v in repository.items():
    print(f"{k}: \t\t {v}") """

# To customize headers, you pass a dictionary of HTTP headers to get() using
# the headers parameter. For example, you can change your previous search request
# to highlight matching search terms in the results by specifying the text-match media type in the Accept header:
# The Accept header tells the server what content types your application can handle. In this case, since you’re
# expecting the matching search terms to be highlighted, you’re using the header value application/vnd.github.v3.text-match+json,
# which is a proprietary GitHub Accept header where the content is a special JSON format.
""" response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)

# View the new `text-matches` array which provides information
# about your search term within the results
json_response = response.json()
repository = json_response['items'][0]
print(f'\n***Text matches: \n{repository["text_matches"]}') """