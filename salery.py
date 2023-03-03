def hoghoogh_1(hour, per_hour):
    print('hoghoogh 1')
    if hour > 8:
        return 'to much work'
    return hour * per_hour

def hoghoogh_2():
    print('hoghoogh 2')
    hour = int(input('how many hours? '))
    per_hour = int(input('how much per hour? '))

    if hour > 8:
        return 'too much work'
    return hour * per_hour

h = int(input('how many hours? '))
p = int(input('how much per hour? '))
print(hoghoogh_1(h, p))

print(hoghoogh_2())