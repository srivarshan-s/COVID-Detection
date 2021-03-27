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


def main():
    # printData()
    convertIntoTree()
    # root.printTree()
    getUserPlace()
    breadthFirstSearch(root)
    print(nearestPlace)


if __name__ == '__main__':
    main()
