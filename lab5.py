#-------------------------------------
# Introdutction to Python
#
# Module 5 Lab
#
# D. Paul Butler
#
# Due 06-Nov-16
#
#-------------------------------------

#!/usr/bin/python

import re
import struct

#determine if 32 or 64 bit machine
intSize = ( 8 * struct.calcsize("P"))

# set up variables
change = {'quarter': '0.25',
          'dime'   : '0.10',
          'nickel' : '0.05',
          'penny'  : '0.01'}

change_values = {float(change['quarter']),
                 float(change['dime']),
                 float(change['nickel']),
                 float(change['penny'])}

#seems to reorder change_values depending on machine size
if (intSize == 64):
    nickel, quarter, dime, penny = change_values
else:
    quarter, penny, nickel, dime = change_values

    
intQuarter = int(quarter * 100)
intDime    = int(dime    * 100)
intNickel  = int(nickel  * 100)
intPenny   = int(penny   * 100)

billAmount = 1.00

# define the regex to test the input value
r = re.compile(r"^\s*(?=.*[0-9])\d*(?:\.\d{2})\s*$")

# Run Calculator Loop
while billAmount > 0.0:
    
    # let's get some user input
    print ("\nChange Calclator - Enter 0.00 to quit")
    billAmount = input("\nEnter amount of bill (2 decimal digits only-e.g. 1.00 for $1, 0.25 for cents, etc): ")

    try:
        if r.match(billAmount):

            # make sure to get a float value of the input
            billAmount = float(billAmount)

            # let's make sure to limit to two decimals
            billAmount = round(billAmount, 2)

            # check for exit value
            if (billAmount == 0.0):
                break

            # let's get an integer value as well
            intBillAmount = int(billAmount * 100)

            # get the number of quarters
            quarterCnt = int(intBillAmount / intQuarter)

            whatsLeft  = intBillAmount - (quarterCnt * intQuarter)

            # get the number of dimes
            dimeCnt = int(whatsLeft  // intDime)

            whatsLeft = whatsLeft  - (dimeCnt * intDime)

            # get the number of nickels
            nickelCnt = int(whatsLeft // intNickel)

            whatsLeft = whatsLeft - (nickelCnt * intNickel)

            # get the number of pennies
            pennyCnt = int(whatsLeft // intPenny)

            print ("\nFor the bill amout of $%0.2f, you will need:" % billAmount)
            print ("\t%s quarter(s), %s dime(s), %s nickel(s), and %s penny/pennies.\n" % (quarterCnt, dimeCnt, nickelCnt, pennyCnt))
        else:
            raise ValueError

    except ValueError:
        print("Value error! Try Again!")
        billAmount = 1.00
    except IOError:
        print("I/O error! Try again!")
        billAmount = 1.00
    except:
        print("Other error! Try again!")
        billAmount = 1.00
        
print("We're Done.  Thanks for using this application")

#-------------------------------------
#
# End of File
#
#-------------------------------------
