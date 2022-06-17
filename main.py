#enter your first number
number = input("Enter a number: ")
sumN = 0
count = 0

while number != "":
  number = int(number)
  sumN += number
  count += 1
  number = input("Enter another number or press ENTER to quit: ")

average = sumN / count

print("The sum of the inputted numbers is", sumN, "and the average of them is", average)