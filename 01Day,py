input = open("day1_input/real_input.txt", "r")
list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numberList = list[0:9]
wordList = list[9:18]
final = 0
for line in input:
    truelist = [0]*len(line)
    for v in list:
        templist = [i for i in range(len(line)) if line.startswith(v, i)]
        for s in templist:
            truelist[s] = v
    truelist = [ v for v in truelist if v != 0 ]
    for idx, x in enumerate(wordList) :
        truelist = [sub.replace(x, numberList[idx]) for sub in truelist]        
    final += int(truelist[0]+ truelist[-1])
print(final)
