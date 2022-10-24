#Program that asks the user how many words in their sentance to be translated, then translates it and prints it.
sentence = []
def translator(sentence):
  #Program that changes inputs into a secret language version by swapping round the 2 halves of a word

  #gets input from user
  input1 = (input('enter word: '))
  #gets length of user input
  length = len(input1)
  #halving the word to find the first half.
  halflength = length/2
  #making the number an integer
  halflength = int(halflength)
  #creating half the word with the start and end
  firsthalf = input1[0:halflength]
  secondhalf = input1[halflength:length]

  newword = (secondhalf+firsthalf)
  sentence.append(newword)
  #print('New word: ',newword)
  



numwords = int(input('How may words do you want to translate?:' ))

for i in range(numwords):
  translator(sentence)
  
print(sentence)

 