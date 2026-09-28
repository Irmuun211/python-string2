# You can remove 'pass' if you written code in the function 

# Exercise 1
def is_valid_email(text):
    a= False
    dot= False
    for i in text:
        if(i == '@'):
            a= True
        if(a == True and i=='.'):
            dot= True
    if(a and dot):
        return "Valid"
    else:
        return "Invalid"

# Exercise 2
def remove_vowels(text):
    for i in text:
        if i.lower() in "aeoui":
            text = text.replace(i, '')
    return text
# Exercise 3
def get_initials(text):
    text1 = text.split()
    ans=text1[0][0].upper()+'.'+text1[1][0].upper()+'.'
    return ans

# Exercise 4
def extract_year(text):
    text1= text.split()
    for i in range(len(text1)):
        if text1[i].isdigit():
            return text1[i]
    return False

# Exercise 5
def is_palindrome(text):
    text1 = text.replace(" ", "")
    for i in text: 
        if i in '.,?!;:"': 
            text1 = text1.replace(i, "")
    text2 = text1[::-1]
    if(text2.lower()==text1.lower()):
        return True
    return False

