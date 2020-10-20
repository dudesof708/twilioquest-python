import sys

a = int(sys.argv[1]) + int(sys.argv[2])

if a <= 0:
    print('You have chose the path of destitution.')
elif a <= 100:
    print('You have chosen the path of plenty.')
else:
    print('You have chosen the path of excess.')