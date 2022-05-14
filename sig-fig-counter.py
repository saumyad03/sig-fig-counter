#sig-fig-counter
'''
Rules
1. Nonzero digits are always significant
2. Any zeros between two significant digits are significant
3. A final zero or trailing zeros in the decimal portion 
ONLY are significant
'''
#all nonzero always significant

#if no decimal point...
#zeros significant? --> leading no, trailing no, in between yes

#if decimal point...
#left of decimal point...
#zeros significant? --> leading no, everything else yes
#right of decimal point...
# zeros significant? --> all significant

#function that does the actual checking, parameter is a string
def checkSigFigs(number):
    #input validation
    try:
        float(number)
    except:
        return "This is not a valid number"
    #actual checker
    count = 0
    nonZeroSeen = False
    zeroCount = 0
    if '.' not in num:
        for digit in num:
            if digit != '0':
                count += 1
                if nonZeroSeen == False:
                    nonZeroSeen = True
                else:
                    count += zeroCount
                zeroCount = 0
            else:
                zeroCount += 1
    else:
        number = number.split('.')
        l = number[0]
        r = number[1]
        count += len(r)
        for digit in l:
            if digit != 0:
                count += 1
                if nonZeroSeen == False:
                    nonZeroSeen = True
            else:
                if nonZeroSeen == True:
                    count += 1
    return count

while True:
    num = input("Enter number to check sig figs for: ")
    print(checkSigFigs(num))

