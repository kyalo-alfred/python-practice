#I created an input function for data entry
text = input("Enter a text: ")

#I then created an empty string where the reversed text will occupy
reversed_text = ""

#Created a for loop for iteration of every character in the string text
for rev in text:
    #the reversed text function below reverses the text by starting
    #the string with the first element with other elements preceeding before it
    #with every iteration
    reversed_text = rev + reversed_text
#Displays the output
print(f"Reversed text: {reversed_text}")