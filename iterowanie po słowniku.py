banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]


'''
monthDays = dict(zip(zawartość))
for key in monthDays:
    print("Key is", key, "value is", monthDays[key])
'''

dict_denominations = dict.fromkeys(banknotes_coins, 0)

dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1

dict_denominations[50] += 1
dict_denominations[20] += 2
dict_denominations[5] += 1
dict_denominations[2] += 2

dict_denominations[100] += 1
dict_denominations[50] += 1
dict_denominations[2] += 1

for key in dict_denominations:
    print("Dominate:    {:>9.2f} - amount     {:>9.0f}".format(key, dict_denominations[key]))



