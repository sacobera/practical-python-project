acronyms = ["lol", "brb", "idk"]

acronyms.append("lol") #.append adds items to the list in the end
acronyms.append("brb")

print (acronyms)


###
acronyms.remove('lol') or del acronyms[0] #removes of deletes within the list 


###
word = "bfn"

if word in acronyms:
    print (word + "is in the list")
else:
    print (word + 'is NOT in the list')

###
for acronym in acronyms:
    print(acronyms)