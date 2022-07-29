def inst():                                                               # function defining
    print("Instructions:")
    print("1.The game is for two players.\n2.Player-1 has to choose a number from 0 to 20.")
    print("3.Player-2 has to find the number by guessing.")
    print("4.There are 4 chances for Player-2.\n5.Player-2 win the game only if he find the number using his chances.\n")
def fn_1(z):                                                              # function_1 defining
        y = 20 - z
        return y                                                          # returning the value of y 
def fn_2(y,b):                                                            # function_2 defining
    for i in range(0,4):                                                  # for loop for repetition 
        if y == b:                                                        # if condition for checking equalness
            print("Congratulations You Won the game")
            break                                                         # break statement for exiting loop
        else:            
            if 3-i == 0:                                                  # if statement for chancess
                print("You lost the game \nPlay again.")
            elif y > b:                                                   # elif statement for clues
                print("Your number is less than the original number")
                print("You have",3-i,"chances\n")
                b = int(input("Enter your guess:"))
            else:                                                         # else statement for clues
                print("Your number is grater than the original number") 
                print("You have",3-i,"chances\n")
                b = int(input("Enter your guess:"))
            
    
print("\t\tGUESS THE HIDDEN\n\tStart Playing By Guessing !!!\n")          # printing tittle 
inst()                                                                    # function calling   
print("Let's Start...")
n_1 = input("Name of First Player:")                                      # input name of players
n_2 = input("Name of SecondPlayer:")
print("\nHi",n_1,end=',')                                                 # end statement for displaying in same line
print("It is your turn\n(You have to choose a number in range  0 and 20)")#instruction for player_1
a = int(input("Enter your number:"))                                      # accepting secret number from player_1
l_1=[1,2,3,4,5,6,7,8,9,10]                                                # list of numbers
l_2=[11,12,13,14,15,16,17,18,19,20]
if a in (l_1) or (l_2):                                                     # if condition for secret number 
    print("\n",n_2,"Now your turn")
    print("Guess the number hidden in ",a)
    b = int(input("Enter your guess:"))                                   # accepting guess value from player_2
    fn_2(fn_1(a),b)                                                       # function calling
else:                                                                     # else statement for secret number
    print("Sorry,you made some mistake! Try Again")
    
