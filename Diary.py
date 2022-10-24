#Ask the user for todays diary entry
#Save diary entry in a text file with the pre-text of todays date.

#Import to get the current date
from datetime import date

#Getting user input
diaryentry = (input('Enter your diary entry from today. '))
print("check diary entry.txt to find your diary entry.")
#Gets todays date
today = date.today()
#converts user input into a string because we can only enter strings into a text file
diaryentrystring = str(diaryentry)

#converts todays date into a string
stringtoday = str(today)

#joins all string words together and makes a new line and 2 tabs
pretext = "Today's Date: " + stringtoday + '\n' + '\t' + "Dear Diary," +'\t'


#converts all pretext into a string
stringpretext = str(pretext)

#opening file as read and write
diaryentry=open('Diary entry.txt', 'r+')

#writes our pre text into diary
diaryentry.write(stringpretext)

#writes the iary entry into text file
diaryentry.write(diaryentrystring)

#closes the diary
diaryentry.close()
