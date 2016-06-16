from sys import argv
from pdb import set_trace
import re

def main(imei):
    #takes a string imei number
    #returns a string imei number compliant with luhn algorithm
    #set_trace()
    
    if validImei(imei):
        if len(imei) == 15:
            imeiNoCheck = imei[:len(imei)-1]
        else:
            imeiNoCheck = imei
    else:
        return None

    check = checkDigit(imeiNoCheck)
    rightImei = imeiNoCheck + str(check)
    
    return rightImei


def validImei(im):
    imeiPattern = r'\d{14}\d?$'
    imeiRegex = re.compile(imeiPattern)
    if imeiRegex.match(im):
        return True


def checkDigit(imeiNoCheck):
    #takes an imei number without check digit
    #returns check digit

    #set_trace()
    digits = [int(d) for d in imeiNoCheck] 
    
    doubleDigits = digits 

    for i in range (len(digits)-1, -1, -2):
        double = 2*digits[i]
        if double > 9:
            doubleDigits[i] = double -9
        else:
            doubleDigits[i] = double

    allDoublesSum = sum(doubleDigits)
    multiply = allDoublesSum * 9
    multiplyList = [int(dig) for dig in str(multiply)]
    return multiplyList[-1]

if __name__ == '__main__':
    
    #imei = str(argv[1])
    #imei = "86711802337929"
    #cdigit = checkDigit(imei)
    receiving = True

    while receiving:
        imei = raw_input("Please enter imei: ")
        c = main(imei)
        if c:
            print "The correct imei is: " + c
        else:
            print "The value entered is not an IMEI"
        confirm = raw_input("Another One? (y/n): ")
        if confirm != 'y':
            break
