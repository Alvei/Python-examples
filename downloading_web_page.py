""" Simple example to download a web page """
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
print(type(res))
print(requests.codes.ok)  # answer should be 200
print(len(res.text))
print(res.text[:250])