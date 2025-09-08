#Multiplos

for i in range (1,10000):
    if i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0 and n%5==0:
        print("FizzBuzz")
    else:
        print(i)