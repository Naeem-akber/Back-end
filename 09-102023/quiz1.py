def get_word(sentence, n):
	
	if n > 0:
		words = sentence.split()
		
		if n <= len(words):
			return(words[n-1])
	return("Nothing")
print("this is a lesson about lists",-4)
print("this is a lesson about lists",4)