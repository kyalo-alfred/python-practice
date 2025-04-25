#I first made an input function for data input
number = int(input("Enter a number: "))

#I then created the variables fact and i to aid in the loop
fact =1
i=1

#Created a while loop and the variables fact and i for each iteration
while i <= number:
  fact = fact * i
  i += 1

#Finalized by displaying the output
print(f"Your factorial of:{number} is {fact}")