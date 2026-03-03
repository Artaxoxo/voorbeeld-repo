names = ["sara", "tom", "liam", "noor"]
name = input("geef een naam op:")
if name in names: 
    print('gevonden')
else: 
    print("niet gevonden")
if "tom" not in names: 
    print("tom is niet in de klas")