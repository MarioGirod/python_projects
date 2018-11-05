#Guess the Number
import random

# please use PEP 8 cosing standard eg snake case in madetory guess_token
# see https://www.python.org/dev/peps/pep-0008/
guessToken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1,20)

# only works with 3.6 or hier
print(f'Well {myName} I am thinking of a number between 1 and 20.')

for guessToken in range(6):
    print('Take a guess.') #Four spaces in front of "print"
    guess = input()
    # this will cras if the input is 'abc' for example you need to handle this
    guess = int(guess)

    if guess < number:
        print('Your guess is too low.') #Eight spaces in front of "print"

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessToken = str(guessToken +1)
    print ('Good job, ' + myName + '! You guessed my number in '+ guessToken + ' guesses!')

if guess != number:
    # only works with 3.6 or hier
    print (f'Nope. The number I was thinking of was {number}.')
       
        
# please use Python main function

def main():
    # your code goes in here


if __name__ == "__main__":
    main()
