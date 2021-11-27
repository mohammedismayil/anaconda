everyelement = list()
firstElement = list()
anotherfirst = list()


def findPossibleLetters(letters):
    for i in range(len(letters)):
            dummy = list(letters)
            firstElement.clear()
            firstElement.append(dummy[i])
            anotherfirst.append(dummy[i])
            dummy.remove(dummy[i])
            if len(dummy) > 2:
                findPossibleLetters(dummy)
                anotherfirst.clear()
            else:
                print(len(anotherfirst))
                for j in range(len(anotherfirst)):
                    dummy.append(anotherfirst[j])
                everyelement.append(dummy)
                everyelement.append(swapTwoValues(dummy))
                anotherfirst.clear()
                print(everyelement)
                # print(anotherfirst)
                print(len(everyelement))

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
    findPossibleLetters("ABCDE")
