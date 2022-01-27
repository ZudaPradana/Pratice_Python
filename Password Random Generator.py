# Challange password random generator
import random
letter = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
number = '1 2 3 4 5 6 7 8 9 10'.split()
symbol = '! # $ % 7 ( ) * +'.split()
print('Welcome to the password generator')
input_len_letter = int(input('How many letters would you like in your password: \n'))
input_num = int(input('How many numbers would you like in your password: \n'))
input_symb = int(input('How many symbol would you like in your password: \n'))
for i in range (0,input_len_letter+1):
    random_letter = random.choices(letter,k=i)
for j in range (0,input_num+1):
    random_number = random.choices(number,k=j)
for k in range (0,input_symb+1):
    random_symbol = random.choices(symbol,k=k)
total = random_letter + random_number + random_symbol
final_random = random.choices(total,k=len(total))
convert_to_string = ''.join(final_random) #''.join() = convert list to string
print(''.join([char.lower() if random.randint(0,1) else char.upper() for char in convert_to_string]))
# or
random.shuffle(total) #random.shuffle() = mengacak nilai pada list, tidak bisa dijadikan variabel dan hanya berfungsi pada type list
convert_to_string = ''.join(total)
print(''.join([char.lower() if random.randint(0,1) else char.upper() for char in convert_to_string]))
