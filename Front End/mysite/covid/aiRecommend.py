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

def getNearestPlace():
    # printData()
    convertIntoTree()
    # root.printTree()
    breadthFirstSearch(root)
    return nearestPlace
