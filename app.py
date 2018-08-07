import json
from difflib import SequenceMatcher

data = json.load(open("data.json"))

word = str.lower(input("Please, introduce the word you want to check: "))

def ment(i):
	hello = str.lower(input("Did you ment '" + i + "'? For Yes type 'y', for No type 'n'"))
	if hello == "y":
		return data[i]
	else:
				return "Sorry, we don't find that word in our dictionary."

def meaning(w):
	if w in data:
		return data[w]
	else:
		for i in data:
			if SequenceMatcher(None, w, i).ratio() > 0.85:
				return ment(i)
		return "Sorry, we don't find that word in our dictionary."

print(meaning(word))