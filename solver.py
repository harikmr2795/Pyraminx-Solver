#define moves
def rotateB(): #bottom face - top corner as axis (bottom face clockwise)
    global left, right, front, bottom
    front, left, right = left, right, front
    bottom[0], bottom[1], bottom[2], bottom[3], bottom[4], bottom[6], bottom[7], bottom[8], bottom[9] = bottom[7], bottom[8], bottom[4], bottom[1], bottom[6], bottom[2], bottom[9], bottom[3], bottom[0]

def rotateL(): #left face - right corner as axis (right corner clockwise)
    global left, right, front, bottom
    front[0], front[1], front[2], front[3], front[4], front[5], front[6], front[7], front[8], front[9], right[0], right[1], right[2], right[3], right[4], right[5], right[6], right[7], right[8], right[9], bottom[0], bottom[1], bottom[2], bottom[3], bottom[4], bottom[5], bottom[6], bottom[7], bottom[8], bottom[9]=    bottom[7], bottom[8], bottom[4], bottom[1], bottom[6], bottom[5], bottom[2], bottom[9], bottom[3], bottom[0], front[7], front[8], front[4], front[1], front[6], front[5], front[2], front[9], front[3], front[0], right[7], right[8], right[4], right[1], right[6], right[5], right[2], right[9], right[3], right[0]
    left[0], left[1], left[2], left[3], left[4], left[6], left[7], left[8], left[9] = left[9], left[3], left[6], left[8], left[2], left[4], left[0], left[1], left[7]

def moveA():
    global left, right, front, bottom
    front[0], front[2], front[3], front[5], front[6], front[9], right[0], right[1], right[2], right[4], right[5], right[7], left[0], bottom[0] = right[7], right[4], right[1], right[5], right[2], right[0], front[9], front[3], front[6], front[2], front[5], front[0], bottom[0], left[0]

def moveB():
    rotateB()
    moveA()
    rotateB()
    rotateB()

def moveC():
    rotateB()
    rotateB()
    moveA()
    rotateB()

def moveD():
    rotateL()
    moveA()
    rotateL()
    rotateL()

def moveE():
    rotateB()
    moveD()
    rotateB()
    rotateB()
    
def moveF():
    rotateB()
    rotateB()
    moveD()
    rotateB()

def isSolved():
    global front, left, right, bottom
    return all([False for face in [front, left, right, bottom] for i in range(len(eval('face'))) if(eval('face')[0] is not eval('face')[i])])

def incMoveSet():
    global moveSet, moveNumber
    moveNumber += 1
    moveSet[0] += 1
    for i in range(len(moveSet)):
        if moveSet[i] == 6:
            moveSet[i] = 0
            if i == len(moveSet)-1:
                moveSet.append(0)
            else:
                moveSet[i+1] += 1

def isRedundant():
    global moveSet
    status = False
    if len(moveSet) > 1:
        for i in range(len(moveSet)-1):
            status = status or moveSet[i] == moveSet[i+1]
        return status
    else:
        return False
f = []
l = []
r = []
b = []
moveSet = [0]
moveNumber = 0
#get inputs
for face in ['f','l','r','b']:
    print('Enter ' + face)
    for i in range(10):
	    eval(face).append(input())

#copy of inputs
front, left, right, bottom = f[:], l[:], r[:], b[:]

#try every possible combination till solved
while isSolved() == False and moveNumber < 10000:
    front, left, right, bottom = f[:], l[:], r[:], b[:]
    for i in moveSet:
        if i == 0:
            moveA()
        elif i == 1:
            moveB()
        elif i == 2:
            moveC()
        elif i == 3:
            moveD()
        elif i == 4:
            moveE()
        elif i == 5:
            moveF()
    if isSolved() == False:
        incMoveSet()
        while(isRedundant() == True):
            incMoveSet()
        print(moveSet)

print(moveSet)
