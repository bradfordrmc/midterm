import csv # import library for csv files

file = open("Books.csv", "a") #opens csv file and readies it for appending
title = input("Enter a Title: ") # asks for user input title
author = input("Enter an Author: " ) #asks for user input author
year = input("Enter the year it was released: ") #asks for user input year
newrecord = title + "," + author + "," + year + "\n" # combines all previous entries into 1 variable called new record, uses commas and newline to seperate 
file.write(str(newrecord)) #converts newrecord to string and puts it in the csv file
file.close() #closes the file 

file = open("Books.csv", "r") # opens file and readies it to be read
for row in file: #for loop that finds the rows in the file
    print(row) #prints all the rows in the file
file.close() # closes the file