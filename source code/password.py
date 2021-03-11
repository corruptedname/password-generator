import random, os, sys
from random import seed, randint
os.system('cls')
#user_input for what is password for
userinput = input("what is password for: example 'youtube:' needs to have a : at the end: ")
#function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#generate tingiez
uppercase1=chr(random.randint(65,90)) #uppercase letter
uppercase2=chr(random.randint(65,90)) #uppercase letter 
uppercase3=chr(random.randint(65,90)) #uppercase letter
uppercase4=chr(random.randint(65,90)) #uppercase letter
uppercase5=chr(random.randint(65,90)) #uppercase letter
lowercase1=''.join((random.choice('qwertyuiopasdfghjklzxcvbnm') for i in range(5))) #lowwercase letter
lowercase2=''.join((random.choice('qwertyuiopasdfghjklzxcvbnm') for i in range(5))) #lowwercase letter
lowercase3=''.join((random.choice('qwertyuiopasdfghjklzxcvbnm') for i in range(5))) #lowwercase letter
lowercase4=''.join((random.choice('qwertyuiopasdfghjklzxcvbnm') for i in range(5))) #lowwercase letter
number1=random.choice(open("number.txt","r").readline().split()) #number
number2=random.choice(open("number.txt","r").readline().split()) #number
number3=random.choice(open("number.txt","r").readline().split()) #number
symbol1=random.choice(open("symbols.txt","r").readline().split()) #symbol
symbol2=random.choice(open("symbols.txt","r").readline().split()) #symbol
symbol3=random.choice(open("symbols.txt","r").readline().split()) #symbol

#generate password using all the characters in random order
password = uppercase1 + uppercase2 + uppercase3 + uppercase4 + uppercase5 + lowercase1 + lowercase2 + lowercase3 + lowercase4 + number1 + number2 + number3 + symbol1 + symbol2 + symbol3
password = shuffle(password)

#Ouput
print(password)

#save a file 
file_path = "password.txt"
with open(file_path, 'a') as file:
    file.write(userinput + password + '\n')
#################################### the end ########################################
print("your password has been saved in password.txt")
os.system('pause')


