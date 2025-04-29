name = True
while name:
    try:
        number = int(input())
    except ValueError:
        print("Expected int recieved str")