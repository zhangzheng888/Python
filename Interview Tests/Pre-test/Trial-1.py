def countOddNums(data):
	count = 0 	# total number of odd numbers
	
	# iter thru strings
	for num in data:
	# converting current string value to int value
		num = int(num)
	# checking int value is odd
	        if num %2!=0:
			count += 1.0
			
	return count;

Def PercentOdd(numOfOdds, totalCount):
	
	# find the percentage of odd numbers and display to the user
	# calculating percentage
	percentage = float(numOfOdds/totalCount) * 100
	print("percentage of odd numbers:" + str(percentage) + "%")


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
	
	oddCountNum = countOddNums(datalines);
	print("Odd numbers in the list :" + str(oddCountNum))
	
	printPercentOdd(oddCountNum, len(datalines));
	infile.close()

main()