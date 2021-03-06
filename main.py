#Password Generator by Anthony Omens
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

totalRandLetter = ""

randomLetterList = []
randomNumberList = []
randomSymbolList = []


for x in range(nr_letters):
  randLetter = letters[random.randint(0, len(letters)-1)]
  randomLetterList.append(randLetter)



for x in range(nr_numbers):
  randNumber = numbers[random.randint(0, len(numbers)-1)]
  randomNumberList.append(randNumber)



for x in range(nr_symbols):
  randSymbol = symbols[random.randint(0, len(symbols)-1)]
  randomSymbolList.append(randSymbol)


allThreeInOrder = randomLetterList + randomNumberList + randomSymbolList

allThreeInString = ''.join(allThreeInOrder)
print(f"Password is {allThreeInString}")

print()

random.shuffle(allThreeInOrder)

allThreeInString = ''.join(allThreeInOrder)
print(f"Better password is {allThreeInString}")