ConsoleString = input("Enter a string: ")
ReversedString = ConsoleString[::-1]					#reversing the string
if ConsoleString.upper() == ReversedString.upper():
	print("Given String '{}'' is Palindrome".format(ReversedString))
else:
	print("Give String is not palindorme")