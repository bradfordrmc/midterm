import math #imports math library
import time #imports time library

Y = int(input("enter your age in years: ")) #ask for user input Age
M = int(input("enter number of months since last birthday: ")) #asks for number of month since user's birthday
D = int(input("enter days into current month: ")) # asks for the user to input the current amount of days into month

D = ((Y * 12 + M) * 30) + D # math to determine total days a person has been alive
seconds = D * 86400 #multiplies day value by the amount of seconds in a day

print( "You have been alive for", seconds , "seconds!" ) # print statement that says how many seconds the person has been alive.