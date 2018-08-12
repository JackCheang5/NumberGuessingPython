import random
numArr = []
while len(numArr) < 4:  # prevent repeating numbers
    randNum = random.randint(0, 9)
    if randNum not in numArr:
        numArr.append(randNum)
print(numArr)
while True:
    guess = input("Enter your guessing: ")
    if not guess.isdigit():  # character checking
        print("Not a number")
        continue
    guessArr = []  # type declaration
    for num in range(len(guess)):
        guessArr.append(int(guess[num]))
    if len(guessArr) > 4:  # length check
        print("Invalid length")
        continue
    repeat = False  # prevent repeating numbers
    for num in guessArr:
        if guessArr.count(num) >= 2:
            print("There are repeating numbers!")
            repeat = True
            break
    if repeat:
        continue
    b = 0  # determination of B
    for i in guessArr:
        for j in numArr:
            if i == j:
                b += 1
    a = 0  # determination of A
    for i in range(len(numArr)):
        if guessArr[i] == numArr[i]:
            a += 1
            b -= 1
    if a == 4:
        print("You win!")
        break
    print(str(a) + 'A' + str(b) + 'B')
