""" save_web_page.py
    Important to remember to open file in binary mode to maintain
    the unicode encoding of the text. """
import requests
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
res.raise_for_status()
play_file = open('RomeoandJuliet.txt', 'wb')

# To avoid downloading too much memory, work in chunks
for chunk in res.iter_content(100000):
    play_file.write(chunk)

play_file.close()