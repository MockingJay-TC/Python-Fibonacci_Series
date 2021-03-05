# Python Assignments
# Author: Victor Aremu
# Date: 26/02/21

# Question 1
def ageName():
    import datetime  # importing the datetime module
    # Recieving input of Name and Age
    name = input("Enter Username: ")
    age = input("Enter Age: ")

    yearCal = 100 - int(age)
    year = datetime.date.today().year + yearCal

    print("In year "+str(year)+" "+name+" will turn 100")


ageName()  # calling the ageName method


# Question 2
#isinstance() to perform this work is another option
def oddEven():
    number = int(input("Enter number: "))
    if (number % 2 == 0):
        print(str(number) + " is an Even number")
    else:
        print(str(number) + " is an Odd number")


oddEven()  # calling the OddEven method


# Question 3
text = "One good thing about functions is that they can be is easily reused in another program."


def count(text):
    new_text = text.split()
    words = ['is', 'that']
    # loops through the list of words to remove words and removes it from the text
    for word in words:
        new_text.removeAll(word)
    print(new_text)


count(text)

# Question 4


def computes():
    # Recieves input from User
    a = int(input("Input an integer : "))
    n = int("%s" % a)
    nn = int("%s%s" % (a, a))
    nnn = int("%s%s%s" % (a, a, a))
    print(n + nnn + nnn)


computes()  # Calls the compute method

# Question 5
sampleText = "here is some dummy string containing numbers 19 and 20"


def count_alpha_num(input_text):
    # assigning variable to 0
    alp = 0
    num = 0
    # a loop to go through the text and return number of char and num
    for text in input_text:
        if text.isalpha():
            alp = alp + 1
        elif text.isdigit():
            num = num + 1
    print("Number of characters is " + str(alp))
    print("Number of numbers is " + str(num))


count_alpha_num(sampleText)  # Calling the count_alpha_num method


#short Circuit in python.
#join is opposite split.

#loop break and continue

# ternary operations = condition statements in a single line
#string assignment 
# 
# https://pyformat.info     ==  format()

# sys and os for files in python

# file source = "C:\Users\techc\Desktop\Amalitech\modules\Assignments\python\"
# file_object 
# with open(file_source,'r') as file_object:

# t = tuple('122233')

# to check the signatire of a variable dir("variable name")
# l = [1,2,3]


str = 'victor'
print(str)