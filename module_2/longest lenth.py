# Write a Python function that takes a list of words and returns the length 
# of the longest one

# Creating a list 
word_list = ["jaydip", "dharma", "jinal", "ajit", "rushik"]

longest_length = 0
longest_word = ""
for word in word_list:
    length = 0

    for alpha in word:  # for count the number of alphabets
        length += 1

    if length > longest_length:
        longest_length = length
        longest_word = word


print("Longest Length = ",longest_length)
print("longest word = ",longest_word)