import os

def file(path):
    with open(path, 'r') as f:
        content = f.read()
        word_count = len(content.split())
        return word_count

path = r'c:\temp\test.txt'

if os.path.isfile(path):
    print("There are the number of {} words in the file{}".format(file(path), path))

#os.path.isfile(path) and  print("There are the number of {} words in the file{}".format(file(path), path))
