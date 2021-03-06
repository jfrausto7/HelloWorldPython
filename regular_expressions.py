# imports
import re

# sentence to search
sentence = "Mike's number is 801-242-5334"
# create regex variable
phoneRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

# create regex mathcing object to search using regex variable
mo = phoneRegex.search(sentence)

# use group function to print it out
stuff = mo.group()

# print it out
print(stuff)

# greedy search below
nameRegex = re.compile(r"First Name: (.*)")
moo = nameRegex.search("First Name: Jacob")
moo.group(1)

# using the sub method
agentRegex = re.compile(r'Agent \w+')
agentRegex.sub('Censored', 'Today I finally sat down with Agent Smithers and had a little chat.')

