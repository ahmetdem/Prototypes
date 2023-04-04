hangman = [
'''
| - - - -
|
|
|
|
|
|
|''',

'''
| - - - -
|       |
|
|
|
|
|
|''',

'''
| - - - -
|       |
|       |
|
|
|
|
|''',

'''
| - - - -
|       |
|       |
|       O
|
|
|
|''',

'''
| - - - -
|       |
|       |
|       O
|       |
|
|
|''',

'''
| - - - -
|       |
|       |
|       O
|       |
|       |
|
|''',

'''
| - - - -
|       |
|       |
|       O
|      /|
|       |
|
|''',

'''
| - - - -
|       |
|       |
|       O
|      /|\\
|       |
|
|''',

'''
| - - - -
|       |
|       |
|       O
|      /|\\
|       |
|      /
|''',

'''
| - - - -
|       |
|       |
|       O
|      /|\\
|       |
|      / \\
|''',  
]

#values
words = ["arthur", "morgan", "gun", "kill", "repeater"]

max_right = 9
right = 0

entered_inputs = set()

turn = 0
point = 0
board = ["_" for i in range(len(words[turn]))]

print("Welcome! This is a normal hangman game where you can guess the full word or letters by letters.\n")

def visual(board):
    print(board, "\n")
    print(hangman[right])

def gameplay(turn, board):
    global entered_inputs
    global right
    
    def changeBoard():
        for i in indexes:
            board[i] = guess
        print()
        
    guess = input("\nEnter a character or the full guess: ")
    indexes = []
    
    if len(guess) == 1:
        if guess not in entered_inputs:
            if guess in words[turn]:  
                index = words[turn].find(guess)
                while index != -1:
                    indexes.append(index)
                    index = words[turn].find(guess, index + 1)
                changeBoard()
                print("------------------------------------------")
            else: 
                right += 1
                print("It is not in the list\n")
                print("------------------------------------------")
        else: 
            right += 1
            print("You entered the character before!")
            print("------------------------------------------")
            
        entered_inputs.add(guess)
    else:
        print("------------------------------------------")
        if guess != words[turn]:
            print("Enter a letter or the entire word!") 
            print("------------------------------------------")
            
    return guess


while True:

    visual(board)
    guess = gameplay(turn, board)

    #winning
    if "_" not in board or guess == words[turn]:
        turn += 1
        point += 1
        right = 0
        board = ["_" for i in range(len(words[turn]))]
        entered_inputs.clear()
        print(f"\nYou Won! \nYour total points are {point}\n")
        print("------------------------------------------")

    #losing
    if right == max_right:
        visual(board)
        right = 0
        point -= 1
        turn += 1 
        board = ["_" for i in range(len(words[turn]))]
        print(f"\nYou Lost! Your point is {point}\n")
        print("------------------------------------------")
        
    #entered inputs output
    print("Entered inputs are: ", end="")
    for i in entered_inputs:
        print(i, end=" ")
    print()
    



