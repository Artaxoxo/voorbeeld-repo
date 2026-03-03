import os
name = input('wa is je naam')
firstname = input('wa is je avoornaam')
print(firstname)
firstname = firstname.lower().replace( " ", "")
name = name.lower().replace( " ", "")
first_name_length = len(firstname)
name_length = len(name) 
username = f'(firstname).(name)'
print(username)
#dit eens hermaken!!