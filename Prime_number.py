# Check number is prime or not
numb = int(input('input your number to check: '))
def prime(number):
    if number == 2 or number == 3:
        print('number prime')
    elif number % 2 == 0 or number % 3 == 0:
            print('number is not prime')
    else:
        print('number prime')
prime(numb)

#or


# Check prime number using looping
numb = int(input('input your number to check: '))
for i in range (numb):
    i+=1
    if i == 2 or i == 3:
        print(f'{i} is prime')
    elif i % 2 == 0 or i % 3 == 0:
        print(f'{i} is not prime')
    else:
        print(f'{i} is prime')
