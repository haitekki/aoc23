input = open("day2_input/real_input.txt", "r")
fGreen = 13
fRed = 12
fBlue = 14
finalOne = 0
finalTwo = 0
for idx, line in enumerate(input):
    gameId = idx+1
    input = line.split(':')[1].strip()
    inputF = input.replace(';', ',')
    possible = True
    greenT = 0
    redT = 0
    blueT = 0
    for one in inputF.strip().split(','):
        splitOne = one.strip().split(' ')
        amount = int(splitOne[0])
        color = splitOne[1].strip()
        if color == 'green':
            if amount > fGreen: possible = False
            if amount > greenT: greenT = amount
        if color == 'red':
            if amount > fRed: possible = False
            if amount > redT: redT = amount
        if color == 'blue':
            if amount > fBlue: possible = False
            if amount > blueT: blueT = amount   
    if possible: finalOne += gameId
    finalTwo += greenT*redT*blueT
print(finalOne)
print(finalTwo)



