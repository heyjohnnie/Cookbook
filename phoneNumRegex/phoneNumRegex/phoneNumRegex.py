#All the regex functions in Python are in the re module.
import re

def phoneNumber(text):
    #Passing a string value representing your regular expression to re.compile() returns a Regex pattern object.
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    #A Regex object’s search() method searches the string it is passed for any matches to the regex.
    #While search() will return a Match object of the first matched text in the searched string,
    #the findall() method will return the strings of every match in the searched string.
    mo = phoneNumRegex.findall(text)
    return mo

message =  "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office"
#findall() will not return a Match object but a list of strings.
number = phoneNumber(message)
for i in number:
    print("Phone number found: " + i)
print("Done")