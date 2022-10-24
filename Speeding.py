def inputspeed():
  #Program that takes 2 input speeds and finds the average. if average is bigger than 30mph.. print speeding.. save speed in a file
  #decimal in programming = float

  #open file speed.txt as a read and write
  speedfile=open('speed.txt', 'r+')

  #forever loop
  while True:
    #2 speed inputs
    speed1 = float(input('enter 1st speed '))
    speed2= float(input('enter 2nd speed '))
    #calculate average of 2 speeds
    meanspeed=(speed1+speed2)/2
    #print speed
    print(meanspeed)
    #check they are not over speed limit
    if meanspeed > 30:
      print('Speeding!!!')
      #check they are not reversing
    elif speed1 < 0 or speed2 < 0:
      print('Reversing on road. Arrest Now!')
    else:
      print('OK, not speeding')
    
  
    #make integer(whole number) a string to put in file
    stringmeanspeed = str(meanspeed)
    #write into speed.txt file
    speedfile.write(stringmeanspeed)
  #close file
  speedfile.close()





  
