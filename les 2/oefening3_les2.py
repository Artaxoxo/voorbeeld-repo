import os
cwd = os.getcwd()
print(cwd)
os.makedirs("data", exist_ok=True)
file = open(cwd +"\\data\hello.txt", "w")
file.write("hello\n")
file.close()
file = open("data\\hello.txt")
print("inhoud" +file.read())