#generat next move
def incMoveSet():
    global moveSet, moveNumber, depth
    moveNumber, moveSet[0] += moveNumber+1, moveSet[0]+1
    for i in range(len(moveSet)):
        if moveSet[i] == 6:
            moveSet[i] = 0
            if i == len(moveSet)-1:
                moveSet.append(0)
                depth += 1
                print('Depth = ',str(depth))
            else:
                moveSet[i+1] += 1

#Check for redundancy in move
def isRedundant():
    global moveSet
    status = False
    if len(moveSet) > 1:
        for i in range(len(moveSet)-1):
            status = status or moveSet[i] == moveSet[i+1]
        return status
    else:
        return False
#initilization
f, l, r, b, depth, moveSet, moveNumber = [], [], [], [], 0, [0], 0

#get inputs
for face in ['f','l','r','b']:
    print('Enter ' + face)
    for i in range(10):
	    eval(face).append(input())

#store a copy
front, left, right, bottom = f[:], l[:], r[:], b[:]

#try all possible combinations
while (all([False for face in [front, left, right, bottom] for i in range(len(eval('face'))) if(eval('face')[0] is not eval('face')[i])])) == False and depth < 20:
    front, left, right, bottom = f[:], l[:], r[:], b[:]
    for i in moveSet:
        if i == 0:
            front[0], front[2], front[3], front[5], front[6], front[9], right[0], right[1], right[2], right[4], right[5], right[7], left[0], bottom[0] = right[7], right[4], right[1], right[5], right[2], right[0], front[9], front[3], front[6], front[2], front[5], front[0], bottom[0], left[0]
        elif i == 1:
            front[0], front[1], front[2], front[4], front[5], front[7], right[0], bottom[7], left[0], left[2], left[3], left[5], left[6], left[9] = left[9], left[3], left[6], left[2], left[5], left[0], bottom[7], right[0], front[7], front[4], front[1], front[5], front[2], front[0]
        elif i == 2:
            front[0], bottom[9], left[0], left[1], left[2], left[4], left[5], left[7], right[0], right[2], right[3], right[5], right[6], right[9] = bottom[9], front[0], right[9], right[3], right[6], right[2], right[5], right[0], left[7], left[4], left[1], left[5], left[2], left[0]
        elif i == 3:
            left[9], right[7], front[4], front[5], front[6], front[7], front[8], front[9], bottom[2], bottom[5], bottom[4], bottom[0], bottom[1], bottom[7] = right[7], left[9] , bottom[2], bottom[5], bottom[4], bottom[0], bottom[1], bottom[7], front[4], front[5], front[6], front[7], front[8], front[9]
        elif i == 4:
            front[7], right[9], left[4], left[5], left[6], left[7], left[8], left[9], bottom[4], bottom[5], bottom[6], bottom[7], bottom[8], bottom[9] = right[9], front[7], bottom[4], bottom[5], bottom[6], bottom[7], bottom[8], bottom[9], left[4], left[5], left[6], left[7], left[8], left[9]
        elif i == 5:
            front[9], left[7], right[4], right[5], right[6], right[7], right[8], right[9], bottom[6], bottom[5], bottom[2], bottom[9], bottom[3], bottom[0] = left[7], front[9], bottom[6], bottom[5], bottom[2], bottom[9], bottom[3], bottom[0], right[4], right[5], right[6], right[7], right[8], right[9]
    if (all([False for face in [front, left, right, bottom] for i in range(len(eval('face'))) if(eval('face')[0] is not eval('face')[i])])) == False:
        incMoveSet()
        while(isRedundant() == True):
            incMoveSet()

print(moveSet)
