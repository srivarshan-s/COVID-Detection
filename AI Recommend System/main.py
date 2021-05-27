from myData import doctor, printData
from binaryTree import Node
from getDist import *


def convertIntoTree():
    global root
    root = Node(doctor[0])
    for i in range(1, len(doctor)):
        root.insert(doctor[i])


def getUserPlace():
    global userPlace
    userPlace = input('Enter Place: ')


def breadthFirstSearch(root):
    if root is None:
        return
    global nearestPlace
    nearestPlace = root.data
    nearestDist = getDistance(userPlace, nearestPlace['place'])
    queue = []
    queue.append(root)
    while queue:
        count = len(queue)
        while count > 0:
            temp = queue.pop(0)
            # print(temp.data)
            docPlace = temp.data['place']
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


def sort(queue):
    for i in range(len(queue)):
        for j in range(len(queue) - i - 1):
            hf1 = getDistance(userPlace, queue[j].data['place'])
            hf1 += 0.1 * queue[j].data['fee']
            hf2 = getDistance(userPlace, queue[j + 1].data['place'])
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
    nearestDist = getDistance(userPlace, nearestPlace['place'])
    fee = nearestPlace['fee']
    heuristicFunc = nearestDist + (0.1 * fee)
    queue = []
    queue.append(root)
    while queue:
        temp = queue.pop(0)
        docPlace = temp.data['place']
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


def main():
    # printData()
    convertIntoTree()
    # root.printTree()
    getUserPlace()
    # breadthFirstSearch(root)
    aStarSearch(root)
    print(nearestPlace)


if __name__ == '__main__':
    main()
