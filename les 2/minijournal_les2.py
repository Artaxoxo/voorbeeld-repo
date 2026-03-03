import os
if not os.path.exists('data\\journal.txt'):
    f = open('data\\journal.txt', 'x')

    f.write('start \n')
    f.close()
f = open('data\\journal.txt', 'a')
f.write ('entr X\n')
f.close()
