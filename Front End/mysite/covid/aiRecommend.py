from .binaryTree import Node
from .doctorData import getAll
from .getDist import getDistance


def convertIntoTree():
    global root
    doctor = getAll()
    root = Node(doctor[0])
    for i in range(1, len(doctor)):
        root.insert(doctor[i])


def getUserPlace(user):
    global userPlace
    userPlace = user


def sort(queue):
    for i in range(len(queue)):
        for j in range(len(queue) - i - 1):
            hf1 = getDistance(userPlace, queue[j].data)
            hf1 += 0.1 * queue[j].data['fee']
            hf2 = getDistance(userPlace, queue[j + 1].data)
            hf2 += 0.1 * queue[j + 1].data['fee']
            if hf1 > hf2:
                temp = queue[j]
                queue[j] = queue[j + 1]
                queue[j + 1] = temp


def aStarSearch(root):
    if root is None:
        return
    global nearestPlace
    nearestPlace = root.data
    nearestDist = getDistance(userPlace, nearestPlace)
    fee = nearestPlace['fee']
    heuristicFunc = nearestDist + (0.1 * fee)
    queue = []
    queue.append(root)
    while queue:
        temp = queue.pop(0)
        docPlace = temp.data
        tempDist = getDistance(userPlace, docPlace)
        tempFee = temp.data['fee']
        hf = tempDist + (0.1 * tempFee)
        if hf == 0:
            nearestPlace = temp.data
            return
        if hf < heuristicFunc:
            nearestPlace = temp.data
            heuristicFunc = hf
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)
        sort(queue)


'''
def breadthFirstSearch(root):
    if root is None:
        return
    global nearestPlace
    nearestPlace = root.data
    nearestDist = getDistance(userPlace, nearestPlace)
    queue = []
    queue.append(root)
    while queue:
        count = len(queue)
        while count > 0:
            temp = queue.pop(0)
            # print(temp.data)
            docPlace = temp.data
            dist = getDistance(userPlace, docPlace)
            if dist == 0:
                nearestPlace = temp.data
                return
            if dist < nearestDist:
                nearestPlace = temp.data
                nearestDist = dist
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
            count = count - 1
'''


def getNearestPlace():
    # printData()
    convertIntoTree()
    # root.printTree()
    # breadthFirstSearch(root)
    aStarSearch(root)
    return nearestPlace
