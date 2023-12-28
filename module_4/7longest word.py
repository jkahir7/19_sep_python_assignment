#Write a python program to find the longest words.
f=open("mynote1.txt","r")
line=f.read()
words=line.split()
longest_word=""

for word in words:
    words_length = len(word)
    lenth = len(longest_word)
    if words_length > lenth:
        longest_word = word

    elif words_length == lenth:
        longest_word = longest_word+" "+word


print("longest word:",longest_word)

