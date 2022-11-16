QueueArray = ["" for i in range(0,10)] #as STRING
HeadPointer = 0 #as INTEGER
TailPointer = 0 #as INTEGER
NumberOfItems = 0 #as INTEGER

def Enqueue(DataToAdd):
    global NumberOfItems
    global TailPointer
    if NumberOfItems >= 10:
        return False
    QueueArray[TailPointer] = DataToAdd
    if TailPointer >= 9:
        TailPointer = 0
    else:
        TailPointer = TailPointer + 1
    NumberOfItems = NumberOfItems + 1
    return True

def Dequeue():
    global NumberOfItems
    global HeadPointer
    if NumberOfItems == 0:
        return False
    else:
        ReturnValue = QueueArray[HeadPointer]
        HeadPointer = HeadPointer + 1
        if HeadPointer >= 9:
            HeadPointer = 0
        NumberOfItems = NumberOfItems - 1
        return ReturnValue

for i in range(0, 11):
    DataToAdd = str(input("Input element to add: "))
    result = Enqueue(DataToAdd)
    if result == True:
        print("Item is Enqueued")
    else:
        print("Queue full, cannot Enqueue")

for i in range(0, 2):
    Result = Dequeue()
    if Result != False:
        print(Result)
