#this code calculate factorial for a whole number
inp = input('your number to calculate fact:')
factorial = 1
for n in range(1, inp+1):
    factorial *= n
print(f'{inp}! = {factorial}')
