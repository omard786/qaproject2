import random 

letter_list = ['A','E','I','U','B','F','J','V']
vowels = 'AEIU'
consonant = 'BFJV'
#choices let you pick the letters from the lise, k=amount of objects from the list 
letter= random.choices(letter_list, k=4)

print('these are your letters :')
dash_list= print('-'.join(letter))

#sort it so the letters dont reproduce 


#list comphrension, using one list with another 
vowel_count = [i for i in letter if i in vowels]
print ('you have this many vowels : ', len(vowel_count))
