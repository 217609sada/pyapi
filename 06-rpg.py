#!/usr/bin/python3

def showinstructions():
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    ''')

def showStatus():
    print('------------------------')
    print('You are in the ' + currentRoom)
    print('Inventory : ' + str(inventory))
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("------------------------")

inventory = []

rooms = {
        'Hall': {
            'south': 'Kitchen',
            'east': 'Dining Room',
            'item': 'Key'
            },
        'Kitchen': {
            'north': 'Hall',
            'item': 'Monstor'
            },
        'Dining Room': {
            'west': 'Hall',
            'item': 'Food'
            }
        }

currentRoom = 'Hall'

showinstructions()

while True:
    showStatus()
    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split()

    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print('You can\'t go that way!')

    if move[0] == 'get':
        if "item" in rooms[currentRoom] and str(move[1]).lower() in str(rooms[currentRoom]['item']).lower():
            inventory += [move[1]]
            print(move[1] + ' got!')
            del rooms[currentRoom]['item']
        else:
            print('Can\'t get ' + move[1] + '!')

    if move[0] == 'quit':
        print('You have ' + str(inventory) + ' and getting out')
        break
