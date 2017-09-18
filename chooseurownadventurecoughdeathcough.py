import time
from lib import asciiart

delay = 1.56
choice_list = []
item_dict = {}
continue_story = True

print('at any time type go to bed if you would like to stop.')

def printIntroduction():
    # introduction
    print('You are Waffle Waffleman.')
    time.sleep(delay)
    print('You are at your very nice house.')
    time.sleep(delay)
    print('You want to do somthing today.')
    time.sleep(delay)
    print('What do you want to do?')
    time.sleep(delay)
    print('your choices are:')
    print('(1) beach')
    print('(2) woods')
    print('(3) hiking')
    print('(4) room')
    time.sleep(delay)
    # indicate valid choices
    return ['1','2','3','4']

def processChoice(choice_list, valid_list):
    if len(valid_list) == 0:
        print('YOU ARE DIE')
        time.sleep(delay)
        asciiart.printSkull()
        return 'dead'
    
    print('enter your choice:')
    choice = input()
    print('you chose %r' % choice)
    if choice == 'go to bed':
        return choice
    elif choice not in valid_list:
        print('This choice isnt here Mrs. Torrance.')
    else:
        choice_list.append(choice)
    time.sleep(delay)
    
    return choice_list

def printError():
    print('sorey, theese choices are geting bilded by babys. expekt delay.')

def choiceLevel1(choice_list):
    # chose beach
    if choice_list[0] == '1':
        print('You walked to the beach.')
        time.sleep(delay)
        print('You see an old submarine that is old.')
        time.sleep(delay)
        print('your choices are:')
        time.sleep(delay)
        print('(1) go in sub')
        print('(2) walk down beach')
        time.sleep(delay)
        # indicate valid choices
        return ['1','2']
    # chose woods
    elif choice_list[0] == '2':
        print('you walk into the woods.')
        time.sleep(delay)
        print('You are dumb because you walked in the woods.')
        time.sleep(delay)
        print('You are now being attacked by a bear.')
        time.sleep(delay)
        print('your choices are:')
        time.sleep(delay)
        print('(1) BE A MAN AND WRESTLE THAT BEAR LIKE JOHN CENA!')
        print('(2) RUN AWAY LIKE THE COWARDLY LION WHO IS NOW THE RULER OF OZ!')
        time.sleep(delay)
        return ['1','2']
    # chose hiking
    elif choice_list[0] == '3':
        print('you walk onto the hiking trail.')
        time.sleep(delay)
        print('You are dumb because you picked up a bear cub on the ground named little bear.')
        item_dict['friends'] = ['little bear']
        time.sleep(delay)
        print('You are now being attacked by a bear.')
        time.sleep(delay)
        print('your choices are:')
        time.sleep(delay)
        print('(1) BE A MAN AND WRESTLE THAT BEAR LIKE JOHN CENA!')
        print('(2) RUN AWAY LIKE THE COWARDLY LION WHO IS NOW THE RULER OF OZ!')
        time.sleep(delay)
        return ['1','2']
    # chose room
    elif choice_list[0] == '4':
        print('you walk into your room.')
        time.sleep(delay)
        print('You decide to play on your NES and you want to try and beat donkey kong.')
        time.sleep(delay)
        print('You are a noob so you try forever until you rage quit.')
        time.sleep(delay)
        print('you then find that time has ended and that you were in the matrix.')
        time.sleep(delay)
        return []
    else:
        printError()

def choiceLevel2(choice_list):
    # chose beach # then sub
    if choice_list[0] == '1' and choice_list[1] == '1':
        print('You hop in the sub, hoping to see the ocean.')
        time.sleep(delay)
        print('But all you see is a robot telling you how to operate the submarine.')
        time.sleep(delay)
        print('What do you want to do?')
        time.sleep(delay)
        print('(1) Listen to the boring robot?')
        print('(2) Or press ALL THE BUTTONZ !?')
        time.sleep(delay)
        return ['1','2']
    # chose beach # then walk
    elif choice_list[0] == '1' and choice_list[1] == '2':
        print('You start to walk down the beach')
        time.sleep(delay)
        print('Then you realize that you just saw a tresure chest.')
        time.sleep(delay)
        print('What do you want to do?')
        time.sleep(delay)
        print('(1) Leave the chest for somone else?')
        print('(2) Or be mad with money?')
        time.sleep(delay)
        return ['1','2']
    # chose hiking # then JOHN CENA
    elif choice_list[0] == '3' and choice_list[1] == '1':
        print('You and the bear hop in the ring to battle it out.')
        time.sleep(delay)
        print('But the bear cheats and eats you.')
        time.sleep(delay)
        print('What do you want to do?')
        time.sleep(delay)
        print('Nothing cuz')
        time.sleep(delay)
        return []
    else:
        printError()
        return []


def choiceLevel3(choice_list):
    # chose beach # then walk # chest
    if choice_list[0] == '1' and choice_list[1] == '2' and choice_list[2] == '2':
        print('"Cue the Zelda music" ')
        time.sleep(delay)
        print('DA DA DA DA.')
        time.sleep(delay)
        print('BOOM! Tarantula in yo face!')
        time.sleep(delay)
        print('You gotted a heart attacka')
        time.sleep(delay)
        return []
    else:
        printError()
        return []
  
while continue_story:
    
    if len(choice_list) == 0:
        valid_choices = printIntroduction()
        choice_list = processChoice(choice_list, valid_choices)
    elif len(choice_list) == 1:
        valid_choices = choiceLevel1(choice_list)
        choice_list = processChoice(choice_list, valid_choices)
    elif len(choice_list) == 2:
        valid_choices = choiceLevel2(choice_list)
        choice_list = processChoice(choice_list, valid_choices)
    elif len(choice_list) == 3:
        valid_choices = choiceLevel3(choice_list)
        choice_list = processChoice(choice_list, valid_choices)
    else:
        print('you have now entered the matrix, now take the blue pill and go home')
        choice_list = []
        continue
    
   # print(choice_list)
   # print(item_dict)

    if choice_list == 'go to bed' or choice_list == 'dead':
        continue_story = False
