## Basic-Print all integers from 0 to 150.
def print_0_to_150():
  for i in range(251):
    print(i)

print_0_to_150()

##Multiples of Five-Print all the multiples of 5 from 5 to 1,000
def print_multiples_of_5():
  for count in range(5,1005,5):
    print(count)

print_multiples_of_5()

##Counting the Dojo Way-Print integers 1 to 100.If divisible by 5,print "Coding" instead.If divisible by 10 print "Coding Dojo"

def Counting_the_Dojo_Way():
  for count in range(1,100):
    if count % 10 == 0:
      print("Coding Dojo")
    elif count % 5 == 0:
      print("Coding")
    else:
      print(count)

Counting_the_Dojo_Way()

#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
total=0

for odd in range(0,500001):
  if(odd % 2 == 1):
    total = odd + total
print(total)

#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours
def countdown_by_4():
  for count in range(2018,0,-4):
    print(count)

countdown_by_4()

#Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 9
mult = 3

for count in range(lowNum,highNum+1):
  if count % mult == 0:
    print(count)