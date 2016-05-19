# Created: Wed May 18 21:18:01 PDT 2016
# Writen By: Joshua Leihe
# Filename: main.py

import datetime
from functions import *

t = datetime.time (1, 1, 1)
d = datetime.date(2016, 5, 19)

print """Please Enter the Year, Monty, and Day to retrieve\ntide data for the Golden Gate Bridge.\n\n"""

r = 'y'
while r != 'n':
	y = input("Year: ")
	m = input("Month: ")
	d = input ("Day: ")
	
	date = datetime.date(y, m, d)
	
	print "\nThe tides on " + str(date) + " are:\n"
	tide(date, t)
	r = input("Continue? (y/n)")
