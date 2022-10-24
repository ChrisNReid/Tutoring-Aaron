

def speeding3():
    #Program that takes 2 input speeds and finds the average. if average is bigger than 30mph.. print speeding.. save speed in a file
  #decimal in programming = float

  import random
  #open file speed.txt as a read and write
  speedfile = open('speed.txt', 'r+')

  #for loop of 2
  for i in range(25):
      #2 speed inputs
      speed1 = random.randint(299, 1000)
      speed2 = random.randint(299, 1000)
      speed3 = random.randint(299, 1000)
      #calculate average of 2 speeds
      meanspeednotrounded = (speed1 + speed2 + speed3) / 3
      #round to 1 decimal place and print speed
      meanspeed = round(meanspeednotrounded,1)
      print(meanspeed)
      #check they are not over speed limit
      if meanspeed > 411:
          print('Speeding!!!')
          #check they are not reversing
      elif speed1 < 0 or speed2 < 0 or speed3 <0:
          print('Reversing on road. Arrest Now!')
      else:
          print('OK, not speeding')

      #make integer(whole number) a string to put in file
      stringmeanspeed = str(meanspeed)
      #write into speed.txt file
      speedfile.write(stringmeanspeed + '\n')
  #close file
  speedfile.close()