'''
cities = ['Paris', 'Warsaw', 'Tokyo']
countries = ['France', 'Poland', 'Japan']

for i, (city, country) in enumerate(zip(cities, countries)):
    print('{} - {} - {}'.format(i + 1, city, country))
'''

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

for (project, leader) in zip(projects, leaders):
    print("The leader of ",project, " is ", leader)


dates = ['2016-06-23', '2016-08-29', '1994-01-01']


for i, (project, leader, date) in enumerate(zip(projects, leaders, dates)):
    print("%i - The leader of %s started %s is %s\n"%(i, project, leader, date))

