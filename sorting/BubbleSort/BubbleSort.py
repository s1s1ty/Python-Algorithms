# Python: BubbleSort

def bubbleSort(aList):
    for i in range(len(aList)):
        for j in range(0, len(aList)-1-i, 1):
            if aList[j] > aList[j+1]:
                aList[j+1], aList[j] = aList[j], aList[j+1]
