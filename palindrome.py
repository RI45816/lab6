# File: palindrome.py
# Author: Uzoma Uwanamodo
# Date: 10/12/2016
# Section: 05
# E-mail: uu3@umbc.edu
# Description:
# Determine whether or not a string is a palindrome
# Collaboration:
# I did not collaborate with anyone on this assignment

def faster():
	string = input("Enter a string: ") # Prompt user for string to be checked
	print(string, "is%s" % ("" if string[::-1] == string else " not"), "a palindrome")
	
def main():
	string = input("Enter a string: ") # Prompt user for string to be checked
	secondString = ""
	for i in range (len(string)-1,-1,-1):
		secondString = secondString + string[i]
	print(string, "is%s" % ("" if secondString == string else " not"), "a palindrome")
		
	
main()