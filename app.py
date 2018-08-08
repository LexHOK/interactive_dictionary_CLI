import json
from difflib import get_close_matches

data = json.load(open("data.json"))

word = str.lower(input("Please, introduce the word you want to check: "))

def beauty_print(x):
	stringify = ""
	count = 1
	for i in x:
		stringify = stringify + str(count) + ". " + i + "\n"
		count = count + 1
	return stringify

def meaning(w):
	if w in data:
		return beauty_print(data[w])
	else:
		short_list = get_close_matches(w, data, n=5, cutoff=0.65)
		for i in short_list:
			option = str.lower(input("Did you ment '" + i + "'? For Yes type 'y', for No type 'n'"))
			if option == "y":
				return beauty_print(data[i])
		return "Sorry, we don't find that word in our dictionary."

print(meaning(word))