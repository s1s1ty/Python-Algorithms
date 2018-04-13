# Python: InsertionSort

def insertionSort(aList):
    for i in range(len(aList)):
        cur_num = aList[i]
        j = i
        while(j > 0 and aList[j-1] > cur_num):
            aList[j] = aList[j-1]
            j = j - 1
        aList[j] = cur_num
