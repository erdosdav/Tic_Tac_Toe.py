board = [' ' for x in range(10)]


# insert letter and position
def choiceandpos(choice, pos):
    board[pos] = choice


# looking if space is available
def available_space(pos):
    return board[pos] == ' '


def displayBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def Winnersboard(board, choice):
    return ((board[7] == choice and board[8] == choice and board[9] == choice) or  # horizontal row top
            (board[4] == choice and board[5] == choice and board[6] == choice) or  # horizontal row middle
            (board[1] == choice and board[2] == choice and board[3] == choice) or  # horizontal row bottom
            (board[7] == choice and board[4] == choice and board[1] == choice) or  # vertical row left
            (board[8] == choice and board[5] == choice and board[2] == choice) or  # vertical row middle
            (board[9] == choice and board[6] == choice and board[3] == choice) or  # vertical row right
            (board[7] == choice and board[5] == choice and board[3] == choice) or  # diagonal
            (board[9] == choice and board[5] == choice and board[1] == choice))  # diagonal


def playerMove():
    run = True
    while run:
        move = input('Please enter your number: (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if available_space(move):
                    run = False
                    choiceandpos('X', move)
                else:
                    print('Choosen space is full, try other one!')
            else:
                print('Please type a number from 1-9!')
        except:
            print('Please type a number!')


# Possibilites for pc move, sorted by odd and even postions.
def pcMove():
    possibilities = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for letter in ['O', 'X']:
        for i in possibilities:
            boardCopy = board[:]
            boardCopy[i] = letter
            if Winnersboard(boardCopy, letter):
                move = i
                return move

    odd_spaces = []
    for i in possibilities:
        if i in [1, 3, 5, 7, 9]:
            odd_spaces.append(i)

    if len(odd_spaces) > 0:
        move = randomop(odd_spaces)
        return move

    even_spaces = []
    for i in possibilities:
        if i in [2, 4, 6, 8]:
            even_spaces.append(i)

    if len(even_spaces) > 0:
        move = randomop(even_spaces)

    return move


def randomop(list):
    import random
    ln = len(list)
    i = random.randrange(0, ln)
    return list[i]


def fullboard(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    separator = ('=' * 40)
    print("Welcome to Tic Tac Toe")
    print(separator)
    print('''GAME RULES:
    Each player can place one mark (or stone)
    per turn on the 3x3 grid. The WINNER is
    who succeeds in placing three of their
    marks in a:
    * horizontal,
    * vertical or
    * diagonal row''')
    print(separator)
    print("Let's start the game")
    displayBoard(board)

    while not (fullboard(board)):
        if not (Winnersboard(board, 'O')):
            playerMove()
            displayBoard(board)
        else:
            print('Game Over!')
            break

        if not (Winnersboard(board, 'X')):
            move = pcMove()
            if move == 0:
                print('Tie Game!')
            else:
                choiceandpos('O', move)
                print('Computer move \'O\' in position', move, ':')
                displayBoard(board)
        else:
            print('X\'You win the game!')
            break

    if fullboard(board):
        print('Tie Game!')


while True:
    separator = ('=' * 40)
    answer = input('Do you want to play Tic tac toe(Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print(separator)
        main()
    else:
        break

