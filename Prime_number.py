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
