def percOddNumbers(data):
	count = 0 	# total number of odd numbers
	total = 0 	# total numbers within the list
	
	# iter thru strings
	for num in data:
		
		# converting current string value to int value
		
		num = int(num)
		
		# checking int value is odd
		
		if num %2!=0:
			count += 1.0
			
		total += 1.0
	
	# find the percentage of odd numbers and display to the user
		
	# calculating percentage
	percentage = float(count/total)	* 100
	
	print("count :" + str(count) + "\npercentage of odd numbers:" + str(percentage) + "%")
	return;

def main():
	# user prompt for filename
	# printmsg = "Enter a filename\n"
	
	infile = raw_input("Enter a filename\n")
	
	print("filename: " + infile)
	
	# opens the numbers.txt regardless of user filename input
	
	OpenOK = False
	while not OpenOK:
		try:
			infile = open(infile, "r")
			OpenOK = True
		except IOError:
			print("Cannot Open '" + infile +"'")
			infle = input(printmsg)	


	# reads all the data in the input file
	datalines = infile.readlines()
	print("list of numbers ",datalines)
	
	percOddNumbers(datalines);
	infile.close()

	
main()