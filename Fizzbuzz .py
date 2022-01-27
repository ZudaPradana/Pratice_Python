# Fizzbuzz using while loop
max_number = int(input('Maksimal angka: \n'))
x = 0
while x < max_number:
    x += 1
    if x % 3 == 0 and x % 5 == 0:
        print(f'{x} is FizzBuzz')
    elif x % 3 == 0:
        print(f'{x} is Fizz')
    elif x % 5 == 0:
        print(f'{x} is Buzz')
    else:
        print(x)
