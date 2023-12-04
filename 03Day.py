def define_symbol(symbol: str, symbolList: list):
    if (symbol.isnumeric() == False and symbol != '.'):
        symbolList.append(symbol)
    return symbolList

def part_1(array2D: list):
    fResult = 0    
    for idx, line in enumerate(array2D):
        numStr = ''
        for jdx, char in enumerate(line):
            if (str(char).isnumeric()): numStr = numStr+str(char)
            if (jdx == len(line)-1 or str(char).isnumeric() == False):
                if (len(numStr) > 0):
                    numLen = len(numStr)
                    numNum = int(numStr)
                    numStr = ""
                    symList = []
                    define_symbol(line[jdx], symList)
                    if jdx == len(line)-1 and line[jdx] != '.': define_symbol(line[jdx-(numLen)], symList)
                    elif jdx - (numLen+1) >= 0: define_symbol(line[jdx-(numLen+1)], symList)
                    i = jdx
                    while (i >= 0 and i >= jdx - (numLen+1)):   
                        if idx - 1 >= 0:
                            sym = str(array2D[idx-1][i])
                            define_symbol(sym, symList)
                        if idx+1 < len(array2D):    
                            sym = str(array2D[idx+1][i])
                            define_symbol(sym, symList)
                        i -= 1
                    if len(symList) > 0: fResult += numNum
    return fResult

def calc_gear_ratio(subArray: list):
    numList = []
    for li in subArray:
        if str(li[2]).isnumeric() or str(li[3]).isnumeric() or str(li[4]).isnumeric():
            numStr = ''
            isAdj = False
            for idx, char in enumerate(li):
                if str(char).isnumeric():
                    numStr += str(char)
                    if idx == 2 or idx == 3 or idx == 4: isAdj = True
                if idx == len(li)-1 or str(char).isnumeric() == False:
                    if isAdj and len(numStr) > 0:
                        numList.append(int(numStr))
                    numStr = ''
                    isAdj = False
    gRatio = 0
    if len(numList) == 2: 
        print(numList)
        gRatio = numList[0] * numList[1]
    return gRatio

def part_2(array2D: list):
    sResult = 0
    for idx, line in enumerate(array2D):
        for jdx, char in enumerate(line):
            if str(char) == '*':
                subArray = []
                i = idx-1
                while i <= idx+1:
                    rArray = []
                    j = jdx-3
                    while j <= jdx+3:
                        if i < 0 or j < 0: rArray.append['.']
                        else:
                            sym = str(array2D[i][j])
                            if i == idx and j == jdx:
                                rArray.append('*')
                            elif sym.isnumeric() == False and sym != '.':
                                rArray.append('.')
                            else:
                                rArray.append(sym)    
                        j += 1 
                    if rArray[2] == '.':
                        rArray[0] = '.'
                        rArray[1] = '.'
                    if rArray[4] == '.':
                        rArray[5] = '.'
                        rArray[6] = '.'
                    subArray.append(rArray)
                    i += 1
                sResult += calc_gear_ratio(subArray)
    return(sResult)


input = open("day3_input/real_input.txt", "r")
array2D = []
for line in input:
    array2D.append([*line.strip()])
print(part_1(array2D))                
print(part_2(array2D))