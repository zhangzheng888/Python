

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
		
	# calculating percentage and formatting to 2 decimal places
	percentage = float(count/total)	* 100.00
	forPerc = format(percentage, ".2f")
	
	print("\npercentage of odd numbers:" + str(forPerc) + "%")
	return count;

def main():
	# user prompt for filename
	
	printmsg = "Enter a filename\n"
	infile = raw_input(printmsg)
	
	print("filename: " + infile)
	
	# there is still a bug where the while loop continues and i need
	# to find a way to close the loop
	
	OpenOK = False
	while not OpenOK:
		try:
		
			infile = open(infile, "r")
			OpenOK = True
		except IOError:
			print("Cannot Open '" + infile +"'")
			infile = raw_input(printmsg)	
	

	# reads all the data in the input file
	datalines = infile.readlines()
	
	# print("list of numbers ",datalines)
	
	
	oddCountNum = percOddNumbers(datalines);
	print("Odd numbers in the list :" + str(oddCountNum))
	infile.close()

	
main()
