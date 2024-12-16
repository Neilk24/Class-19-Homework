import math

trignometry=str(input('What would you like to find. sin, cos, or tan: '))
num=int(input('What number do you want to solve your problem: '))

if trignometry=='sin':
    print(math.sin(num))
elif trignometry=='cos':
    print(math.cos(num))
elif trignometry=='tan':
    print(math.tan(num))
else:
    print('Try again. We could not process your request.')