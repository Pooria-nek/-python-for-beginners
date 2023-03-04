friends = []
# def addtolist(length):
#     n = 1
#     while n <= length:
#         name = input(str(n) + '-whats is the name? ')
#         friends.append(name)
#         n = n+1
#     print('i found ' ,(n-1) ,' friends')

def addtolist():
    x = True
    while x:
        name = input(str(len(friends)+1) + '-whats is the name? ')
        if name == "-end":
            return friends
        friends.append(name)

def showlist():
    for i in friends:
        print(i)

    # i = 0
    # while i < len(friends):
    #     print(friends[i])
    #     i += 1

addtolist()
showlist()