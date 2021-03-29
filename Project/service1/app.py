import random 
#this code needs to run 8 times for my list 

odd_numbers= (1,3,5,7)
even_numbers= (2,4,6,8)

number1 = random.randint(1, 8)
number2 = random.randint(1, 8)
number3 = random.randint(1, 8)
number4 = random.randint(1, 8)
number5 = random.randint(1, 8)
number6 = random.randint(1, 8)
number7 = random.randint(1, 8)
number8 = random.randint(1, 8)
random_num_list=(f"{number1}{number2}{number3}{number4}{number5}{number6}{number7}{number8}")
# print(random_num_list)
print("-".join(random_num_list))

even_number_occurances=random_num_list.count("2")
print("this list has the number ", even_number_occurances)

for num in range(random_num_list):
    if num % 2 == 0:
        print("this is even numbers")


