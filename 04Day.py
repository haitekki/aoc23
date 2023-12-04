def calc_line (liInput: list):
    inter = set(liInput[1]).intersection(liInput[2])
    return len(inter)

def part_one (arrayedInput: list):
    fSum = 0
    for li in arrayedInput:
        wins = calc_line(li)
        if wins == 1: 
            fSum += 1
        elif wins >= 1:
            fSum += 2**(wins-1)
    return fSum

def part_two (arrayedInput: list):
    lastCardId = arrayedInput[-1][0]
    for card in arrayedInput:
        num = calc_line(card)
        if num > 0:
            for cardId in range(card[0]+1, card[0]+num+1):
                for c in arrayedInput:
                    if c[0] == cardId:
                        arrayedInput.append(c)
                        break
    return len(arrayedInput)

input = open("day4_input/real_input.txt", "r")
eInput = []
for idx, line in enumerate(input):
    line = line.replace('  ', ' ')
    fSplit = line.split(':')[1]
    sSplit = fSplit.split('|')
    eInput.append([idx+1, str(sSplit[0]).strip().split(' '), str(sSplit[1]).strip().split(' ')])
print(part_one(eInput))
print(part_two(eInput))