#FizzBuzz game
for i in range(1,101):
    #if number is divisible by both 3 & 5
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    #if number is divisible by 3 only
    elif i%3==0:
        print("Fizz")
    #if number is divisible by 5 only
    elif i%5==0:
        print("Buzz")
    #if number is not divisible by 5 or 3
    else:
        print(i)
