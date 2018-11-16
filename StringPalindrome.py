#Check if String is a Palindrome
def isPanlindrome(n):
	if n is '':  #Empty String
		return True
	low = 0 #left
	high = len(n) - 1 #right 
	while low < high: #middle handle 
		if n[low] != n[high]: #right must equal left
			return False
		low += 1 #converge to right
		high -=1 #converge to left
	return True 
print(isPanlindrome(""))
