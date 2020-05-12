""" download_web_page.py """
import requests
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
print(type(res))
print(res.status_code == requests.codes.ok)  # check if http status is 200
print(len(res.text))
print(res.text[:250])