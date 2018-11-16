#Hackerrank Grading Students
def gradingStudents(grades):
	for i in range(0, len(grades)):
		if grades[i] >= 38: 	#criteria limit
			remainder = grades[i] % 5 	#difference from 3
			whole = grades[i] - remainder 	#difference from next grade 
			if ((whole + 5) - grades[i]) < 3: 	# range within multiples of fives
				grades[i] = whole + 5
			if ((whole + 10) - grades[i]) < 3: 	#range within multiples of ten
				grades[i] = whole + 10
	return grades 	#return modified grades
print(gradingStudents([38, 40, 43, 47, 49]))		#Test Case		
