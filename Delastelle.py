numbersInOrder=input("Please, enter the Delastelle values\n")

listOfNumbers=[]

for number in numbersInOrder:
    listOfNumbers.append(number)

counter=len(numbersInOrder)
while counter>=0:
    listOfNumbers.insert(counter, ' ')
    counter-=3

finalNumbers=''.join(listOfNumbers)
print(finalNumbers)