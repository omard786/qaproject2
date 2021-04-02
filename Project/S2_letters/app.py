import random 

letter_generator = ['A','E','I','U','B','F','J','V']

letter= random.choices(letter_generator, k=4)
gen=print(letter)

print('this is your letters',letter)