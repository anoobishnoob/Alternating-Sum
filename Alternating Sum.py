#Title: Lab #1 alternating sum, Samme Qandil
#input: n that is a positive int
#output 1 - 2 + 3 - 4 + 5 - 6 + 7 - 8 + 9 - 10 ... +|- n 
#import math
# my second solution 
print("Please provide me a positive interger")

total = 0
i =1
n = float(input())

while i <= n:
  if (i%2 != 0): #prints all odd integers
    total += i 
  else:
    total += -1*i 
  i+=1
print(total)
