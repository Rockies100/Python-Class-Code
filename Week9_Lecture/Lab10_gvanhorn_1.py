#This program is titled "Word Count". It will take a text file from the user and count how frequently a word appears in that file.
#Gavin Van Horn
#March 26th, 2025
import string
import os

def word_freq(file):
    freq = {}

    line = file.readline() 

    punctChars = string.punctuation
    while line:
        for c in punctChars:
            line = line.replace(c,"")
        words = line.split()

        for word in words:
            word = word.lower()
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
        line = file.readline()
    return freq

def printWds(freq):
    for word in sorted(freq.keys()):
        print(f"{word} :: {freq[word]}")

def main():
    filename = input("Please enter the filename: ")

    try:
        with open(filename, 'r') as file:
            
            word_count = word_freq(file)

        printWds(word_count)

    except:
        print(f"The file '{filename}' could not be found")
main()