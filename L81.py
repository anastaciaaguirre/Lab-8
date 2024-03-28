#Abigail Lopez & Anastacia Aguirre

#Part A: Joining Strings
lines= ["Haiku frogs in snow",
        "A limmerick cam from nantucket",
        "Tetra,etric drum-beats thrumming, Hiwathianic rythm."]
def breakify(str_list):
    print("<br>".join(str_list))

breakify(lines)

#Modify Strings
string= "hello world!"
output= []  #Creates an empty list
index=0
while index < len(string):
    output.append(string[index])  #string[index] uses the current index to select a character from the string  #output.append() takes that character and adds it to the list
    index = index + 1  #Moves onto the next index number

print(output)


