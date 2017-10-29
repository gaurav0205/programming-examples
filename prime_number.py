# A Python program in Python to check if the number is prime or not
# input from the user
num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   for i in range(2,num):
      if (num % i) == 0:
         print(num,"is not a prime number")
         break
      else:
          print(num,"is a prime number")
          break
else:
   print("Please enter a number greater than 1")
   
