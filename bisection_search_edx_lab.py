
highest = 100
lowest = 0
guess = (highest+lowest)//2
print("Please think of a number between 0 and 100!")

ans = ''
while ans != 'c':
    print("Is your secret number ", str(guess), "?")
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if ans == 'h':
        highest = guess
        guess = (highest+lowest) // 2
    elif ans == 'l':
        lowest = guess
        guess = (highest+lowest) // 2
    elif ans == 'c':
        print("Game over. Your secret number was: " + str(guess))
    else:
        print("eyyyyy")
        
    








# [0,1,2,3,4,5,6,7,8,9,10]
# user = 7
# range: highest = 10, lowest = 0
# mid_range: 5
# prompt: user number  ==5, >5, or <5 ?
# if user says c, exit loop => Game over
# elif user says h, new range 6-10 => reassign highest=10 and lowest=6 range
#   reassign guess to midpoint = (highest + lowest) // 2  ==> //will floor the division
# elif user says l, new range 0-4 => reassign highest=4 and lowest=0 range
#   reassign guess to midpoint = (highest + lowest) // 2  ==> //will floor the division
# repeat until input == 'c'
