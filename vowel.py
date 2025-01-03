phrase = str(input("enter the sentence to know vowels/not:").lower()) #Taking an Sentence from user
vowel = 0 # Setting Values of Vowels and Consonants to 0
Consonants  = 0

for letter in phrase: #Creating for loop with conditions
    if letter in "aeiou":
        vowel = vowel + 1
    elif letter == " ":
        pass
    else: 
        Consonants  = Consonants  + 1
print("Total vowels are : {}".format(vowel)) #Displaying count of Vowels and Consonants
print("Total not vowels are : {}".format(Consonants ))
