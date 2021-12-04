everyelement = list()
firstElement = list()
anotherfirst = list()

initialElements = list()
def findPossibleLetters(letters):

    for i in range(len(letters)):
            dummy = list(letters)
            firstElement.append(dummy[i])
            dummy.remove(dummy[i])

            if len(dummy) > 2:
                if i == len(letters):
                 firstElement.pop()
                findPossibleLetters(dummy)
                firstElement.pop()
            else:
                for j in range(len(firstElement)):
                    dummy.append(firstElement[j])
                swapped = (swapTwoValues(dummy))
                everyelement.append(dummy)
                everyelement.append(swapped)

                firstElement.pop()
                print(len(everyelement))
                print(everyelement)









def swapTwoValues(values):
    news = list(values)
    finalValues = news
    temp = finalValues[1]
    finalValues[1] = finalValues[0]
    finalValues[0] = temp
    return finalValues
if __name__ == '__main__':
    print("main function initiated")
    # findFactorial(5)
    findPossibleLetters("ABCDEF")
