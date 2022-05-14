'''
PSEUDOCODE (how the if statements are broken down)
all nonzero are always significant

if no decimal point...
   zeros significant? --> leading no, trailing no, in between yes

elif decimal point...
if left is not 0
   left of decimal point...
       zeros significant? --> leading no, everything else yes
   right of decimal point...
       zeros significant? --> all significant
elif left is 0
   left of decimal point...
       zeros significant? --> no
   right of decimal point...
       zeros signficant? --> leading no, everything else yes
'''
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
        if int(l) != 0:
            count += len(l) + len(r)
        else:
            for digit in r:
                if digit != '0':
                    count += 1
                    if nonZeroSeen == False:
                        nonZeroSeen = True
                else:
                    if nonZeroSeen == True:
                        count += 1
    return count

print("Type quit to stop checking sig figs")
while True:
    num = input("Enter number to check sig figs for: ")
    if (num == "quit"):
        break
    else:
        print(checkSigFigs(num))