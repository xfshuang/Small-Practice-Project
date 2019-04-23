#!/usr/local/bin/python3 
# Name: Shirley Huang
# File: lab3.2.py
# Desc: 1) counts the frequency of words and; 2) counts the words that are palindromes.

import re

# Create a list of stop words
stop_words = [i.strip() for i in open('stop_words.txt').readlines()]

# Read Einstein's text into a string
relativity = open('relativity.txt').read()

# Create a list of words by splitting on non-words
#relativity = re.split("\W+", relativity)  # 34313
relativity = re.split(r"[^a-zA-Z0-9]+", relativity)  # 34311

# Remove any blank words that occur with the regex matches
# non-word characters at the end of a line.
relativity = [i.lower() for i in relativity if i != '']

# How many words?
#print("There are {} words in Einstein's \"Relativity: The Special and General Theory\".".format(len(relativity))) #34313

# Find all of the words in Relativity that are not stop words
relevant_words = [i for i in relativity if i not in stop_words]
#print("After removing stop words, there are {} words.".format(len(relevant_words)))#13648
#print("{} words were stop words.".format(len(relativity) - len(relevant_words))) #20665

print("\n",'-'*20, "Words by frequency", '-'*20, "\n")

#Count the frequency of the words in the text. Do count any stop words.
tmp = {} #create and empty dict to store the # counts for each unique word
for word in relevant_words:
    if word in tmp: #if word is in dic, value add 1
        tmp[word] += 1
    else:  # if word is not in dic, value add 1
        tmp[word] = 1
	
sorted100 = []  #store all the keys with higgest values to the lowest
#Sort a dict's keys by their value
for i in sorted(tmp, key=tmp.__getitem__, reverse=True)[:100]: 
    # i = relativity 196 /n theory 183 /n
    s = "{:>20} ({:>3})".format(i, tmp[i])
    # format i as "           relativity (196)"
    sorted100.append(s)

n = 5 #divde the list into 5 columns
chunks = [
    sorted100[i * n:(i + 1) * n]  # (0*5):(0+1)*5) = [0:5]
    for i in range(round(100/5))  # loop 20 times = (20 lists of 5 items per list)
]

# This for loop is to seperate the list in lists
for chunk in chunks:
    chunklist = [] 
    for element in chunk:
        x = '{}'.format(element) 
        chunklist.append(x)
    print(*chunklist) # * will is not displaying type

#Count the palindromes in the text (the full text) using your is_palindrome() function. 
#HEADS UP: Some of the palindromes will be numbers 
#or single alphabetical characters because your code is considering all words, 
#including stop words.

print("\n", '-'*20, "Palindromes", '-'*20, "\n")

#Write a for loop and append all the palindrome words in a list.
palindrome_word = [] 
for i in relativity:
    if i == i[::-1]:
        palindrome_word.append(i)

#count the frenquency for each palindrome word 
count_pali ={}
for word in palindrome_word:
    if word in count_pali:
        count_pali[word]+= 1
    else:
        count_pali[word] = 1

#sort the result by the highest value 
for i in sorted(count_pali, key=count_pali.__getitem__, reverse=True):
    print("{:<7}  {}".format(i, count_pali[i]))




