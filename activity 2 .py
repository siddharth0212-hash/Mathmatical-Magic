# to find factors of user input 

# Goes from 1 to nuumber and checks iff i divide. If yes, it is a factor
def print_factors(number):
    print("The factors of",number, "are:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)

# Taking input from the user
number = int(input("Enter your number to find it's factors: "))

# Calling our function
print_factors(number)