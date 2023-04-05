ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
ports2 = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

routes = [(start, stop) for start in ports for stop in ports]
print(routes)
print(len(routes))

print("XXXXXXXXXXXXXXXXXXXXXXXXXX")

routes = [(start, stop) for start in ports for stop in ports if start != stop]
print(routes)
print(len(routes))

print("XXXXXXXXXXXXXXXXXXXXXXXXXX")

routes = [(start, stop) for start in ports for stop in ports if start < stop ]
print(routes)
print(len(routes))

print("Analogiczne generatory:")

genRoutesAll = ((start, stop) for start in ports for stop in ports)
print(next(genRoutesAll))
print(len(routes))
i = 0
while True:

    try:
        print(next(genRoutesAll))
        i += 1
    except StopIteration:
        print("So many values have been generated:\t {}".format(i))
        break


print("XXXXXXXXXXXXXXXXXXXXXXXXXX")

genRoutesTheSame = ((start, stop) for start in ports for stop in ports if start != stop)
i = 0
while True:

    try:
        print(next(genRoutesTheSame))
        i += 1
    except StopIteration:
        print("So many values have been generated:\t {}".format(i))
        break


print("XXXXXXXXXXXXXXXXXXXXXXXXXX")

genRoutesGood = ((start, stop) for start in ports for stop in ports if start < stop)
i = 0
while True:

    try:
        print(next(genRoutesGood))
        i += 1
    except StopIteration:
        print("So many values have been generated:\t {}".format(i))
        break

