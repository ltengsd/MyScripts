import urllib
import re

print "we will try to open this url, in order to get IP Address"

url = "http://checkip.dyndns.org"

print url

request = urllib.urlopen(url).read()

theIP = re.findall(r"d{1,3}.d{1,3}.d{1,3}.d{1,3}", request)

print "your IP Address is: ",  theIP

# Get three test score
round1 = int(raw_input("Enter score for round 1: "))

round2 = int(raw_input("Enter score for round 2: "))

round3 = int(raw_input("Enter score for round 3: "))
   
# Calculate the average
average = (round1 + round2 + round3) / 3

# Print out the test score
print "the average score is: ", average 


import string
from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(randint(8, 16)))
print password

import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print "Rolling the dices..."
    print "The values are...."
    print random.randint(min, max)
    print random.randint(min, max)

    roll_again = raw_input("Roll the dices again?")