#Print the mean of the numbers given as arguments
import sys
sum= 0

#if i forget to add any arguments after mean.py, exit the program
if len(sys.argv) == 1:
	print'Error: No arguments given.'
	exit()
# do a for loop of arguments from 1 (which is the 2nd in python) to the end (:) and then average it based on the number of arguments -1 (which is the program name)

for num in sys.argv[1:]:
	sum += float(num)

print sum / (len(sys.argv) - 1)


