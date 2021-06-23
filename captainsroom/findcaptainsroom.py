count =  input().split()
roomNumbers =  [int(i) for i in (input().split())]

roomNumbers = sorted(roomNumbers)

for i in range(len(roomNumbers)):
    if i != len(roomNumbers)-1:
        if (roomNumbers[i] != roomNumbers[i-1] and roomNumbers[i] != roomNumbers[i+1]):
              print(roomNumbers[i])
              break
    else:
        print(roomNumbers[i])