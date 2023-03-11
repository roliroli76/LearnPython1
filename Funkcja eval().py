import math

argument_list = []

i = 0
'''
while i < 10.0:
    argument_list.append(i)
    i += 0.1
'''
for argument in range(100):
    argument_list.append(argument * 0.1)
formula = input("Give me the formula of a function as a variable x:\t" )

for x in argument_list:
    result = eval(formula)
    print(x, result)
