friends = ['Atena', 'Mehti', 'Amin', 'Pegah', 'Amir', 'Matin', 'Fatemeh', 'Erfan', 'Nima', 'Mohammad', 'Negin', 'Ali']
blocks = ['Ali', 'Amir', 'Amin', 'Nima']

def showlist():
    count = 1
    for name in friends:
        n = name

        for b in blocks: 
            if name == b:
                n = '*****'

        print(count, '-', n)
        count = count+1

def addfriends():
    name = input('whats is the name? ')
    friends.append(name)

def addblocks():
    name = input('whats is the name? ')
    blocks.append(name)

def removefriends():
    name = input('whats is the name? ')
    friends.remove(name)

word = input('> ')
while word != 'end':
    if word == 'Showf':
        showlist()
    elif word == 'Removef':
        removefriends()
    elif word == 'Addf':
        addfriends()
    elif word == 'Addb':
        addblocks()
    else:
        print('dari eshtebah mizani haji!!!')

    word = input('> ')