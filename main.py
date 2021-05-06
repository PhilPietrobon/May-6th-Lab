#Q1
#Gather Inputs
x = str(input("What is you first name: "))
y = str(input("Tell me your surname: "))

#Print in reverse order
print(y, x)

#Q2
#Set variables
x = int(input("Pick a number: "))

#check remainder to determine if it can be even
y = x % 2

#print message because it's zero
if x == 0:
  print("This is a zero")

#print message because it's odd
elif y > 0: 
  print("This is an odd number. ") 

#print message because it's even
else: 
  print("This is an even number")

#Q3
#Gather inputs
x = int(input())

#Scan each number and put it with appropriate dates by subtracting by how ever many days have past minus 31 or 30 depending on the month. (feb is 28)
if x >= 1 and x <= 31: 
  print("January, ", x)

elif x >= 32 and x <= 59: 
  print("Febuary, ", x -31 )

elif x >= 60 and x <= 90: 
  print("March, ", x -59 )

elif x >= 92 and x <= 120: 
  print("April, ", x -90 )

elif x >= 121 and x <= 151: 
  print("May, ", x -120 )

elif x >= 152 and x <= 181: 
  print("June, ", x -151 )

elif x >= 182 and x <= 212: 
  print("July, ", x -181 )

elif x >= 213 and x <= 243: 
  print("August, ", x -212 )

elif x >= 244 and x <= 273: 
  print("September, ", x -243 )

elif x >= 274 and x <= 304: 
  print("October, ", x -273 )

elif x >= 305 and x <= 334: 
  print("November, ", x -3304 )

elif x >= 335 and x <= 365: 
  print("December, ", x -334 )

#Q4

#Starting with number five, loop a new line removing 1 from 5 each loop
for num in range(5 + 1):
  for num2 in range(5, 0 + num, -1):
    print(num2, end=' ')

  #print
  print()

#Q5
#recieve an input (pick)
pick = int(input("Select a number to make a ladder: "))

#for a number in the range, create a loop that prints a new line subtracting one number from the line each time
for num in range(pick + 1):
  for num2 in range(pick, 0 + num, -1):
    print(num2, end=' ')

  #print
  print()