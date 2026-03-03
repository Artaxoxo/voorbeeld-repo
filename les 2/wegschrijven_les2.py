import os
if os.path.exists("files")
    print("directory bestaat")
else :
    os.mkdir("files")
f = open("files\\data.txt", "w")
f.write ("welkom in mijn nieuwe betsand")
f.close()