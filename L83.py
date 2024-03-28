#Abigail Lopez & Anastacia Aguirre

#Find and Replace
def replace_substring(string, target, replacement):
    output= []
    index=0
    while index < len(string):
        if string[index: index+len(target)] == target:
            output.append(replacement)
            index= index+len(target)
        else:
            output.append(string[index])
            index += 1
    print("".join(output))


typos="This is a sring. Oh no this sring keeps spelling sring wrong. I should spell sring correctly"
replace_substring(typos, "sring", "string")
