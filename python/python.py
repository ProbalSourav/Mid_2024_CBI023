#Function to calculate number of vowels and consonets
def nb_consonent_vowels(s):
    vowels=0
    consonents=0
    for i in range(0,len(s)):   
    #Checks whether a character is a vowel  
        if s[i] in ('a',"e","i","o","u",'A',"E","I","O","U"):  
            vowels = vowels + 1  
        elif (s[i] >= 'a' and s[i] <= 'z' or s[i] >= 'A' and s[i] <= 'Z'):  
            consonents= consonents + 1
    return vowels, consonents

s=input("Enter string:")
s.lower()
list=nb_consonent_vowels(s)

print("Number of vowels are:")
print(list[0])
print("Number of consonents are:")
print(list[1])


