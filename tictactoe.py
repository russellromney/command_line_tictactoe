# this is my attempt at a command line tic tac toe game

import time # for nice pauses

List = [ # stores turn number, player names, and outcome possibilities
            1,'Player 1', 'Player 2',
            [['a1','a2','a3'],['b1','b2','b3'],['c1','c2','c3'],
            ['a1','b1','c1'],['a2','b2','c2'],['a3','b3','c3'],
            ['a1','b2','c3'],['a3','b2','c1']]
        ]

ListReset = [ # stores turn number, player names, and outcome possibilities
                1,'Player 1', 'Player 2',
                [['a1','a2','a3'],['b1','b2','b3'],['c1','c2','c3'],
                ['a1','b1','c1'],['a2','b2','c2'],['a3','b3','c3'],
                ['a1','b2','c3'],['a3','b2','c1']]
            ]

nameKeep = ['','']

Dict = { # stores position info and player names
            'a1':'_','a2':'_','a3':'_',
            'b1':'_','b2':'_','b3':'_',
            'c1':'_','c2':'_','c3':'_'
        }

def quitCheck(s): # quits if the user wants to
    if s == 'quit':
        exitHandler()
    else:
        return s

def player(): # returns a string of the name of the player
    if List[0] % 2 == 0:
        return List[2]
    return List[1]

def again():
    if quitCheck(raw_input('Do you want to play again? y/n: ')) == 'y':
        if quitCheck(raw_input('Do you want to change the player names or order? y/n: ')) == 'y':
            List = ListReset
            gameSetup()
            turn()
        else:
            List = ListReset
            List[1] = nameKeep[0]
            List[2] = nameKeep[1]
            board()
            turn()
    else:
        exitHandler()

def win():
    print '%s wins!' % (player())
    again()

def cats():
    print 'Looks like a tie; next time, avoid such unexciting mediocrity!'
    again()

def move(): # returns either X or O depending on the player
    return Dict[player()]

def gameOpen(): # welcomes to new game
    print "Welcome to 'Command Line Tic Tac Toe', a game of drama and intrigue"
    print "If at any time you want to quit, type 'quit'"
    print "Start by entering your names"

def gameSetup(): # starts game and modifies List to match players
    List[1] = quitCheck(raw_input('Name of first player: '))
    nameKeep[0] = List[1]
    print "Congrats, %s, you're X's" % List[1]
    List[2] = quitCheck(raw_input('Name of second player: '))
    nameKeep[1] = List[2]
    print "Congrats, %s, you're O's" % List[2]
    Dict[List[1]] = 'X'
    Dict[List[2]] = 'O'
    time.sleep(1)
    print '\n\n\nHow to Play: when it is your turn, type the position (e.g. a3) where you want to play and press Enter'
    time.sleep(2)
    print "\n\n\nTime to get started - may the superior player win!\n"
    board()

def board(): # prints the "board" using position values from Dict
    print '  1 2 3 '
    print 'a %s %s %s ' % (Dict['a1'], Dict['a2'], Dict['a3'])
    print 'b %s %s %s ' % (Dict['b1'], Dict['b2'], Dict['b3'])
    print 'c %s %s %s ' % (Dict['c1'], Dict['c2'], Dict['c3'])

def outcomeCheck():
    for l in List[3]:
        if Dict[l[0]] == Dict[l[1]] and Dict[l[1]] == Dict[l[2]] and Dict[l[0]] != '_':
            win()

def exitHandler():
    print "\nExiting 'Command Line Tic Tac Toe'\n\nGood-bye!\n"
    exit()

def turn(): #does the full turn process
    while List[0] < 10:
        while True:
            play = quitCheck(raw_input("%s's move: " % player()))
            if play in ['a1','a2','a3','b1','b2','b3','c1','c2','c3']:
                if play not in List:
                    Dict[play] = move()
                    List.append(play)
                    break
                else:
                    print 'That has already been played. Try again.'
            else:
                print 'That position does not exist. Try again.'
        board()
        outcomeCheck()
        time.sleep(1)
        List[0] += 1
        turn()
    cats()

def gameStart():
    gameOpen()
    gameSetup()
    turn()


# ----------- code below this line runs the game --------------


gameStart()
