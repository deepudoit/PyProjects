import os
print(os.path.join('C:\\', 'Users', 'pgandla'))

myfiles = ['Docs.docx', 'Welcome.txt', 'Session.ppt']
for doc in myfiles:
    print(os.path.join('C:\\Documents', doc))

with open('work.txt', 'w') as f:
    f.write('Welcome to Awesome')

