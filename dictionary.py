acronyms= {} #empty list


#adding some data to the empty list 
acronyms =["LOL"] : "LAUGH OUT LOUD"
acronyms = ["IDK"] : "I don't know"
acronyms = ["TBH"] : "TO BE HONEST"
print(acronyms) 


###to delete 
acronyms = {'LOL' : 'laugh out loud',
            'IDK' : "I don't know",
            'TBH' : "to be honest "}

del acronyms['LOL']


###FULL DICTIONARY

acronyms = {'LOL' : 'laugh out loud',
            'IDK' : "I don't know",
            'TBH' : "to be honest "}

sentence = 'IDK' + 'what happened' + 'TBH'
translation = acronyms.get('IDK') + 'what happened' + acronyms.get('TBH')

print('sentence:', sentence)
print('translation:', translation)

