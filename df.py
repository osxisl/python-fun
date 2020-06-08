import pandas as pd
import json, csv
from collections import Counter

filename = 'data.txt'

l = list()
#create a dictionary from firstl line on data.txt file (don't forget to delete this line from file)
d = {"time": 1591163469.338345, "✊🏿": 6, "🤢": 1, "👏🏿": 11, "🤷🏽‍♀️": 1, "☕": 1, "‼": 4, "📢": 3, "🤯": 2, "😳": 1, "😕": 1, "📹": 1, "😒": 1, "😤": 1, "💔": 1, "💞": 1, "👏": 2, "❤": 5, "✊": 1, "✊🏻": 1, "✊🏼": 1, "✊🏽": 3, "✊🏾": 5, "😩": 1, "🤸🏿‍♂️": 1, "💌": 1, "🖤": 6, "😬": 1, "💪🏽": 1, "🤦🏽‍♂️": 1, "💝": 1, "🇳🇱": 1, "😜": 1}
#create a list of dictionaries
l.append(dict(d))
# print(l)

with open(filename) as f:
	for line in f:
		d = json.loads(line.rstrip())
		l.append(d.copy())
#create pandas Data Frame from list of dictionaries
df = pd.DataFrame(l)
print(df)
df.to_csv('out.csv')
