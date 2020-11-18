file = open('words.txt')

for i in file.readlines():
    s = i.strip()
    if s.endswith(('er', 'or', 'ur')):
        print("{0} her? I barley even knew her!".format(s[:-2]))

file.close()
