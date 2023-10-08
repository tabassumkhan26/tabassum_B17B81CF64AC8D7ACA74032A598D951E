def isLeapYear(Year):
  if(year%4==0 and year % 100 !=0) or year %400 ==0:
    return True 
  else:
    return False


year =int(input("Enter a value:"))
if isLeapYear(year):
  print('{} is a leapyear.'.format(yaer))
else:
  print('{} is not a leapyear.'.format(year))