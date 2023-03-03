friends = []

def addtolist(length):
    n = 1
    while n <= length:
        name = input(str(n) + '-whats is the name? ')
        friends.append(name)
        n = n+1
    print('i found ' ,(n-1) ,' friends')

def showlist():
    for i in friends:
        print(i)

    # i = 0
    # while i < len(friends):
    #     print(friends[i])
    #     i += 1

addtolist(int(input("length of list? ")))
showlist()