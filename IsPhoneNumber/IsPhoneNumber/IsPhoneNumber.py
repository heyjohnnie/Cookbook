#The isPhoneNumber() function has code that does several checks to see whether the string in text is a valid phone number.
#If any of these checks fail, the function returns False.

def isPhoneNumber (text):
    #First the code checks that the string is exactly 12 characters.
    if len(text) != 12:
        return False
    #Then it checks that the area code (that is, the first three characters in text) consists of only numeric characters
    for i in range (0, 3):
        if not text[i].isdecimal():
            return False
    # The rest of the function checks that the string follows the pattern of a phone number:
    #The number must have the first hyphen after the area code.
    if text[3] != "-":
        return False
    for i in range (4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range (8, 12):
        if not text[i].isdecimal():
            return False

    #If the program execution manages to get past all the checks, it returns True
    return True

#print('415-555-4242 is a phone number:')
#print(isPhoneNumber('415-555-4242'))
#print('Moshi moshi is a phone number:')
#print(isPhoneNumber('Moshi moshi'))

message =  "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office"
#On each iteration of the for loop, a new chunk of 12 characters from message is assigned to the variable chunk.
for i in range (len(message)):
    chunk = message[i:i+12]
    #You pass chunk to isPhoneNumber() to see whether it matches the phone number pattern, and if so, you print the chunk.
    if isPhoneNumber(chunk):
        print("Phone number found: " + chunk)
print("Done")