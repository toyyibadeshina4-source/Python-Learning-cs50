import pyperclip
text = pyperclip.paste()
# TODO: Seperate lines and add stars
lines = text.split('\n')
for line in range(len(lines)):
    lines[line] = '*'  + lines[line]
text = '\n'.join(lines)
pyperclip.copy(text) 
print(text)