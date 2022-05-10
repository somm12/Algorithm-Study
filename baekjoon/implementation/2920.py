music = [i for i in range(1,9)]

inputList = list(map(int, input().split()))

def checkSame(music,inputList):
    answer = "yes"
    for i in range(len(music)):
        if music[i] == inputList[i]:
            answer = "yes"
        else:
            answer = "no"
            break
    return answer 

answer = checkSame(music,inputList)

if answer == "no":
    music.reverse()
    answer = checkSame(music,inputList)
    if answer == "yes":
        print("descending")
    else:
        print("mixed")

elif answer == "yes":
    print("ascending")


