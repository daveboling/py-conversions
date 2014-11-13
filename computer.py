def bin2dec(biNum):
    biNum = biNum[::-1]
    decNum = 0
    for i in range(len(biNum)):
        decNum = decNum + (int(biNum[i]) * 2**i)
    return decNum

print(bin2dec('1110'))


def dec2bin(decNum):
    binNum = []
    dividend = decNum
    while dividend >= 1:
        binNum.append(str(dividend % 2))
        dividend = dividend / 2

    return ''.join(binNum)

print(dec2bin(9))
