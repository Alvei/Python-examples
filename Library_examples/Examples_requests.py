""" Examples using the requests libray. 
    Will use hhtpbin.org to help with the testing. """
import requests

payload = {"page": 2, "count": 25}  # Defines parameters for a query
response = requests.get("https://httpbin.org/get", params=payload)

# Returns json with ["args", "headers", "origin", "url"]
print(f"text: {response.text}")
print(f"url: {response.url}")

payload = {"user": "bob", "pwd": "john"}  # Defines parameters for posting
response = requests.post("https://httpbin.org/post", data=payload)

# See that the payload was put in form
print(f"text: {response.text}")

# Convert json to dictionary
r_dict = response.json()
print(f"dict: {r_dict}")
print(f"form: {r_dict['form']}")  # Access the "form" keyword


# Does basic authentication expecting user=corey and pwd = testing
credentials = ("corey", "testing")
response = requests.get(
    "https://httpbin.org/basic-auth/corey/testing", auth=credentials
)
print(f"auth1: {response} {response.text}")  # Print the http code 1st then the result
credentials = ("corey", "wrongpwd")
response = requests.get(
    "https://httpbin.org/basic-auth/corey/testing", auth=credentials
)
print(f"auth2: {response} {response.text}")


# Testing delay
response = requests.get("https://httpbin.org/delay/6", timeout=3)
print(f"delay: {response}")
