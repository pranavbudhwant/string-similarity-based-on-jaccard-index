import re
import csv

stop_words = []

#stopWords.txt --> contains the manually added stopwords(each on a newline).
with open('stopWords.txt','r') as stopWordFile:
	tWord = stopWordFile.readline()
	tWord = tWord.strip('\n')
	stop_words.append(tWord)
	while tWord:
		tWord = stopWordFile.readline()
		tWord = tWord.strip('\n')
		if tWord not in stop_words: #Avoid duplicates
			stop_words.append(tWord)

#This function accepts a string as a parameter and returns a cleaned string, one without any redundant characters/words
def clean(temp):
	temp = temp.lower()

	#Replace all special characters with spaces:
	temp = re.sub(r'\\|\/|\,|\ |\.|\@|\'|\"|\#\;|\:|\+|\-',' ',temp)
	
	#Replace all multiple occurances of spaces with a single space:
	temp = re.sub(r'\ {1,5}',' ',temp)

	#Remove all redundant groups of characters:
	temp = re.sub(r'(\b\d{1,4}\b|\b[A-Za-z]{3}\b|\b[A-Za-z]{2}\b|\ [A-Za-z]\ |\b[A-Za-z]+\/[A-Za-z]+\b|\b\d{1,2}[A-Za-z]+\b|\.|[A-Za-z]{1,3}\d{1,3})','',temp)
	#1-4 digit number|3 characters|2 characters|(space)single character(space)|character(s)/character(s)|1-2 digits followed by character(s)|.

	#Replace all multiple occurances of spaces with a single space:
	temp = re.sub(r'\ {1,5}',' ',temp)

	temp = re.sub(r'\(\)','',temp)
	
	#Remove all stop words
	queryWords = temp.split(' ')
	resultWords = [word for word in queryWords if word.lower() not in stop_words]
	result = ' '.join(resultWords)

	#Replace all multiple occurances of spaces with a single space:
	result = re.sub(r'\ {1,5}',' ',result)

	#Remove any occurances of single/double/triple characters
	result = re.sub(r'[^[A-Za-z]][A-Za-z]{1,3}[^[A-Za-z]]','',result)

	return result
