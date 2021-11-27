everyelement = list()
firstElement = list()
anotherfirst = list()


def findPossibleLetters(letters):
    if (len(letters) > 2):

        for i in range(len(letters)):
            print(i)
            dummy = list(letters)
            firstElement.clear()

            firstElement.append(dummy[i])
            anotherfirst.append(dummy[i])
            print(anotherfirst)
            dummy.remove(dummy[i])
            findPossibleLetters(dummy)
    else:

        letters.append(firstElement[0])
        letters.append(anotherfirst[0])

        everyelement.append(letters)
        everyelement.append(swapTwoValues(letters))
        # print(len(everyelement))
        # print(len(anotherfirst))
        # print(anotherfirst)
        anotherfirst.clear()
        print(everyelement)


#

def swapTwoValues(values):
    news = list(values)
    finalValues = news
    temp = finalValues[1]
    finalValues[1] = finalValues[0]
    finalValues[0] = temp
    return finalValues


def findLetters(letters):
    print(letters)


if __name__ == '__main__':
    print("main function initiated")
    # findFactorial(5)
    findPossibleLetters("ABCD")

