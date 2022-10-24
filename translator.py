#Program that asks the user how many words in their sentence to be translated, then translates it and print it.
print('  Translation Station')
print('-----------------------')
inputword = input('Enter a sentence to be translated: ')
lowerword = inputword.lower()

word = list(lowerword)
print(word)

for i in range(0,len(word)-1):
  if word[i] == "." or  word[i] == ",":
    word.remove(word[i])
  
# hello my name is
# olleh ym eman si

# hello my name is 
# sentence = [hello, my, name, is]
word = "".join(word)
listsplit = word.split()
print(listsplit)


# new_list = list(reversed(listsplit))
# print(new_list)
newlist = []

for i in range(0,len(listsplit)):
# reverse each word in the list
  newstring = reversed(listsplit[i])
# have to join the reversed word because it splits it up to individual letters
  newlist.append(''.join(newstring))


print('Your translated sentence is :',' '.join(newlist))

