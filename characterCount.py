message = 'I want to  be fluent in Python because of my goals in cybersecurity. It is either I become A S.O.C Analyst or a Penetration Tester'
count = {}
for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1 
print(count)