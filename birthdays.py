birthdays = {'Toyyib':'Feb 24','Yusuf':'Dec 12','Halimah':'Dec 16','Habeeb':'Oct 12'}
while True:
    print('Enter a name you like:(blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
      print(f'{birthdays[name]} is the birthday of {name}')             
    else:
       print(f'I do not have birthday information for {name}')
       print('What is the person birthday?')
       bday = input()
       birthdays[name] = bday
       print('Birthday database updated')
       