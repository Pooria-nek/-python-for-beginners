list = []
def avrg():
    x = True
    while x:
        num = int(input("enter number: "))
        if num == -1:
            return sum(list)/len(list)
        list.append(num)

print("->", avrg())