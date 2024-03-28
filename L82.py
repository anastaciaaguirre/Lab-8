#Abigail Lopez & Anastacia Aguirre

#Find and Remove
string= "SPAM!HelloSPAM! worldSPAM!!"
output=[]
index= 0
while index < len(string):
    if string[index:index+5] == "SPAM!":  #checks if the substring at the current starting index position is SPAM!
        index+=5   #Advances index to skip over SPAM! substrings
    else:
        output.append(string[index])  #Adds  non-spam characters to the list
        index += 1
print(" ".join(output))  #Puts the new spame-free sting together


def remove_string(string, target):
    output= []
    index=0
    while index < len(string):
        if string[index: index+len(target)] == target:
            index= index+len(target)
        else:
            output.append(string[index])
            index += 1
    print("".join(output))

words="SPAM!HelloSPAM! worldSPAM!!"
remove_string(words, "SPAM!")
